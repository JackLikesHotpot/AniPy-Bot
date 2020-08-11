def removeTags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)