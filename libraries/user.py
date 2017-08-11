import asyncio

import os
import pickle
import datetime

fileName = "./save.data"

#######################################################################################################################

class User:
	def __init__(self):
		# self.joinDate = joinDate
		self.counter = 0
	def add(self):
		self.counter += 1
	def get(self):
		return self.counter

def dataUpdate(data, objet, id):
	dt = {str(id):objet}
	data.update(dt)

def dataRemove(data, id):
	try:
		del data[str(id)]
	except KeyError:
		raise KeyError("User data not found")

def getFromData(data, id):
	try:
		get = data[str(id)]
		return get
	except KeyError:
		return None

def dataSave(data):
	f = open(fileName, "wb")
	p = pickle.Pickler(f)
	p.dump(data)
	f.close()

def dataGet():
	if os.path.exists(fileName):
		f = open(fileName, "rb")
		d = pickle.Unpickler(f)
		data = d.load()
		f.close()
	else:
		data = {}

	return data

#######################################################################################################################