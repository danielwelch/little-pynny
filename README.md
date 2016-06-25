# little-pynny
An effort to generate documentation for the [stats.nba.com](stats.nba.com) API that complies with the [Swagger Specification](http://swagger.io/specification/).

Work in progress.

###### The most recent generated documentation is available at the [project page](http://danielwelch.github.io/little-pynny/).

----

### How was this documentation created?
1. Parsed the awesome documentation provided by [seemethere/nba_py](https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation). 
2. Programmatically hit each API endpoint, using [requests](https://github.com/kennethreitz/requests) and parse the response to determine:
    a. If the endpoint is active
    b. The required paramaters for each active endpoint
3. When given bad parameters, the API will sometimes give requirements for parameters (regular expressions for strings, ranges for integers). Use these responses to generate a quick description of each parameter (work in progress)
4. Spit out what we have in a Swagger-compliant JSON file, [swagger.json](swagger.json).