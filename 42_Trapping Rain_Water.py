# CASE 1
height = [0,1,0,2,1,0,1,3,2,1,2,1]

# CASE 2
#height = [4,2,0,3,2,5]

def zeroremove (height):
    if height:
        if height[0] == 0:
            del height[0]
            return zeroremove(height)
        if height[-1] == 0:
            del height[-1]
            return zeroremove(height)
    return height    

def zerocounter (height): 
    return height.count(0)

def minusone(height):    
    return list(map(lambda ele: ele - 1 if ele != 0 else ele, height))
           
def solution(height):
    sumcounter = 0
    if len(height) > 1:
        height = zeroremove(height)
        sumcounter += zerocounter(height)
        height = minusone(height)
        sumcounter += solution(height)
    return sumcounter

print(solution(height))