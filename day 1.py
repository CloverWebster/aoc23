with open('1.txt') as j:
    data = [i for i in j.read().strip().split("\n")]



#needs tidying



def part1():
    nums = ['0','1','2','3','4','5','6','7','8','9']
    total = 0
    for line in data:
        for x in line:
            if x in nums:
                num = x
                break
        for x in range(len(line)-1,-1,-1):
            if line[x] in nums:
                num += line[x]
                break
        total += int(num)
    print(total)



def part2():
    nums = ['0','1','2','3','4','5','6','7','8','9']
    total = 0
    global number
    for line in data:
        number = ''
        for x in range(0,len(line)):
            if line[x] in nums:
                number = line[x]
                break
            elif words(line,x) == True:
                break
        for x in range(len(line)-1,-1,-1):
            if line[x] in nums:
                number += line[x]
                break
            elif backwords(line,x) == True:
                break
        total += int(number)
    print(total)

def words(data, inx):
# one, two, six
    global number
    original = number
    if len(data) - 3 > inx:
        if data[inx:inx + 3] == 'one':      
            number += '1'
        elif data[inx:inx + 3] == 'two':
            number += '2'
        elif data[inx:inx + 3] == 'six':
            number += '6'
# four, five, nine
    if len(data) - 4 > inx:
        if data[inx:inx + 4] == 'four':
            number += '4'
        elif data[inx:inx + 4] == 'five':
            number += '5'
        elif data[inx:inx + 4] == 'nine':
            number += '9'
# three, seven, eight
    if len(data) - 5 > inx:
        if data[inx:inx + 5] == 'three':
            number += '3'
        elif data[inx:inx + 5] == 'seven':
            number += '7'
        elif data[inx:inx + 5] == 'eight':
            number += '8'
    if original != number:
        return True
    return False


def backwords(data, inx):
# one, two, six
    global number
    original = number
    if inx - 3 >= 0:
        if data[inx - 2 : inx +1] == 'one':      
            number += '1'
        elif data[inx - 2 : inx +1] == 'two':
            number += '2'
        elif data[inx - 2 : inx +1] == 'six':
            number += '6'
# four, five, nine
    if inx - 4 >= 0:
        if data[inx - 3 : inx +1] == 'four':
            number += '4'
        elif data[inx - 3 : inx +1] == 'five':
            number += '5'
        elif data[inx - 3 : inx +1] == 'nine':
            number += '9'
# three, seven, eight
    if inx - 5 >= 0:
        if data[inx - 4 : inx +1] == 'three':
            number += '3'
        elif data[inx - 4 : inx +1] == 'seven':
            number += '7'
        elif data[inx - 4 : inx +1] == 'eight':
            number += '8'
    if original != number:
        return True
    return False


part1()
part2()