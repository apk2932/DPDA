# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:54:39 2019

@author: prc1424
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:39:32 2019

@author: prc1424
"""

from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd


#http://FLHQ-AKULKARNI1.us.ad.hertz.com:5000/Rentals_Returns
#http://FLHQ-AKULKARNI1.us.ad.hertz.com:5000/Shuttles
#http://HERTZ2119-X.us.ad.hertz.com:5000/Rentals_Returns
#http://HERTZ2119-X.us.ad.hertz.com:5000/Shuttles
#http://127.0.0.1:5000/Rentals_Returns
#http://127.0.0.1:5000/Shuttles
app = Flask(__name__)
api = Api(app)

class Shuttles(Resource):
    def get(self):
        infile = r"\\HERTZ2119-X\SAS User Folders\Incremental_Shuttles\Incremental_Shuttle_Data.txt"
        #query =  pd.read_csv(infile, delimiter=',') # This line performs query and returns json result
        #query = query.to_json(orient='columns')
        query = "HEllo World"
        return query
    
    
class Rentals_Returns(Resource):
    def get(self,Location):
        infile = r"\\HERTZ2119-X\SAS User Folders\RentalsReturns_Location\Rental_Return_Forecast.txt"
        #query =  pd.read_csv(infile, delimiter=',') # This line performs query and returns json result
        #query['LOC'] = query['LOC'].str.strip()
        #query = query[query['LOC']==Location]
        #query = query.to_json(orient='columns')
        query = "HEllo World"
        return query


        

api.add_resource(Shuttles, '/Shuttles') # Route_1
api.add_resource(Rentals_Returns, '/Rentals_Returns/<Location>') # Route_2

if __name__ == '__main__':
     app.run()
        
    
    
