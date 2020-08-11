def SearchUser():
    query = '''
    query ($search: String) {
    User(name: $search) {
        id
        name
        siteUrl
        avatar {
            large
        }
        favourites {                                #print out favourites
            anime (perPage: 10) {
                nodes {
                siteUrl
                    title {
                        romaji
                        english
                    }
                }
            }
            manga (perPage: 10) {
                nodes {
                siteUrl
                    title {
                        romaji
                        english
                    }
                }
            }
        }
        about (asHtml: true),
        statistics {
            anime {
                minutesWatched
                meanScore
                count
                    }
            manga {
                chaptersRead
                meanScore
                count
            }
        }
    }
    }
    '''
    return query