# Predictive Modeling on SWAN Data

### This repository contains predictive models built on the Study of Women's Health Across the Nation (SWAN) dataset. The models aim to predict access to treatment based on a set of predictor variables. In addition, it includes the deployment code to port the trained models to the wiki site and implment them in a web form.

Note: swandata.csv contained preprocessing errors. Swannew was processed properly and includes economic predictors and information on severity such that we can normalize by severity of illness. The new models are on the lower half of the notebook

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Models](#models)

## General Info

The SWAN dataset contains various health indicators for a sample of women. The objective of this project is to build a set of models that predict certain health factors using a number of predictor variables. The predictor variables include:

- Race
- Menopause status
- Age
- Interview Language
- Insurance Status
- Affordability of health care
- Income
- Hot flashes

The target variables include:

- Estradiol (Estr110)
- Estradiol injection (EstrInjec110)
- Combined estradiol/progestin therapy (EstrProgComb110)
- Other hormone therapy (OtherHormone1)

Each of these target variables is predicted separately, resulting in an individual model for each.

## Technologies

The project is implemented in Python using the following libraries:

- Pandas
- Scikit-learn
- Numpy

## Models

The models are built using Scikit-learn's `RandomForestClassifier` and 'support vector classifiers' after hyperparameter optimization. The predictor variables are preprocessed using a combination of standard scaling (for numeric variables) and one-hot encoding (for categorical variables).

Each model is evaluated on a held-out test set, and the performance is reported in terms of accuracy and the classification report, which includes precision, recall, f-score, and support.

the models attained accuracies of near 80% in predicting access.
