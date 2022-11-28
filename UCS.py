game = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."

# Create a converter function
def convert(game):
    #Split game into 6 character arrays
    game = [game[i:i+6] for i in range(0, len(game), 6)]

    #For each item in array, split into characters array
    for i in range(len(game)):
        game[i] = list(game[i])

    return game

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

            

# # Create a function that finds children of a game 
# def findChildren(game):
#     #list of seen cars
#     seen = []

#     #Iterate through each row of the game
#     for row in range(6):
#         for col in range(6):
#             item = game[row][col]
#             if item == '.' or (item in seen):
#                 continue
#             else:
#                 #check car direction
#                 if carDirection[item] == 'h':
#                     #check if car can move left or right
#                     # if car can move left, create a new game
#                     while col-1 >= 0 and game[row][col-1] == '.':

                        
                

                    



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

        
        