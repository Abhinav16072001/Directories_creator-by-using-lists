class Store_number:

    def __init__(self):
        self.a = []
        while True:
            p = input("Enter value (press n to end) :")
            if p == "n":
                break
            self.a.append(int(p))

    def show(self):
        for i in self.a:
            print(i, end=" ")

    def sum(self):
        x = sum(self.a)
        return x

    def remove(self, value):
        self.value = value
        self.a.remove(self.value)


def showcase():
    j = 0
    for i in x:
        print('Directory', j, ":", end="")
        i.show()
        print()
        j += 1


def allsum():
    j = 0
    for i in x:
        print('Directory', j, ":", i.sum())
        j += 1

def asum():
    s = 0
    for i in x:
        s = i.sum() + s
    return s


if __name__ == '__main__':
    n = int(input("Number of Directories:"))
    x = list()
    for i in range(n):
        print("Directory ", i)
        x.append(Store_number())

    print("Press 1 to Display all directories.\n"
          "Press 2 to Sum of individual directories.\n"
          "Press 3 to Sum of al directories.\n"
          "Press 4 to clear directory.")

    while True:
        m = input("->")
        if m == "1":
            showcase()
        elif m == "2":
            allsum()
        elif m == "3":
            a = asum()
            print("Total Sum =", a)
        elif m == "4":
            a = int(input("Enter Directory number:"))
            x.pop(a)
        elif m == "n":
            break
        else:
            continue
