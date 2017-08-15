import MySQLdb as db

class DBManager:
	def __init__(self):
		db_con = db.connect('localhost','root','carrot24','Chef')
		self.cursor = db_con.cursor()
		
	def getMeals(self,category=False):
		if category:
			self.cursor.execute("select * from meal where category='%s'"%category)
		else:
			self.cursor.execute("select * from meal")

		tray = self.cursor.fetchall()
		result = []
 
		for item in tray:
			result.append([str(item[0]),str(item[1]),float(item[2]),int(item[3])])

		return result
