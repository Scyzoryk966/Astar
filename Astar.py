from operator import attrgetter


def matrxidisp(matrix, start, end, test=None):  # fun wyswietlanko z kolorkami + podświetlanie danej krotki w celach testowych
    if test is None:
        test = [None, None]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 5:
                print('\033[91m' + str(matrix[i][j]) + '\033[0m' + '  ', end='')  # "sciany" czerwone
            elif matrix[i][j] == 3 and (start[0] != i or start[1] != j) and (end[0] != i or end[1] != j) and (test[0] != i or test[1] != j):
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
    if x >= 0 and y >= 0 and x <= len(grid[0])-1 and y <= len(grid)-1 and grid[x][y] != 5:
        temp = Area(x, y, end[0], end[1], visitedlist[-1])
        if temp not in visitedlist and temp not in checklist:
            checklist.append(temp)
        else:                  # to jest chyba nie potrzebne w przypadku kiedy mamy koszt=1 i poruszanie sie tylko d,l,g,p
            for i in visitedlist:
                if i.h > temp.h:   # działa?
                    visitedlist[visitedlist.index(i)] = temp
                    break


def traceroute(last, grid):
    grid[last.x][last.y] = 3
    if last.parent:
        return traceroute(last.parent, grid)


class Area:
    def __init__(self, x, y, endX, endY, parent, cost=None):  # konstruktor
        if cost is None:
            cost = 1 + parent.cost
        else:
            cost = cost
        self.x = x
        self.y = y
        self.cost = cost
        self.h = cost + self.heuristics(endX, endY)
        self.parent = parent

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def heuristics(self, endX, endY):
        return ((self.x - endX) ** 2 + (self.y - endY) ** 2) ** 0.5

    def display(self):
        print("X:", self.x, " Y:", self.y, " Heuristics:", self.h, end='')
        if (self.parent):
            print(" Parent:[", self.parent.x, ",", self.parent.y, "]")
        else:
            print()


end = [19, 19]  # CEL
start = [0, 0]  # punkt startowy
objectStart = Area(start[0], start[1], end[0], end[1], None, 0)  # obiekt pkt startowego
checklist = []  # lista sprawdzanych pol
visitedlist = [objectStart]  # lista zamknieta odwiedzonych pol
grid = fileread('grid.txt') # wczytywanie mapy

while True:
    x = visitedlist[-1].x
    y = visitedlist[-1].y

    checktuple(x + 1, y, grid, end, checklist, visitedlist)
    checktuple(x, y - 1, grid, end, checklist, visitedlist)
    checktuple(x - 1, y, grid, end, checklist, visitedlist)
    checktuple(x, y + 1, grid, end, checklist, visitedlist)

    checklist.sort(key=lambda h: h.h, reverse=True)  # sortowanie listy otwartej po koszcie
    if not (checklist[-1] in visitedlist):
        checklist[-1].display()
        visitedlist.append(checklist[-1])
    checklist.pop()
    if visitedlist[-1].x == end[0] and visitedlist[-1].y == end[1]:
        break
    else:
        continue

for i in visitedlist:   # wstawia 1 w odwiedzonych krotkach
    grid[i.x][i.y] = 1

traceroute(visitedlist[-1], grid)
matrxidisp(grid, start, end)
