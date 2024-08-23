from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json', 'r') as c:
    params=json.load(c)['params']

local_server = True
app = Flask(__name__)


if(local_server): 
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:   
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)

class grateful(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String(48), nullable=False)
    Grateful_for=db.Column(db.String, nullable=False)

class activities_for_happy_chemicals(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    activity=db.Column(db.String(48), nullable=False)

@app.route("/home")
@app.route("/", methods=['GET','POST'])
def greateful():
    # if (request.method =='POST'):
    #     userDetails = request.form    
    #     Name=userDetails['Name']
    #     Grateful_for=userDetails['Grateful_for']
    #     entry=grateful(Name=Name, Grateful_for=Grateful_for)
    #     db.session.add(entry)
    #     db.session.commit() 
    #     db.session.close()
     
        # return redirect("/grateful")
    
    # userDetails = grateful.query.filter_by().all() 
    return render_template('grateful.html')
    
# run.pyss
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0") #host="0.0.0.0" will make the page accessable by going to http://[ip]:5000/ on any computer in the network


