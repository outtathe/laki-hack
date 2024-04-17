from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import params.confing as env
from database.models.base import Base

def drop_everything(engine):
    """(On a live db) drops all foreign key constraints before dropping all tables.
    Workaround for SQLAlchemy not doing DROP ## CASCADE for drop_all()
    (https://github.com/pallets/flask-sqlalchemy/issues/722)
    """
    from sqlalchemy.engine.reflection import Inspector
    from sqlalchemy.schema import (
        DropConstraint,
        DropTable,
        MetaData,
        Table,
        ForeignKeyConstraint,
    )

    con = engine.connect()
    trans = con.begin()
    inspector = Inspector.from_engine(engine)

    # We need to re-create a minimal metadata with only the required things to
    # successfully emit drop constraints and tables commands for postgres (based
    # on the actual schema of the running instance)
    meta = MetaData()
    tables = []
    all_fkeys = []

    for table_name in inspector.get_table_names():
        fkeys = []

        for fkey in inspector.get_foreign_keys(table_name):
            if not fkey["name"]:
                continue

            fkeys.append(ForeignKeyConstraint((), (), name=fkey["name"]))

        tables.append(Table(table_name, meta, *fkeys))
        all_fkeys.extend(fkeys)

    for fkey in all_fkeys:
        con.execute(DropConstraint(fkey))

    for table in tables:
        con.execute(DropTable(table))

    trans.commit()

url = f'postgresql+asyncpg://{env.DBUSER}:{env.DBPASSWORD}@{env.DBHOST}:{env.DBPORT}/{env.DBNAME}'

engine = create_async_engine(
    url, 
    future=True,
    echo=False,
    pool_pre_ping=True
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


# def db_insert_default_values():
#     connection = psycopg2.connect(
#         user=env.DBUSER, 
#         password=env.DBPASSWORD, 
#         database=env.DBNAME, 
#         host=env.DBHOST, 
#         port=env.DBPORT
#     )
#     add_new_admin(
#             'admin',
#             'admin',
#             'admin',
#         )
#     DELETE 
#     commands = [
#         "INSERT INTO statuses VALUES ('1', 'added on website');",
#         "INSERT INTO statuses VALUES ('2', 'added response on advert');",
#         "INSERT INTO statuses VALUES ('3', 'declined response');",
#         "INSERT INTO statuses VALUES ('4', 'in working');",
#         "INSERT INTO statuses VALUES ('5', 'offer a job');",
#         "INSERT INTO statuses VALUES ('6', 'declined a job');",
#         "INSERT INTO statuses VALUES ('7', 'work finished');",
#         "INSERT INTO parameters VALUES('city', 'city of advert(optional)');"
#         "INSERT INTO parameters VALUES('category', 'category of advert');",
#     ]
    
#     curs = connection.cursor()

#     for com in commands:
#         curs.execute(com)

#     connection.commit()
#     connection.close()


def db_create() -> None:
    if env.RESET_DB == 'True':
        sync_url = f'postgresql://{env.DBUSER}:{env.DBPASSWORD}@{env.DBHOST}:{env.DBPORT}/{env.DBNAME}'
        sync_engine = create_engine(sync_url)
        drop_everything(sync_engine)
        Base.metadata.create_all(sync_engine)
        # db_insert_default_values()
        print('Database reseted')
    else:
        print('Database up-to-date')
