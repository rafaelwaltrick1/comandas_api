from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import STR_DATABASE

engine = create_engine(STR_DATABASE, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=True)
Base = declarative_base()

async def cria_tabelas():
    from infra.orm.FuncionarioModel import FuncionarioDB
    from infra.orm.ClienteModel import ClienteDB
    from infra.orm.ProdutoModel import ProdutoDB
    Base.metadata.create_all(bind=engine)

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()