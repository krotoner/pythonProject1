print("---157---")
mark = input("Введите оценку: ")
d = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
while mark != "":
    mark = mark.upper()
    try:
        letter = str(mark)
        for i in letter:
            print(d[i])
    except Exception:
        for key, value in d.items():
            if str(value) == mark:
                print(key)
    mark = input('Введите оценку: ')

