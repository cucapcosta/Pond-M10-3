from sqlmodel import create_engine, Session, SQLModel

engine = create_engine("sqlite:///my_database.db", echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
