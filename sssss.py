
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")