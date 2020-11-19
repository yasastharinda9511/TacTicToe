grid=[[0,0,0],
      [0,0,0],
      [0,0,0]]
def empty(grid):
    empty=[]
    for i in range(len(grid)):
        for r in range(len(grid[i])):
            if grid[i][r]==0:
                empty.append([i,r])
    return empty
def winning(x):
    c2=0
    c4=0
    for i in range(len(grid)):
        c1=0
        c3=0
        for r in range(len(grid[i])):
            if grid[i][r]==x:
                c1 +=1
            if grid[r][i]==x:
                c3= +1
        if c1==3:
            return True
        if c3==3:
            return True
        if grid[i][i]==x:
            c2 +=1
        if grid[i][2-i]==x:
            c4 +=1
    if (c2==3):
        return True
    if (c4==3):
        return True
    return False
def winningChance(side):
    space1=[]
    space2=[]
    c1=0
    c2=0
    for i in range(len(grid)):
        space3=[]
        space4=[]
        c3=0
        c4=0
        for r in range(len(grid[i])):
            if grid[i][r]==side:
                c3 +=1
            elif grid[i][r]==0:
                space3.append((i,r))
            if grid[r][i]==side:
                c4 +=1
            elif grid[r][i]==0:
                space4.append((r,i))
        if grid[i][i]==side:
            c1+=1
        elif grid[i][i]==0:
            space1.append((i,r))
        if grid[i][2-i]==side:
            c2+=1
        elif grid[i][2-i]==0:
            space2.append((i,2-i))
        if c3==2 and len(space3)==1:
            return True,space3
        if c4==2 and len(space4)==1:
            return True,space4
    if c1==2 and len(space1)==1:
        return True,space1
    if c2==2 and len(space2)==1:
        return True,space2
    return False,None
def countingValues(grid,side,AI):
    c1=0
    c2=0
    spaceC1=0
    spaceC2=0
    count=0
    for i in range(len(grid)):
        c3=0
        c4=0
        spaceC3=0
        spaceC4=0
        for r in range(len(grid[i])):
            if grid[i][r]==side:
                c3+=1
            elif grid[i][r]==0:
                spaceC3+=1
            if grid[r][i]==side:
                c4+=1
            elif grid[r][i]==0:
                spaceC4+=1
        if c3==1 and spaceC3==2 :
            if side==AI:
                count+=1
            else:
                count -=1
        elif c3==2 and spaceC3==1:
            if side==AI:
                count+=10
            else:
                count -=10
        if c4==1 and spaceC4==2 :
            if side==AI:
                count+=1
            else:
                count -=1
        elif c4==2 and spaceC4==1:
            if side==AI:
                count+=10
            else:
                count -=10
        if grid[i][i]==side:
            c1+=1
        elif grid[i][i]==0:
            spaceC1+=1
        if grid[2-i][i]==side:
            c2+=1
        elif grid[2-i][i]==0:
            spaceC2+=1
    if c1==1 and spaceC1==2 :
        if side==AI:
            count+=1
        else:
            count -=1
    elif c1==2 and spaceC1==1:
        if side==AI:
            count+=10
        else:
            count -=10
    if c2==1 and spaceC2==2 :
        if side==AI:
            count+=1
        else:
            count -=1
    elif c2==2 and spaceC2==1:
        if side==AI:
            count+=10
        else:
            count -=10
    return count
def search_item(dic,value):
    x=dic.keys()
    for i in x :
        if dic[i]==value:
            return i
#print search_item({1:23,2:50,3:30},30)
def alphabetaprunning(turn,grid,deep,AI,opponent):
    empty1=empty(grid)
    dic={}
    if len(empty1)==0:
        return countingValues(grid,AI,AI)+countingValues(grid,opponent,AI),None
    for i in empty1:
        if (i[0],i[1]) not in dic:
            dic[(i[0],i[1])]=0
        if (turn%2==0):
            grid[i[0]][i[1]]=AI
        else:
            grid[i[0]][i[1]]=opponent
        if winning(opponent):
            dic[(i[0],i[1])]=+100
        elif winning(AI):
            dic[(i[0],i[1])]=-100
        else:
            if deep==1:
                dic[(i[0],i[1])]= countingValues(grid,AI,AI)+countingValues(grid,opponent,AI)
            else:
                p,q=alphabetaprunning(turn+1,grid,deep-1,AI,opponent)
                dic[(i[0],i[1])]=p
            #print(alphabetaprunning(turn+1,grid,deep-1))
        grid[i[0]][i[1]]=0
    ##print (min(dic.values()))
    #print ((dic.values()))
    #print dic
    #print("####")
    #print (min(dic.values()))
    #print(dic)
    if (turn%2==0):
        z=max(dic.values())
        return z,search_item(dic,z)
    else:
        z=min(dic.values())
        return z,search_item(dic,z)

#print(alphabetaprunning(0,grid,4))
def printgrid(grid):
    for i in range(len(grid)):
        for r in range(len(grid[i])):
            print(grid[i][r]),
            print ("   "),
        print("\n")
    print ("####################################")
def player(turn,side):
    if side==1:
        AI=1
        opponent=2
    else:
        AI=2
        opponent=1
    if side==1 and turn==1:
        p,q=alphabetaprunning(0,grid,4,AI,opponent)
        print(alphabetaprunning(0,grid,4,AI,opponent))
        coordx,coordy=q
        grid[coordx][coordy]=AI
        printgrid(grid)
        return 
    condition,listCoord=winningChance(opponent)
    condition1,listCoord1=winningChance(AI)
    if (condition==False and condition1==False):
        print("no winning chance here")
        p,q=alphabetaprunning(0,grid,4,AI,opponent)
        print(alphabetaprunning(0,grid,4,AI,opponent))
        coordx,coordy=q
        grid[coordx][coordy]=AI
    elif (condition1):
        coordx,coordy=listCoord1[0]
        grid[coordx][coordy]=AI
        print (str(side)+" wins")
    else :
        print(winningChance(opponent))
        coordx,coordy=listCoord[0]
        print (coordx)
        print(coordy)
        grid[coordx][coordy]=AI
    printgrid(grid)
turn=1
while(1):
    player(turn,1)
    empty1=empty(grid)
    ##print(len(empty1))
    if (len(empty1))==0:
        print("Game Over")
        z=raw_input()
        printgrid(grid)
        break
    player(turn,2)
    if (len(empty1))==0:
        print("Game Over")
        z=raw_input()
        printgrid(grid)
        break
    turn=turn+1
    
