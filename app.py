from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///the_eye.db'
db = SQLAlchemy(app)

# Database Model
class Events(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    application = db.Column(db.String(80), unique=False, nullable=False) # The calling application. Currently this is randomly generated number
    session_id = db.Column(db.String(80), unique=False, nullable=False) # session id that is handled by application
    category = db.Column(db.String(120), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False) # timestamp from event and not internal timestamp
    data = db.Column(db.JSON) # JSON column type to store JSON formatted data. Allows easy querying


@app.route("/")
def index():
    return "Index Page"

@app.route("/api/the_eye", methods=['POST'])
def the_eye():
    # retrieve json from post
    json_data = request.get_json()

    # Data Validation
    if json_data.get('session_id') and json_data.get('category') and json_data.get('name') and json_data.get('timestamp') and json_data.get('data'):
        event = Events(
            application = f'{random.randint(1,99999999)}',
            session_id = json_data['session_id'],
            category = json_data['category'],
            name = json_data['name'],
            timestamp = datetime.datetime.fromisoformat(json_data['timestamp']),
            data = json_data['data']
            )
        db.session.add(event)
        db.session.commit()

        return "Received"

    else:
        return "Failed Validation"


if __name__ == '__main__':
    # run app in debug mode on port 5000 - http://127.0.0.1:5000
    app.run(debug=True, port=5000)    