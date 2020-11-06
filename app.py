# coding: utf-8

import pickle
import numpy as np
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


def time_convert(x):
    h,m,s = map(int,x.split(':'))
    return (h*360)+(m*60)+s

app = Flask(__name__)

app.config["DATABASE_URL"] = "postgres://ttsskopxdmnsfo:4378043c6d59d120e32dd53458a7b496edba8ae3199207429f3709d03c59db82@ec2-52-203-165-126.compute-1.amazonaws.com:5432/d4arif9evev4vq"
postgres = SQLAlchemy(app)

# start home page
@app.route("/")
def index():
    return render_template('index.html')

# create prediction module
@app.route('/predict', methods=['POST'])
def predict():
    # get user inputs
    distance = request.form['distance']
    down = request.form['down']
    quarter = request.form['quarter']
    clock = request.form['clock']

    # convert clock to something the ML model can take in
    # how is ML model using time???
    # bin it - pick midpoint of
    """***---???---***"""
    """***---???---***"""
    """***---???---***"""

    # take inputs and put into array, ready for ML model
    feature_list = [down, distance, quarter, clock]
    features = [np.array(feature_list)]

    # call the play

    # use pickle or H5?????
    # load H5 from sklearn/pandas pd.read_hdf
    model = pickle.load(open('random_forest/random_forest.pkl'))
    prediction = model.predict(features)
    output = prediction[0]

    # binary output for pass or rush call
    if output == 0:
        result = 'Pass'
    else:
        result = 'Rush'

    return render_template('index.htnml', call = result)

@app.route('/findings')
def findings():
    return render_template('templates/findings.html')

@app.route('/methodology')
def methodology():
    return render_template('templates/methodology.html')
if __name__ == "__main__":
    app.run()