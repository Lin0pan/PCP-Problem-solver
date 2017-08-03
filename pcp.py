#written by Janek Speit

import time
stoneList = [("a", "aaa"),("abaaa", "ab"),("ab", "b")]
#stoneList = [("ab", "b"),("b", "bbb"),("bb", "ba")] #place pcp stones here

def isPrefix(u, v):
    if len(u) < len(v):
        return (v[0:len(u)] == u)
    else:
        return (u[0:len(v)] == v)


def pcp(string, stoneList, maxDepth, currentDepth):
    if currentDepth <= maxDepth:
        oldString = string
        for stone in stoneList:
            if isPrefix(string[0] + stone[0], string[1] + stone[1]):
                newString = (string[0] + stone[0],string[1] + stone[1])
                if newString[0] == newString[1]:
                    print "done, solution tuple:"
                    print newString
                    return True
                else:
                    if pcp(newString, stoneList, maxDepth, currentDepth + 1): #recursion
                        return True
                    else:
                        newString = oldString #go back
    return False



#s = time.time()
#pcp (("",""),stoneList,65,0)

#e = time.time()
#print("time: ")
#print(e - s)

s = time.time()
for i in range(100):
    print "step: " + str(i + 1)
    if pcp(("",""),stoneList, i, 0):
        break
e = time.time()
print("time: ")
print(e - s)
