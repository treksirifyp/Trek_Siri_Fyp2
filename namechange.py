import os

files = os.listdir("./static/img")
for file in files:
    os.rename("./static/img/" + file, "./static/img/" + file.lower())
