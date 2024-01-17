
#Creating a simple program that will take user input to parse through a log file
#The log file will be converted into a dict which will then be used to search for
#the search term. The program will also identify the most commonly used word and
#how many times it was used.

def ser(par,passeddict):
    for num in passeddict:
        if passeddict[par] > 0:
            return passeddict[par]


def lar(passeddict):
    largestword = None
    timesrepeated = None
    for word,value in passeddict.items():
        #word and value for a key and value pair for dict to go through
        #they itterate at the same time
        if timesrepeated is None or value > timesrepeated:
            largestword = word
            timesrepeated = value
    print(largestword,timesrepeated)

### MAIN BODY ###

filename = input('Enter file name:')
fhand = open(filename, 'r')
counts = dict()
for lines in fhand:
    #Stripping any \n to the right hand side of the parsed lines
    stripspace = lines.rstrip()
    #Splitting the line into its component words
    splitstep = lines.split()
    #Creating a loop that goes into the extracted lines
    for words in splitstep:
        counts[words] = counts.get(words, 0) + 1
        #the get method checks if a key is already in the dict
        #if it is not then it creates an entry with the defauly value of 0
print('What would you like to do?')
print('1. Find the word that has been used the most.')
print('2. Search for a particular word and how many times it has been used.')
userchoice = input('')
#print(userchoice)
if userchoice == '1':
    lar(counts)
    #print('Test')
elif userchoice == '2':
    print('Please enter search term:')
    searchterm = input('')
    #print('Test')
    numcount = ser(searchterm, counts)
    print('The term', searchterm, 'has been used', numcount, 'times.')
else:
    quit()
    
    



