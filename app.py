from flask import Flask, render_template, request
import machine

app = Flask(__name__)

@app.route('/')
def index():
    title = "Rental Car Time Prediction"
    return render_template("index.html", title=title)

@app.route('/results', methods=["POST"])
def results():
    title = "Expected Time"

    departure = request.form.get("departure")
    destination = request.form.get("destination")
    date = request.form.get("date")
    day =  date.split("-")[2]

    final_result = machine.getFromString(departure, destination, int(day))

    return render_template("form.html", title=title,
            departure=departure, destination=destination, day=day, final_result=final_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')