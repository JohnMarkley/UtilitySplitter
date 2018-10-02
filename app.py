from flask import Flask, render_template, request

app = Flask(__name__)

#Home
@app.route('/')
def index():
    return render_template("index.html")

#Run once form is submitted
@app.route('/calc', methods=['POST'])
def calculate():
    #Set default values

    electricBill = '0'
    waterBill = '0'
    internetBill = '0'
    roommates = '6'

    #Collect data from forms
    electricBill = request.form['electricBill']
    waterBill = request.form['waterBill']
    internetBill = request.form['internetBill']
    roommates = request.form['roommateNum']

    #Calculate
    result = (float(electricBill) + float(waterBill) + float(internetBill))/float(roommates)
    return render_template("calculated.html", result = result)


@app.route('/source')
def source():
    return render_template("source.html")

if __name__ == '__main__':
    app.debug = True
    app.run()

