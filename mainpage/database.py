from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import click
from flask.cli import with_appcontext

#engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
engine=create_engine("mysql+pymysql://root:2020@localhost:3306/test",echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import mainpage.models
    Base.metadata.create_all(bind=engine)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    #app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)