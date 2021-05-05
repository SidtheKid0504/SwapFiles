def swapFileData():
    file1Path = input("First File Path: ")
    file2Path = input("Second File Path: ")

    file1 = open(file1Path)
    file2 = open(file2Path)

    data_a = file1.read()
    data_b = file2.read()

    file1.close()
    file2.close()

    with open(file1Path, 'w') as a:
        a.write(data_b)

    with open(file2Path, 'w') as b:
        b.write(data_a)

swapFileData()