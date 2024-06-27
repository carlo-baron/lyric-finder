import tkinter as tk
from tkinter import scrolledtext
from lyricsgenius import Genius

class LyricFinder(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.GENIUS_TOKEN = Genius('TOKEN')

        self.title("Lyric Finder")
        
        self.entry_frame = tk.Frame(self)
        self.button_frame = tk.Frame(self)
        
        self.entry_frame.pack(pady=20)
        self.button_frame.pack()

        self.song = tk.StringVar()
        self.artist = tk.StringVar()
        
        self.song_name_label = tk.Label(self.entry_frame, text="Song:")
        self.artist_name_label = tk.Label(self.entry_frame, text="Artist:")
        self.song_name_entry = tk.Entry(self.entry_frame, textvariable=self.song, width=30)
        self.artist_name_entry = tk.Entry(self.entry_frame, textvariable=self.artist, width=30)
        
        self.song_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.artist_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.song_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.artist_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.lyrics_label = scrolledtext.ScrolledText(self.button_frame, wrap=tk.WORD, width=50, height=10)
        self.lyrics_label.pack(pady=10)
        
        self.debug_button = tk.Button(self.button_frame, text="DEBUG", command=self.debug)
        self.debug_button.pack(pady=10)

    def debug(self):
        self.lyrics_label.delete(1.0, tk.END)
        
        self.lyrics = self.GENIUS_TOKEN.search_song(self.song.get(), self.artist.get())
        self.lyrics_label.insert(tk.END , self.lyrics.lyrics)

app = LyricFinder()
app.mainloop()
