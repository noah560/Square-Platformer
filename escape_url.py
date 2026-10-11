# Turn the minified file into a URL

with open("minified.html", "rt") as f:
    txt = f.read()

with open("url.txt", "wt") as f:
    f.write("data:text/html," + txt.replace("#", "%23").replace("\n", ""))
