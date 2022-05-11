import pandas as pd
import numpy as np
import datetime
import json


col_names = ('event_no', 'type', 'initials', 'ship_date', 'ship_time', 'water_depth', 'station_id', 'cast_no', 'start_date', 'start_time', 'start_julian_day', 'start_lat_deg', 'start_lat_min', 'start_lat', 'start_lon_deg', 'start_lon_min', 'start_lon','end_date', 'end_time', 'end_julian_day', 'end_lat_deg', 'end_lat_min', 'end_lat', 'end_lon_deg', 'end_lon_min', 'end_lon','event', 'filename', 'notes')
df = pd.read_csv('NBP22-02_Event_Log_headless.csv', names=col_names)

degree_sign = u'\N{DEGREE SIGN}'
def coord_dec_to_pretty(coord_in, absolute=True):
    if np.isnan(coord_in):
        return 'NaN'
    # convert from decimal degrees to pretty formatted string for popup text
    if absolute:
        coord_in = abs(coord_in)
    deg = int(coord_in)
    minutes = abs(coord_in - deg) * 60
    coord_str = str(deg) + degree_sign + " " + str(round(minutes, 2)) + "'"
    return coord_str


def core_to_json(df) -> dict:
    """ converts a dataframe of coring events to geojson format"""
    features = []
    for i, row in df.iterrows():
        event_popup = f"Cast: {row.cast_no}<br>Event no.{row.event_no}<br>{coord_dec_to_pretty(row.start_lat)}S \
        {coord_dec_to_pretty(row.start_lon)} W<br>Event: {row.event}<br>Start: {row.start}<br>End: {row.end}<br>{row.notes}"

        target_item = {
            "geometry": {
                "type": "Point",
                "coordinates": [
                    row.start_lon,
                    row.start_lat
                ]
            },
            "type": "Feature",
            "properties": {
                "popupContent": event_popup
            },
            "id": i,
            "start": row.start.isoformat(),
            "end": row.end.isoformat()
        }
        features.append(target_item)

    tgtdict = {
        "type": "FeatureCollection",
        "features": features
    }
    return tgtdict

# Create geojson files ready for plotting
out = ctd_to_json(df_ctd)
with open('output/ctd.json', 'w') as stream:
    json.dump(out, stream, indent=2)
