def find_circular_path(n, m):
    # Start at index 0
    current_index = 0
    path = []

    # While the path length is less than n
    while len(path) < n:
        path.append(current_index + 1)

        current_index = (current_index + m - 1) % n

    return path


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        sys.exit(1)

    n, m = map(int, sys.argv[1:])
    result = find_circular_path(n, m)
    print("Circular path:", "".join(map(str, result)))
