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
        favourites {                             
            anime (perPage: 5) {
                nodes {
                siteUrl
                    title {
                        romaji
                        english
                    }
                }
            }
            manga (perPage: 5) {
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