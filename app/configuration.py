
class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
	BOOTSTRAP_FONTAWESOME = True
	SECRET_KEY = "secret"
	CSRF_ENABLED = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SERVER_IP = 0000

class ProductionConfig(Config):
	ENV = 'Production'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'    # Change when in production
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEVELOPMENT = False
	DEBUG = False

class DevelopmentConfig(Config):
	ENV = 'Development'
	DEBUG = True
	DEVELOPMENT = True