def searchStudio():
    query = '''
    query ($search: String) {
    Studio(search: $search) {
        name
        siteUrl
        media (isMain: true, sort: POPULARITY_DESC, perPage: 10) {
            nodes {
                siteUrl
                title {
                    english
                    romaji
                }
            }
        }
    }
}
    '''
    return query