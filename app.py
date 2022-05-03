from flask import Flask, render_template, request, session, flash, json, jsonify
from flask_wtf import FlaskForm
from wtforms import TextField,TextAreaField, SubmitField, BooleanField, RadioField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

import json
import pandas as pd


##########################################################################################################################################
# Load data into DataFrame
##########################################################################################################################################


customers = pd.read_csv('static/model/customers.csv')
customer_list = dict(zip(customers['customer_id'],customers['name']))

prediction = pd.read_csv('static/model/prediction.csv')
prediction['prediction'] = prediction['prediction'].apply(lambda x: x.split())
prediction['recent_purchase'] = prediction['recent_purchase'].apply(lambda x: x.split())

temp_pred = prediction['prediction'][0]
temp_recent = prediction['recent_purchase'][0]

articles = pd.read_csv('static/model/articles.csv')


##########################################################################################################################################
# Flask Set-Up
##########################################################################################################################################

app = Flask(__name__) # Set name of the app.
app.config['SECRET_KEY'] = 'mykey'

#*Render Template
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html",nameDict=customer_list,rec_items=temp_pred,last_items=temp_recent,articles=articles)

@app.route('/', methods=['POST'])  
def updatehome():     
    select = request.form.get('customers')
    temp_pred2 = prediction['prediction'][prediction.name == select]
    temp_recent2 = prediction['recent_purchase'][prediction.name == select]
    return render_template("home.html",nameDict=customer_list,rec_items=temp_pred2,last_items=temp_recent2,articles=articles)


if __name__=='__main__':
    app.run()
