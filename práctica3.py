#!/usr/bin/python
# -*- coding: UTF-8 -*-

import web
from web.contrib.template import render_mako


web.config.debug = False
# Creación de template con mako
render = render_mako(
    directories = ['templates'],
    input_encoding = 'utf-8',
    output_encoding ='utf-8')

urls = ('/','graficos'
)
app = web.application(urls, globals())

#Clase de manejo de googleCharts

class graficos:
	def GET(self):
		return render.graficos()
	
def main():
	app.run()
	return 0

if __name__ == "__main__": main()
