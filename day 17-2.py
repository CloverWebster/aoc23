class Crucibles:
    def __init__(Crucible, xpos, ypos, heat, dire, streak):
        Crucible.xpos = xpos
        Crucible.ypos = ypos
        Crucible.heat = heat
        Crucible.dire = dire
        Crucible.streak = streak


def move(crucible):

#move right
    if crucible.xpos < len(grid[0])-1 and crucible.dire != 'L':
        if crucible.streak < 10 or crucible.dire != 'R':
            if (crucible.dire != 'R' and crucible.streak >= 4) or crucible.dire == 'R':
                curCruc = Crucibles(crucible.xpos + 1,crucible.ypos, crucible.heat, 'R', 1)
                curCruc.heat += grid[curCruc.ypos][curCruc.xpos]
                if crucible.dire =='R':
                    curCruc.streak = crucible.streak + 1 
                newCrucs.append(curCruc)

# left
    if crucible.xpos > 0 and crucible.dire != 'R':
        if crucible.streak < 10 or crucible.dire != 'L':
            if (crucible.dire != 'L' and crucible.streak >= 4) or crucible.dire == 'L':
                curCruc = Crucibles(crucible.xpos - 1,crucible.ypos, crucible.heat, 'L', 1)
                curCruc.heat += grid[curCruc.ypos][curCruc.xpos] 
                if crucible.dire =='L':
                    curCruc.streak = crucible.streak + 1 
                newCrucs.append(curCruc)

# up
    if crucible.ypos > 0 and crucible.dire != 'D':
        if crucible.streak < 10 or crucible.dire != 'U':
            if (crucible.dire != 'U' and crucible.streak >= 4) or crucible.dire == 'U':
                curCruc = Crucibles(crucible.xpos,crucible.ypos - 1, crucible.heat, 'U', 1)
                curCruc.heat += grid[curCruc.ypos][curCruc.xpos]
                if crucible.dire =='U':
                    curCruc.streak = crucible.streak + 1  
                newCrucs.append(curCruc)

# down
    if crucible.ypos < len(grid)-1 and crucible.dire != 'U':
        if crucible.streak < 10 or crucible.dire != 'D':
            if (crucible.dire != 'D' and crucible.streak >= 4) or crucible.dire == 'D':
                curCruc = Crucibles(crucible.xpos,crucible.ypos + 1, crucible.heat, 'D', 1)
                curCruc.heat += grid[curCruc.ypos][curCruc.xpos]
                if crucible.dire =='D':
                    curCruc.streak = crucible.streak + 1  
                newCrucs.append(curCruc)



def finished(crucible):
    if crucible.xpos == len(grid[0]) - 1:
        if crucible.ypos == len(grid) -1:
            return True
    return False


def firstCrucible():
    cruc = Crucibles(0,0,0,'D', 0)
    cruc1 = Crucibles(0,0,0,'R', 0)
    global allCrucibles
    allCrucibles = [cruc,cruc1]
firstCrucible()


def prune(crucList):
    finish = []
    while len(crucList) > 0:
        y = crucList[0]
        cellHeats =[crucList[0].heat]
        x = 1
        while x < len(crucList):
            if crucList[0].xpos == crucList[x].xpos and crucList[0].ypos == crucList[x].ypos:
                if crucList[0].dire == crucList[x].dire and crucList[0].streak == crucList[x].streak:
                    cellHeats.append(crucList[x].heat)
                    crucList.remove(crucList[x])
                else: 
                    x += 1
            else:
                x += 1
        minheat = min(cellHeats)
        finish.append(Crucibles(y.xpos,y.ypos,minheat,y.dire,y.streak))
        crucList.remove(y)

    fullCrucs = []
    global minGrid
    for x in range(0,len(finish)):
        crucible = finish[x]
        if crucible.dire == 'R':
            direction = 0
        elif crucible.dire == 'L':
            direction = 1
        elif crucible.dire == 'U':
            direction = 2
        elif crucible.dire == 'D':
            direction = 3

        if crucible.heat <= minGrid[crucible.ypos][crucible.xpos][direction][crucible.streak -1]:
            fullCrucs.append(crucible)
            minGrid[crucible.ypos][crucible.xpos][direction][crucible.streak-1] = crucible.heat
    return fullCrucs



def shorten(crucibles):
    
    minscore = 1000000000000000
    maxscore = 0    
    for x in range(0,len(crucibles)):
        toGO = ((len(grid[0]) - crucibles[x].xpos) + (len(grid) - crucibles[x].ypos)) * 4
        if crucibles[x].heat + toGO < minscore:
            minscore = crucibles[x].heat + toGO
        if crucibles[x].heat + toGO > maxscore:
            maxscore = crucibles[x].heat + toGO
    midscore = (minscore + maxscore)//2
    finish = []
    for x in range(0,len(crucibles)):
        toGO = ((len(grid[0]) - crucibles[x].xpos) + (len(grid) - crucibles[x].ypos)) * 4
        if crucibles[x].heat + toGO < midscore:
            finish.append(crucibles[x])
    return finish



with open('17.txt') as j:
    data = [i for i in j.read().strip().split("\n")]
grid = []
for x in data:
    curData = []
    for y in range(0,len(x)):
        curData.append(int(x[y]))
    grid.append(curData)

minGrid = []
for x in range(0,len(grid)):
    current = []
    for y in range(0,len(grid[0])):
        curr = []
        for i in range(0,10):
            curr.append(813)
        current.append([curr,curr,curr,curr])
    minGrid.append(current)

minHeat = 813

counter = 0
while len(allCrucibles) > 0:
    counter += 1
    print(counter)
    newCrucs = []
    for instance in allCrucibles:
        move(instance)
    allCrucibles = []
    for instance in newCrucs:
        if finished(instance) == False:
            if instance.heat <= minHeat:
                if instance.xpos != 0 or instance.ypos != 0:
                    allCrucibles.append(instance)
        elif instance.heat < minHeat:
            minHeat = instance.heat
            print('new min heat', minHeat)
        if finished(instance) == True:
            print('finished', instance.heat)
    if len(allCrucibles) > 0:
        allCrucibles = prune(allCrucibles)
    if len(allCrucibles) > 5000:
        allCrucibles = shorten(allCrucibles)
        print('shortened')

print('end',minHeat)