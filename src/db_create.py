import os
import sys

from manage import app

sys.path.append(".")

from models import Base

from migrate.versioning import api

Base.metadata.create_all()

if not os.path.exists(app.config.SQLALCHEMY_MIGRATE_REPO):
    api.create(app.config.SQLALCHEMY_MIGRATE_REPO, 'migrations')
    api.version_control(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO,
                        api.version(app.config.SQLALCHEMY_MIGRATE_REPO))
