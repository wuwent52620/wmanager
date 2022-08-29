from migrate.versioning import api
from models import Base
from src import app

migration = app.config.SQLALCHEMY_MIGRATE_REPO + '/versions/%03d_migration.py' % (
        api.db_version(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO) + 1)
import types

old_model = api.create_model(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO)
new = types.ModuleType('old_model')
exec(old_model, new.__dict__)
script = api.make_update_script_for_model(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO,
                                          new.meta,
                                          Base.metadata)
open(migration, 'wt').write(script)
api.upgrade(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as ' + migration)
print('Current database version: ' + str(
    api.db_version(app.config.SQLALCHEMY_DATABASE_URI, app.config.SQLALCHEMY_MIGRATE_REPO)))
