from flask import Flask
app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#configuration = 'app.configuration.ProductionConfig'
configuration = 'app.configuration.DevelopmentConfig'
app.config.from_object(configuration)
print('Running server on ' + app.config['ENV'] + '.')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
print('Running database at', app.config['SQLALCHEMY_DATABASE_URI'])

from app import views, models

db.create_all()