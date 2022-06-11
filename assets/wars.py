from json import load, dump
from datetime import datetime
import assets.players 

def access_war():
    with open("assets/data/wars.json", 'r') as f:
        return load(f)

def write_war(data):
    with open("assets/data/wars.json", 'w') as f:
        dump(data, f, indent=4)
    
def is_there_war():
    data = access_war()
    if data == {}:
        return False
    return True


    

def someone_dead(current_time: datetime) -> dict:
    data = access_war()
    for key, value in data.items():
        if key == "wars": continue
        
        if key["end"] <= current_time:
            attributes = data[key]
            del data[key]
            players.add_defeat(attributes["defender"])
            players.add_victory(attributes["attacker"])
            players.modify_hp(attributes["defender"], -10)
            return (True, attributes)
    return (False)

def get_war_info(attributes: dict) -> str:
    text = f"""
__War {attributes['id']} was **won** by {players.ping(attributes['attacker'])}__

*Start of the war*: `{str(attributes['start'])}`

*{players.ping(attributes['defender'])}* hadn't responded for `{str(attributes["end"])}` 
-> **He loses 10HP! ** 
 """



def del_war(id):
    data = access_war()
    for key, value in data.items():
        if key["id"] == id:
            del data[key]
    write_war(data)

def add_war(attacker, defender):
    data = access_war()
    add_number_of_war()
    now = datetime.now()
    last_moment =  now + datetime. timedelta(min = 5)
    attributes = {
        "attacker": attacker,
        "defender": defender, 
        "start": now,
        "end": last_moment,
        "id": get_number_of_war()
        }
    data[f"{get_number_of_war()}: | {attacker} VS {defender} |"] = attributes
    write_war(data)

def add_number_of_war():
    data = access_war()
    data["wars"] += 1
    write_war(data)

def get_number_of_war():
    data = access_war()
    return data["wars"]