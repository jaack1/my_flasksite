from flask import render_template
from flask import request
from app import app
from openpyxl import load_workbook

iplist = ['192.168.5.128','95.221.207.34', '89.208.212.254']

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Jack'}
	def get_user_ip():
		ip = request.headers.get('X-Real-IP')
		return ip
	ip = get_user_ip()
	return render_template("index.html",
		title = 'Home',
		user = user,
		ip = ip)


@app.route('/numbers')
def numbers():
	sotr1 = []
	sotr2 = []
	workbook = load_workbook('/home/jack/flasksite/app/en.xlsx')
	worksheet = workbook.get_active_sheet()
	def get_user_ip():
		ip = request.headers.get('X-Real-IP')
		return ip
	ip = get_user_ip()
	for row in worksheet:
		for cell in row:
			if cell.value is None:
				sotr2.append(' ')
			else:
				sotr2.append(str(cell.value))
		sotr1.append(sotr2)
		sotr2 = []
	if ip in iplist:
		return render_template("enums.html",
		title = 'Список внутренних номеров',
		sotr1 = sotr1)
	else:
		return render_template("accessdenied.html")
