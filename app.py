from flask import Flask, render_template, redirect, request, jsonify, json
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def Home():
    # Return template and data
    return render_template("index.html")

@app.route("/Tableau1")
def Tableau1():
    # Return template and data
    return render_template("Tableau1.html")

@app.route("/Tableau2")
def Tableau2():
    # Return template and data
    return render_template("Tableau2.html")


@app.route("/Project_Paper")
def Project_Paper():
    # Return template and data
    return render_template("Project_Paper.html")

@app.route("/About_Us")
def PAbout_Us():
    # Return template and data
    return render_template("About_Us.html")

@app.route("/", methods=["POST"])
def recommendation_df():
    
    content = request.json["data"]
    print(content)

    # parse
    hotel = request.json["hotel"]
    #rating = request.json["rating"]

    recommendation = modelHelper.recommendation_df(hotel)
    print(recommendation)
    return(jsonify({"ok": True, "recommendation":json.loads(recommendation.to_json(orient="records"))})) 


######################################################
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
