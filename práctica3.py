#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.


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
