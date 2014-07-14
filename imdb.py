from lxml import html
import requests


def get_rating(movie_name):
	return imdb_connect(movie_name)

def imdb_connect(movie_name):
	base_url = "http://www.imdb.com"
	search_url = "/find?q="+ movie_name.replace(' ','+')
	page = requests.get(base_url+search_url)
	tree = html.fromstring(page.text)
	movies = tree.xpath("//div[@class='findSection']/table[@class='findList']/tr/td/a/@href")
	movie_url = movies[0]
	movie_info = requests.get(base_url+movie_url)
	movie_info = html.fromstring(movie_info.text)
	return data_extract(movie_info,movie_url)


def data_extract(movie_info,movie_url):
	
	Movie_id = get_substring(movie_url).strip('/')
	
	Movie_url = movie_url
	
	#Title of the Movie
	Title = movie_info.xpath("//table[@id='title-overview-widget-layout']/tbody/tr" \
                                 "/td[@id='overview-top']/h1[@class='header']/span[@class='itemprop']/text()")
	#Rating of the Movie
	Rating = movie_info.xpath("//table[@id='title-overview-widget-layout']/tbody/tr" \
                                  "/td[@id='overview-top']//div[@class='titlePageSprite star-box-giga-star']/text()")
	#Description
	description = movie_info.xpath("//table[@id='title-overview-widget-layout']/tbody/tr" \
					"/td[@id='overview-top']/p[@itemprop='description']/text()")
	#Runtime in Minutes
	Time = movie_info.xpath("//table[@id='title-overview-widget-layout']/tbody/tr/" \
				"td[@id='overview-top']/div[@class='infobar']/time/text()")
	#Genres, these are raw, need to processed more
	Genres = movie_info.xpath("//table[@id='title-overview-widget-layout']/tbody/" \
				  "tr/td[@id='overview-top']/div[@class='infobar']/a/@href")
	Genres_clean= []
	for r in Genres:
 		Genres_clean.append(get_substring(r))

	
	return dict_maker(movie_url,Movie_id,Title,description,Time,Genres,Rating)

def get_substring(raw_data):
	raw_element =raw_data.split('/')
	raw_string = str(raw_element[2])
	return raw_string[:raw_string.find("?")]

def dict_maker(url,Movie_id,Title,description,Time,Genres,Rating):
	
	Movie_data = {}
	#IMDB ID for the movie	
	imdb_id = Movie_id

	#Url - Only the Suffix
	Movie_url = url
	
	#IMDB Rating
	Movie_rating = Rating
	
	#clean genres
        Genres_clean= []
        for genr in Genres:
                Genres_clean.append(get_substring(genr))
	#clean Movie title
	Movie_title = str(Title[0])
	
	#clean movie Description
	Movie_description = str(description[0].strip())
	
	#Only Numeric Duration
	Duration_in_min = int(str(Time[0].strip().replace('min','')))

	Movie_data['imdb_id'] = imdb_id
	Movie_data['movie_url'] = Movie_url
	Movie_data['movie_rating'] = Movie_rating
	Movie_data['genre'] = Genres_clean
	Movie_data['title'] = Movie_title
	Movie_data['desc'] = Movie_description
	Movie_data['duration_in_min'] = Duration_in_min
	
	return Movie_data
