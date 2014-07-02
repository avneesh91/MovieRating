import os
import json
import urllib2
#import pynotify
from gi.repository import Nautilus, GObject


class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    def execute(self,menu,files):
        if len(files) == 1:
          print files[0].get_name()
          cmd = "notify-send '"+ files[0].get_name() +"'"
          os.system(cmd)
	else:
          pass
    def get_file_items(self, window, files):
        top_menuitem = Nautilus.MenuItem(name='MovieRating', 
                                         label='Movie Actions', 
                                         tip='',
                                         icon='')
        
 	top_menuitem.connect('activate',self.execute,files)       
        return top_menuitem,





class rottenTom:
    """A very basic wrapper for the rottentomatoes api"""

    cache_count = 20
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?' + \
          'apikey=ufykyv9d94bcxfrjaw6xacqr&q={}&page_limit={}'

    def __init__(self):

        self.movie_cache = {} # caches data returned by api
        self.movies_in_cache = {} # caches movie names and number of calls since last used

  

    def getMovie(self,movie_name,page_limit = 1):

    	movie_name = movie_name.lower().strip()
    	movie_format = movie_name.replace(u" ", u"+")
    	"""
    	Get a list of movies in theaters. 
    	"""
    	# in the url we need to use '+' instead of spaces
    	movie_format = movie_name.replace(u" ", u"+")
    	query = self.url.format(movie_format, page_limit)
    	result_data = urllib2.urlopen(query)
    	results = json.loads(result_data.read())
       
    	return json.dumps(results)
