def point_in_poly(x,y,poly): # lon,lat
        n = len(poly)
        inside = False
        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside
        

# [[LON,LAT],[LON,LAT],[LON,LAT]]
polygon=[[10,10],[50,10],[50,50],[10,50]]

print(point_in_poly(1,1,polygon)) # false
print(point_in_poly(20,20,polygon)) # true
print(point_in_poly(100,100,polygon)) # false
