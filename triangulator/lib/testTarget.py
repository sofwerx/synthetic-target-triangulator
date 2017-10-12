from swx import Target

inputCoordsYes = '{"coords": [{"lat": -3, "lon": 3, "aob": 126, "angleUnit": "deg"}, {"lat": -3, "lon": -3, "aob": 54, "angleUnit": "deg"}, {"lat": 3, "lon": -3, "aob": 326, "angleUnit": "deg"}]}'
inputCoordsNo = '{"coords": [{"lat": -3, "lon": 3, "aob": 126, "angleUnit": "deg"}, {"lat": -3, "lon": -3, "aob": 54, "angleUnit": "deg"}, {"lat": -5, "lon": -5, "aob": 54, "angleUnit": "deg"}]}'

#Coordinates Taken From SWX Parking Lot (10 - 15 Meters Apart) - Target Actual Values {lat: 27.957047, lon: -82.436344}
#Current Code Generates Values {lat:27.95696337783232, lon: -82.43607217387613}
#lat varies by ~0.00008, lon varies by ~.000027
###########################################################################
#                      Approximate DRONE FORMATION
#
#               1
#
#
#
#                                t                    3
#
#
#
#               2
#
###########################################################################
inputCoordsSWXParkingLot = '{"coords": [{"lat": 27.957261, "lon": -82.436587, "aob": 134.91444444, "angleUnit": "deg"}, {"lat": 27.956774, "lon": -82.436587, "aob": 38.17583333, "angleUnit": "deg"}, {"lat": 27.957050, "lon": -82.435950, "aob": 269.50611111, "angleUnit": "deg"}]}'

#Coordinates Taken From Camp Nou (Soccer Stadium, 100 Meters Apart) Barcelona, Spain - Target Actual Values {lat:41.381009, lon: 2.122952}
#Current Code Generates Values {lat: 41.38118484439955, lon: 2.1124399032619716}
#lat varies by ~0.00017584, lon varies by ~0.010512
############################################################################
#                     Approximate Drone Formation
#
#                3                  1
#
#
#
#                                   T
#
#
#
#                                   2
#
############################################################################
inputCoordsSpain= '{"coords": [{"lat": 41.381437, "lon": 2.122948, "aob": 179.59833333, "angleUnit": "deg"}, {"lat": 41.380444, "lon": 2.122952, "aob": 357.71861111, "angleUnit": "deg"}, {"lat": 41.381202, "lon": 2.122220, "aob": 109.36083333, "angleUnit": "deg"}]}'

#Coordinates Taken From Moscow, Russia (~20-30 Meters Apart) - Target Actual Values {lat:55.766693, lon: 37.614312}
#Current Code Generates Values {lat: 55.76673453811139, lon: 37.61441821497933}
#lat varies by ~0.000041538, lon varies by ~0.000106214
############################################################################
#                     Approximate Drone Formation
#
#    1               2               3
#
#            t
#
############################################################################
inputCoordsRussia= '{"coords": [{"lat": 55.766761, "lon": 37.614236, "aob": 147.84055556, "angleUnit": "deg"}, {"lat": 55.766759, "lon": 37.614359, "aob": 201.83166667, "angleUnit": "deg"}, {"lat": 55.766756, "lon": 37.614496, "aob": 238.67416667, "angleUnit": "deg"}]}'

#Coordinates Taken From Buenos Aires, Argentina (Few Blocks Apart) - Target Actual Values {lat:-34.605027, lon: -58.437577}
#Current Code Generates Values {lat: -34.6108186539048, lon: -58.43099820355034}
#lat varies by ~0.0057916539, lon varies by ~0.0065787965
############################################################################
#                     Approximate Drone Formation
#
#      t
#
#
#
#
#                                           3
#
#                                     2
#
#                              1
############################################################################
inputCoordsArgentina= '{"coords": [{"lat": -34.608330, "lon": -58.434057, "aob": 318.74361111, "angleUnit": "deg"}, {"lat": -34.607676, "lon": -58.433221, "aob": 306.45750000, "angleUnit": "deg"}, {"lat": -34.606617, "lon": -58.432920, "aob": 292.52777778, "angleUnit": "deg"}]}'

