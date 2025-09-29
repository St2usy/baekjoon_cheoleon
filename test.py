def find_missing_points(sqr) :
    xs = [x[0] for x in sqr]
    ys = [y[1] for y in sqr]

    for x in xs :
        if xs.count(x) == 1:
            missing_x = x
    for y in ys :
        if ys.count(y) == 1:
            missing_y = y
    return (missing_x, missing_y)
points = [(1, 2), (1, 5), (4, 2)]
print(find_missing_points(points)) 