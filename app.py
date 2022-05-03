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
max_recent = min([len(temp_recent),6])

cus_name = customers['name'][0]

articles = pd.read_csv('static/model/articles.csv')
articles_list = dict(zip(articles['article_id'],articles['prod_name']))

##########################################################################################################################################
# Flask Set-Up
##########################################################################################################################################

app = Flask(__name__) # Set name of the app.
app.config['SECRET_KEY'] = 'mykey'

#*Render Template
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        select = request.form.get('customers')
        temp_pred2 = prediction['prediction'][prediction.customer_id == select].values[0]
        temp_recent2 = prediction['recent_purchase'][prediction.customer_id == select].values[0]
        max_recent2 = min([len(temp_recent2),6])  
        cus_name2 = customers['name'][customers.customer_id == select].values[0]
        print(select)
        print('temp_pred2',len(temp_pred2))
        print('temp_recent2',len(temp_recent2))
        print('max_recent2',len(cus_name2))
        print(cus_name2)
        return render_template("home.html",nameDict=customer_list,cus_name=cus_name2,rec_items=temp_pred2,last_items=temp_recent2,articles=articles_list,max_recent=max_recent2)
    return render_template("home.html",nameDict=customer_list,cus_name=cus_name,rec_items=temp_pred,last_items=temp_recent,articles=articles_list,max_recent=max_recent)

# @app.route('/home', methods=['POST'])  
# def updatehome():     
#     select = request.form.get('customers')
#     temp_pred2 = prediction['prediction'][prediction.name == select]
#     temp_recent2 = prediction['recent_purchase'][prediction.name == select]
#     print(select)
#     return render_template("home.html",nameDict=customer_list,rec_items=temp_pred2,last_items=temp_recent2,articles=articles)

# @app.route("/test" , methods=['GET', 'POST'])
# def test():
#     select = request.form.get('customers')
#     flash(str(tts)+'is being selected')

if __name__=='__main__':
    app.run(debug=True)
