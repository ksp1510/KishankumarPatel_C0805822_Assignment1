# Implementation of graph using dictionary data type.
# Below is the implementation of graph using dict Keys are starting stations node and list values are stations directly
# linked to the starting station along with distance between them.
stations_routes = {"A": [["B", 1]],
                   "B": [["C", 3], ["D", 2], ["E", 1]],
                   "C": [["D", 1], ["E", 4]],
                   "D": [["A", 2], ["E", 2]],
                   "E": [["F", 3]],
                   "G": [["D", 1]],
                   "F": None}


def calcDistance(route: list):
    distance = 0
    if isRoute(route):
        r = [route[0]]
        lastStation = route[len(route) - 1]
        for station in route:
            # print(station)
            if station == lastStation:
                break
            for next in stations_routes.get(station):
                # print(next)
                for x in next:
                    if type(x) == str:
                        if x == route[route.index(station) + 1]:
                            # print(x)
                            nxtStation, dist = next
                            r.append(nxtStation)
                            distance += dist
        return f"\nTotal distance of route {r} is {distance}."
    else:
        return f"\nRoute {route} does not exist."


def isRoute(route: list):
    route1 = [route[0]]
    lastStation = route[len(route) - 1]
    for station in route:
        #print(station)
        if station == lastStation:
            break
        for next in stations_routes.get(station):
            #print(next)
            for x in next:
                if type(x) == str:
                    if x == route[route.index(station) + 1]:
                        route1.append(x)
    if route == route1:
        return True
    else:
        return False

