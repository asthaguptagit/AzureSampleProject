from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL
from orm.Entity import User


class DBService():

    def __init__(self):
        self.url = URL.create("postgresql+psycopg2",username="postgres",password="root",host="localhost",database="postgres",port="5432")
        self.engine = engine = create_engine(self.url)
    
    def persist_obj(self,obj):
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()
    
    def get_user_by_id(self,email,password):
        session:Session = sessionmaker(bind=self.engine)
        session.query(User).filter_by(email=email,password=password)

        
