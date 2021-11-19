def test_rule_low_risk(file):
    # ciało funkcji - właściwa reguła operująca na danych z args
    # procesowanie pcap
    # for pcap in kwargs[pcap]:
    # procesowanie evtx
    # for evtx in kwargs[evtx]:
    # procesowanie xml
    # for xml in kwargs[xml]:
    # procesowanie json
    # for json in kwargs[json]:
    # procesowanie txt
    # for txt in kwargs[txt]:
    # ostateczna reguła - tj. co ma się wykonać

    condition = True

    if condition == True:
        action_alert = "local" # akcja: "local", "remote"
        action_block = False # or False
        description = "Opis eventu, low risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description



def test_rule_medium_risk(file):
    # ciało funkcji - właściwa reguła operująca na danych z args
    # procesowanie pcap
    # for pcap in kwargs[pcap]:
    # procesowanie evtx
    # for evtx in kwargs[evtx]:
    # procesowanie xml
    # for xml in kwargs[xml]:
    # procesowanie json
    # for json in kwargs[json]:
    # procesowanie txt
    # for txt in kwargs[txt]:
    # ostateczna reguła - tj. co ma się wykonać

    condition = True

    if condition==True:
        action_alert = "remote" # akcja: "local", "remote"
        action_block = False # or False
        description = "Opis eventu, medium risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description\

    
def test_rule_high_risk(file):
    # ciało funkcji - właściwa reguła operująca na danych z args
    # procesowanie pcap
    # for pcap in kwargs[pcap]:
    # procesowanie evtx
    # for evtx in kwargs[evtx]:
    # procesowanie xml
    # for xml in kwargs[xml]:
    # procesowanie json
    # for json in kwargs[json]:
    # procesowanie txt
    # for txt in kwargs[txt]:
    # ostateczna reguła - tj. co ma się wykonać

    condition = True

    if condition==True:
        action_alert = "remote" # akcja: "local", "remote"
        action_block = True # or False
        description = "opis Eventu, high risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description




def test_rule_no_risk(file):
    # ciało funkcji - właściwa reguła operująca na danych z args
    # procesowanie pcap
    # for pcap in kwargs[pcap]:
    # procesowanie evtx
    # for evtx in kwargs[evtx]:
    # procesowanie xml
    # for xml in kwargs[xml]:
    # procesowanie json
    # for json in kwargs[json]:
    # procesowanie txt
    # for txt in kwargs[txt]:
    # ostateczna reguła - tj. co ma się wykonać

    condition = False

    if condition==True:
        action_alert = "local" # akcja: "local", "remote"
        action_block = False # or False
        description = "No dangers found" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description