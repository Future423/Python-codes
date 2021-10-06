import requests
import time
import json
from playsound import playsound

pincodes = ['411001', '411006', '411011']
date = '07-10-2021'

while True:
    for pincode in pincodes:
        time.sleep(3)
        r = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + pincode + '&date=' + date)

        slots = json.loads(r.text)
        for session in slots['sessions']:
            if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                print(time.asctime(time.localtime(time.time())))
                print('Center: ' + session['name'])
                print('Available: ' + str(session['available_capacity']))
                print('Vaccine: ' + session['vaccine'])
                print('Cost: ' + session['fee_type'])
                playsound('alarm.mp3')