from flask import Flask, request, render_template
import connector

app = Flask(__name__)

@app.route('/', methods=['Get'])
def index():
	return render_template('home.html')

@app.route('/menu/', methods=['Get'])
def menu():
	breakfast = connector.DBManager().getMeals("BreakFast")
	salads = connector.DBManager().getMeals("Salads")
	
	return render_template('menu.html',breakfast=breakfast, salads=salads)

@app.route('/cart/', methods=['Get'])
def cart():
	return "display cart content"

@app.route('/cart/order', methods=['Post'])
def order():
	return "nothin here now"


def main():
	app.run(debug=True, port=8000)

if __name__=="__main__":
	main()
