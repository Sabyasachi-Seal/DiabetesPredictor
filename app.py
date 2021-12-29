import pandas as pd
from flask import Flask, request, render_template
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

    X_pred = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8]]

    X_pred = pd.DataFrame(X_pred, columns=['Pregnancies', 'Glucose', 'BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])

    savename = "model.sav"

    load_model = pickle.load(open(savename, "rb"))

    predicted = load_model.predict(X_pred)

    probability = load_model.predict_proba(X_pred)[:,1][0]*100

    if predicted==1:
        output = "The patient is diagnosed with Diabetes"
        output1 = "Confidence: {}".format(probability)
    else:
        output = "The patient is not diagnosed with Diabetes"
        output1 = "Confidence: {}".format(100-probability)
    
    return render_template('index.html', output1=output, output2=output1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'])

