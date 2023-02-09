from math import sqrt

mirror_no = 1#int(input())

ray = [int(i) for i in input().split(',')]
s = (ray[3]-ray[1])/(ray[2]-ray[0])
ml = [s, -1, ray[1]-s*ray[0]]

mirror_co = [[(0, 5), (10, 5)], [(0, 0), (10, 0)]]

prev_point = [ray[0], ray[1]]
current_point = [ray[0], ray[1]]


def distance(p1, p2):
    return sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)


def find_intersection(ml):
    cl = []
    for _, i in enumerate(mirror_co):
        mirror_slope = (i[1][1] - i[0][1]) / ((i[1][0] - i[0][0]))
        mp = [mirror_slope, -1, i[0][1] - mirror_slope * i[0][0]]

        if ml[0] != mirror_slope:
            x0 = (ml[1] * mp[2] - mp[1] * ml[2]) / (ml[0] * mp[1] - mp[0] * ml[1])
            y0 = (ml[2] * mp[0] - mp[2] * ml[0]) / (ml[0] * mp[1] - mp[0] * ml[1])
            if i[0][0] <= x0 <= i[1][0] and i[0][1] <= y0 <= i[1][1] and x0 != current_point[0] and\
                    y0 != current_point[1]:  #TODO think about something here
                cl.append([x0, y0, _])

    return cl


def find_next_point(point, list):
    min, dist = [0, 0], 1000000000000
    for i in list:
        if distance(point, i) < dist:
            min = point
            dist = distance(point, i)

    return min


def find_next_line(point):
    i = mirror_co[point[2]]
    mirror_slope = (i[1][1] - i[0][1]) / ((i[1][0] - i[0][0]))
    mp = [mirror_slope, -1, i[0][1] - mirror_slope * i[0][0]]
    nothing = (ml[0]*mp[1]**2 - ml[0]*mp[0]**2 - 2*ml[1]*mp[0]*mp[1]) / (ml[1]*mp[1]**2 - ml[1]*mp[0]**2 + 2*ml[0]*mp[0]*mp[1])

    nl = [nothing, -1, (ml[0]*mp[2] - ml[2]*mp[0]) / (ml[1]*mp[0] - ml[0]*mp[1]) - nothing*(ml[1]*mp[2] - ml[2]*mp[1])/(ml[0]*mp[1]-ml[1]*mp[0])]
    return nl


def refine_points(points):
    nl = []
    if len(points) != 0:
        for _ in points:
            i = mirror_co[_[2]]
            mirror_slope = (i[1][1] - i[0][1]) / ((i[1][0] - i[0][0]))
            mp = [mirror_slope, -1, i[0][1] - mirror_slope * i[0][0]]

            if (prev_point[0] * mp[0] + prev_point[1] * mp[1] + mp[2] <= 0 and _[0] * mp[0] + _[1] * mp[1] + mp[
                2] <= 0) or \
                    (prev_point[0] * mp[0] + prev_point[1] * mp[1] + mp[2] >= 0 and _[0] * mp[0] + _[1] * mp[1] + mp[
                        2] >= 0):
                nl.append(_)
    return nl


while True:
    points = refine_points(find_intersection(ml))
    if len(points) == 0:
        result = find_intersection([[1, 0, -10]])
        print(result[1])
    pt = find_next_point(current_point, points)
    ml = find_next_line(pt)

