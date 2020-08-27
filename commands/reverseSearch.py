import tracemoepy


def reverseSearch(link):
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    try:
        title = (tracemoe.search(link, is_url=True))
    except:
        return False

    for key, value in title["docs"][0].items():
        if key == "anilist_id":
            return value