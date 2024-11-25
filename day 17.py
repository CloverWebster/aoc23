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
        if crucible.streak != 3 or crucible.dire != 'R':
            curCruc = Crucibles(crucible.xpos + 1,crucible.ypos, crucible.heat, 'R', 1)
            curCruc.heat += grid[curCruc.ypos][curCruc.xpos]
            if crucible.dire =='R':
                curCruc.streak = crucible.streak + 1 
            newCrucs.append(curCruc)

# left
    if crucible.xpos > 0 and crucible.dire != 'R':
        if crucible.streak != 3 or crucible.dire != 'L':
            curCruc = Crucibles(crucible.xpos - 1,crucible.ypos, crucible.heat, 'L', 1)
            curCruc.heat += grid[curCruc.ypos][curCruc.xpos] 
            if crucible.dire =='L':
                curCruc.streak = crucible.streak + 1 
            newCrucs.append(curCruc)

# up
    if crucible.ypos > 0 and crucible.dire != 'D':
        if crucible.streak != 3 or crucible.dire != 'U':
            curCruc = Crucibles(crucible.xpos,crucible.ypos - 1, crucible.heat, 'U', 1)
            curCruc.heat += grid[curCruc.ypos][curCruc.xpos]
            if crucible.dire =='U':
                curCruc.streak = crucible.streak + 1  
            newCrucs.append(curCruc)

# down
    if crucible.ypos < len(grid)-1 and crucible.dire != 'U':
        if crucible.streak != 3 or crucible.dire != 'D':
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
    cruc = Crucibles(0,0,0,'', 0)
    global allCrucibles
    allCrucibles = [cruc]
firstCrucible()


def prune(crucList):
    finish = []
    while len(crucList) > 0:
        curMatch =[crucList[0].heat]
        matchPos = [0]
        for x in range(1,len(crucList)):
            if crucList[0].xpos == crucList[x].xpos and crucList[0].ypos == crucList[x].ypos:
                if crucList[0].dire == crucList[x].dire and crucList[0].streak == crucList[x].streak:
                    curMatch.append(crucList[x].heat)
                    matchPos.append(x)
        minheat = min(curMatch)
        for x in range(0, len(curMatch)):
            if curMatch[x] == minheat:
                finish.append(crucList[matchPos[x]])
                break
        for x in range(len(matchPos) - 1, -1, -1):
            crucList.remove(crucList[x])
    return finish



with open('17.txt') as j:
    data = [i for i in j.read().strip().split("\n")]
grid = []
for x in data:
    curData = []
    for y in range(0,len(x)):
        curData.append(int(x[y]))
    grid.append(curData)
#grid= [[1,2,3],
       #[4,5,6],
       #[7,8,9]]

minHeat = 200

counter = 0
while len(allCrucibles) > 0:
    counter += 1
    print(counter)
    newCrucs = []
    for instance in allCrucibles:
        move(instance)
    allCrucibles = []
    for instance in newCrucs:
        #print(instance.xpos, instance.ypos, '/ heat:', instance.heat, '/ dir:', instance.dire, '/ streak:', instance.streak)
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
    #print('all crucibles:',len(allCrucibles))



# test print
#for x in newCrucs:
    #print(x.xpos, x.ypos, '/ heat:', x.heat, '/ dir:', x.dire, '/ streak:', x.streak)
print('end',minHeat)