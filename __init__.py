from flask import Flask, render_template, request
from flask import session, redirect
from data import makeGraphic
app = Flask(__name__)

#homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

#handling data
@app.route('/data')
def getGraphic():
    limit1=request.args.get('limit1')
    limit2=request.args.get('limit2')
    metric = request.args.get('metric')
    specification = request.args.get('specification')
    data = makeGraphic(limit1, limit2, specification, metric)
    return render_template("data.html", graph=data, Metric = metric, Specification = specification, Limit1=limit1,Limit2=limit2)

if __name__ == "__main__":
    app.debug = True
    app.run()
