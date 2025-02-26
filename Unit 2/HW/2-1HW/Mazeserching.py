
import random, time,os
file=open('hwmaze.txt','r')
maze=[]
while True:
    line = file.readline()
    if line == "":
        break
    else:
        maze.append(line.rstrip('\n').split(','))

step=0

def displayMaze():

    #Slow down to watch simulation
    time.sleep(0.2)
    os.system("cls")

    #Adjust output to make it look better on the screen
    map = "\n\n"
    for row in range(0,len(maze)):
        for col in range(0,len(maze[row])):
            if maze[row][col] == "1":
                map = map + "[X]"

            if maze[row][col] == "0":
                map = map +  "   "

            if maze[row][col] == ".":
                map = map + " . "

            if maze[row][col] == "2":
                map = map + "   "

            if maze[row][col] == "E":
                map = map + " E "

            if maze[row][col] == "S":
                map = map + " S "

        map = map + "\n"

    print(map)

def move(row,col):
   
    global maze,step

    
    possibles = [[row,col+1],[row,col-1],[row-1,col],[row+1,col]]
    random.shuffle(possibles)


    if 0<=row <len(maze) and 0<=col <len(maze[0]) and (maze[row][col] == "0" or maze[row][col] == "s"):
        maze[row][col] = "."
        step=step+1 
      
        

        if (move(possibles[0][0],possibles[0][1])):  
            return True

        elif (move(possibles[1][0],possibles[1][1])): 
            return True

        elif (move(possibles[2][0],possibles[2][1])):
            return True

        elif (move(possibles[3][0],possibles[3][1])):
            return True

        else:
            maze[row][col] = "2"
            
            return False

    
    elif  0<=row <len(maze) and 0<=col <len(maze[0])and ( maze[row][col] == "e"):
        maze[row][col] = "."
        return True

    return False

def main():
    global step, maze
    steps=[]
    for i in range(10):
        
        move(0,3)
       
        with open('hwmane2.txt', 'a') as file1:
            for row in maze:   
                file1.write(' '.join([str(item) for item in row]))   
                file1.write('\n')
            file1.write('\n')
               
        steps.append(step)

    maxx=max(steps)
    minn=min(steps)
    ave= sum(steps)//len(steps)
    print(f'''max steps= {maxx}
            min dteps={minn}
            everage steps={ave}''')
    

main()

