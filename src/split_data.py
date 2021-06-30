# Steps:
# Split the Raw Data
# Save it in data\processed directory

import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from get_data import read_params


def split_and_save_data(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(raw_data_path, sep=",")
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)
    train.to_csv(train_data_path, sep=",", encoding="utf-8", index=False)
    test.to_csv(test_data_path, sep=",", encoding="utf-8", index=False)


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="params.yaml")
    arg_parser = arg.parse_args()
    split_and_save_data(config_path=arg_parser.config)
