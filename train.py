# Implementation of graph using dictionary data type.


# Below is the implementation of graph using dict Keys are starting stations node and list values are stations directly
# linked to the starting station along with distance between them.
stations_routes = {"A": [["B", 1]],
                   "B": [["C", 3], ["D", 2],  ["E", 1]],
                   "C": [["D", 1], ["E", 4]],
                   "D": [["A", 2], ["E", 2]],
                   "E": [["F", 3]],
                   "G": [["D", 1]],}


def calcDistance(route: list):
      distance = 0
      route1 = [route[0]]
      lastStation = route[len(route) - 1]
      for station in route:
            #print(type(station))
            if station == lastStation:
                  break
            for next in stations_routes.get(station):
                  #print(next)
                  for x in next:
                        if type(x) == str:
                              if x == route[route.index(station) + 1]:
                                    #print(x)
                                    nxtStation, dist = next
                                    route1.append(nxtStation)
                                    distance += dist
      if route1 == route:
            return f"\nTotal distance of route {route1} is {distance}."
      else:
            return f"\nRoute {route} does not exist."


