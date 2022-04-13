import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://py48user:12345@localhost:5432/py48db')
connection = engine.connect()

# 1
album_years = connection.execute("""SELECT album_title, edition_year from albums
WHERE edition_year = 2018;
""").fetchall()

# print(album_years)

# 2
max_track_duration = connection.execute("""SELECT track_name, track_duration from tracks
WHERE track_duration = (select max(track_duration) from tracks);
""").fetchall()

# print(max_track_duration)

# 3
some_track_dur = connection.execute("""SELECT track_name from tracks
WHERE track_duration >= 33000;
""").fetchall()

# print(some_track_dur)

# 4
some_collections = connection.execute("""SELECT collection_name from collection
WHERE edition_year between 2018 and 2020;
""").fetchall()

# print(some_collections)

# 5
one_word_artist = connection.execute("""SELECT name from artist
WHERE name not like '%% %%';
""").fetchall()

# print(one_word_artist)

# 6
word_my = connection.execute("""SELECT track_name from tracks
WHERE track_name ilike '%%мой%%' or track_name ilike '%%my%%';
""").fetchall()

#print(word_my)
