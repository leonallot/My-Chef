import MySQLdb as db

class DBManager:
	def __init__(self):
		self.db_con = db.connect('localhost','root','carrot24','Chef')
		self.cursor = self.db_con.cursor()

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

	#cart connections
	def addToCart(self,username,item):
		self.cursor.execute('insert into cart(user_id, meal_id) values ("%s", %s)'%(username,item))
		self.db_con.commit()

	def getCartContent(self,username):
		self.cursor.execute('select ml.name, ml.price, ct.quantity from meal as ml, cart as ct where ml.id = ct.meal_id')
		tray = self.cursor.fetchall()
                result = []
                for item in tray:
                        result.append([str(item[0]),float(item[1]),int(item[2])])
                return result

	def updateCartQuantity(self, username, quantity):
		self.cursor.execute('update cart set quantity = %s where meal_id=%s and username="%s"'%(quantity,username))
		self.db_con.commit()

	def clearCart(self,username):
		self.cursor.execute('delete from cart where user_id="%s"'%username)
	
	def removeItem(self,username,id):
		self.cursor.execute('delete from cart where user_id="%s" and meal_id=%s'%(username, id))

	#ordering
	def makeOrder(self):
		return "Done"

	def __exit__(self):
		self.db_con.close()
