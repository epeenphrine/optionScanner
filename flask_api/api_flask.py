from flask import Flask, request, render_template, jsonify
from option_scripts.filter_json import get_callies 
from flask_cors import CORS
import json


#from callie_scripts.make_options_req import MakeRequest 
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    message = "" 
    return "home"

#example : yourip:5000/api/callieSpreads?days=20&goldenRatio=.7&volume=50
@app.route('/callieSpreads', methods=['GET', 'POST'])
def callie_spreads():
    if request.method == 'POST':
        print('in post ')
        return 'something'
    if request.method == 'GET':
        days = request.args.get('days', 14, int)
        goldenRatio = request.args.get('goldenRatio', .65,type=float)
        totalVolume = request.args.get('totalVolume', 500,  type=int)
        openInterest = request.args.get('openInterest', 1000, type=int)
        option_filter = get_callies(
            date_delta=days,
            goldenRatio=goldenRatio,
            totalVolume=totalVolume, 
            openInterest=openInterest,
            )
        data = option_filter
        return jsonify(data) 

@app.route('/optionsArbitrage', methods=['GET', 'POST'])
def options_arbitrage():
    if request.method == "POST":
        arbRatio = request.args.get('arbRatio', .5, type =float)
        ticker = request.args.get('ticker', None, type=str) 
    pass
@app.route('/sp500/options/rawData', methods=['GET'])
def rawData():
    if request.method == "GET":
        with open('callie_scripts/option_chains_list.json', 'r') as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

@app.route('/ipo/thisWeek', methods=['GET'])
def ipoThisWeek():
    if request.method == "GET":
        with open("scrapers/json/this_week.json", "r") as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

@app.route('/ipo/nextWeek', methods=['GET'])
def ipoNextWeek():
    if request.method == "GET":
        with open("scrapers/json/next_week.json", "r") as f:
            jsonObject = json.load(f)
        return jsonify(jsonObject)

#@app.route('/api/makeTdaRequest', methods=['GEt', 'POST'])
#def makeTdaRequest():
    #if request.method =='GET':
        #start_tda_request = MakeRequest 
        #return "finished running script"
if __name__ == "__main__":
    app.run(host="0.0.0.0")