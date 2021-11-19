from main import event_detection
from . import FileManager as file_manager
from pprint import pprint


#Jakos ten import tylko konkretnych detection-rules __import__ cos tam



def scan_files(files, rules):
    event_number = 1
    log_message = []
    try:
        for f in files:
            for r in rules:
                #Wykonaj skan przy użyciu reguły r na pliku f
                #result = detection-rules.regula_1(f) -> zwraca tablice 3 informacji : action_alert, action_block i description i na ich podstawie dalsze działania
                
                result = ["local", True, "Odpowiednia deskrypcja eventu"]    #Przykładowy return ze skanu
                
                log_message.append("Event number:"+ str(event_number))
                log_message.append("Alert source : " + f)
                log_message.append("Alert rule : "+r)
                log_message.append("Alert type : " + result[0])
                log_message.append("Alert description : "+ result[2])
                
                if(result[0]=="local"): #wypisz na CLI, do loga i do SQL                                 
                    print("\n Added to sql database\n")
                    #save_to_sql_database
                
                elif(result[0]=="remote"): #wypisz na CLI, do loga, do SQL i wyśli do zdalnego hosta
                    print("\n Added to sql database and sent to remote host\n")    
                    #save_to_sql_database
                    #send_description_to_remote(result[2])

                if(result[1]): #Jesli action_block = True
                    log_message.append("Sending firewall rules to remote host")                    
                    #send_firewall_rules_to_remote()

                
                log_message.append("")
                log_message.append("")
                event_number+=1
        pprint(log_message)                  #Wyświetl na CLI
        file_manager.write_log(log_message) #Zapis loga z przeprowadzonych skanow

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)