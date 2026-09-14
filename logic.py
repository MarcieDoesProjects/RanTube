def get_random_music():
    music_genres = [
    "Pop", "Rock", "Hip Hop", 
    "R&B", "Jazz", "Classical", 
    "Electronic", "House", "Techno", 
    "Dubstep", "Reggae", "Blues", 
    "Country", "Metal", "Folk", 
    "Indie", "K-Pop", "Latin", 
    "Afrobeats", "Drill"
]
    music_years = [
    "1980", "1985", "1990", "1995",
    "2000", "2003", "2005", "2008",
    "2010", "2011", "2012", "2014",
    "2015", "2016", "2017", "2018",
    "2019", "2020", "2021", "2022"
    ]
    music_artists = {
    "Pop": ["Taylor Swift", "Ariana Grande", "Ed Sheeran", "Dua Lipa", "Billie Eilish", "Olivia Rodrigo", "Harry Styles", "Justin Bieber"],
    "Rock": ["Imagine Dragons", "Linkin Park", "Arctic Monkeys", "Foo Fighters", "Nirvana", "Green Day", "Red Hot Chili Peppers"],
    "Hip Hop": ["Drake", "Kendrick Lamar", "J. Cole", "Travis Scott", "Nicki Minaj", "Lil Baby", "Future"],
    "R&B": ["SZA", "The Weeknd", "Frank Ocean", "H.E.R.", "Usher", "Brent Faiyaz"],
    "Jazz": ["Miles Davis", "John Coltrane", "Louis Armstrong", "Herbie Hancock"],
    "Classical": ["Mozart", "Beethoven", "Bach", "Chopin"],
    "Electronic": ["Daft Punk", "Calvin Harris", "Avicii", "Deadmau5", "Marshmello"],
    "House": ["Martin Garrix", "Fisher", "Swedish House Mafia", "Disclosure"],
    "Techno": ["Charlotte de Witte", "Amelie Lens", "Carl Cox"],
    "Dubstep": ["Skrillex", "Excision", "Zeds Dead"],
    "Reggae": ["Bob Marley", "Sean Paul", "Shaggy"],
    "Blues": ["B.B. King", "Muddy Waters", "Eric Clapton"],
    "Country": ["Luke Combs", "Morgan Wallen", "Taylor Swift", "Johnny Cash"],
    "Metal": ["Metallica", "Slipknot", "Iron Maiden", "Bring Me The Horizon"],
    "Folk": ["Bob Dylan", "Mumford & Sons", "The Lumineers"],
    "Indie": ["Tame Impala", "Lana Del Rey", "The 1975", "Phoebe Bridgers"],
    "K-Pop": ["BTS", "BLACKPINK", "Stray Kids", "TWICE", "EXO"],
    "Latin": ["Bad Bunny", "J Balvin", "Karol G", "Shakira"],
    "Afrobeats": ["Burna Boy", "Wizkid", "Tems", "Davido"],
    "Drill": ["Pop Smoke", "Central Cee", "Headie One", "Fivio Foreign"]
}
    easter_egg =[
        "issbrokie"
    ]
    return music_genres, music_years, music_artists, easter_egg
