from flask import Flask, request, jsonify, render_template, redirect, url_for
from function import ForestFire
app = Flask(__name__)

@app.route('/')
def home1():
    return render_template('forest.html')


@app.route('/predict_area', methods = ['POST'])
def predict_area():
        data = request.form
        print("Data : ",data)

        X = float(data['X']) #East-West Coordinate 1 to 9
        Y = float(data['Y']) #North-South Coordinate 1 to 9
        month = data['month'] 
        FFMC = float(data['FFMC']) #Fine Fuel Moisture Code 18.7 to 96.20
        DMC = float(data['DMC']) #Duff Moisture Code 1.1 to 291.3
        DC = float(data['DC']) #Drought Code 7.9 to 860.6
        ISI = float(data['ISI']) #Initial Spread Index 0.0 to 56.10
        temp = float(data['temp']) #2.2 to 33.30
        RH = float(data['RH']) #Relative Humidity 15.0 to 100
        wind = float(data['wind']) #0.40 to 9.40 
        rain = float(data['rain']) #0.0 to 6.4

        area = ForestFire(X,Y,month,FFMC,DMC,DC,ISI,temp,RH,wind,rain) #0.00 to 1090.84
        
        pred_area = area.get_predicted_area()
        # print(predicted_area)
        # return jsonify({"result":f"predicted_area=={predicted_area}"})
        return render_template('forest.html', fire_area=pred_area)
        
       




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080 ,debug = False)