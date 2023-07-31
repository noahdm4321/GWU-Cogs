import json

## Database functions to call in cogs ##

## read database ##
def read(key, id):
	with open('database/db.json', "r") as json_file:
		data = json_file.read()
	data = json.loads(data)
	return data[key][id]

## write to database ##
def write(key, id, value):
	with open("database/db.json", "r") as json_file:
		data = json_file.read()
	data = json.loads(data)
	data[key][id] = value
	with open("database/db.json", "w") as json_file:
		json.dump(data, json_file)
	return True

## append to database list ##
def append(key, id, value):
	with open("database/db.json", "r") as json_file:
		data = json_file.read()
	data = json.loads(data)
	data[key][id] = data[key][id].append(value)
	with open("database/db.json", "w") as json_file:
		json.dump(data, json_file)
	return True