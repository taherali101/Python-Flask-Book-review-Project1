# CS50W Project 1

## Web Programming with Python and JavaScript
### https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/

## Use the app on Heroku

### https://taher-project1-books.herokuapp.com/login

## Usage

* Register
* Search books by name, author or ISBN
* Get info about a book and submit your own review!

## :gear: Setup your own

```bash
# Clone repo
$ git clone https://github.com/taherali101/Python-Flask-Book-review-Project1.git

$ cd project1

# Create a virtualenv (Optional but reccomended)
$ python3 -m venv myvirtualenv

# Activate the virtualenv
$ source myvirtualenv/bin/activate (Linux)
myvirtualenv\Scripts\activate(windows)

# Install all dependencies
$ pip install -r requirements.txt

# ENV Variables
$ export FLASK_APP = application.py # flask run
$ export DATABASE_URL = Heroku Postgres DB URI
$ export GOODREADS_KEY = Goodreads API Key. # More info: https://www.goodreads.com/api
```

### DB Schema

Feel free to add your own improvements!
![DB](https://i.imgur.com/ii6nkNr.png)
