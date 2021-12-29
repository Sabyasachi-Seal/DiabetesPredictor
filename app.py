
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import re
import math
import pickle

app = Flask("__name__")

q = ""

@app.route("/")
def loadPage():
	return render_template('index.html', query="")



@app.route("/", methods=['POST'])
def diabetesPrediction():
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']

    inputdata = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8]]

    filename = "model.sav"

    mlmodel = pickle.load(open(filename, "rb"))

    single = mlmodel.classifier(inputdata)[0]

    probability = mlmodel.predict_proba(inputdata)[:,1][0]

    if single==1:
        output = "The patient is diagnosed with Diabetes"
        output1 = "Confidence: {}".format(probability*100)
    else:
        output = "The patient is not diagnosed with Diabetes"
        output1 = ""
    
    return render_template('index.html', output1=output, output2=output1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'])
    
app.run()