#Coordinates Taken From Sydney, Australia (Few Meters Apart) - Target Actual Values {lat: -33.905704, lon: 151.186705}
#Current Code Generates Values {lat: -33.90544260723012, lon: 151.19164649826962}
#lat varies by ~0.00026139, lon varies by ~0.0049414
############################################################################
#                     Approximate Drone Formation
#
#                            1
#                              2
#
#                             t
#
#                             3
############################################################################
inputCoordsAustralia= '{"coords": [{"lat": -33.905685, "lon": 151.186700, "aob": 167.67944444, "angleUnit": "deg"}, {"lat": -33.905689, "lon": 151.186706, "aob": 183.16694444, "angleUnit": "deg"}, {"lat": -33.905772, "lon": 151.186700, "aob": 3.49222222, "angleUnit": "deg"}]}'


################## BAD AUSTRALIA COORDINATES: Changed drone 3 to be looking the opposite direction ###############################
# This yields same result as normal Australia coordinates at the moment due to
# no error checking to see if the drone is facing the correct direction
# This feature is to be implemented next
############################################################################
#                     Approximate Drone Formation
#
#                            1
#                              2
#
#                             t1
#
#                             3
#
#                             t2
############################################################################
inputCoordsBadAustralia= '{"coords": [{"lat": -33.905685, "lon": 151.186700, "aob": 167.67944444, "angleUnit": "deg"}, {"lat": -33.905689, "lon": 151.186706, "aob": 183.16694444, "angleUnit": "deg"}, {"lat": -33.905772, "lon": 151.186700, "aob": 183.49222222, "angleUnit": "deg"}]}'

##################### NON-INTERSECTING AUSTRALIA COORDINATES: Took drone 3 from australia and rotated it 90 degrees so the lines intersect too far away from one another
# Notes: Threshold for accuracy currently set at .003 degrees.  This will still return a value due to the fact that
# the original Australia coordinates are only a few meters away.
# Accuracy not currently precise enough to see that drones are not currently looking at the same target
############################################################################
#                     Approximate Drone Formation
#
#                            1
#                              2
#
#                             t1
#
#                             3      t2
############################################################################
inputCoordsNonIntersectAustralia= '{"coords": [{"lat": -33.905685, "lon": 151.186700, "aob": 167.67944444, "angleUnit": "deg"}, {"lat": -33.905689, "lon": 151.186706, "aob": 183.16694444, "angleUnit": "deg"}, {"lat": -33.905772, "lon": 151.186700, "aob": 93.49222222, "angleUnit": "deg"}]}'

###################### NON-INTERSECTING ARGENTINA COORDINATES: Took drone 3 and rotated it 90 degrees
############################################################################
#                     Approximate Drone Formation
#
#      t
#
#
#
#
#                                           3
#
#                                     2
#
#                              1
############################################################################
inputCoordsNonIntersectArgentina= '{"coords": [{"lat": -34.608330, "lon": -58.434057, "aob": 318.74361111, "angleUnit": "deg"}, {"lat": -34.607676, "lon": -58.433221, "aob": 306.45750000, "angleUnit": "deg"}, {"lat": -34.606617, "lon": -58.432920, "aob": 202.52777778, "angleUnit": "deg"}]}'




t = Target.TargetLoc()

print(inputCoordsYes)
targetLoc = t.locate(inputCoordsYes)
print(targetLoc)

print(inputCoordsNo)
targetLoc = t.locate(inputCoordsNo)
print(targetLoc)

print(inputCoordsSWXParkingLot)
targetLoc = t.locate(inputCoordsSWXParkingLot)
print(targetLoc)

print(inputCoordsSpain)
targetLoc = t.locate(inputCoordsSpain)
print(targetLoc)

print(inputCoordsRussia)
targetLoc = t.locate(inputCoordsRussia)
print(targetLoc)

print(inputCoordsArgentina)
targetLoc = t.locate(inputCoordsArgentina)
print(targetLoc)

print(inputCoordsAustralia)
targetLoc = t.locate(inputCoordsAustralia)
print(targetLoc)

print(inputCoordsBadAustralia)
targetLoc = t.locate(inputCoordsBadAustralia)
print(targetLoc)

print(inputCoordsNonIntersectAustralia)
targetLoc = t.locate(inputCoordsNonIntersectAustralia)
print(targetLoc)

print(inputCoordsNonIntersectArgentina)
targetLoc = t.locate(inputCoordsNonIntersectArgentina)
print(targetLoc)