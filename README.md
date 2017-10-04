# synthetic-target-area-of-interest

Identify and geolocate object(s) of interest using imagery and sensor data from multiple UAVs viewing a common target area, add / update corresponding feature on GIS map layer.

Web services:

Start django web server using
```python manage.py runserver```

Geolocation from lat/lon + angle of bearing, webservice component:
```http://localhost:8000/LocateTarget/```

Sample input data (JSON):
```
{
  "coords": [
    {"lat": -3, "lon": 3, "aob": 126, "angleUnit": "deg"},
    {"lat": -3, "lon": -3, "aob": 54, "angleUnit": "deg"},
    {"lat": 3, "lon": -3, "aob": 326, "angleUnit": "deg"}
  ]
}
```

Sample return (JSON):
```
{
  "hasIntersect": true,
  "targetLoc": {
    "lat": 0.995195720313976,
    "lon": 0.047692750601487664
  }
}
```
