def matrxidisp(matrix):  # fun wyswietlanko
    for i in range(len(matrix)):
        print(matrix[i])


def fileread(name):  # fun otwieranie pliku
    file = open(name)
    grid = file.readlines()  # czytanie wszytskich linii do listy
    for i in range(len(grid)):
        grid[i] = list(map(int, grid[i].split(
            ' ')))  # rzut na liste *list* i podzielenie *split* stringa z 'przerywaczem' SPACJA i rzutowaniem na inta
    file.close()
    return grid

#Zmienne Globalne (brak)

class Area:
    def __init__(self, x, y, endX, endY, parent): #konstruktor
        self.x = x
        self.y = y
        self.h = self.heuristics(endX, endY)
        self.parent = parent

    def heuristics(self, endX, endY):
        return ((self.x - endX) ** 2 + (self.y - endY) ** 2) ** 0.5

    def display(self):
        print("X:", self.x, " Y:", self.y, " Heuristics:", self.h, end='')
        if(self.parent):
            print(" Parent:[", self.parent.x, ",", self.parent.x, "]")
        else:
            print()


celTest = [18, 19]
obiektTest1 = Area(0, 0, celTest[0], celTest[1], None)
obiektTest2 = Area(1, 0, celTest[0], celTest[1], obiektTest1)

obiektTest1.display()
obiektTest2.display()

grid = fileread('grid.txt')
matrxidisp(grid)
