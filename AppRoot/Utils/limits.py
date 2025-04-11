#Here we create general limits, the idea is to prevent some possible Attacks, which can easyli been protected against, by simple limits

GENERALSTRING_LEN = 100
USERNAME_LEN = 32
PASSWORD_LEN = 64

def checkLen(string,_type=GENERALSTRING_LEN):
    if(len(string) > _type):
        return False
    else:
        return True

def __init__():
    pass
def load():
    pass
def addLimit():
    pass

