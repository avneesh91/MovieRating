from gi.repository import Nautilus, GObject
import imdb
import MessageMaker
import notify
import os

class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    def imdb_info(self,menu,files):
  	 movie_name = Filename(files)  
	 movie_dict = imdb.get_rating(movie_name)
	 	
    def get_file_items(self, window, files):
        top_menuitem = Nautilus.MenuItem(name='MovieRating', 
                                         label='Get IMDB Rating', 
                                         tip='',
                                         icon='')
     	top_menuitem.connect('activate',self.imdb_info,files)       
        return top_menuitem,
	
def Extracter(movie_info_raw):
	data_list = []
	title = str(movie_info_raw["movies"][0]["title"])
	synopsis = str(movie_info_raw["movies"][0]["synopsis"])
	re.sub('[^A-Za-z0-9]+', ' ', synopsis)
 	re.sub('[^A-Za-z0-9]+', '', title)
	data_list.append(title)
	data_list.append(synopsis)
	return data_list
	
def Filename(files):
	if len(files) == 1:
          if '.' in files[0].get_name():
                return files[0].get_name().split('.')[0]
          else:
                return files[0].get_name()
