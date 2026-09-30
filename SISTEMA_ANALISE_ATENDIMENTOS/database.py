from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# ==========================================
# CONFIGURAÇÕES DO BANCO DE DADOS
# ==========================================

DB_USER = "root"
DB_PASSWORD = "SENHA_REMOVIDA"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "atendimentos_db"


# ==========================================
# TRATAMENTO DA SENHA
# ==========================================

# Permite utilizar caracteres especiais na senha,
# como @, #, %, ! etc.
DB_PASSWORD_ENCODED = quote_plus(DB_PASSWORD)


# ==========================================
# URL DE CONEXÃO
# ==========================================

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ENCODED}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# ==========================================
# CRIAÇÃO DA CONEXÃO
# ==========================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# ==========================================
# SESSÃO DO BANCO
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================
# CLASSE BASE DOS MODELOS
# ==========================================

Base = declarative_base()


# ==========================================
# DEPENDÊNCIA PARA O FASTAPI
# ==========================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ==========================================
# TESTE DE CONEXÃO
# ==========================================

if __name__ == "__main__":

    try:

        with engine.connect() as connection:
            print("Conexão com o MySQL realizada com sucesso!")

    except Exception as erro:

        print("Erro ao conectar ao MySQL:")
        print(erro)