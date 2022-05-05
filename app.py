from flask import Flask, render_template, request, session, flash, json, jsonify
from flask_wtf import FlaskForm

# from wtforms import TextField,TextAreaField, SubmitField, BooleanField, RadioField, SelectField
# from wtforms import validators
# from wtforms.validators import DataRequired
# from flask_bootstrap import Bootstrap

import json
import pandas as pd

##########################################################################################################################################
# Load data into DataFrame
##########################################################################################################################################

customers = pd.read_csv('static/model/customers_v2.csv')
customer_list = dict(zip(customers['customer_id'],customers['name']))

prediction = pd.read_csv('static/model/prediction.csv')
prediction['prediction'] = prediction['prediction'].apply(lambda x: x.split())
prediction['recent_purchase'] = prediction['recent_purchase'].apply(lambda x: x.split())
prediction['actual'] = prediction['actual'].apply(lambda x: x.split())

temp_pred = prediction['prediction'][0]
temp_recent = prediction['recent_purchase'][0]
temp_actual = prediction['actual'][0]
max_recent = min([len(temp_recent),6])
max_actual = min([len(temp_actual),6])

cus_name = customers['name'][0]
model = 'ALS Model'

articles = pd.read_csv('static/model/articles_v2.csv')
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
        # get customer_id & model from dropdown
        select = request.form.get('customers')
        model2 = request.form.get('model_types')
        # filter data to update back to website
        temp_pred2 = prediction['prediction'][(prediction.customer_id == select)&(prediction.model==model2)].values[0]
        temp_recent2 = prediction['recent_purchase'][(prediction.customer_id == select)&(prediction.model==model2)].values[0]
        temp_actual2 = prediction['actual'][(prediction.customer_id == select)&(prediction.model==model2)].values[0]
        max_recent2 = min([len(temp_recent2),6])
        # max_actual2 = min([len(temp_actual),6])  
        cus_name2 = customers['name'][customers.customer_id == select].values[0]
        print(model2)
        print(temp_recent2)
        return render_template("home.html",nameDict=customer_list,cus_name=cus_name2,rec_items=temp_pred2,last_items=temp_recent2,articles=articles_list,max_recent=max_recent2,model=model2,actual_items=temp_actual2)
    return render_template("home.html",nameDict=customer_list,cus_name=cus_name,rec_items=temp_pred,last_items=temp_recent,articles=articles_list,max_recent=max_recent,model=model,actual_items=temp_actual)


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
