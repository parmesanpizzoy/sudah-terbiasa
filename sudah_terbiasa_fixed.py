import time

def show_lyrics():
    lyrics = [
        "sudah terbiasa terjadi tante",
        "teman datang ketika lagi butuh saja",
        "coba kalo lagi susaah..",
        "mereka semua menghilAAAANGGGG"
    ]
    
    for sentence in lyrics:
        for letter in sentence:
            print(letter, end='', flush=True)
            time.sleep(0.1)
        print()
        time.sleep(0.5)
    
if __name__ == "__main__":
    print("Lyrics :")
    show_lyrics()
