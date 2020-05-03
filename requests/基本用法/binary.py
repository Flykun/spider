import requests

# https://github.com/fluidicon.png
r = requests.get("https://github.com/fluidicon.png")
print(r.content)

with open('favicon.png', 'wb') as f:
    f.write(r.content)