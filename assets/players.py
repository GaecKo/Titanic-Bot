from json import dump, load

def access_players():
	with open("assets/data/players.json", 'r') as f:
		return load(f)


def write_players(data):
	with open("assets/data/players.json", 'w') as f:
		dump(data, f, indent=4)

def ping(player_id):
	return f"<@{player_id}>"

def create_player(player_id):
	data = access_players()
	if player_id not in data:
		initial_attributes = {
		"hp": 100,
		"help": 10, 
		"attacks" : 0,
		"win": 0,
		"attacked": 0,
		"defence": 0,
		"getting_attacked": False
		}
		data[player_id] = initial_attributes
		write_players(data)
	return False


