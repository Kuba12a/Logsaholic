from . import FileManager as file_manager
import datetime
import HttpClient.HttpClient as http_client
from pprint import pprint
import Database.DbService as db
import Model.Alert as alert_model

detection_rules = __import__('detection-rules')


def scan_files(files, rules, firewall_address, host_address):
    print(files)
    print(rules)
    event_number = 1
    log_message = []
    method = getattr(detection_rules, rules[0])
    result = method("example_files/wireshark_pcap.pcapng")

    for r in rules:
        for f in files:
            method = getattr(detection_rules, r)
            result = method(f)

            log_message.append("Event number:" + str(event_number))
            log_message.append("Alert source : " + f)
            log_message.append("Alert rule : " + r)
            log_message.append("Alert type : " + result[0])
            log_message.append("Alert description : " + result[2])

            if (result[0] == "local"):  # wypisz na CLI, do loga i do SQL
                db.insert_alert(db.AlertToInsert(source=f, date=datetime.datetime.now(), message=result[2]))
                print("\n Added to sql database\n")
                # save_to_sql_database

            elif (result[0] == "remote"):  # wypisz na CLI, do loga, do SQL i wyśli do zdalnego hosta
                db.insert_alert(db.AlertToInsert(source=f, date=datetime.datetime.now(), message=result[2]))
                http_client.send_alert(host_address,
                                       alert_model.Alert(alert_id=event_number, source=f,
                                                         date=str(datetime.datetime.now()), message=result[2]))
                print("\n Added to sql database and sent to remote host\n")
                # save_to_sql_database
                # send_description_to_remote(result[2])

            if (result[1]):  # Jesli action_block = True
                http_client.send_alert(firewall_address,
                                       alert_model.Alert(alert_id=event_number, source=f,
                                                         date=str(datetime.datetime.now()), message=result[2]))
                log_message.append("Sending firewall rules to remote host")
                # send_firewall_rules_to_remote()

            log_message.append("")
            log_message.append("")
            event_number += 1
    pprint(log_message)  # Wyświetl na CLI
    file_manager.write_log(log_message)  # Zapis loga z przeprowadzonych skanow

# except Exception as ex:

# template = "An exception of type {0} occurred. Arguments:\n{1!r}"
# message = template.format(type(ex).__name__, ex.args)
# print(message)
