import os
import json
import urllib2
#import pynotify
from gi.repository import Nautilus, GObject


class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    def execute(self,menu,files):
        print files[0].get_name()
        cmd = "notify-send '"+ files.name +"'"
        os.system(cmd)
	pass
    def get_file_items(self, window, files):
        top_menuitem = Nautilus.MenuItem(name='MovieRating', 
                                         label='Movie Actions', 
                                         tip='',
                                         icon='')
        
 	top_menuitem.connect('activate',self.execute,files)       
        return top_menuitem,
