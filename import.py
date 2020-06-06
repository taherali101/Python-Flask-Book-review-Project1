import os, csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# database engine object from SQLAlchemy that manages connections to the database
engine = create_engine(os.getenv("DATABASE_URL"))

# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate
db = scoped_session(sessionmaker(bind=engine))

file = open("books.csv")

reader = csv.reader(file)
def main():
    # these commands are just used to fix mistakes!!

    # db.execute("DROP TABLE users;")
    # db.execute("DROP TABLE reviews;")
    # db.execute("DROP TABLE books;")
    # db.execute("ALTER TABLE users RENAME COLUMN password TO hash;")
# print(f"DELETED FROM database.")
# db.commit()
    
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL)")
    db.execute("CREATE TABLE books (id SERIAL PRIMARY KEY NOT NULL, isbn VARCHAR(10) NOT NULL, title TEXT NOT NULL,author TEXT NOT NULL, year VARCHAR(4) NOT NULL)")
    db.execute("CREATE TABLE reviews (id SERIAL PRIMARY KEY NOT NULL, user_id INT NOT NULL,book_id INT NOT NULL, comment TEXT NOT NULL, rating INT NOT NULL,time TIMESTAMP(6))")
    

    f=open("books.csv")
    reader =csv.reader(f)
    for isbn,title,author,year in reader:
    	db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})
                   
    	print(f"Added {title} to the database")
        db.commit() 

if __name__ == "__main__":
	main()