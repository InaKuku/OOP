from project.album import Album
from project.song import Song
from project.band import Band

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.add_song(second_song))
third_song = Song("Lakaka", 3.45, True)
print(album.add_song(third_song))
print(album.remove_song(third_song))
not_in_the_album_song = Song("Akjhkhkhkj", 2.34, False)
print(album.remove_song(not_in_the_album_song))
print(album.details())
print(album.publish())
print(album.publish())
forth_song = Song("Laa", 3.45, False)
print(album.add_song(forth_song))
band = Band("Manuel")
print(band.add_album(album))
print(band.add_album(album))
print(band.remove_album("Initial D"))
second_album = Album("Test", forth_song, not_in_the_album_song, third_song)
print(band.remove_album("Test"))
print(band.add_album(second_album))
print(band.remove_album("Test"))

print(band.details())