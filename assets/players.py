from json import dump, load

def access_players():
    with open("assets/data/players.json", 'r') as f:
        return load(f)


def write_players(data):
    with open("assets/data/players.json", 'w') as f:
        dump(data, f, indent=4)

def ping(player_id):
    return f"<@{player_id}>"

def add_victory(id):
    data = access_players()
    data[id]["victories"] += 1
    write_players(data)

def add_defeat(id):
    data = access_players()
    data[id]["defeats"] += 1
    write_players(data)

def modify_hp(id, value):
    data = access_players()
    data[id]["hp"] += value
    write_players(data)

def modify_help(id, value):
    data = access_players()
    data[id]["help"] += value
    write_players(data)

def create_player(player_id):
    data = access_players()
    if player_id not in data:
        initial_attributes = {
        "hp": 100,
        "help": 10, 
        "defeats": 0,
        "victories": 0
        }
        data[player_id] = initial_attributes
        write_players(data)
    return False


