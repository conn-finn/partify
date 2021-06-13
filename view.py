from time import sleep
import os
import webview
from controller import handleSpotify

class TrackHandler:
    def __init__(self, current_track, stylesheet="partifyStylesheet.css", filename="partify"):
        self.current_track = current_track
        self.stylesheet = stylesheet
        self.filename = filename + ".html"
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


class Api():
    def addItem(self, title):
        print('Added item %s' % title)

    def removeItem(self, item):
        print('Removed item %s' % item)

    def editItem(self, item):
        print('Edited item %s' % item)

    def toggleItem(self, item):
        print('Toggled item %s' % item)

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()


def launchApp(filename):
    api = Api()
    window = webview.create_window('Partify', filename, js_api=api, min_size=(600, 450))
    webview.start(checkTrackAndUpdate, (window, filename))
    window.destroy()

def checkTrackAndUpdate(window, file):
    while (True): # rip
        next_track = handleSpotify()
        while (next_track['name'] == th.current_track['name']):
            sleep(5.0)
            next_track = handleSpotify() # can't request spotify API this frequently, maybe I could just scrape this information from a webplayer instead?
        th.handleNewTrack(next_track)
        window.load_url(file)


if __name__ == '__main__':
    th = TrackHandler(handleSpotify())
    launchApp(th.filename)

