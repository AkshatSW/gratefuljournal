hosting this app on render 
host: akshatsrivastava200213@gmail.com

#database uri when in production, will go in config.json
"local_uri": "postgresql+psycopg2://bmbgvufubvcnth:f450589057f27e68209e037b8c066519479a1b9d73930e5bb9aa045cb8468cf7@ec2-44-210-36-247.compute-1.amazonaws.com:5432/d7m1i63pr6dlm4",
"prod_uri": "postgresql://bmbgvufubvcnth:f450589057f27e68209e037b8c066519479a1b9d73930e5bb9aa045cb8468cf7@ec2-44-210-36-247.compute-1.amazonaws.com:5432/d7m1i63pr6dlm4"


#Acess database using the following link:
    https://datazenit.com/heroku-data-explorer.html#/

# '''
    # Issue arised: no module found named "mysql db"
    # solution:
    # pip install mysqlclient
    # '''

sql uri > 
// use "postgresql" instead of postgres for heroku. Same for using "mysql+pymysql" instead of mysql 


#limiting beliefs List Of Beliefs table made embedded from airtable 

commands for setting up table in postgres heroku >
change the main.py file to app.py
run code in terminal > 
>heroku config --app zariyaa
>heroku run python 
>from app import db
>db.create_all()

