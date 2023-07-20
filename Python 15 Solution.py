list = [[ 2, 3, 5], [-8, 4, 6], [9, 3, 77], [11, -2, 9]]

def getEven(list):
    print("2D list")
    for row in list:
        for column in row:
            print("{0:2d}".format(column), end = " ")
        print()
    print ('\n'"Number of even non negative value")
    for row in range (len(list)):
        print("Row", row+1,":", end = " ")
        count = 0
        for column in range (len(list[row])):
            if (list[row][column] % 2 == 0 and list[row][column] > 0):
                count += 1
        print(count)


getEven(list)
