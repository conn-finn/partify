from time import sleep
from controller import handleSpotify

class Track:
    def __init__(self, current_track, stylesheet="partifyStylesheet.css", filename="partify"):
        self.current_track = current_track
        self.stylesheet = stylesheet
        self.filename = filename + ".html"  #f'{filename}-{self.current_track["name"]}.html'
        self._createHtmlPage()

    def _createHtmlPage(self):
        htmlBody = f'<div class="album-container"><img src="{self.current_track["coverUrl"]}"></div>'
        htmlBody += f'<div class="album-info"><h2 class="artist-name">{self.current_track["artist"]}</h2><div class="border"></div><h2 class="album-name">{self.current_track["album"]}</h2></div>'
        htmlBody += f'<div class="title-container"><h4 class="track-name">Current Track: {self.current_track["name"]}</h4></div>'
        htmlString = f'<html><head><link rel="stylesheet" href="{self.stylesheet}"></head><body><div id="content">' + htmlBody + f'</div></body></html>'

        # create new file, overwriting anything that exists
        with open(self.filename, 'r') as f:
            f.read()
        with open(self.filename, 'w') as f:
            f.write(htmlString)

    def handleNewTrack(self, new_track):
        self.current_track = new_track
        self._createHtmlPage()
        

cur = Track(handleSpotify())
while (True): # rip
    next_track = handleSpotify()
    while (next_track['name'] == cur.current_track['name']):
        sleep(5.0)
        next_track = handleSpotify()
    cur.handleNewTrack(next_track)
