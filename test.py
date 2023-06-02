def isPlaylist(URL):
    if URL.find('playlist') > 0:
        return True
    return False

print(isPlaylist("https://www.youtube.com/watch?v=ci9QyYE3m6o"))