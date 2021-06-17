
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

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'    # Change when in production
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True