def searchStaff():
    query = '''
    query ($search: String) {
        Staff(search: $search) 
        {
            id
            siteUrl
            name
            {
                full
            }
        image
        {
            large
        }
        characters(sort: FAVOURITES_DESC, perPage: 10) {
        edges
        {
            role
            node
            {
                siteUrl
                name
                {
                    full
                }
            }
        }
    }
    }
    }
    '''
    return query