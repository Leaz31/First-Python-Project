#!/usr/bin/env python3

# import the necessary packages
import joblib
import argparse
import os

def load_model(version):
    filename = f"model-{version}.model"
    return joblib.load("./models/"+filename)


if __name__ == "__main__":
    print("Starting...")
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--version", required=True, help="Version of the model")
    ap.add_argument("-d", "--data", nargs="+", required=True, help="input data")
    args = vars(ap.parse_args())

    version = args["version"]
    print(f"Version selected : {version}")
    data = args["data"]
    data_as_int = []
    
    for value in data:
        data_as_int.append(int(value))
    
    print(f"Data: {data_as_int}")
    
    model = load_model(version)
    print(model)
    # Surface réelle
    # Nombre de pièces
    values = data_as_int

    predictions = model.predict([values])
    prediction = predictions[0]
    print(f"The prediction is : {prediction}")
    print("Done.")