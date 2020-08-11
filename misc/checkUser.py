from commands.searchUser import SearchUser
from variables.userVar import GetUser
from queries.runQuery import run_query

def checkUser(userName):
    query = SearchUser()
    variables = GetUser(userName)
    if variables:
        result = run_query(query, variables)
        if not result:
            return False
        return True