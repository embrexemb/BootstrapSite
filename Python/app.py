from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo

import os
import sys
from scrape_mars import scrape



app = Flask(__name__)

#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

database = "mongodb+srv://Scott:#######@cluster0.w73ay.mongodb.net/test?authSource=admin&replicaSet=atlas-42n68g-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"

uri = database
client = pymongo.MongoClient(uri)
mars_app = client.mars_app
mars_get = mars_app.mars

@app.route('/')
def index():
    #mars=mongo.db.mars.find_one()
    mars=mars_get.find_one()
    #print(mars['news_title'])
    return render_template('index.html', data=mars)
    #return render_template('index.html')

@app.route('/scrape.py')
def scraped():
    print(f'before scrape')
    #mars = mars_get
    data = scrape()
    
    #mars.insert_one(data)  
    mars_get.update({},data,upsert=True)
   
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)
