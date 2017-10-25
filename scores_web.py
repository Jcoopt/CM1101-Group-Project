import sqlite3 # imports the SQLite3 library for accessing the database of scores
import flask # imports the flask framework to serve as te webserver

app = flask.Flask(__name__) # sets up flask


@app.route('/') # landing page of webserver
def index(): # defines the content of the landing page
    SQLcursor =get_db().cursor()
    data= SQLcursor.execute('SELECT * FROM Scores ORDER BY Time')
    formattedData=[]
    for row in data:
        formattedData.append("{} - {}".format(row[0],round(row[1],4))) # displays the correctly formatted name and time

    return flask.render_template('scores.html', score=formattedData) # access a HTML template to aid in display.

@app.teardown_appcontext # for closing connection to database
def close_Connection(exception):
    db = getattr(flask.g, '_database', None)
    if db is not None:
        db.close()


def get_db():# creates connection to the scores database
    db=getattr(flask.g,'_database',None)
    if db is None:
        db=flask.g._database=sqlite3.connect('Scores.db')
    return db

app.run()