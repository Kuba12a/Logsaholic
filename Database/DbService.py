import sqlite3
from pydantic import BaseModel
import datetime




class AlertToInsert(BaseModel):
    source: str
    date: datetime.datetime
    message: str




def insert_alert(alert: AlertToInsert):
    connection = sqlite3.connect("events.db")
    connection_cursor = connection.cursor()
    with connection:
        connection_cursor.execute(
            "CREATE TABLE IF NOT EXISTS events (event_id int PRIMARY KEY , source test, date text, message text)")
        connection_cursor.execute(
            f"INSERT INTO events (source, date, message) VALUES ('{alert.source}', '{alert.date.strftime('%m/%d/%Y, %H:%M:%S')}', '{alert.message}')")



def select_alerts():
    connection = sqlite3.connect("events.db")
    connection_cursor = connection.cursor()
    with connection:
        connection_cursor.execute(
            "SELECT * from events")
    return connection_cursor.fetchall()


#insert_alert(AlertToInsert(source="x", date=datetime.datetime.now(), message="result[2]"))
#xd = select_alerts()
#print(xd)
