#!/usr/bin/python

import sys
import gtk
import pygtk
pygtk.require('2.0')
import mateapplet
from nm_dispatcher_olsrd_applet import applet_factory

if __name__ == '__main__':	 # testing for execution
	print('Starting factory')

	if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
		mainWindow = gtk.Window()
		mainWindow.set_title('Applet window')
		mainWindow.connect('destroy', gtk.main_quit)
		applet = mateapplet.Applet()
		applet_factory(applet, None)
		applet.reparent(mainWindow)
		mainWindow.show_all()
		gtk.main()
		sys.exit()
	else:
		mateapplet.matecomponent_factory('OAFIID:MATE_nm-dispatcher-olsrd-applet_Factory',
				mateapplet.Applet.__gtype__,
				'MATE_nm-dispatcher-olsrd-applet',
				'0.0',
				applet_factory)
