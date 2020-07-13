import math as m
t1 = float(input("Enter latitude of the first point:"))
g1 = float(input("Enter longitude of the first point:"))

t2 = float(input("Enter latitude of the second point:"))
g2 = float(input("Enter longitude of th second point:"))

d = 6371.01* m.acos(m.sin(t1)*m.sin(t2)+m.cos(t1)*m.cos(t2)*m.cos(g1-g2))

print("The distance between the two points=",d,"km")