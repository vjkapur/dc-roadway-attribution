#!/usr/bin/env python3

import geopandas as gpd
import pandas as pd

# each data source has an associated file and relevant width attribute
BIKE_LANES = 'bike_lanes'
ROADWAY_BLOCK = 'roadway_block'

data_sources = {BIKE_LANES: 'Bicycle_Lanes.geojson', 
                ROADWAY_BLOCK: 'Roadway_Block.geojson'}
                # 'alleys_and_parking': 'Alleys_and_Parking.geojson'}

PBLS = 'protected_bike_lanes' # no file for this one; we'll split it out from the general bike data

# reading in each of the above sources
data = {data_source: gpd.read_file("data/%s"%data_sources[data_source]) for data_source in data_sources}

# projecting to miles
# NOTE: scalar projection is inherently presumptive; see coastline paradox
ECKERT_IV_PROJ4_STRING = "+proj=eck4 +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=mi +no_defs"
data_eckert4 = {data_source: data[data_source].to_crs(ECKERT_IV_PROJ4_STRING) for data_source in data}

# creating attributes for geometry length (in miles and feet)
for data_source in data_eckert4:
    data_eckert4[data_source]['geolength'] = data_eckert4[data_source].geometry.length
    data_eckert4[data_source]['geolength_feet'] = data_eckert4[data_source].geolength * 5280

# roadway_block crosswidth area is inclusive of all bike, bus, parking, drive, and median width; 
#  may want to perform subtraction for at least median width since this is not really used by any vehicles
# bike_lanes width is inclusive of buffer (which may or may not be present and may or may not contain protection if present)
# area calculations are presuming rectilinearity of these segments
for data_source, width_attribute in [(BIKE_LANES, 'TOTALBIKELANEWIDTH'), (ROADWAY_BLOCK, 'TOTALCROSSSECTIONWIDTH')]:
    data_eckert4[data_source]['area_feet'] = data_eckert4[data_source].geolength_feet * data_eckert4[data_source][width_attribute]

for data_source in data_eckert4:
    data_eckert4[data_source]['area_miles'] =  data_eckert4[data_source].area_feet / 27878400

# attribute protection to bike lanes; currently using whether any values for BIKELANE_PROTECTED and BIKELANE_DUAL_PROTECTED,
# OR if the lane is not marked as being throughlane-adjacent; the result is ~33.42 miles of protected bike lanes
data_eckert4[PBLS] = data_eckert4[BIKE_LANES][data_eckert4[BIKE_LANES][['BIKELANE_PROTECTED', 'BIKELANE_DUAL_PROTECTED']].any(axis=1) | 
                                                                        pd.isna(data_eckert4[BIKE_LANES].BIKELANE_THROUGHLANE_ADJACENT)]

for data_source in data_eckert4:
    print('total %s length (mi): %s'%(data_source, data_eckert4[data_source].geolength.sum()))
    print('total %s area (sq mi): %s'%(data_source, data_eckert4[data_source].area_miles.sum()))

calc = data_eckert4[BIKE_LANES].geolength.sum() / data_eckert4[ROADWAY_BLOCK].geolength.sum()
print('percent of roadway length with bike lanes: %s%%'%calc)

calc = data_eckert4[PBLS].geolength.sum() / data_eckert4[ROADWAY_BLOCK].geolength.sum()
print('percent of roadway length with protected bike lanes: %s%%'%calc)

calc = data_eckert4[PBLS].geolength.sum() / data_eckert4[BIKE_LANES].geolength.sum()
print('percent of bike lane length with protection: %s%%'%calc)

calc = data_eckert4[BIKE_LANES].area_feet.sum() / data_eckert4[ROADWAY_BLOCK].area_feet.sum()
print('percent of roadway area comprised of bike lane area: %s%%'%calc)

calc = data_eckert4[PBLS].area_feet.sum() / data_eckert4[ROADWAY_BLOCK].area_feet.sum()
print('percent of roadway area comprised of protected bike lane area: %s%%'%calc)

# ward-specific calculating
for ward in range(1, 9):
    print('Ward %i: total roadway block length (mi): %s'%(ward, data_eckert4['roadway_block'][data_eckert4['roadway_block'].WARD_ID == str(ward)].geolength.sum()))
    print('Ward %i: total roadway block  area (sq mi): %s'%(ward, data_eckert4['roadway_block'][data_eckert4['roadway_block'].WARD_ID == str(ward)].area_miles.sum()))

