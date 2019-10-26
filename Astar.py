from operator import attrgetter

def matrxidisp(matrix, start, end, test=None):  # fun wyswietlanko z kolorkami + podświetlanie danej krotki w celach testowych
    if test is None:
        test = [None, None]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 5:
                print('\033[91m' + str(matrix[i][j]) + '\033[0m' + '  ', end='')  # "sciany" czerwone
            elif matrix[i][j] == 3:
                print('\033[94m' + str(matrix[i][j]) + '\033[0m' + '  ', end='')  # trasa niebieska
            elif i == start[0] and j == start[1]:
                print('\033[92m' + str(matrix[i][j]) + '\033[0m' + '  ', end='')  # start zielony
            elif i == end[0] and j == end[1]:
                print('\033[95m' + str(matrix[i][j]) + '\033[0m' + '  ', end='')  # cel rozowy
            elif i == test[0] and j == test[1]:
                print('\033[96m' + str(matrix[i][j]) + '\033[0m' + '  ',
                      end='')  # podświetla na morski komorke o podanych wspolzednych - w celach testowych
            else:
                print(str(matrix[i][j]) + '  ', end='')
        print()


def fileread(name):  # fun otwieranie pliku
    file = open(name)
    grid = file.readlines()  # czytanie wszytskich linii do listy
    for i in range(len(grid)):
        grid[i] = list(map(int, grid[i].split(
            ' ')))  # rzut na liste *list* i podzielenie *split* stringa z 'przerywaczem' SPACJA i rzutowaniem na inta
    file.close()
    return grid


def checktuple(x, y, grid, end, checklist, visitedlist):    # sprawdzamy krotki
    if x >= 0 and grid[x][y] != 5:
        temp = Area(x, y, end[0], end[1], visitedlist[-1])
        checklist.append()


# Zmienne Globalne (brak)

class Area:
    def __init__(self, x, y, endX, endY, parent, cost=None):  # konstruktor
        if cost is None:
            cost = 0 + parent.cost
        else:
            cost = cost
        self.x = x
        self.y = y
        self.cost = cost
        self.h = cost + self.heuristics(endX, endY)
        self.parent = parent

    def heuristics(self, endX, endY):
        return ((self.x - endX) ** 2 + (self.y - endY) ** 2) ** 0.5

    def display(self):
        print("X:", self.x, " Y:", self.y, " Heuristics:", self.h, end='')
        if (self.parent):
            print(" Parent:[", self.parent.x, ",", self.parent.y, "]")
        else:
            print()


end = [19, 0]  # CEL
start = [0, 0]  # punkt startowy
objectStart = Area(start[0], start[1], end[0], end[1], None, 0)  # obiekt pkt startowego
checklist = []  # lista sprawdzanych pol
visitedlist = [objectStart]  # lista zamknieta odwiedzonych pol

grid = fileread('grid.txt')
# matrxidisp(grid, start, end)

i = 0
while i <= 5: # pozniej zmienić na True
    x = visitedlist[-1].x
    y = visitedlist[-1].y

    checktuple(x + 1, y, grid, end, checklist, visitedlist)
    checktuple(x, y - 1, grid, end, checklist, visitedlist) # Dodac sprawdzanie czy sprawdzana krotka jest juz w liscie zamknietej i zopbaczyc co sie bedzie działo
    checktuple(x - 1, y, grid, end, checklist, visitedlist)
    checktuple(x, y + 1, grid, end, checklist, visitedlist)

    checklist.sort(key=lambda h: h.h)  # sortowanie listy otwartej po koszcie
    visitedlist.append(checklist[0])
    print(visitedlist[-1].display())
    checklist.clear()
    if visitedlist[-1].x == end[0] and visitedlist[-1].y == end[1]:
        break
    else:
        i += 1  # pozniej usunac / zmienic na continue
print(visitedlist)
matrxidisp(grid, start, end, [1, 0])
