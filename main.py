# from sqlalchemy import create_engine,Column,String,INTEGER
# from sqlalchemy.orm import sessionmaker,declarative_base,Session
# from fastapi import FastAPI,Depends
# app=FastAPI()

# #DATABASE URL
# DATABASE_URL="sqlite:///./text.db"

# #Engine create (DB connection)
# engine=create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread":False}
# )

# #Session (DB operation ka liya)
# SessionLocal=sessionmaker(bind=engine)

# #Base (model ka liya)
# Base=declarative_base()

# #Table (Model)
# class Todo(Base):
#     __tablename__="todos"
#     id=Column(INTEGER,primary_key=True,index=True)
#     table=Column(String)
#     completed=Column(String)

# #Table create
# Base.metadata.create_all(bind=engine)

# #Dependency (DB session provide karege)
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine,Column,String,INTEGER
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI,Depends
app=FastAPI()
DATABASE_URL="sqlite:///./test.db"
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
class Todo(Base):
    __tablename__="todos"
    id=Column(INTEGER,primary_key=True,index=True)
    title=Column(String)
    completed=Column(String)
Base.metadata.create_all(bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def get_db(db:Session=Depends(get_db)):
    return {
        "message":"DB connected fine."
    }