ConsumerAffairs-Practical-Test

Conclusion:
When creating this service, it is assumped that the applications utilizing this service are all authenticated. The service doesn't verify any authentication.
Sessions are being handled by the calling application so no verification was added and are written to the Events table as is.

The database structure only has the rowid as the primary key. All other columns were left as non-unique as applications, sessions, names, and data can be sent multiple times.

I utilized Redis / Celery to handle the # of events / sec. To quickly release the calling application from waiting for a reply, the service needed to return a reply as soon as possible.
The /api/the_eye route's only task should be to pass on the JSON data to a celery worker and then return back a response. This leaves the more expensive tasks to the background celery workers.

Putting the service data into a database allows the analytics team query all the events captured. I used SQLAlchemy to hook into a SQLite3 database for testing purposes, but the intent was to utilize SQLAlchemy to hook into a production grade database of choice for the analytics team.
The Events.data column type of JSON was used to capture and store the "data" portion of the JSON post. I chose this because the structure at first did not seem consistent. This data type allows the DB to store any type of JSON structure and allows the analytics team to easily extract the data.

Install:

pip install -r requirements.txt

from app import db

db.create_all()
