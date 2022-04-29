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

### Required Data
# item-item recommend list
# user-item recommend list
# articles' description


# overall_data = pd.read_csv('static/data/overall_annual.csv')
# account_dict = {key:"{:,}".format(overall_data[overall_data.channel == key]['annual_accounts'].values[0]) for key in overall_data.channel}
# update_date = pd.to_datetime(overall_data['latest_created_at'].max(),format='%Y-%m-%d %H:%M:%S').strftime('%d%b%Y')

# f = open('static/data/Streamgraph.json',)
# stream_data = json.load(f)
# f.close()

##########################################################################################################################################
# Flask Set-Up
##########################################################################################################################################

app = Flask(__name__) # Set name of the app.
app.config['SECRET_KEY'] = 'mykey'

#*Render Template
# @app.route('/')
# def home():
#     return render_template("home.html",account_dict=account_dict,update_date=update_date)

def ranking_page():
# @app.route('/ranking')
# def ranking_page():
#     return render_template("ranking.html",ranking_spec=ranking_data)

# @app.route('/engagement')
# def engagement_page():
#     return render_template("engagement_v2.html",heatmap_spec1=heatmap1_data,heatmap_spec2=heatmap2_data)

# @app.route('/category')
# def category_page():
#     return render_template("category_v2.html",scatter_spec=scatter_data,stream_spec=stream_data)

if __name__=='__main__':
    app.run()
