class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://punicharana:password@localhost:5432/template1'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False
    PROPAGATE_EXCEPTIONS = False