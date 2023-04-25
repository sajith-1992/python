#words = dict()
words = set()
def check(word): #for writting a function
    if word.lower() in words: 
            return True
    else:
        return False
    
    

def load(dictionary):
    file = open(dictionary,"r")
    for line in file:
        words.add(line)
     close (file)
    return True
def size():
        return len(words) #the length of word 
 def unload():       
     return True # no need to return 