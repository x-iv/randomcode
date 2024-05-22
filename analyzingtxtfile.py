with open('sampletxt1-nigeria.txt', 'r') as file:
    for countw in file:
        print(countw.count('o'))
