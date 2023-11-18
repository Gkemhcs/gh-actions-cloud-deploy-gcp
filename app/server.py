import os
from flask import request,render_template,url_for,redirect,Flask
app=Flask("__main__")
environ=os.environ.get("ENVIRONMENT")
@app.route("/")
def home():
       return render_template("home.html",title=f"GITHUB-ACTIONS TO CLOUD-DEPLOY DEMO {environ} ",content="THIS PROJECTS SHOWS THE INTERGRATION OF GITHUB ACTIONS WITH CLOUD DEPLOY FOR CI/CD  ") 
@app.route("/health")
def health_check():
        return " healthy"
if(__name__=="__main__"):
     app.run(port=8080,host="0.0.0.0")