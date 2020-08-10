def GetUser(userName):
    variables = {
        'search' : userName
    }
    return variables

def GetByTitle(type, title):
    type = type.upper()
    if type != 'ANIME' and type != 'MANGA':
        return False
    variables = {
        'type' : type,
        'search' : title
    }
    return variables

def GetByID(type, id):
    type = type.upper()
    if type != 'ANIME' and type != 'MANGA':
        return False
    variables = {
        'type' : type,
        'id': id
    }
    return variables

def GetByStudio(studioName):
    variables = {
        'search' : studioName
    }
    return variables