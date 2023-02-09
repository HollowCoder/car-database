def open_file(filename):
    list = []
    with open(filename) as f:
        list = f.readlines()
    for i, v in enumerate(list):
        list[i] = v.rstrip()
    return list