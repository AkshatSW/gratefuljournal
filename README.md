
# Zariyaa Rediscover Yourself 

This is a flask based web app currectly hosted on made for zariyaa happy wellness private limited for the their retreat purposes. 


## Run Locally 

Clone the project
```bash
git clone https://github.com/AkshatSW/ZariyaaWebApp.git
```
Set up the virtual enviornment 
```bash
cd zariyaawebapp
pip install virtualenv
virtualenv env
.env/Scripts/Activate.ps1
```
Install required packages
```bash
pip install -r requirements.txt
```
Run the local server
```bash
python app.py
```
## Misc
#### SQL URI (in config.json)

Use "postgresql" instead of postgres for heroku. Same for using "mysql+pymysql" instead of mysql

#### Limiting beliefs.html
limiting beliefs List Of Beliefs table made embedded from airtable

#### Postgres database setup
change the main.py file to app.py run code in terminal 

```bash
heroku config --app zariyaa 
heroku run python
from app import db
db.create_all()
```
Check the config.json and notes.md file for details