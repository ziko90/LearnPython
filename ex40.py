#Exercise 40.1.4 A First Class Example:

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]) #rospisane w formie listy
                                # list of strings !! as the lyrics
bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

print('-'*10)
print(happy_bday.lyrics)
print(len(happy_bday.lyrics))
print('-'*10)
print(happy_bday.lyrics[2])
print('-'*10)

bulls_on_parade.sing_me_a_song()
print('-'*20)
song = ['Hahaha', 'lalla', 'nanana', 'banana']

my_song = Song(song)
my_song.sing_me_a_song()

print('-'*20)
print(my_song.lyrics)
print(my_song.lyrics[-1])