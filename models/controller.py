from flask import request, render_template, Flask
from models import DBMapper

app = Flask(__name__)
obj = DBMapper()

#Home-Page
@app.route("/")
def start_():
    """
    Homepage route path.
    """
    return render_template("homepage.html")

#Query List Page
@app.route("/player_points")
def player_stat():
    """
    Path/Page where all the queries reside
    """
    return render_template("player_points.html")

#Q1 - Results Page 
@app.route("/form_player_points", methods = ["GET","POST"])
def form_player_points():
    """
    Path/Page to parse the input of Q1 and return the respective values in an object format.
    """
    name = request.form["player_name"]
    rows = obj.find_player_names(name)
    if len(rows) > 0 :
        return render_template("s_player_points.html", rows=rows)    
    return render_template("failure_page.html")

#Q2 - Results Page
@app.route("/active_players", methods = ["GET","POST"])
def active_players():
    """
    Path/Page to return the list of active players of the club GSW.
    """
    rows = obj.gsw_active_players()
    return render_template("s_active_players.html", rows=rows)

#Q3 - Results Page
@app.route("/form_player_filter", methods = ["GET","POST"])
def form_player_filter():
    """
    Path/Page to parse the input of Q3 and return the respective values in an object format.
    """
    points = request.form["total_points"]
    rows = obj.gsw_points_filter(points)
    if len(rows) > 0 :
        return render_template("s_player_filter.html", rows=rows)
    return render_template("failure_page.html")

#Q4 - Results Page
@app.route("/blocks_total", methods = ["GET","POST"])
def blocks_total():
    """
    Path/Page to return the leader in blocked shots along with the total blocks.
    """
    rows = obj.blocks_leader()
    return render_template("s_blocks_leader.html", rows=rows)


@app.route("/fg_percent_filter", methods = ["GET","POST"])
def form_player_fgs():
    """
    Path/Page to parse the input of Q5 and return the respective values in an object format.
    """
    fg_percent = request.form["fg_percent"]
    rows = obj.fg_percent_filter(fg_percent)
    if len(rows) > 0 :
        return render_template("s_fg_percent.html", rows=rows)
    return render_template("failure_page.html")

app.run(debug=True, port=5001)
