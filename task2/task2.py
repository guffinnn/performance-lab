def read_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [tuple(map(float, line.strip().split())) for line in lines]


def squared_distance(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


def main(file1='file1.txt', file2='file2.txt'):
    center, radius = read_coordinates(file1)
    points = read_coordinates(file2)

    squared_radius = radius[0] ** 2

    for point in points:
        dist_sq = squared_distance(point, center)
        if dist_sq < squared_radius:
            print(1)  # Inside
        elif int(dist_sq) == int(squared_radius):
            print(0)  # On circle
        else:
            print(2)  # Outside


if __name__ == '__main__':
    main()
