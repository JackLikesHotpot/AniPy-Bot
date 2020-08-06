import requests
from Queries import *

def run_query(query, variables): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://graphql.anilist.co', json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 404:
        print ("Invalid search.")
        return
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def SearchByID():
    query = '''
    query($id: Int, $type: MediaType) {
        Media(id: $id, type: $type) {
        title
        {
            romaji
            english
        }
        siteUrl
        type
        format
        genres
        status
        episodes
        duration
        status
        description(asHtml: true)
        coverImage {
            large
        }
        season
        seasonYear
        startDate {
            day
            month
            year
        }
        averageScore
        favourites
        studios
        {
            edges
            {
                node
                {
                    name
                }
            }
        }
        chapters
        volumes
        hashtag
        }
        }
    '''
    return query

def SearchByTitle():
    query = '''
    query($search: String, $type: MediaType) {
        Media(search: $search, type: $type) {
        title
        {
            romaji
            english
        }
        siteUrl
        type
        format
        genres
        status
        episodes
        duration
        status
        description(asHtml: true)
        coverImage {
            large
        }
        season
        seasonYear
        startDate {
            day
            month
            year
        }
        averageScore
        favourites
        studios
        {
            edges
            {
                node
                {
                    name
                }
            }
        }
        chapters
        volumes
        hashtag
        }
        }
    '''
    return query

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
            anime {
                nodes {
                siteUrl
                    title {
                        romaji
                        english
                    }
                }
            }
            manga {
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
