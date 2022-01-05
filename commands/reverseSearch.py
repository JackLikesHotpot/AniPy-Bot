import tracemoepy

def reverseSearch(link):

    tracemoe = tracemoepy.tracemoe.TraceMoe()
    try:
        title = (tracemoe.search(link, is_url=True))
        if (title['result'][0]['similarity']) > 0.9:
            return title['result'][0]['anilist']['id']
    except:
        return False
