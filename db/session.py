from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


engine = create_engine(
    'mysql+pymysql://user:password@localhost:3306/database',
    pool_pre_ping=True,
    pool_recycle=3600,
)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
