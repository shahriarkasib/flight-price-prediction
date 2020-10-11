import pandas as pd
import sklearn
import pickle
from flask import Flask,request,render_template
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl","rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET","POST"])
@cross_origin()

def predict():
    if request.method == "POST":
        
        #DATE OF JOURNEY
        date_journey = request.form["Dep_Time"]
        journey_day = int(pd.to_datetime(date_journey,format = "%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_journey,format = "%Y-%m-%dT%H:%M").month)
        
        dep_hour = int(pd.to_datetime(date_journey,format = "%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(date_journey,format = "%Y-%m-%dT%H:%M").minute)
        
        
        #Arrival
        arrival_time = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(arrival_time, format = "%Y-%m-%dT%H:%M").hour)
        Arrival_minute = int(pd.to_datetime(arrival_time, format = "%Y-%m-%dT%H:%M").minute)
        
        #Duration
        
        Duration_in_hour = abs(Arrival_hour - dep_hour)
        Duration_in_minute = abs(Arrival_minute - dep_minute)
        
        #Total Stops
        Total_stops = int(request.form["stops"])
        
        #Airline
        
        Airline = request.form["airline"]
        
        if (Airline == "Jet Airways"):
            Jet_Airways = 1
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
        elif (Airline == "Indigo"):
            Jet_Airways = 0
            Indigo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
                
                        
        elif (Airline == "Air_India"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
                            
                        
        elif (Airline == "Multiple_carriers"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
                
                                        
                        
        elif (Airline == "SpiceJet"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
                
                                                    
                        
        elif (Airline == "Vistara"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
                
                
        elif (Airline == "GoAir"):
                Jet_Airways = 0
                Indigo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 1
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0
                
                            
        elif (Airline == "Multiple_carriers_Premium_economy"):
                Jet_Airways = 0
                Indigo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 1
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0
                
                                        
        elif (Airline == "Jet_Airways_Business"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0
                
                            
                                        
        elif (Airline == "Vistara_Premium_economy"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
                
                                        
                                        
        elif (Airline == "Trujet"):
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
            
        else:
            Jet_Airways = 0
            Indigo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
                        
        #source   
        Source = request.form["Source"]
        
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        
        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
                
        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0 
            
        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            
        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
            
        Destination = request.form["Destination"]
        
        if(Destination == "Cochin"):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            
        
        elif(Destination == "Delhi"):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif(Destination == "New_Delhi"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif(Destination == "Hyderabad"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            
        elif(Destination == "Kolkata"):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            
            
        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0           
            
        prediction = model.predict([[
            journey_day,
            journey_month,
            dep_hour,
            dep_minute,
            Arrival_hour,
            Arrival_minute,
            Duration_in_hour,
            Duration_in_minute,
            Total_stops,
            Jet_Airways,
            Indigo,
            Air_India,
            Multiple_carriers,
            SpiceJet,
            Vistara,
            GoAir,
            Multiple_carriers_Premium_economy,
            Jet_Airways_Business,
            Vistara_Premium_economy,
            Trujet,  
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            s_Chennai,
            d_Cochin,
            d_Delhi,
            d_New_Delhi,
            d_Hyderabad,
            d_Kolkata]])
        
        output = round(prediction[0],2)
        
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)