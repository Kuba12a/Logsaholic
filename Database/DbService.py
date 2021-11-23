import sqlite3
from pydantic import BaseModel
import datetime

connection = sqlite3.connect('events.db')


class Event(BaseModel):
    event_id: int
    source: str
    date: datetime.datetime
    message: str



connection_cursor = connection.cursor()


def insert_event(event: Event):
    with connection:
        connection_cursor.execute(
            f"INSERT INTO events VALUES ('{event.event_id}', '{event.source}', '{event.date.strftime('%m/%d/%Y, %H:%M:%S')}', '{event.message}')")

def select_events():
    with connection:
        connection_cursor.execute(
            "SELECT * from events")
    return connection_cursor.fetchall()