def get_random_video():
    video_genres=[
    "Gaming", "Cars", "Motorcycles", 
    "Crime", "True Crime", "Mystery", 
    "Documentary", "Science", "Technology", 
    "Programming", "Coding", "AI", 
    "Cybersecurity", "Hacking", "Education", 
    "Math", "History", "Geography", 
    "News", "Politics", "Finance", 
    "Investing", "Business", "Entrepreneurship", 
    "Self Improvement", "Fitness", "Gym", 
    "Bodybuilding", "Health", "Medical", 
    "Psychology", "Philosophy", "Cooking", 
    "Food", "Travel", "Vlogs", 
    "Lifestyle", "Fashion", "Beauty", 
    "Makeup", "Skincare", "DIY", 
    "Crafts", "Home Improvement", "Construction", 
    "Engineering", "Space", "Astronomy", 
    "Nature", "Animals", "Wildlife", 
    "Sports", "Football", "Basketball", 
    "Motorsport", "F1", "Esports", 
    "Reviews", "Unboxing", "Product Reviews",
    "Tech Reviews", "Reaction Videos", "Memes", 
    "Comedy", "Stand-up", "Animation", 
    "Storytime", "Explained", "Investigations",
    "LGBTQ+", "LGBT", "Queer", 
    "Gay", "Lesbian", "Bisexual", 
    "Transgender", "Non-binary", "Genderqueer", 
    "Pansexual", "Asexual", "Intersex", "Genderfluid", 
    "anime", "amv", "history", 
]
    video_years=[

    "2006", "2007", "2008",
    "2009", "2010", "2011", 
    "2012", "2013", "2014", 
    "2015", "2016", "2017", 
    "2018", "2019", "2020", 
    "2021", "2022", "2023", 
    "2024", "2025", "2026"
]
    Video_youtubers = {
    "Gaming": ["Markiplier", "Jacksepticeye", "PewDiePie", "DanTDM", "VanossGaming", "Dream", "LDShadowLady", "CoryxKenshin", "SSSniperWolf", "Kubz Scouts"],
    "Cars": ["Donut Media", "Doug DeMuro", "Carwow", "Shmee150", "TheStradman", "DailyDrivenExotics", "Vehicle Virgins", "Supercar Blondie"],
    "Technology": ["Marques Brownlee", "Linus Tech Tips", "Mrwhosetheboss", "Unbox Therapy", "Austin Evans", "Dave2D", "ShortCircuit"],
    "Programming": ["Fireship", "Tech With Tim", "The Net Ninja", "Programming with Mosh", "freeCodeCamp", "Traversy Media", "Corey Schafer", "CodeWithHarry"],
    "Coding": ["Fireship", "Tech With Tim", "The Net Ninja", "Programming with Mosh", "freeCodeCamp", "Traversy Media", "Corey Schafer", "CodeWithHarry"],
    "AI": ["Two Minute Papers", "Yannic Kilcher", "Sentdex", "CodeEmporium", "DeepLearningAI"],
    "Cybersecurity": ["NetworkChuck", "David Bombal", "The Cyber Mentor", "John Hammond", "LiveOverflow", "Hak5"],
    "Hacking": ["LiveOverflow", "John Hammond", "NetworkChuck", "The Cyber Mentor", "Hak5"],
    "Education": ["CrashCourse", "Khan Academy", "Veritasium", "Vsauce", "CGP Grey", "Kurzgesagt", "SciShow"],
    "Math": ["3Blue1Brown", "Numberphile", "Mathologer", "Blackpenredpen"],
    "History": ["Oversimplified", "Simple History", "History Matters", "Kings and Generals", "Extra Credits"],
    "Fitness": ["Jeff Nippard", "Athlean-X", "Chris Heria", "Chloe Ting", "Pamela Reif", "LeanBeefPatty"],
    "Gym": ["Jeff Nippard", "Athlean-X", "Chris Heria", "LeanBeefPatty"],
    "Bodybuilding": ["CBum", "Nick's Strength and Power", "More Plates More Dates"],
    "Cooking": ["Gordon Ramsay", "Binging with Babish", "Joshua Weissman", "Nick DiGiovanni"],
    "Travel": ["Drew Binsky", "Mark Wiens", "Kara and Nate"],
    "Vlogs": ["Casey Neistat", "Emma Chamberlain", "MrBeast", "David Dobrik"],
    "Fashion": ["BestDressed", "Wisdom Kaye"],
    "Beauty": ["James Charles", "NikkieTutorials", "Jeffree Star"],
    "DIY": ["5-Minute Crafts", "Mr. Kate"],
    "Engineering": ["Mark Rober", "Stuff Made Here", "Real Engineering"],
    "Space": ["Scott Manley", "Everyday Astronaut", "NASA"],
    "Animals": ["Brave Wilderness", "The Dodo"],
    "Sports": ["Dude Perfect", "Sidemen"],
    "Basketball": ["Chris Smoove", "FlightReacts", "Jesser"],
    "Football": ["F2Freestylers", "Mark Goldbridge"],
    "F1": ["Chain Bear", "Driver61"],
    "Esports": ["TSM", "FaZe Clan"],
    "Reviews": ["Unbox Therapy", "Marques Brownlee", "Linus Tech Tips"],
    "Comedy": ["Ryan Trahan", "Danny Gonzalez", "Drew Gooden", "Kurtis Conner"],
    "Animation": ["Jaiden Animations", "TheOdd1sOut", "Domics"],
    "Storytime": ["Jaiden Animations", "TheOdd1sOut", "Storybooth"],
    "Explained": ["Vox", "Wendover Productions", "Half as Interesting"],
    "Investigations": ["Coffeezilla", "Internet Anarchist", "SunnyV2"],
    "True Crime": ["MrBallen", "That Chapter", "Kendall Rae", "Bailey Sarian"],
    "Mystery": ["Nexpo", "Barely Sociable", "ReignBot"],
    "LGBTQ+": ["ContraPoints", "Philosophy Tube", "Jammidodger", "Samantha Lux", "OneTopic", "JammiDodger"],
    "Transgender": ["Jammidodger", "Samantha Lux", "NoahFinnce"],
    "Gay": ["Ty Turner", "MarkE Miller"],
    "Lesbian": ["Alayna Joy", "Rose and Rosie"],
    "Bisexual": ["Shane Dawson"],
    "Non-binary": ["Ash Hardell"],
    "Anime": ["Gigguk", "The Anime Man", "CDawgVA"],
    "AMV": ["Anime MV Sensei"],
    "Memes": ["Dhar Mann", "Memeulous", "Dolan Dark"]
    }
    return video_genres, video_years, Video_youtubers
def get_golden_age_video():
    golden_years = [
        "2008", "2009", "2010", "2011",
        "2012", "2013", "2014", "2015"
    ]

    golden_youtubers = [
        "PewDiePie", "Markiplier", "Jacksepticeye",
        "VanossGaming", "DanTDM", "SkyDoesMinecraft",
        "CaptainSparklez", "TheSyndicateProject",
        "Yogscast", "SeaNanners","penguinz0"
    ]

    golden_games = [
        "Minecraft", "Happy Wheels", "GTA V",
        "Call of Duty", "Skyrim", "Amnesia",
        "Five Nights at Freddy's", "Garry's Mod"
    ]

    return golden_years, golden_youtubers, golden_games