#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11
def sequence():
    num = 0
    while True:
        num += 1
        yield num


if __name__ == '__main__':
    seq = sequence()
    for i in range(50):
       print(next(seq))
    
