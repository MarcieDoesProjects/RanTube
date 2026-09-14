import random
import webbrowser
import colorama
from logic import (
    get_random_music,
    get_random_video,
    get_golden_age_video
)
from Player import open_video
from Data import (
    random_messages_lists
)
list_music_messages, list_video_messages, list_suprise_messages, list_broken_messages, list_bye_messages  = random_messages_lists()


def sublements():
    Music_sub = (random.choice(list_music_messages))
    Video_sub = (random.choice(list_video_messages))
    Suprise_sub = (random.choice(list_suprise_messages))
    Bye_sub = (random.choice(list_bye_messages))
    Broken_sub =(random.choice(list_broken_messages))
    return Bye_sub, Suprise_sub, Video_sub, Music_sub, Broken_sub

Music_sub, Video_sub, Suprise_sub,  Bye_sub, Broken_sub = sublements()

def show_menu():
    print("=== PLACE ===")
    print("your one stop all random stop")
    print(F"1. {Bye_sub}")
    print(F"2. {Suprise_sub}")
    print(F"3. {Video_sub}")
    print(F"4. {Broken_sub}")
    print("there are easter eggs if you are smart enough to find em >:3c")


def run_app():
    print("""hello random person hehe
RANTUBE - your random youtube chaos machine
""")

    while True:
        show_menu()
        choice = input("> ").strip().lower()

        if choice == "1":
            print(random.choice(list_music_messages))

            genres, years, artists, easter_egg = get_random_music()
            genre = random.choice(genres)
            artist = random.choice(artists[genre])
            year = random.choice(years)

            search_query = f"{artist} {genre} official music video {year}"
            open_video(search_query)
            print(f"jamming to {genre} NOW!! 🎵")

        elif choice == "2":
            print(random.choice(list_video_messages))

            genres, years, youtubers = get_random_video()
            genre = random.choice(genres)
            youtuber = random.choice(youtubers.get(genre, ["random video"]))
            year = random.choice(years)

            search_query = f"{youtuber} {genre} {year}"
            open_video(search_query)

        elif choice == "3":
            mode = random.choice(["music", "video"])

            if mode == "music":
                print(random.choice(list_music_messages))

                genres, years, artists, _ = get_random_music()
                genre = random.choice(genres)
                artist = random.choice(artists[genre])
                year = random.choice(years)

                search_query = f"{artist} {genre} official music video {year}"
                open_video(search_query)

            else:
                print(random.choice(list_video_messages))

                genres, years, youtubers = get_random_video()
                genre = random.choice(genres)
                youtuber = random.choice(youtubers.get(genre, ["random video"]))
                year = random.choice(years)

                search_query = f"{youtuber} {genre} {year}"
                open_video(search_query)

        # IF YOU SEE THIS SHEW SHEW GET OUTTA HERE >:3c
        elif choice == "issbrokie":
            _, _, _, easter_egg = get_random_music()
            search_query = random.choice(easter_egg)

            print("oh wow someones a W fan aswell >:3c")
            open_video(search_query)

        elif choice == "golden":
            print("woah you found the golden easter egg (get it get it) >:3c")

            years, youtubers, games = get_golden_age_video()

            year = random.choice(years)
            youtuber = random.choice(youtubers)
            game = random.choice(games)

            search_query = f"{youtuber} {game} {year}"
            open_video(search_query)

        # EXIT
        elif choice == "4":
            print("bye bye has a good day :3")
            exit(run_app)

if __name__ == "__main__":
    run_app()