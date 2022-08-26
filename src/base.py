from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from . import app

# print(app.config.SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

bind = create_async_engine(app.config.SQLALCHEMY_DATABASE_URI, echo=True)
