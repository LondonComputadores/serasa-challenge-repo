class BaseConfig(object):
    SECRET_KEY = 'cabinquest-probe'
    ENV = "development"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
 
    # POSTGRESQL - REMOTE 
    DB_USER_REMOTE = 'my-remote-user'
    DB_PASSWORD_REMOTE = 'my-remote-password'
    DB_NAME_REMOTE = 'my-remote-db-name'
    DB_HOST_REMOTE = 'my-host-remote'
    DB_PORT_REMOTE = 5432

    # POSTGRESQL - LOCAL 
    DB_USER_LOCAL = 'my-local-user'
    DB_PASSWORD_LOCAL = 'my-local-password'
    DB_NAME_LOCAL = 'my-local-db-name'
    DB_HOST_LOCAL = 'localhost'
    DB_PORT_LOCAL = 5432

    if ENV == "development":
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
            user=DB_USER_LOCAL,
            password=DB_PASSWORD_LOCAL,
            host=DB_HOST_LOCAL,
            port=DB_PORT_LOCAL,
            name=DB_NAME_LOCAL,
        )
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
            user=DB_USER_REMOTE,
            password=DB_PASSWORD_REMOTE,
            host=DB_HOST_REMOTE,
            port=DB_PORT_REMOTE,
            name=DB_NAME_REMOTE,
        )   
     

    # SQLITE
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "example.db"))