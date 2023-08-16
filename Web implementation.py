from os import path
from pathlib import Path

from flask import Flask, render_template, request, jsonify
from flask_frozen import Freezer
import plotly.express as px
import pandas as pd
import joblib
import numpy as np

# Load models and preprocessor
targets = ['Estr110', 'EstrInjec110', 'EstrProgComb110', 'OtherHormone1']

models = {target: joblib.load(f"{target}_model.pkl") for target in targets}
preprocessor = joblib.load("preprocessor.pkl")

# @app.route('/modeling', methods=['GET','POST'])
# def modeling():
#     predictions = {}
#     data_dict = {}
#     if request.method == 'POST':
#         # Extract input data from the POST request
#         data = request.form
#         print("Received data:", data)
#         data_dict = dict(data)
        
#         # Ensure no empty values and convert them to default or NaN
#         for key, value in data_dict.items():
#             if value == '':
#                 data_dict[key] = np.nan   # replace with appropriate default or NaN

#         # Convert to DataFrame
#         input_data = pd.DataFrame([data_dict])

#         # Ensure the column order matches the order the model expects
#         input_data = input_data[['Race', 'MenoStatus', 'Age', 'Language', 'data.INSURAN10', 'data.NOTAFFR10', 'data.INCOME10', 'data.HOTFLAS10']]
#         input_data = input_data.drop(columns=targets)

#         # Get predictions for each model and store in a dictionary
#         for target, model in models.items():
#             preprocessed_input = preprocessor.transform(input_data)
#             transformer = preprocessor.fit_transform(X)
#             features = preprocessor.get_feature_names_out()
#             print(features)
#             print(preprocessed_input.shape)
#             print(preprocessed_input)
#             prediction = model.predict(preprocessed_input)
#             predictions[target] = int(prediction[0])  # Assuming binary classification, convert prediction to int
#             print(f"Prediction for {target}: {prediction}")

#     # Render the template, passing in predictions (will be empty dictionary if GET request)
#     return render_template(str(Path('pages')) + '/' + 'modeling' + '.html', predictions=predictions, data_dict=data_dict)


@app.route('/modeling', methods=['GET', 'POST'])
def modeling():
    predictions = {}
    df = {}
    if request.method == 'POST':
        data = {
            'Race': [request.form['Race']],
            'MenoStatus': [request.form['MenoStatus']],
            'Age': [int(request.form['Age'])],
            'Language': [request.form['Language']],
            'data.INSURAN10': [int(request.form['data.INSURAN10'])],
            'data.NOTAFFR10': [int(request.form['data.NOTAFFR10'])],
            'data.INCOME10': [int(request.form['data.INCOME10'])],
            'data.HOTFLAS10': [int(request.form['data.HOTFLAS10'])]
        }
        df = pd.DataFrame(data)
        print(df)
        predictions = {target: models[target].predict(df)[0] for target in targets}

    return render_template(str(Path('pages')) + '/' + 'modeling' + '.html', predictions=predictions, data_dict=df)


# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)
