from flask import *
import sys
sys.path.append('/Users/nandy/Git_repos/APP-Project/models/')
from models import San 


# app = Flask(__name__, template_folder="new_folder_name")
#move controllers to a folder and keep app.run() outside in a seperate folder and import app line down below 
app = Flask(__name__, template_folder='/Users/nandy/Git_repos/APP-Project/models/templates/')

obj = San()


@app.route("/")
def start_(): 
    return render_template("homepage.html")

@app.route("/player_stats")
def player_stat(): 
    return render_template("player_stats.html")

@app.route("/form_player_stats", methods = ["GET","POST"])
def form_player_stat(): 
    name = request.form["player_name"]
    rows = obj.find_player_names(name)
    print(rows, type(rows))
    if len(rows) > 0 : 
        return render_template("s_playerstats.html", rows=rows)
    else : 
        return render_template("failure_page.html",)

app.run(debug=True, port=5001)

