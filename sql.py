# sql.py - Create a SQLite3 table and populate it with data


import sqlite3

# create a new db if the db doesn't already exist
with sqlite3.connect("blog.db") as connection:

	# get a cursor object used to execute SQL commands
	c = connection.cursor()

	# create a table
	c.execute('CREATE TABLE posts(name TEXT, post TEXT, date TEXT)')
	
	# create a list of dummy data, i.e. a list of tuples
	posts_data = [("Zev", "Today we\'ll try to create a flask blog from scratch", "04-16-15"),
			("Brandon", "OK, let\'s get it done!", "04-16-15"),
			("Tom", "1 hour time limit?", "04-16-15"),
			("Mark", "Yeah that should be doable.", "04-16-15"),
			("Holden", "Hmm... we\'ll see about that.", "04-16-15")]
   
	# insert dummy data into the db table 
	c.executemany('INSERT INTO posts VALUES(?, ?, ?)', posts_data)
