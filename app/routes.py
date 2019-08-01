from app import app
from flask import render_template, request, redirect
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/stockmarket')
def stockmarket():
    return render_template('stockmarket.html')
    
@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/aboutgame')
def aboutgame():
    return render_template('aboutgame.html')
    
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/cong')
def cong():
    return render_template('cong.html')
    
@app.route('/weather')
def weather():
    return render_template('weather.html')
    
@app.route('/shares', methods = ['GET', 'POST'])
def shares():
    if request.method == "GET":
        return "Please fill out the form."
    else:
        userdata = dict(request.form)
        print(userdata)
        all_shares = model.shares_calculator(userdata['symbol'], float(userdata['initial_balance']), userdata['day'])
        return render_template('shares.html', all_shares = all_shares, initial_day = userdata['day'], initial_balance = float(userdata['initial_balance']), symbol = userdata['symbol'])
        

@app.route('/finalbalance', methods = ['GET', 'POST'])
def finalbalance():
    if request.method == "GET":
        return "Please fill out the form."
    else:
        userdata = dict(request.form)
        total_sharesfinal = float(userdata['all_shares'])
        final_balance = round(model.balance_calculator(total_sharesfinal, float(userdata['shares']), userdata['symbol'], float(userdata['initial_balance']), userdata['initial_day'], userdata['sell_day']), 2)
        return render_template('finalbalance.html', finalbalance = final_balance, symbol = userdata['symbol'])
        
@app.route('/weatherfinal', methods = ['GET', 'POST'])
def weatherfinal():
    if request.method == "GET":
        return "Please fill out the form"
    else:
        userdata = dict(request.form)
        print(userdata)
        return "hi"