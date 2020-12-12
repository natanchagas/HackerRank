if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    results = []

    print([[val_x, val_y, val_z] for val_x in range(x + 1) for val_y in range(y + 1) for val_z in range(z + 1) if ((val_x + val_y + val_z) != n)])