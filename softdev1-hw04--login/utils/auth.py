import hashlib
import cPickle #used to serialize data
import os.path #used to check if file empty

path_userData = "data/userData.p"

logErrList = [
    "LogErrNo1: i think u 4got to enter a username, fam",
    "LogErrNo2: i think u 4got to enter a password, fam",
    "LogErrNo3: usrname doesn't exist XD u shud prob register an acc",
    "LogErrNo4: wrong password lmao if u dont rmbr it u shud just make a new acc cuz theres no password recovery system"
]

regErrList = [
    "RegErrNo1: i think u 4got to enter a username, fam",
    "RegErrNo2: i think u 4got to enter a password, fam",
    "RegErrNo3: usrname already exists XD u shud prob make another acc" 
]


'''
Registers user by hashing password 
and adding it to serialized data
> Input:
    username: String for arg username
    password: String for arg password
> Output:
    0 if registration is successful
    1 if username is empty
    2 if password is empty
    3 if username already exists
'''
def register( username, password ):    
    if not(username): #is username empty?
        return 1
    if not(password): #is password empty?
        return 2
        
    global path_userData
    with open(path_userData, 'a+') as f:
        print os.path.getsize(path_userData)
        userDict = cPickle.load(f) if os.path.getsize(path_userData) else {} #if file isn't empty, load it, else just use {}
        if username not in userDict:
            hashBrownmykolyk = hashlib.sha256()
            hashBrownmykolyk.update(password)
            userDict[username] = hashBrownmykolyk.hexdigest() 
            with open(path_userData,'w') as g:
                cPickle.dump(userDict, g)
            return 0
    return 3



'''
Verifies if arg credentials match any
preexisting credentials from serialized data
> Input:
    username: String for arg username
    password: String for arg password
> Output:
    0 if login is successful
    1 if username is empty
    2 if password is empty
    3 if username doesn't exist in dict
    4 if username exists but username/password mismatch
'''
def login( username, password ):
    if not(username): #is username empty?
        return 1
    if not(password): #is password empty?
        return 2
        
    global path_userData
    with open(path_userData, 'a+') as f:
        if os.path.getsize(path_userData): #obv not successful if file is empty
            userDict = cPickle.load(f)
            hashBrownmykolyk = hashlib.sha256()
            hashBrownmykolyk.update(password)
            if username in userDict:
                if userDict[username] == hashBrownmykolyk.hexdigest(): #if this passwd hash matches actual hash
                    return 0
                return 4
    return 3
    
