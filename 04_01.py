#euclidean 거리 측정
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock

point1 = [3,4]
point2 = [6,6]

print(euclidean(point1, point2))
print(cityblock(point1, point2))

