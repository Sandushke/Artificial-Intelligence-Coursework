import random

print("--- 6 x 6 Maze ---")
# TASK 1
def create_maze():
    # Create a 2D array for the maze
    maze_size = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

    # Set a start goal point between the last two columns
    global start_X, start_Y
    start_X = random.randint(0, 5)
    start_Y = random.randint(0, 1)

    # Setting the start goal point to 2
    maze_size[start_X][start_Y] = 2

    # Set an end goal point between the 1st two columns
    global end_X, end_Y
    end_X = random.randint(0, 5)
    end_Y = random.randint(4, 5)

    # Set the end goal point as 4
    maze_size[end_X][end_Y] = 4

    # Create a barrier to the maize
    barrier = 0
    while barrier < 4:
        barrier_X = random.randint(0, 5)
        barrier_Y = random.randint(0, 5)

        # Check if barrier falls on the index values of start and end goal
        barrier_point = maze_size[barrier_X][barrier_Y]
        if barrier_point == 2 or barrier_point == 4 or barrier_point == 1:
            barrier = barrier
            continue

        # Place 4 barrier nodes in the maze
        else:
            maze_size[barrier_X][barrier_Y] = 1
            barrier += 1

    # Print the 2D array one below the other
    for i in maze_size:
        for j in i:
            print(j, end=" ")
        print()

    DFS(maze_size, start_X, start_Y, end_X, end_Y)
    aStar(maze_size, start_X, start_Y, end_X, end_Y)


# ----------------------------------------------------------

# TASK 2
print("-----DFS ALGORITHM-------")

# Create maze using DFS algorithm
def DFS(maze_size, start_row, start_col, end_row, end_col):
    # initializing the variables
    currentPath = []
    exploredNode= []
    start = (start_row, start_col)
    currentPath.append(start)
    exploredNode.append(start)
    dfs_path = {}
    subNode = ()

    pathFound = False

    while not pathFound:
        if len(currentPath) == 0:
            print("DFS path couldn't found")
            break
        else:
            current = currentPath.pop()
            exploredNode.append(current)

            #Set the starting col to index 0 and starting row to index 1
            start_col = current[0]
            start_row = current[1]

        # check if the start start goal node is == 4
        # if yes, print as dfs path found
        if maze_size[start_row][start_col] == 4:
            print("")
            print("-----DFS path found-----")
            print("DFS path travelled:", exploredNode)
            pathFound = True
            break

        else:
            # check for left, top, bottom and right in order
            for i in "LTBR":
                # Check when i in left
                if i == "L":
                    if start_row - 1 >=0:
                        if maze_size[start_col][start_row - 1] == 0 or maze_size[start_col][start_row -1] == 4:
                            subNode = (start_col, start_row - 1)

                #check when i in top
                elif i == "T":
                    if start_col - 1 >= 0:
                        if maze_size[start_col - 1][start_row] == 0 or maze_size[start_col - 1][start_row] == 4:
                            subNode = (start_col - 1, start_row)

                # check when i in bottom
                elif i == "B":
                    if start_col+1 <=5:
                        if maze_size[start_col+1][start_row] == 0 or maze_size[start_col+1][start_row]== 4:
                            subNode = (start_col+1, start_row-1)

                # check when i in right
                elif i == "R":
                    if start_row + 1 <= 5:
                        if maze_size[start_col][start_row + 1] == 0 or maze_size[start_col][start_row + 1]== 4:
                            subNode = (start_col, start_row + 1)


                #append the each and every exploring node to the path list
                if subNode in exploredNode:
                    continue
                currentPath.append(subNode)
                dfs_path[subNode] = current

    frontPath = {}
    coordinates = (start_col, start_row)
    while coordinates != start:
        frontPath[dfs_path[coordinates]] = coordinates
        coordinates = dfs_path[coordinates]

    #Calculate the time taken to travel the path using DFS algorithm
    if pathFound == True:
        timeTaken = len(dfs_path)
        print("Time taken by DFS to find the goal node: "+ str(timeTaken)+ " minutes")
        print("")


