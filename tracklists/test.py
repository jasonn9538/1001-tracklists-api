from tracklists import *

tracklist = Tracklist("https://www.1001tracklists.com/tracklist/pp78sv9/seven-lions-visions-4-throwback-set-2020-08-25.html")

# Initial fetch
tracklist.fetch()

# Get a list of tracks
tracks = tracklist.get_tracks()

# Get spotify and apple id for the first track

# print(tracks[0].external_ids)


	# for i in range(0,len(tracks)-1):
	# 	if 'spotify' in tracks[i].external_ids and 'spotify' in tracks[i+1].external_ids:
	# 		# print(tracks[i].title, i, tracks[i].get_external('spotify'))
	# 		# print('*** mixed with ***')
	# 		# print(tracks[i+1].title, i+1, tracks[i+1].get_external('spotify'))
	# 		line = tracks[i].title, i, tracks[i].get_external('spotify'), 'next', tracks[i+1].title, i+1, tracks[i+1].get_external('spotify')
	# 		csv_writer.writerow(line)

