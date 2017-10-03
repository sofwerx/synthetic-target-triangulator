# import wrapper as w
# import math

from swx import Target

# Test1 for degrees
# test_input1 = (-3,3,126)
# test_input2 = (-3,-3,54)
# test_input3 = (3,-3,326)
# test_input4 = (8,8,90)
# bad_input = (-5,-5,54)

inputCoordsYes = '{"coords": [{"lat": -3, "lon": 3, "aob": 126, "angleUnit": "deg"}, {"lat": -3, "lon": -3, "aob": 54, "angleUnit": "deg"}, {"lat": 3, "lon": -3, "aob": 326, "angleUnit": "deg"}]}'
inputCoordsNo = '{"coords": [{"lat": -3, "lon": 3, "aob": 126, "angleUnit": "deg"}, {"lat": -3, "lon": -3, "aob": 54, "angleUnit": "deg"}, {"lat": -5, "lon": -5, "aob": 54, "angleUnit": "deg"}]}'

t = Target.TargetLoc()

print(inputCoordsYes)
targetLoc = t.locate(inputCoordsYes)
print(targetLoc)

print(inputCordsNo)
targetLoc = t.locate(inputCordsNo)
print(targetLoc)
