import requests
import Model.Alert as Alert
import json
import datetime


def send_alert(URL, alert: Alert):

    data = json.dumps(alert.__dict__)

    response = requests.post(url=URL, data=data)

    # extracting data in json format
    status_code = response.status_code
    return status_code