from flask import render_template, request
from server import app
#from server.models import Sample

samples = [
    {
        'sensor': 'BME280',
        'type': 'Humidity',
        'data': '44',
        'date_posted': 'April 20, 2018'
    },
    {
        'sensor': 'BME280',
        'type': 'Temperature',
        'data': '12',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    global timeString
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        timeString = data['time']
        print(data)
        return render_template('home.html', val=timeString)
    elif request.method == 'GET':
        print("This is a GET")
        return render_template('home.html', val=timeString)
    else:
        print("Not a POST")
        return render_template('home.html', val=102)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/data")
def data():
    return render_template('data.html', samples=samples)