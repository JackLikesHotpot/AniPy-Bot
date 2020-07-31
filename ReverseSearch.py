import tracemoepy

def reverseSearch(link):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    a = (tracemoe.search(link, is_url = True))
    for key, value in a["docs"][0].items():
        if key == "anilist_id":
            return value

#reverseSearch('https://i.imgur.com/pqI1BT3.jpeg')