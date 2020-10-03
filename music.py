from playsound import playsound
from random import randint
#playsound('C://Users//TOSHIBA//Music//ai//playing.mp3')
a=['8 Parche','Akh Lad Jaave','Ankhon Mein Teri','Bacha','Bilyaan Bilyan','Bohut Pyar Karte Hain','Chaar Chudiyaan','Dabda','Defaulter','Dil Khabe Paase','DOLLAR','Duji Vaar Pyar','FILHALL','Gall Goriye','Ghungroo','Gupp Marda','Halka Halka','I am a rider','Ishq Ka Raja','JAMILA','Jeena Jeena','Kaabil','Kabhi Kabhi Mere Dil Mein','Kangan','Koi Vi Nahi','koon hove gaa','Le Gayi Le Gayi','Main Teri Ho Gayi','Mere Gully Mein','Mere Khawabon Main Jo Aaye','Mere Samne Wali Khidki Mein','na ja','oh aa tera yaar','Oh Oh Jaane Jaana','Pachtaoge','Pehli Mulakat','Relation','Rona Sikhade Ve','saja hoo gaya jeena','SAKHIYAAN','SANDAL','Shadow','Shoot Da Order','Struggler','Tera Fitoor','Teri Mitti','Ude Jab Jab Zulfen Teri','Ve Maahi','Wafa Ne Bewafai','WISH','Yaad Piya Ki','Yaari','Yaarr Ni Milyaa']
b=randint(0,len(a))
print(a[b-1],'song is playing')
v='C://Users//TOSHIBA//Music//'+a[b-1]+'.mp3'
playsound(v)
