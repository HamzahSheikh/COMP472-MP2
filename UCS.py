game = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."

# Create a converter function
def convert(game):
    #Split game into 6 character arrays
    game = [game[i:i+6] for i in range(0, len(game), 6)]

    #For each item in array, split into characters array
    for i in range(len(game)):
        game[i] = list(game[i])

    return game

def printGame(game):

    if game == None:
        print("No solution")
        return

    for row in range(len(game)):
        for col in range(len(game[row])):
            print(game[row][col], end=" ")
        print()

#Hash table to store car and direction
carDirection = {}

#Hash table to store car length
carLength = {}

#Find if the car is horitzontal or vertical
def findDirectionAndLength(game):
    
    #Seen cars
    seen = []

    for row in range(len(game)):
        for col in range(len(game[row])):
            if game[row][col] != '.' and (game[row][col] not in seen):
                seen.append(game[row][col])
                #check if car is to the right 
                if (col+1 <= 5) and game[row][col+1] == game[row][col]:
                    carDirection[game[row][col]] = 'h'
                    carLength[game[row][col]] = 2
                    #keep checking if car is to the right
                    x = 2
                    while (col+x <= 5) and game[row][col+x] == game[row][col]:
                        carLength[game[row][col]] += 1
                        x += 1
                else:
                    carDirection[game[row][col]] = 'v'
                    carLength[game[row][col]] = 2
                    #keep checking if car is below
                    x = 2
                    while (row+x <= 5) and game[row+x][col] == game[row][col]:
                        carLength[game[row][col]] += 1
                        x += 1

    return carDirection

findDirectionAndLength(convert(game))

print(convert(game))
print()
print(carDirection)
print()
print(carLength)  

#Function to move car right
def moveRight(game, car):
    #Iterate through the game 
    for row in range(len(game)):
        for col in range(len(game[row])):
            carBack = None
            carFront = None
            #Find the car
            if game[row][col] == car:
                carBack = col
                carFront = col + carLength[car] - 1
            else:
                continue
            
            #If the car is not at the right edge
            if carFront < 5 and game[row][carFront+1] == '.':
                #Move the car right
                game[row][carFront+1] = game[row][car]
                game[row][carBack] = '.'
                return game  
            else:
                return None
    return None

#Function to move car left
def moveLeft(game, car):
    #Iterate through the game 
    for row in range(len(game)):
        for col in range(len(game[row])):
            carBack = None
            carFront = None
            #Find the car
            if game[row][col] == car:
                carFront = col
                carBack = col + carLength[car] - 1
            else:
                continue
            
            #If the car is not at the left edge
            if carFront > 0 and game[row][carFront-1] == '.':
                
                #Move the car left
                game[row][carFront-1] = game[row][car]
                game[row][carBack] = '.'
                return game  
            else:
                return None 
    return None

#Function to move car up
def moveUp(game, car):
    #Iterate through the game 
    for row in range(len(game)):
        for col in range(len(game[row])):
            carBack = None
            carFront = None
            #Find the car
            if game[row][col] == car:
                carFront = row
                carBack = row + carLength[car] - 1
            else:
                continue
            
            #If the car is not at the top edge
            if row > 0 and game[carFront-1][col] == '.':
                #Move the car up
                game[carFront-1][col] = game[row][col]
                game[carBack][col] = '.'
                return game 
            else:
                return None   
    return None

#Function to move car down
def moveDown(game, car):
    #Iterate through the game 
    for row in range(len(game)):
        for col in range(len(game[row])):
            carBack = None
            carFront = None
            #Find the car
            if game[row][col] == car:
                carBack = row
                carFront = row + carLength[car] - 1
            else:
                continue
            
            #If the car is not at the bottom edge
            if carFront < 5 and game[carFront+1][col] == '.':
                #Move the car down
                game[carFront+1][col] = game[row][col]
                game[carBack][col] = '.'
                return game  
            else:
                return None  
    return None

            

# Create a function that finds children of a game 
def findChildren(game):
    #list of seen cars
    seenCars = []
    seenNodes = []

    #Iterate through the game 
    for row in range(len(game)):
        for col in range(len(game[row])):
            #If the car is not empty and has not been seen
            if game[row][col] != '.' and (game[row][col] not in seenCars):
                seenCars.append(game[row][col])
                print("Trying car: "+game[row][col])
                #If the car is horizontal
                if carDirection[game[row][col]] == 'h':
                    
                    currentGame = game

                    #keep moving car right until it hits the edge
                    while moveRight(currentGame, game[row][col]) is not None:
                        currentGame = moveRight(currentGame, game[row][col])
                        #If the node has not been seen
                        if currentGame not in seenNodes:
                            seenNodes.append(currentGame)
                            print(currentGame)
                            print()
                    
                    currentGame = game

                    #keep moving car left until it hits the edge
                    while moveLeft(currentGame, game[row][col]) is not None:
                        currentGame = moveLeft(currentGame, game[row][col])
                        #If the node has not been seen
                        if currentGame not in seenNodes:
                            seenNodes.append(currentGame)
                            print(currentGame)
                            print()
                #If the car is vertical
                if carDirection[game[row][col]] == 'v':
                    printGame(game[row][col])
                    print(row)
                    print(col)
                    currentGame = game
                    check = moveDown(currentGame, game[row][col])
                    print(row)
                    print(col)
                    printGame(game[row][col])
                    print(game[row][col])
                    #keep moving car down until it hits the edge
                    while check is not None:
                        currentGame = moveDown(currentGame, game[row][col])
                        check = moveDown(currentGame, game[row][col])
                        #If the node has not been seen
                        if currentGame not in seenNodes:
                            seenNodes.append(currentGame)
                            print()
                    
                    currentGame = game
                    check = moveUp(currentGame, game[row][col])

                    #keep moving car up until it hits the edge
                    while check is not None:
                        currentGame = moveUp(currentGame, game[row][col])
                        check = moveUp(currentGame, game[row][col])
                        #If the node has not been seen
                        if currentGame not in seenNodes:
                            seenNodes.append(currentGame)
                            print(currentGame)
                            print()
    return seenNodes


print()
printGame(convert(game))
print()
printGame(findChildren(convert(game)))
                    


    #Iterate 

                        
                

                    



# # Create a hash map that stores visited nodes
# visited = {}

# #Create class node with attributes game, list child, and depth

# class Node:
#     def __init__(self, game, child, depth):
#         self.game = game
#         self.child = child
#         self.depth = depth


# #Create a Node root
# root = Node(convert(game), , 0)







# visited[0] = game

# x = convert(game)

# print(x)

        
        