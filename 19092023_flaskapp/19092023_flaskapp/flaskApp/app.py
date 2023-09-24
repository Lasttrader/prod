#import
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
import pickle
import os

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# exec("x{} = {}".format(i, i * i))
# i += 1

#load models
with open('models_tech/contact_le.pkl', 'rb') as f:
    contact_le = pickle.load(f)
with open('models_tech/default_le.pkl', 'rb') as f:
    default_le = pickle.load(f)
with open('models_tech/education_le.pkl', 'rb') as f:
    education_le = pickle.load(f)
with open('models_tech/housing_le.pkl', 'rb') as f:
    housing_le = pickle.load(f)
with open('models_tech/job_le.pkl', 'rb') as f:
    job_le = pickle.load(f)
with open('models_tech/loan_le.pkl', 'rb') as f:
    loan_le = pickle.load(f)
with open('models_tech/marital_le.pkl', 'rb') as f:
    marital_le = pickle.load(f)
with open('models_tech/month_le.pkl', 'rb') as f:
    month_le = pickle.load(f)
with open('models_tech/poutcome_le.pkl', 'rb') as f:
    poutcome_le = pickle.load(f)
with open('models_tech/y_le.pkl', 'rb') as f:
    y_le = pickle.load(f)

with open('models_tech/num_scaler.pkl', 'rb') as f:
    num_scaler = pickle.load(f)

with open('models_tech/kNNR.pkl', 'rb') as f:
    kNNR = pickle.load(f)

#WEB интерфейс
@app.route('/',  methods = ['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    
    if request.method == 'POST':
        #input_X
        job	= float(job_le.transform([request.form['job']]))
        marital	= float(marital_le.transform([request.form['marital']]))
        education = float(education_le.transform([request.form['education']]))
        default	= float(default_le.transform([request.form['default']]))
        balance	= float(request.form['balance'])
        housing	= float(housing_le.transform([request.form['housing']]))
        loan = float(loan_le.transform([request.form['loan']]))
        contact = float(contact_le.transform([request.form['contact']]))
        day	= float(request.form['day'])
        month = float(month_le.transform([request.form['month']]))
        duration = float(float(request.form['duration']))	
        campaign = float(request.form['campaign'])	
        pdays = float(request.form['pdays'])	
        previous = float(request.form['previous'])	
        poutcome =  float(poutcome_le.transform([request.form['poutcome']]))
        y = float(y_le.transform([request.form['y']]))
        
        cat_X = [job,	
            marital, 
            education,	
            default,
            housing,
            loan,
            contact,
            month,
            poutcome,
            y]
        print('cat_X', cat_X)
        num_X = num_scaler.transform([[balance,	
                               day,	
                               duration,	
                               campaign,	
                               pdays,	
                               previous]])
        print('num_X', num_X)
        
        X = []
        X.extend(cat_X)
        X.extend(num_X[0])
        print('X', X)
        predicted_age = kNNR.predict([X])
        print(predicted_age)
        return render_template('main.html', result = predicted_age)

@app.route('/api/api_message/v1/',  methods = ['POST', 'GET'])
def api_message():
    message = request.json
    X = message['X']
    predict = kNNR.predict(X)
    return jsonify({'age_predicted' : str(predict)})


if __name__ == '__main__':
    app.run()




