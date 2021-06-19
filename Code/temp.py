from flask import Flask, send_from_directory
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH,start_server
from pywebio.input import *
from pywebio.output import *
import argparse
import pickle
app=Flask(__name__)
model= pickle.load(open('model.pkl','rb'))
def predict():
    age=input("Enter your age",type=NUMBER)    
    gender =input("Gender, 1 for male and 0 for female",type=NUMBER)  
    chest=input("Chest pain from 0 to 3",type=NUMBER)  
    bp=input("Resting BP in mm/Hg",type=NUMBER)   
    chol=input("Cholestrol in mg/dl",type=NUMBER) 
    sugar=input("Fasting blood sugar in 1 and 0",type=NUMBER)   
    ec=input("Electrocardiograph in 1 and 0",type=NUMBER)   
    exercise= input("Exercise 1 for yes 0 for no",type=NUMBER)
    dep= input("Depression 0 to 6",type=NUMBER) 
    slope= input("SLope from 0 to 2",type=NUMBER)   
    vessels=input("Major vessels from 0 to 4",type=NUMBER)
    thal=input("Thal from 1 to 3",type=NUMBER)   
    prediction=model.predict([[age,gender,chest,bp,chol,sugar,ec,exercise,dep,slope,vessels,thal]])
    output=prediction
    if output ==0:
        put_text("You dont have a heart disease")
    else:
        put_text("You have a heart disease")
        
app.add_url_rule('/tool', 'webio_view',webio_view(predict),methods=['GET','POST','OPTIONS'])
if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument("-p", "--port",default=8080)
    args=arg.parse_args()
    start_server(predict,port=args.port)
    #app.run(debug=True)