from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import os
import sys
from scrape_mars import scrape



app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/')
def index():
    mars=mongo.db.mars.find_one()
    #print(mars['news_title'])
    return render_template('index.html', data=mars)
    #return render_template('index.html')

@app.route('/scrape')
def scraped():
    print(f'before scrape')
    mars = mongo.db.mars
    data = scrape()
    
    #mars.insert_one(data)  
    mars.update({},data,upsert=True)
   
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)