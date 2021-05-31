
from splinter import Browser 
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import os
import pandas as pd
import time

def init_browser():
    return Browser("chrome", headless=False)

def scrape():
    browser = init_browser()

    url = "https://redplanetscience.com"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    
    try:
        url_element=soup.select_one("div.list_text")
        news_title=url_element.find("div", class_="content_title").get_text()
        news_p=url_element.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None

    print(news_title)
    print(news_p)
   
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)
    html_image = browser.html
    image_soup = bs(html_image, "html.parser")

    try:
        mars_image = image_soup.find("img", class_="headerimage")["src"]
    except AttributeError:
        return None
    mars_image = image_url + mars_image
    print(mars_image)


    table_url = "https://galaxyfacts-mars.com"
    try:
        tables = pd.read_html(table_url)
    except BaseException:
        return None

    mars_df = tables[0]
    #print(mars_df)
    mars_df.columns=mars_df.columns.get_level_values(0)
    mars_df = pd.DataFrame(mars_df)
    mars_df.columns = mars_df.iloc[0]
    mars_df = mars_df[1:]
    #mars_df.to_html('Pa#ndasTable.html')
    #table for database dicionary
    mars_table = mars_df.to_html(classes="table table-striped")
    print (mars_table)
    
    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)

    response = requests.get(hemi_url)
    mars_data = bs(response.text, "html.parser")

    mars_hemi_urls = []
    for img in mars_data.find_all('img', class_='thumb'):
        h_title = img.get('alt')
        h_url = img.get('src')
        h_image="https://marshemispheres.com/" + h_url
        
        temp_dictionary = {
            'title': h_title,
            'img_url': h_image
        }
        mars_hemi_urls.append(temp_dictionary)

    print(mars_hemi_urls)

    browser.quit()
    # set up data dicionary to return

    data ={
        "news_title":news_title,
        "news_paragraph": news_p,
        "featured_image": mars_image,
        "mars_facts_table": mars_table,
        "hemisphere_img_url": mars_hemi_urls
    }

    return data