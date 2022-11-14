from flask import *
from models import DBMapper 

# import sys
# sys.path.append('/Users/nandy/Git_repos/APP-Project/models/')
# app = Flask(__name__, template_folder="new_folder_name")

#move controllers to a folder and keep app.run() outside in a seperate folder and import app line down below 
app = Flask(__name__)

obj = DBMapper()

#Home-Page
@app.route("/")
def start_(): 
    return render_template("homepage.html")

#Query List Page
@app.route("/player_points")
def player_stat(): 
    return render_template("player_points.html")

#Q1 - Results Page 
@app.route("/form_player_points", methods = ["GET","POST"])
def form_player_points(): 
    name = request.form["player_name"]
    rows = obj.find_player_names(name)
    if len(rows) > 0 : 
        return render_template("s_player_points.html", rows=rows)
    else : 
        return render_template("failure_page.html")

#Q2 - Results Page
@app.route("/active_players", methods = ["GET","POST"])
def active_players(): 
    rows = obj.gsw_active_players()
    return render_template("s_active_players.html", rows=rows)

#Q3 - Results Page     
@app.route("/form_player_filter", methods = ["GET","POST"])
def form_player_filter(): 
    points = request.form["total_points"]
    rows = obj.gsw_points_filter(points)
    print(rows, type(rows))
    if len(rows) > 0 : 
        return render_template("s_player_filter.html", rows=rows)
    else : 
        return render_template("failure_page.html")

#Q4 - Results Page 
@app.route("/blocks_total", methods = ["GET","POST"])
def blocks_total(): 
    rows = obj.blocks_leader()
    return render_template("s_blocks_leader.html", rows=rows)


@app.route("/fg_percent_filter", methods = ["GET","POST"])
def form_player_fgs(): 
    fg_percent = request.form["fg_percent"]
    rows = obj.fg_percent_filter(fg_percent)
    print(rows, type(rows))
    if len(rows) > 0 : 
        return render_template("s_fg_percent.html", rows=rows)
    else : 
        return render_template("failure_page.html")

app.run(debug=True, port=5001)