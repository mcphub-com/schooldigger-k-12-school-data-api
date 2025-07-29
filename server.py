import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/schooldigger-schooldigger-default/api/schooldigger-k-12-school-data-api'

mcp = FastMCP('schooldigger-k-12-school-data-api')

@mcp.tool()
def get_school(id: Annotated[str, Field(description='The 12 digit School ID (e.g. 064215006903)')]) -> dict: 
    '''Retrieve a school record from the SchoolDigger database'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/schools/%7Bid%7D'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_schools(st: Annotated[str, Field(description="Two character state (e.g. 'CA') - required")],
                q: Annotated[Union[str, None], Field(description='Search term - note: will match school name or city (optional)')] = None,
                qSearchSchoolNameOnly: Annotated[Union[bool, None], Field(description="For parameter 'q', only search school names instead of school and city (optional)")] = None,
                districtID: Annotated[Union[str, None], Field(description='Search for schools within this district (7 digit district id) (optional)')] = None,
                level: Annotated[Union[str, None], Field(description="Search for schools at this level. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Public', 'Private' (optional). 'Public' returns all Elementary, Middle, High and Alternative schools")] = None,
                city: Annotated[Union[str, None], Field(description='Search for schools in this city (optional)')] = None,
                zip: Annotated[Union[str, None], Field(description='Search for schools in this 5-digit zip code (optional)')] = None,
                isMagnet: Annotated[Union[bool, None], Field(description='True = return only magnet schools, False = return only non-magnet schools (optional) (Ultra, Mega API levels only)')] = None,
                isCharter: Annotated[Union[bool, None], Field(description='True = return only charter schools, False = return only non-charter schools (optional) (Ultra, Mega API levels only)')] = None,
                isVirtual: Annotated[Union[bool, None], Field(description='True = return only virtual schools, False = return only non-virtual schools (optional) (Ultra, Mega API levels only)')] = None,
                isTitleI: Annotated[Union[bool, None], Field(description='True = return only Title I schools, False = return only non-Title I schools (optional) (Ultra, Mega API levels only)')] = None,
                isTitleISchoolwide: Annotated[Union[bool, None], Field(description='True = return only Title I school-wide schools, False = return only non-Title I school-wide schools (optional) (Ultra, Mega API levels only)')] = None,
                nearLatitude: Annotated[Union[int, float, None], Field(description='Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Ultra, Mega API levels only.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308')] = None,
                nearLongitude: Annotated[Union[int, float, None], Field(description='Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Ultra, Mega API levels only.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308')] = None,
                nearAddress: Annotated[Union[str, None], Field(description="Search for schools within (distanceMiles) of this address. Example: '123 Main St. AnyTown CA 90001' (optional) (Ultra, Mega API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times")] = None,
                distanceMiles: Annotated[Union[int, float, None], Field(description='Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Ultra, Mega API levels only) Minimum: -2147483648 Maximum: 2147483647')] = None,
                boxLatitudeNW: Annotated[Union[int, float, None], Field(description="Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                boxLongitudeNW: Annotated[Union[int, float, None], Field(description="Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                boxLatitudeSE: Annotated[Union[int, float, None], Field(description="Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                boxLongitudeSE: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                page: Annotated[Union[int, float, None], Field(description='Page number to retrieve (optional, default: 1) Minimum: -2147483648 Maximum: 2147483647')] = None,
                perPage: Annotated[Union[int, float, None], Field(description='Number of schools to retrieve on a page (50 max) (optional, default: 10) Minimum: -2147483648 Maximum: 2147483647')] = None,
                sortBy: Annotated[Union[str, None], Field(description="Sort list. Values are: schoolname, distance, rank. For descending order, precede with '-' i.e. -schoolname (optional, default: schoolname)")] = None,
                includeUnrankedSchoolsInRankSort: Annotated[Union[bool, None], Field(description="If sortBy is 'rank', this boolean determines if schools with no rank are included in the result (optional, default: false)")] = None) -> dict: 
    '''Search the SchoolDigger database for schools. You may use any combination of criteria as query parameters.'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/schools'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'st': st,
        'q': q,
        'qSearchSchoolNameOnly': qSearchSchoolNameOnly,
        'districtID': districtID,
        'level': level,
        'city': city,
        'zip': zip,
        'isMagnet': isMagnet,
        'isCharter': isCharter,
        'isVirtual': isVirtual,
        'isTitleI': isTitleI,
        'isTitleISchoolwide': isTitleISchoolwide,
        'nearLatitude': nearLatitude,
        'nearLongitude': nearLongitude,
        'nearAddress': nearAddress,
        'distanceMiles': distanceMiles,
        'boxLatitudeNW': boxLatitudeNW,
        'boxLongitudeNW': boxLongitudeNW,
        'boxLatitudeSE': boxLatitudeSE,
        'boxLongitudeSE': boxLongitudeSE,
        'page': page,
        'perPage': perPage,
        'sortBy': sortBy,
        'includeUnrankedSchoolsInRankSort': includeUnrankedSchoolsInRankSort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_district(id: Annotated[str, Field(description='The 7 digit District ID (e.g. 0642150)')]) -> dict: 
    '''Retrieve a single district record from the SchoolDigger database'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/districts/%7Bid%7D'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_districts(st: Annotated[str, Field(description="Two character state (e.g. 'CA') - required")],
                  q: Annotated[Union[str, None], Field(description='Search term - note: will match district name or city (optional)')] = None,
                  city: Annotated[Union[str, None], Field(description='Search for districts in this city (optional)')] = None,
                  zip: Annotated[Union[str, None], Field(description='Search for districts in this 5-digit zip code (optional)')] = None,
                  nearLatitude: Annotated[Union[int, float, None], Field(description='Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Ultra, Mega API levels only. Mega API level will flag districts that include lat/long in its attendance boundary.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308')] = None,
                  nearLongitude: Annotated[Union[int, float, None], Field(description='Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Ultra, Mega API levels only. Mega API level will flag districts that include lat/long in its attendance boundary.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308')] = None,
                  boundaryAddress: Annotated[Union[str, None], Field(description="Full U.S. address: flag returned districts that include this address in its attendance boundary. Example: '123 Main St. AnyTown CA 90001' (optional) (Mega API level only)")] = None,
                  distanceMiles: Annotated[Union[int, float, None], Field(description='Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 50 miles) (optional) (Ultra, Mega API levels only) Minimum: -2147483648 Maximum: 2147483647')] = None,
                  isInBoundaryOnly: Annotated[Union[bool, None], Field(description='Return only the districts that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Mega API level only)')] = None,
                  boxLatitudeNW: Annotated[Union[int, float, None], Field(description="Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                  boxLongitudeNW: Annotated[Union[int, float, None], Field(description="Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                  boxLatitudeSE: Annotated[Union[int, float, None], Field(description="Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                  boxLongitudeSE: Annotated[Union[int, float, None], Field(description="Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                  page: Annotated[Union[int, float, None], Field(description='Page number to retrieve (optional, default: 1) Minimum: -2147483648 Maximum: 2147483647')] = None,
                  perPage: Annotated[Union[int, float, None], Field(description='Number of districts to retrieve on a page (50 max) (optional, default: 10) Minimum: -2147483648 Maximum: 2147483647')] = None,
                  sortBy: Annotated[Union[str, None], Field(description="Sort list. Values are: districtname, distance, rank. For descending order, precede with '-' i.e. -districtname (optional, default: districtname)")] = None,
                  includeUnrankedDistrictsInRankSort: Annotated[Union[bool, None], Field(description="If sortBy is 'rank', this boolean determines if districts with no rank are included in the result (optional, default: false)")] = None) -> dict: 
    '''Search the SchoolDigger database for districts. You may use any combination of criteria as query parameters.'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/districts'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'st': st,
        'q': q,
        'city': city,
        'zip': zip,
        'nearLatitude': nearLatitude,
        'nearLongitude': nearLongitude,
        'boundaryAddress': boundaryAddress,
        'distanceMiles': distanceMiles,
        'isInBoundaryOnly': isInBoundaryOnly,
        'boxLatitudeNW': boxLatitudeNW,
        'boxLongitudeNW': boxLongitudeNW,
        'boxLatitudeSE': boxLatitudeSE,
        'boxLongitudeSE': boxLongitudeSE,
        'page': page,
        'perPage': perPage,
        'sortBy': sortBy,
        'includeUnrankedDistrictsInRankSort': includeUnrankedDistrictsInRankSort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_rank_schools(year: Annotated[Union[int, float, None], Field(description='The ranking year (leave blank for most recent year) Minimum: -2147483648 Maximum: 2147483647')] = None,
                     level: Annotated[Union[str, None], Field(description="Level of ranking: 'Elementary', 'Middle', or 'High'")] = None,
                     page: Annotated[Union[int, float, None], Field(description='Page number to retrieve (optional, default: 1) Minimum: -2147483648 Maximum: 2147483647')] = None,
                     perPage: Annotated[Union[int, float, None], Field(description='Number of schools to retrieve on a page (50 max) (optional, default: 10) Minimum: -2147483648 Maximum: 2147483647')] = None) -> dict: 
    '''Returns a SchoolDigger school ranking list'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/rankings/schools/%7Bst%7D'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
        'level': level,
        'page': page,
        'perPage': perPage,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_rank_districts(year: Annotated[Union[int, float, None], Field(description='The ranking year (leave blank for most recent year) Minimum: -2147483648 Maximum: 2147483647')] = None,
                       page: Annotated[Union[int, float, None], Field(description='Page number to retrieve (optional, default: 1) Minimum: -2147483648 Maximum: 2147483647')] = None,
                       perPage: Annotated[Union[int, float, None], Field(description='Number of districts to retrieve on a page (50 max) (optional, default: 10) Minimum: -2147483648 Maximum: 2147483647')] = None) -> dict: 
    '''Returns a SchoolDigger district ranking list'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/rankings/districts/%7Bst%7D'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
        'page': page,
        'perPage': perPage,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete(q: Annotated[str, Field(description="Search term for autocomplete (e.g. 'Lincol') (required)")],
                 st: Annotated[Union[str, None], Field(description="Two character state (e.g. 'CA') (optional -- leave blank to search entire U.S.)")] = None,
                 level: Annotated[Union[str, None], Field(description="Search for schools at this level only. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Private' (optional - leave blank to search for all schools)")] = None,
                 qSearchCityStateName: Annotated[Union[bool, None], Field(description="Extend the search term to include city and state (e.g. 'Lincoln el paso' matches Lincoln Middle School in El Paso) (optional)")] = None,
                 returnCount: Annotated[Union[int, float, None], Field(description='Number of schools to return. Valid values: 1-20. (default: 10) Minimum: -2147483648 Maximum: 2147483647')] = None,
                 boxLatitudeNW: Annotated[Union[int, float, None], Field(description="Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Ultra, Mega API levels only.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                 boxLongitudeNW: Annotated[Union[int, float, None], Field(description="Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Ultra, Mega API levels only.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                 boxLatitudeSE: Annotated[Union[int, float, None], Field(description="Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Ultra, Mega API levels only.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None,
                 boxLongitudeSE: Annotated[Union[int, float, None], Field(description="Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Ultra, Mega API levels only.) Minimum: -1.7976931348623157e+308 Maximum: 1.7976931348623157e+308")] = None) -> dict: 
    '''Returns a simple and quick list of schools for use in a client-typed autocomplete'''
    url = 'https://schooldigger-k-12-school-data-api.p.rapidapi.com/v2.0/autocomplete/schools'
    headers = {'x-rapidapi-host': 'schooldigger-k-12-school-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'st': st,
        'level': level,
        'qSearchCityStateName': qSearchCityStateName,
        'returnCount': returnCount,
        'boxLatitudeNW': boxLatitudeNW,
        'boxLongitudeNW': boxLongitudeNW,
        'boxLatitudeSE': boxLatitudeSE,
        'boxLongitudeSE': boxLongitudeSE,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
