
from flask import request,render_template,url_for,redirect,Flask
app=Flask("__main__")
@app.route("/")
def home():
       return render_template("home.html",title="GITHUB-ACTIONS TO CLOUD-DEPLOY DEMO ",content="THIS PROJECTS SHOWS THE INTERGRATION OF GITHUB ACTIONS WITH CLOUD DEPLOY FOR CI/CD  ") 

if(__name__=="__main__"):
     app.run(port=8080,host="0.0.0.0")