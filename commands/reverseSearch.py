import tracemoepy


def reverseSearch(link):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    try:
        title = tracemoe.search(link, is_url=True)
        return title['result'][0]['anilist']['id']
    except:
        return False
