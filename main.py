from sqlalchemy import create_engine,Column,String,INTEGER
from sqlalchemy.orm import declarative_base,Session,sessionmaker
from fastapi import FastAPI,Depends
app=FastAPI()
DATABASE_URL="sqlite:///./test.db"
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)
sessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
class Todo(Base):
    __tablename__="todos"
    id=Column(INTEGER,primary_key=True,index=True)
    title=Column(String)
    completed=Column(String)
Base.metadata.create_all(bind=engine)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def get_db(db:Session=Depends(get_db)):
    return {
        "message":"db connection find"
    }