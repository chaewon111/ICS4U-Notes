
import random
file=open('hwmaze.txt','r')
maze=[]
while True:
    line = file.readline()
    if line == "":
        break
    else:
        maze.append(line.rstrip('\n').split())

step=0


def move(row,col):
   
    global maze

    
    possibles = [[row,col+1],[row,col-1],[row-1,col],[row+1,col]]
    random.shuffle(possibles)


    if maze[row][col] == "0" or maze[row][col] == "S":
        maze[row][col] = "."
        step=step+1 # 가능한 인덱스 어팬드드
        

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

    #Found exit
    elif maze[row][col] == "E":
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
        steps.append(step)

    maxx=max(steps)
    minn=min(steps)
    ave= sum(steps)//len(steps)
    print(f'''max steps= {maxx}
            min dteps={minn}
            everage steps={ave}''')

