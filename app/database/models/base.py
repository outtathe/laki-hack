from sqlalchemy.orm import declarative_base

# Base = declarative_base()

class MyBaseClass(object):

    async def update(self, **kwargs):
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

Base = declarative_base(cls=MyBaseClass)

