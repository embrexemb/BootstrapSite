from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import sys

app = Flask(__name__)
app.config['MONGO_URI']="mongodb://localhost:27017/Mission_To_Mars_DB"
mongo = PyMongo(app)

@app.route('/')
def index():
    
    mars_mission_news=list(mongo.db.mars_db.find())
    print(mars_mission_news)
    return render_template('index.html', mars_mission=mars_mission_news)

@app.route('/scrape')
def scrape():
    mars_mission = mongo.db.mars_db
    data = scrape_mars.scrape()
    mars_mission.update(
        {},
        data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
