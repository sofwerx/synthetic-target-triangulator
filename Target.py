from __future__ import division
import math
import json

class TargetLoc:

    # Generates new points along the line between drone and target using drones current x,y position and Line of Bearing
    def locate(self, inputCoords):
        tc = json.loads(inputCoords)
        
        # inputs are JSON Records a set of three points in the form of 'lat', 'lon' 'aob'(angle of bearing), 'angleUnit'
        # angleUnit is a string that thought be set to either 'deg' if bearing is in degrees or 'rad' if bearing is in radians
        pt = []
        ln = []
        for p in tc["coords"]:
            lat_lon = (p["lat"], p["lon"], p["aob"])
            pt = self.addPoint(lat_lon, p["angleUnit"])
            ln.append(self.extendLine(lat_lon, pt))
        
        crossing = []
        crossing.append(self.intersection(ln[0], ln[1]))
        crossing.append(self.intersection(ln[1], ln[2]))
        crossing.append(self.intersection(ln[0], ln[2]))
        
        [isect, tloc] = self.intersectedCheck(crossing) 
        
        resp = {
            "hasIntersect": isect,
            "targetLoc": {
                    "lat": tloc[0],
                    "lon": tloc[1]
                }
            }
        return json.dumps(resp)
    
    # Converts Line of Bearing into Radians if LOB was given in degrees
    def LOB_to_theta(self, LOB, rad_or_deg):
        if rad_or_deg == 'deg':
            return -(LOB - 90)
        elif rad_or_deg == 'rad':
            return -(LOB - (math.pi/2))

    # Generates a second pair of x,y coordinates for line intersection
    def addPoint(self, p, rad_or_deg):
    
        theta = self.LOB_to_theta(p[2], rad_or_deg)
        # Will only convert theta to radians if using degrees - math.tan requires radians
        if rad_or_deg == 'deg':
            theta = math.radians(theta)
        # By default, generate new point at x=1
        # if p[0] = 1, generate new point at x=2
        if p[0] != 1:
            x = 1
            y = (math.tan(theta) * (x - p[0]) + p[1])
        else:
            x = 2
            y = (math.tan(theta) * (x - p[0]) + p[1])
    
        new_point = [x, y]
        return new_point

    # Generates A, B and C from line equation Ax + By = C to be used in intersection method
    # to calculate the Differential, Dx and Dy in intersection function
    def extendLine(self, p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0]*p2[1] - p2[0]*p1[1])
        return A, B, -C

    # Given 2 lines, determines if they intersect.  Returns point of intersection if they do and False if the do not
    def intersection(self, L1, L2):
        D = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            return (x, y)
        else:
            return False

    # Determines whether intersection points are int same position or different
    def intersectedCheck(self, intersectPoints):
        # If all 3 lines intersect one another at some point, checks for relative distance from one intersections' x & y
        # coordinates.  Returns average coordinates if found, false otherwise.
        I1 = intersectPoints[0]
        I2 = intersectPoints[1]
        I3 = intersectPoints[2]
        
        if I1 and I2 and I3:
            if abs(I1[0] - I2[0]) < 0.3 and abs(I2[0] - I3[0]) < 0.3 and abs(I1[0] - I3[0]) < 0.3:
                if abs(I1[1] - I2[1]) < 0.3 and abs(I2[1] - I3[1]) < 0.3 and abs(I1[1] - I3[1]) < 0.3:
                    midpoint = ((I1[0] + I2[0] + I3[0])/3, (I1[1] + I2[1] + I3[1])/3)
                    return [True, midpoint]
                else:
                    return [False, (None, None)]
            else:
                return [False, (None, None)]
        else:
            return [False, (None, None)]
