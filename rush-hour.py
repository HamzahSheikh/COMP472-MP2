#Open file
f = open(r"C:\Users\Hamzah\Projects\COMP472-MP2\Sample\sample-input.txt", 'r')

#Read lines in file
lines = f.readlines()

#Close file
f.close()

#Cycle through each line
for line in lines:
    #Skip empty lines or lines starting with #
    if line == '' or line[0] == '#':
        continue
    
    print(line)

    fuelHashtable = {}
    carHashtable = {}
   
    counth1 = 0
    counth2 = 0
    
    #Print 6 charactes of each line at a time
    for i in range(0, len(line), 6):
        foundA = False
        if i < 36:
        #iterate through each character
            for j in line[i:i+6]:
                
                if j == 'A':
                    foundA = True

                if j != 'A' and foundA == True:
                    if j != '.':
                        counth2 += 1

                        #if character is not in carHashtable, add it
                        if j not in carHashtable:
                            carHashtable[j] = 0
                            counth1 += 1

                if j not in fuelHashtable and j != ' ' and j != '.' and j != '\n':
                    fuelHashtable[j] = 100
        #if line is over 36 characters, print full line
        else:
            #if line is not empty, iterate through each word
            if line[i:] != '':
                for word in line[i:].split():
                    #if word is not empty, print word
                    if word != '':
                        #add charater at position 0 to hash table
                        fuelHashtable[word[0]] = word[1]
            break            
        print(line[i:i+6], end='')
        print()
    #Print fuelHashtable alphabetically if not empty
    if fuelHashtable:
        print(sorted(fuelHashtable.items()))
        print("h1: ", counth1)
        print("h2: ", counth2)
        
        constantH3 = 5
        print("h3: ", counth1*constantH3)

#create an array to store visited nodes
visited = []


    

  
    








