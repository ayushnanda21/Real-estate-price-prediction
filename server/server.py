from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    return "hi"


@app.route('/predict_home_price', method = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify([
        'estimated_price': util.get_estimated_price(location,total_sqft, bhk,bath)
    ])
 
    response.headers.add('Access-Control-Allow-Origin','*')

    return response
    

if __name__ =="__main__":
    print('Starting Python Flask Server for Real estate price Prediction')
    app.run()

