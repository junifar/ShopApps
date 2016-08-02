import sys
from flask import Flask
import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# engine = create_engine("mysql+pymysql://root@192.168.1.155/atk-django", isolation_level="READ UNCOMMITTED")
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))

# Base = declarative_base()
# Base.query = db_session.query_property()


# class Item(Base):
#     __tablename__ = 'auth_permission'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))

#     def __init__(self, name=None):
#         self.name = name

#     def __repr__(self):
#         return '<Item %r>' % self.name


@app.route("/")
def hello():
    # response = requests.get('http://localhost:8000/member/?format=json', auth=('admin', 'janganlagi'))
    # data = response.json()

    # session = requests.session()
    # session.auth = ('admin', 'janganlagi')

    # r = session.get('http://localhost:8000/member/?format=json', auth=('admin', 'janganlagi'))
    # print(r.content)

    # r = session.get('http://localhost:8000/users/?format=json')
    # print(r.content)

    # try:
    #     engine.connect()
    # except engine.exc.OperationalError as pesan:
    #     sys.exit(pesan[0].strip())

    # sql = "SELECT * FROM auth_permission"
    # q = engine.execute(sql)

    # print(Item.query.all())
    # for row in q:
    #     print(row)

    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
