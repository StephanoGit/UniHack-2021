#Importing required packages.
import pandas as pd
import pickle
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
#from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
#math
from math import isclose
from math import sin, cos, sqrt, atan2, radians


def getID(x):
    #Hamburg
    if(isclose(x, 53.630402, abs_tol=0.001)):
        return 0
    #Vancouver
    if(isclose(x, 49.193901, abs_tol=0.001)):
        return 1
    #Sydney
    if(isclose(x, -33.946098, abs_tol=0.001)):
        return 2
    #Montreal
    if(isclose(x, 45.470600, abs_tol=0.001)):
        return 3
    #New york
    if(isclose(x, 40.639801, abs_tol=0.001)):
        return 4
    #Orlando
    if(isclose(x, 28.429399, abs_tol=0.001)):
        return 5
    #Manchester
    if(isclose(x, 53.353699, abs_tol=0.001)):
        return 6
    #London
    if(isclose(x, 51.470600, abs_tol=0.001)):
        return 7
    return -1
def getidname(name):
    #Hamburg
    if(name.lower()=="hamburg"):
        return 0
    #Vancouver
    if(name.lower()=="vancouver"):
        return 1
    #Sydney
    if(name.lower()=="sydney"):
        return 2
    #Montreal
    if(name.lower()=="montreal"):
        return 3
    #New york
    if(name.lower()=="new york" or name.lower() =="jfk" or "newyork"):
        return 4
    #Orlando
    if(name.lower()=="orlando"):
        return 5
    #Manchester
    if(name.lower()=="manchester"):
        return 6
    #London
    if(name.lower()=="london"):
        return 7
    return -1
def getCoords(id):
    #Hamburg
    if(id==0):
        return [53.63040161,9.988229752]
    #Vancouver
    if(id==1):
        return [49.19390106,-123.1839981]
    #Sydney
    if(id==2):
        return [-33.94609833, 151.177002]
    #Montreal
    if(id==3):
        return [45.47060013, -73.74079895]
    #New york
    if(id==4):
        return [40.639801 -73.7789]
    #Orlando
    if(id==5):
        return [28.42939949 -81.30899811]
    #Manchester
    if(id==6):
        return [53.35369873 -2.274950027]
    #London
    if(id==7):
        return [51.4706 -0.461941]
    return [0,0]

def getdist(origin, dest):
    """
    Montreal / Pierre Elliott Trudeau International Airport 45.47060013 -73.74079895
    London Heathrow Airport 51.4706 -0.461941
    Orlando International Airport 28.42939949 -81.30899811
    John F Kennedy International Airport 40.639801 -73.7789
    Vancouver International Airport 49.19390106 -123.1839981
    Sydney Kingsford Smith International Airport -33.94609833 151.177002
    Manchester Airport 53.35369.873 -2.274950027
    Hamburg Airport 53.63040161 9.988229752
    """
    origins=getCoords(origin)
    dests = getCoords(dest)

    R = 6373.0

    lat1 = radians(origins[0])
    lon1 = radians(origins[1])
    lat2 = radians(dests[0])
    lon2 = radians(dests[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def getFromUser():
    dept = input("Enter departure airport: ")
    dest = input("Enter destination: ")

    user_id = getidname(dest)
    print(user_id)
    user_day = int(input("enter day"))
    user_dist = getdist(dept, dest)
    print(user_dist)
    print(user_id)
    print(rfc.predict([[user_id,user_day,0,user_dist]]))
    print(rfc.predict([[user_id,user_day,1,user_dist]]))

def getFromString(dept, dest,user_day):
    user_id = getidname(dest)
    user_dist = getdist(dept, dest)

    returner = []
    returner.append(str(rfc.predict([[user_id,user_day,0,user_dist]])))
    returner.append(str(rfc.predict([[user_id,user_day,1,user_dist]])))

    return returner


rfc = pickle.load(open('rfc.pkl','rb'))