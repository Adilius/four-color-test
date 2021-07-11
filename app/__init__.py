from flask import Flask
app = Flask(__name__)
app.config.from_object('app.configuration.Config')

#Configuration of application, see configuration.py, choose one and uncomment.
#configuration = 'app.configuration.ProductionConfig'
configuration = 'app.configuration.DevelopmentConfig'
print('Running server on ' + app.config['ENV'] + '.')
app.config.from_object(configuration)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
print('Running database at', app.config['SQLALCHEMY_DATABASE_URI'])

from app import views, models

db.create_all()