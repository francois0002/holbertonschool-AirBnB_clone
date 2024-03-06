#!/usr/bin/python3
import models from BaseModel

class User(BaseModel):
	email = charField()
	password = charField()
	first_name = charField()
	last_name = charfield()