# --------------------------------------------------------------------------------------------------------
# Task 3
# Find the heuristic cost value
def getHeuristicCost(end_X, end_Y):
    a = 0
    gx = end_X
    gy = end_Y
    heuristicList = []

    while a < 6:
        b = 0
        while b < 6:
            heuristicValue = max(abs(a - gx), abs(b - gy))
            heuristicList.append(heuristicValue)
            b += 1
        a += 1
    return heuristicList


# -------------------------------------------------------------------------------------------------------
# Task 4
#Cretae a* algorithm for maze
def aStar(maze_size, start_row, start_col, end_row, end_col):
    #Initialize the variables
    starGoal = (start_col, start_row)
    endGoal = (end_col, end_row)
    queuePath = []
    nodeValues = []
    exploredNodes = []
    heuristicValues = {}
    subNode = starGoal
    previousNode = {}

    pathFound = False

    #get the gx,gy values passing from hueristic cost function
    hueristicCost = getHeuristicCost(end_row, end_col)
    print("------a* algorithm------")
    print("Heuristic cost: ", hueristicCost)
    print("")
    print("a* path travelled: ")

    for i in range(6):
        for j in range(6):
            temp = (j, i)
            nodeValues.append(temp)

    for i in range(36):
        tempValueHolder = nodeValues[i]
        heuristicValues[tempValueHolder] = hueristicCost[i]

    gValue ={value: float("inf") for value in nodeValues}
    gValue[starGoal] = 0
    fValue = {value: float("inf") for value in nodeValues}
    fValue[starGoal] = heuristicValues[starGoal]
    queuePath.append(starGoal)

    while len(queuePath)!= 0:
        current = queuePath.pop(0)
        start_col = current[0]
        start_row = current[1]
        exploredNodes.append(current)

        if current == endGoal:
            print("a* path found")
            print(exploredNodes)
            break
        else:
            # check for left, top, bottom and right in order
            for i in "LTBR":
                # Check when i in left
                if i == "L":
                    if start_row - 1 >= 0:
                        if maze_size[start_col][start_row - 1] == 0 or maze_size[start_col][start_row - 1] == 4:
                            subNode = (start_col, start_row - 1)
                            pathFound = True

                # check when i in top
                elif i == "T":
                    if start_col - 1 >= 0:
                        if maze_size[start_col - 1][start_row] == 0 or maze_size[start_col - 1][start_row] == 4:
                            subNode = (start_col - 1, start_row)
                            pathFound = True

                # check when i in bottom
                elif i == "B":
                    if start_col + 1 <= 5:
                        if maze_size[start_col + 1][start_row] == 0 or maze_size[start_col + 1][start_row] == 4:
                            subNode = (start_col + 1, start_row - 1)
                            pathFound = True

                # check when i in right
                elif i == "R":
                    if start_row + 1 <= 5:
                        if maze_size[start_col][start_row + 1] == 0 or maze_size[start_col][start_row + 1] == 4:
                            subNode = (start_col, start_row + 1)
                            pathFound = True


                #Checking the final correct path it travelled and append all the values to the list
                tmpGResult = gValue[current] + 1
                tempFResult = tmpGResult + heuristicValues[subNode]
                if tempFResult < fValue[subNode]:
                    fValue[subNode] = tmpGResult
                    fValue[subNode] = tempFResult
                    queuePath.append(subNode)
                    previousNode[subNode] = current

        nextNode = {}
        node = []
        coordinates = (start_col, start_row)
        while coordinates != starGoal:
            nextNode[previousNode[coordinates]] = coordinates
            coordinates = previousNode[coordinates]
            astar = nextNode
            node.append(*astar.values())
            print(node, end="")

    #Get the time taken to find the goal node using a*
    if pathFound == True:
        timeTaken = len(previousNode)
        print("")
        print("Time taken by a* to reach the goal node: "+ str(timeTaken)+ " minutes")
        print("")

# Call the main function create_maze
create_maze()