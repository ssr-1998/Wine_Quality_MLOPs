from flask import Flask, render_template, request, jsonify
import os
from src import get_data
# import yaml
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"
statis_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=statis_dir, template_folder=template_dir)


def predict(data):
    config = get_data.read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]


def api_response(response):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {'response': response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something Went Wrong!!\nTry Again"}
        return error


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return render_template("index.html", response=response)
            elif request.json:  # For API for testing purpose
                response = api_response(request)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something Went Wrong!!\nTry Again"}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
