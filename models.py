from os import getenv

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from dotenv import load_dotenv
load_dotenv()

# Bazaga ulanish
# engine = create_engine("database+driver://user:password@host:port/database")

DB_USER = getenv("DB_USER")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")
DB_HOST = getenv("DB_HOST")
DB_PASSWORD = getenv("DB_PASSWORD")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

Base = declarative_base()

# Modelni qurish
class User(Base):
     __tablename__ = "users"
     id: Mapped[int] = mapped_column(BigInteger,primary_key=True, autoincrement=True)
     first_name: Mapped[str] = mapped_column(String(30))
     words: Mapped[list["Word"]] = relationship(back_populates="user")

class Word(Base):
     __tablename__ = "words"
     id: Mapped[int] = mapped_column(primary_key=True)
     word: Mapped[str] = mapped_column(Text)
     user_id:Mapped[int] = mapped_column(BigInteger,ForeignKey("users.id", ondelete="CASCADE"))
     user: Mapped[User] = relationship(back_populates="words")

# Jadvalni yaratish
Base.metadata.create_all(engine)
