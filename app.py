from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():

    url="https://www.businesstoday.in/technology/news"
    req=requests.get(url)
    # proxies = { "http": None, "https": None}
    # req=requests.get("https://www.businesstoday.in/technology/news", proxies=proxies, timeout=3)
    soup=BeautifulSoup(req.content,"html.parser")
    outerdata=soup.find_all("div",class_="widget-listing",limit=6)
    finalNews=""

    for data in outerdata:
        news=data.div.div.a["title"]
        finalNews+="\u2022 "+ news + "\n" 
    return render_template("index.html",News=finalNews)
    
if __name__ == "__main__":
    app.run()    
