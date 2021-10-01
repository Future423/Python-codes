import pickle as pk
import numpy as np
model=pk.load(open('modelprediction/model_save','rb'))

def processing(d):
    l=['Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Source_Chennai', 'Source_Delhi',
       'Source_Kolkata', 'Source_Mumbai', 'Airline_Air India', 'Airline_GoAir',
       'Airline_IndiGo', 'Airline_Jet Airways', 'Airline_Jet Airways Business',
       'Airline_Multiple carriers',
       'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
       'Total_Stops', 'Duration_Hours', 'Duration_Min', 'Day_Of_Journey',
       'Month_Of_Journey', 'Dep_hour', 'Dep_min', 'Arrival_hour',
       'Arrival_min']
    Destination_Cochin=0
    Destination_Delhi=0
    Destination_Hyderabad=0
    Destination_Kolkata=0
    if(d['destination']=='Delhi'):
        Destination_Delhi=1
    if(d['destination']=='Cochin'):
        Destination_Cochin=1
    if(d['destination']=='Kolkata'):
        Destination_Kolkata=1
    if(d['destination']=='Hyderabad'):
        Destination_Hyderabad=1
    Source_Chennai=0
    Source_Delhi=0
    Source_Kolkata=0
    Source_Mumbai=0
    if(d['source']=='Chennai'):
        Source_Chennai=1
    if(d['source']=='Delhi'):
        Source_Delhi=1
    if(d['source']=='Kolkata'):
        Source_Kolkata=1
    if(d['source']=='Mumbai'):
        Source_Mumbai=1
    Airline_GoAir=0
    Airline_Air_India=0
    Airline_IndiGo=0
    Airline_Jet_Airways=0
    Airline_Jet_Airways_Business=0
    Airline_Multiple_carriers=0
    Airline_Multiple_carriers_Premium_economy=0
    Airline_SpiceJet=0
    Airline_Trujet=0
    Airline_Vistara=0
    Airline_Vistara_Premium_economy=0
    if(d['company']=='GoAir'):
        Airline_GoAir=1
    if(d['company']=='IndiGo'):
        Airline_IndiGo=1
    if(d['company']=='Jet Airways'):
        Airline_Jet_Airways=1
    if(d['company']=='SpiceJet'):
        Airline_SpiceJet=1
    if(d['company']=='Air India'):
        Airline_Air_India=1
    if(d['company']=='Trujet'):
        Airline_Trujet=1
    if(d['company']=='Vistara'):
        Airline_Vistara=1
    no_of_stops=int(d['stops'])
    day=int(d['datej'][-2:])
    month=int(d['datej'][-5:-3])
    dep_h=int(d['departure'][0:2])
    dep_m=int(d['departure'][3:])
    arr_h=int(d['arrival'][:2])
    arr_m=int(d['arrival'][3:])
    dur_h=abs(dep_h-arr_h)
    dur_m=abs(dep_m-arr_m)
    l=np.array([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])
  
    actual= (round(model.predict(l)[0],2))
    
    
    airlines={'Airline_Air India':0, 'Airline_GoAir':0,
       'Airline_IndiGo':0, 'Airline_Jet Airways':0, 
       'Airline_SpiceJet':0,
       'Airline_Trujet':0, 'Airline_Vistara':0}
    
    
    Airline_GoAir=0
    Airline_Air_India=0
    Airline_IndiGo=0
    Airline_Jet_Airways=0
    Airline_Jet_Airways_Business=0
    Airline_Multiple_carriers=0
    Airline_Multiple_carriers_Premium_economy=0
    Airline_SpiceJet=0
    Airline_Trujet=0
    Airline_Vistara=0
    Airline_Vistara_Premium_economy=0
    
    #FOR GOAIR
    Airline_GoAir=1
    airlines['Airline_GoAir']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    
    #FOR AIRINDIA
    Airline_Air_India=1
    Airline_GoAir=0
    airlines['Airline_AirIndia']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    
    
    
    #FOR INDIGO
    Airline_Air_India=0
    Airline_GoAir=0
    Airline_IndiGo=1
    airlines['Airline_IndiGo']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    
    
    #FOR JETAIRWAYS
    Airline_Air_India=0
    Airline_GoAir=0
    Airline_IndiGo=0
    Airline_Jet_Airways=1
    airlines['Airline_JetAirways']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    
    #FOR SPICJET
    Airline_Air_India=0
    Airline_GoAir=0
    Airline_IndiGo=0
    Airline_Jet_Airways=0
    Airline_SpiceJet=1
    airlines['Airline_SpiceJet']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    
    
    #FOR TRUJET
    Airline_Air_India=0
    Airline_GoAir=0
    Airline_IndiGo=0
    Airline_Jet_Airways=0
    Airline_SpiceJet=0
    Airline_Trujet=1
    airlines['Airline_Trujet']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    
    
    #FOR VISTARA
    Airline_Air_India=0
    Airline_GoAir=0
    Airline_IndiGo=0
    Airline_Jet_Airways=0
    Airline_SpiceJet=0
    Airline_Trujet=0
    Airline_Vistara=1
    airlines['Airline_Vistara']=round(model.predict([[Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Source_Chennai, Source_Delhi,
       Source_Kolkata,Source_Mumbai,Airline_Air_India, Airline_GoAir,
       Airline_IndiGo, Airline_Jet_Airways,Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
       Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,
       no_of_stops, dur_h, dur_m, day,
       month, dep_h, dep_m, arr_h,
       arr_m]])[0],2)
    airlines['actual']=actual
    return airlines
    
    
    
       