from flask import Flask, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
# Design a query to retrieve the last 12 months of precipitation data and plot the results
percep = pd.DataFrame(engine.execute(f'SELECT * FROM measurement ORDER BY measurement.date DESC').fetchall())
percep.rename(columns={0:"id",1:"station",2:"date",3:"prcp",4:"tobs"},inplace = True)
percep = percep.set_index("id")
max_date = percep.date.max()
min_date = "2016-08-23"
# Calculate the date 1 year ago from the last data point in the database (percipitation)
prev_year = percep[percep["date"]>=min_date]
prev_year = prev_year.sort_values("date")
prcp = prev_year["prcp"]
prev_year_dict = prev_year[["date","prcp"]]
prev_year_dict.set_index("date")
date = prev_year_dict["date"]
prcp = prev_year_dict["prcp"]
prcp_dict = dict(zip(date,prcp))
# Calculate the date 1 year ago from the last data point in the database (tobs)
prev_year_dict_tobs = prev_year[["date","tobs"]]
prev_year_dict_tobs.set_index("date")
date = prev_year_dict_tobs["date"]
tobs = prev_year_dict_tobs["tobs"]
tobs_dict = dict(zip(date,tobs))
tobs_dict

# pull station ID and name into a dictionary from the station table in MySQL
station_pd = pd.DataFrame(engine.execute('SELECT * FROM station').fetchall())
station_pd = station_pd.rename(columns = {0:"id",1:"station",2:"name",3:"latitude",4:"longitude",5:"elevation"})
station_pd.set_index("id")
station_dict = dict(zip(station_pd.id,station_pd.station))
station_dict

# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for each date in that range of dates
# use group by to allow you to view all dates

def calc_temps_by_date(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).group_by(Measurement.date).all()

# function usage example
start_date = "2011-07-01"
end_date = '2011-07-12'
calc_temps_by_date(start_date, end_date)

#add dates into dictionary and then create a list of the dictionaries to jsonify
date_dict_list = []
date_dict = {}

row = 0
for x in range(0,len(calc_temps_by_date(start_date, end_date))):
    date_dict["Date"] = calc_temps_by_date(start_date, end_date)[row][0]
    date_dict["TMIN"] = calc_temps_by_date(start_date, end_date)[row][1]
    date_dict["TAVE"] = round(calc_temps_by_date(start_date, end_date)[row][2],2)
    date_dict["TMAX"] = calc_temps_by_date(start_date, end_date)[row][3]
    #append the dictionary created above to a list
    date_dict_list.append(dict(date_dict))
    row = row+1
    
date_dict_list
    

#genearte flask app
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
#design welcome page with all available routes
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/end"
    )

#design individual routes based upon code above
@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify(prcp_dict)

@app.route("/api/v1.0/station")
def station():

    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs():

    return jsonify(tobs_dict)

@app.route("/api/v1.0/start/end")
def start_end():

    return jsonify(date_dict_list)
    
if __name__ == '__main__':
    app.run(debug=True)
