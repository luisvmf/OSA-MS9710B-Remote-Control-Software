import time
import os
from multiprocessing import Process
def func1():
	import gtk
	settings = gtk.settings_get_default()
	print settings.get_property("gtk-color-scheme")
	print "---fim---"
while 2==2:
	p1=Process(target=func1)
	p1.start()
	time.sleep(1)
	os.system('clear')
