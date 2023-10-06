# FREE NBA API APPLICATION

## Docker execution

Potentially need to delete this line from /users/<user>/.docker/ config.json file if execution unsuccessful
    
    "credsStore": "desktop",

### Environment Setup

build image...

    [sudo] docker build --tag python-docker . 

run container...

    docker run -d -p 5001:5000 python-docker

### To use the api

Navigate / make requests to...

    http://localhost:5001/

The api has three endpoints:

1. Game ID endpoint:

    http://localhost:5001/game_id/< id >/

2. Games on date:

    http://localhost:5001/games_on_date/< date:YYYY-MM-DD >/

3. Statistics Summary for date range:

    http://localhost:5001/stats/< st_date:YYYY-MM-DD >/< en_date:YYYY-MM-DD >/



## Development Steps Taken

1. Understand free NBA API and get responses working (done)
2. Overlay flask and create end points (done)
3. Handle the key filters for games (dones)
4. Build caching capability and extract db build statements (done - not fully functional currently the application is monkey patching 'requests')
5. Handle pagination & appends (done)
6. Create summary view for stats (done with stretch)
7. Format stats response to csv (done)
8. Produce docker file (done)
9. Build logging (partially complete)

### Still do to / could do...

1. Implement dataclasses in the application to make json handling more straight forward
2. Package functions into classes
3. Logging is one continual steam to the logs/record.log file this should be enhanced to capture key stages e.g. req/resp elements
4. Testing has been carried out manually for specific scenarios, but I would look to use a testing package given more time.
5. but there are no real fail safes included to handle exceptions.
6. API keys are currenly in config, but these would need to be handled more securely as env vars.
7. Tidy up the api end points to include documentation in html / css templates
