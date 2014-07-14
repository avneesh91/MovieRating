def CreateSummary(movie_info_dict):
	Movie_message = str(movie_info_dict['desc']) + '\n'
	Movie_message += "Genres: " + (','.join(str(element) for element in movie_info_dict['genre'] )) + '\n'
	Movie_message += "Duration : "+ str(movie_info_dict['duration_in_min']) + " minutes"
	return Movie_message
	
	
