from flask import Flask, request, render_template
import connector

app = Flask(__name__)

@app.route('/', methods=['Get'])
@app.route('/<string:username>', methods=['Get'])
def index(username = False):
	return render_template('home.html')

@app.route('/menu/', methods=['Get'])
@app.route('/<string:username>/menu/')
def menu(username=False):
	breakfast = connector.DBManager().getMeals("BreakFast")
	salads = connector.DBManager().getMeals("Salads")
	cont_loc = connector.DBManager().getMeals("Continental & Local")
	local = connector.DBManager().getMeals("Local")
	saubbq = connector.DBManager().getMeals("Sauce & BBQ")
	if not username:
		return render_template('menu1.html',breakfast=breakfast, salads=salads, cont_loc=cont_loc, local=local, saubbq=saubbq)
	return render_template('menu.html',username=username,breakfast=breakfast, salads=salads, cont_loc=cont_loc, local=local, saubbq=saubbq)

@app.route('/cart/', methods=['Get'])
@app.route('/<string:username>/cart/', methods=['Get'])
def cart(username=False):
	if not username:
		return "nothing to do here"
	content=connector.DBManager().getCartContent(username)
	return render_template('cart.html')

@app.route('/<string:username>/cart/add/<int:item>/', methods=['Get'])
def addItem(username,item):
	connector.DBManager().addToCart(username,item)
	return menu(username)

@app.route('/<string:username>/cart/order', methods=['Post'])
def order(username):
	#connector.DBManager().makeOrder(username)
	return "nothin here now"


def main():
	app.run(debug=True, port=8000)

if __name__=="__main__":
	main()
