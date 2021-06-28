create env
```bash
conda create -n WineQ python=3.7 -y
```

activate env
```bash
conda activate WineQ
```

created a Requirements.txt file

installed Requirements.txt
```bash
pip install -r requirements.txt
```

Download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

One Liner Updates for README.md
```bash
git add . && git commit -m "Update README.md"
```

```bash
git branch -M main
```

```bash
git remote add origin  https://github.com/ssr-1998/Wine_Quality_MLOPs.git
```

```bash
git push origin main
```

tox command -
```bash
tox
```

For Rebuilding -
```bash
tox -r
```

pytest command -
```bash
pytest -v
```

setup command -
```bash
pip install -e .
```

Build your Own Package Commands -
```bash
python setup.py sdist bdist_wheel
```
