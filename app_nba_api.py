
from flask import Flask, make_response
import requests_cache
import logging
import sys

from src.gets import games, tm_stats

logging.basicConfig(filename='logs/record.log', level=logging.DEBUG)

# monkey patches 'requests.get' currently would use 'sessions' in future
# good for intialising, further work need to switch to prod setup
# code to initialise sqlite in docker has been provided too
requests_cache.install_cache(cache_name='free_nba_cache', 
                             backend='sqlite', 
                             expire_after=180)

# creating an instance of Flask class
app = Flask(__name__)

# home path for api usage info
@app.route('/')
def index():
    # showing different logging levels
    app.logger.debug("debug log info")
    app.logger.info("Info log information")

    return 'BV NBA API Home', 200

# use the route decorator to tell Flask what URL should trigger our function
@app.route('/games_on_date/<date1>/')
# function returns the message "Hello World!" on user's browser
def games_on_dt(date1):

    data = games.date_getter(date1)

    # print(date1, data)
    return data, 200


# end point for retreiving games by id (int)
@app.route('/game_id/<id>/')
def game_id(id):

    data = games.id_getter(id)

    # print(date1, data)
    return data, 200

# endpoint for getting stats summary between dates grouped by team
@app.route('/stats/<st_date>/<en_date>/')
def stats(st_date, en_date):

    data = tm_stats.stats_getter(st_date, en_date)
    resp = make_response(data.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=team_summ_{}_{}.csv".format(st_date,en_date)
    resp.headers["Content-Type"] = "text/csv"

    return resp, 200

# runs the flask application using the app.run method
if __name__ == '__main__':
    app.run(debug=True)