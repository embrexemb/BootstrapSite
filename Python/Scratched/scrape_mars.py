#dependencies

import selenium
from splinter import Browser 
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import pandas as pd
import time

def init_browser():
    return Browser("chrome", headless=False)

def scrape():
#set up a dictionary for Mars Mission News
    browser=init_browser()
    mars_mission_data = {}

    mars_news="https://redplanetscience.com"
    browser.visit(mars_news)
    time.sleep(2)

    html=browser.html
    soup=bs(html,'html.parser')

#scrape latest mission data news
    news_title=soup.find('div',class_='col-md-8').find('content_title').text
    print(news_title)
    news_paragraph=soup.find('div',class_='article_teaser_body').text
    print(news_paragraph)

    mars_mission_data['news_title']=news_title
    mars_mission_data['news_paragraph']=news_paragraph
    return mars_mission_data