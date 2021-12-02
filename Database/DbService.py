import sqlite3
from pydantic import BaseModel
import datetime

connection = sqlite3.connect("events.db")


class AlertToInsert(BaseModel):
    source: str
    date: datetime.datetime
    message: str


connection_cursor = connection.cursor()


def insert_alert(alert: AlertToInsert):
    connection2 = sqlite3.connect("events.db")
    connection_cursor2 = connection.cursor()
    print("siema")
    with connection2:
        print("siema2")
        connection_cursor2.execute(
            f"INSERT INTO events (source, date, message) VALUES ('{alert.source}', '{alert.date.strftime('%m/%d/%Y, %H:%M:%S')}', '{alert.message}')")


def select_alerts():
    with connection:
        connection_cursor.execute(
            "SELECT * from events")
    return connection_cursor.fetchall()


#insert_alert(AlertToInsert(source="x", date=datetime.datetime.now(), message="result[2]"))
xd = select_alerts()
print(xd)
