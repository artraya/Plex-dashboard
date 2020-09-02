from flask import Flask, render_template, url_for
from plexapi.server import PlexServer
import plexapi

app = Flask(__name__)


baseurl = 'http://192.168.0.100:32400'
token = 'w7Xdc147T4vukDTwMVkJ'
plex = PlexServer(baseurl, token)

recentlyAdded = plex.library.recentlyAdded()

for i in recentlyAdded:
    print(i.title)


@app.route("/")
def home():
    return render_template('home.html', recentlyAdded=recentlyAdded)

if __name__ == "__main__":
    app.run(debug=True)

