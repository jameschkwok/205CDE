from flask import Flask, redirect, url_for, render_template, request, session, flash

import pymysql

app = Flask(__name__)
app.secret_key = 'secre_key'

db = pymysql.connect("localhost", "phpmyadmin", "evangelion", "book" )
conn = pymysql.connect("localhost", "phpmyadmin", "evangelion", "book" )

@app.route('/logining', methods =  ['POST','GET'])
def logining():
	if request.method == 'POST':
		username = request.form.get("username")
		pwd = request.form.get("pwd")
		email = request.form.get("email")
		checkemail = None
		cursor = db.cursor()

		sql = ("SELECT * FROM `customer` WHERE `email` = '"+email+"' ")
 
		cursor.execute(sql)
	    
		db.commit()
		check = cursor.fetchall()
		for row in check:
			checkemail = row[2]

		if 	request.form['email'] == checkemail:
			if request.form['pwd'] == row[1]:

				print ("success login")
		
			
				results = cursor.fetchall()
				print(results)
				session['email'] = row[2]
				return render_template ('logined.html')

			else:
				return render_template('wrongpwd.html')

		else :

			return render_template('New_arrivals.html')

	




@app.route('/Register', methods = ["POST","GET"])
def Register():
	if request.method == "POST":
		username = request.form.get("username")
		pwd = request.form.get("pwd")
		email = request.form.get("email")

		cursor = db.cursor()

		sql = ''' 
		INSERT INTO customer(username, password, email) 
		VALUES ('%s', '%s', '%s') 
		'''
		cursor.execute(sql% (username, pwd, email))
		db.commit()
		return render_template('login.html')
	return render_template('Register.html')

		
						
@app.route("/logout", methods = ['POST', 'GET'])
def logout():
	session.pop('email', None)
	return render_template('index.html')


@app.route("/storeincar", methods = ['POST', 'GET'])
def storeincar():
	if request.method == "POST":
		Title = request.form.get("Title")
		Author = request.form.get("Author")
		Price = request.form.get("Price (HK)")

		cursor = conn.cursor()

		sql = ''' 
		INSERT INTO cart (Title, Author ,Price (HK) ) 
		VALUES ('%s', '%s', '%s') ''' 

		cursor.execute(sql% (Title, Author, Price))
		results = cursor.fetchall()

		conn.commit()

		return render_template('Language.html')

	elif 'user' not in session:
		return render_template('login.html')

	else:
		return render_template('Shopping_cart.html')








@app.route("/car", methods = ['POST', 'GET'])
def car():

	cursor = conn.cursor()

	sql = "SELECT * FROM cart"
	cursor.execute(sql)
	books = cursor.fetchall()

	for row in goods:
		Title = row[0]
		Author = row[1]
		Price  = row[2]

		conn.commit()

	return render_template("Shopping_cart.html", Title = Title,
	 Author=Author, Price=Price)
	





@app.route('/index', methods = ['POST', 'GET'])
def index():
	return render_template('index.html')


@app.route('/New_arrivals', methods = ['POST', 'GET'])
def New_arrivals():
	return render_template('New_arrivals.html')


@app.route('/Fiction', methods = ['POST', 'GET'])
def Fiction():
	return render_template('Fiction.html')


@app.route('/General', methods = ['POST', 'GET'])
def General():
	return render_template('General.html')


@app.route('/Language', methods = ['POST', 'GET'])
def Language():
	return render_template('Language.html')


@app.route('/Non_Fiction', methods = ['POST', 'GET'])
def Non_Fiction():
	return render_template('Non_Fiction.html')


@app.route('/Science', methods = ['POST', 'GET'])
def Science():
	return render_template('Science.html')


@app.route('/Contact', methods = ['POST', 'GET'])
def Contact():
	return render_template('Contact.html')


@app.route('/Shopping_cart', methods = ['POST', 'GET'])
def Shopping_cart():
	return render_template('Shopping_cart.html')


@app.route('/logined', methods = ['POST', 'GET'])
def logined():
	return render_template('logined.html')


@app.route('/memberlogin', methods = ['POST', 'GET'])
def memberlogin():
	return render_template('memberlogin.html')


@app.route('/wrondpwd', methods = ['POST', 'GET'])
def wrongpwd():
	return render_template('wrongpwd.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
	if 'email' in session:
		return render_template ('memberlogin.html')
	else:

		return render_template('login.html')


@app.route('/thx', methods = ['POST', 'GET'])
def thx():
	return render_template('thx.html')

if __name__ == '__main__':
	app.run(debug = True)
