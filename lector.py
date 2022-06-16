if __name__ == '__main__':
    f = open("TrajData.csv", "r")
    content = f.read()
    f.close()

    data = content.split("\n")
    print(data[0])
    print(data[1])

    headers = data[0].split(",")
    iter_end = 2
    for idx in range(1, iter_end):
        row = data[idx].split(",")
        for i in range(len(row)):
            if row[i] == "NaN":
                print(f"Columna {headers[i]} es un NaN")