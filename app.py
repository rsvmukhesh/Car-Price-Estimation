from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
 

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        y_min = 1992
        y_max = 2020
        km_min = 1
        km_max = 170000

        fuel = int(request.form['fuel'])
        transmission = int(request.form['transmission'])
        seller_type = int(request.form['seller_type'])
        owner = int(request.form['owner'])
        km_driven = int(request.form["driven"])
        year = int(request.form["year"])

        year = (year - y_min)/(y_max-y_min)
        km_driven = (km_driven - km_min)/(km_max-km_min)
        t = [fuel,km_driven,year,seller_type,owner,transmission]
        test = np.array(t).reshape(1, 6)

        prediction=model.predict(test)

        output=round(prediction[0],2)
        return render_template('home.html',prediction_text="Your car price is Rs. {}".format(abs(output)))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)