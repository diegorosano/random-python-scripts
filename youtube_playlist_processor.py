from pytube import YouTube, Playlist
import csv

playlist_link = "https://www.youtube.com/playlist?list=PLRe9ARNnYSY41I4NXMtfHQ2HN2wap_YtX"

playlist_item = Playlist(playlist_link)

print(f"There are { str(playlist_item.length) } items in the playlist")

video_links = playlist_item.video_urls

file_name = "Youtube_Playlist_videos.csv"
file_headers = ['Name', "Link"]
final_file = []

counter = 1

for link in video_links:
    print(f"Reading { str(counter) }/{ str(playlist_item.length) }")
    
    # This could take awhile as it reads one by one
    final_file.append([YouTube(link).title, link])

    counter = counter + 1

with open(file_name, 'w', encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(file_headers)
    csv_writer.writerows(final_file)