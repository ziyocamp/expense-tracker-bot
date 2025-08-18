from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

from .connection import engine

SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_session():
    """
    Yields a new session and ensures it's properly
    committed/rolled back and closed.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
