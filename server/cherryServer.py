import cherrypy
from ghost import Ghost
import subprocess
import os, os.path
os.putenv('DISPLAY', ':0.0')

ghost = Ghost()
newUrl = 'https://neopets.com'

class GrabImages(object):
	sitesVisited = []
	@cherrypy.expose
	def index(self):
		return "I am online"

	@cherrypy.expose
	def retrieve(self, inputURL="cnn.com"):
		f = open('scaffold.js')
		content = f.read() 
		content = content.replace('sample', inputURL, 1)
		f.close()
		f = open('prompt.js', 'w')
		f.write(content)
		f.close()

		subprocess.call(['./phantomjs.exe','prompt.js'])
		return "success?"

	@cherrypy.expose
	def serve(self):
		return """ <html>
<head>
<title>CherryPy static image</title>
</head>
<html>
<body>
<img src="/image.png">
</body>
</html>"""

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080, })

conf = {'/': {'tools.staticdir.on': True,
        'tools.staticdir.dir': '/home/aqwin/server'}}
print conf
cherrypy.quickstart(GrabImages(), '/', config=conf)
