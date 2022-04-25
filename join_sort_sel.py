import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://py48user:12345@localhost:5432/py48db')
connection = engine.connect()

# 1 количество исполнителей в каждом жанре;
cnt_artists_gen = connection.execute("""SELECT name_genre, count(id_artists) from artists_genres ag
JOIN genres g ON ag.id_genres = g.id
GROUP BY name_genre;
""").fetchall()

# print(cnt_artists_gen)

# 2 количество треков, вошедших в альбомы 2019-2020 годов;
tracks_sum = connection.execute("""SELECT album_title, count(track_name) from  tracks t
JOIN albums a ON t.id_album = a.id
WHERE edition_year BETWEEN 2000 AND 2020
GROUP BY album_title;
""").fetchall()

# print(tracks_sum)

# 3 средняя продолжительность треков по каждому альбому;
avg_time_dur_tr = connection.execute("""SELECT album_title, AVG(track_duration) avg_t from  tracks t
JOIN albums a ON t.id_album = a.id
GROUP BY album_title
ORDER BY avg_t;
""").fetchall()

# print(avg_time_dur_tr)

# 4 все исполнители, которые не выпустили альбомы в 2020 году;
max_track_duration = connection.execute("""SELECT name from artist a
JOIN artists_albums aa ON a.id = aa.id_artist
JOIN albums alb ON aa.id_album = alb.id
WHERE name NOT IN (SELECT name from artist WHERE edition_year = 2020);
""").fetchall()

# print(max_track_duration)

# 5 названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
coll_art = connection.execute("""SELECT collection_name from collection clc
JOIN collections_track cltr ON clc.id = cltr.id_collection
JOIN tracks tr ON cltr.id_track = tr.id
JOIN albums alb ON tr.id_album = alb.id
JOIN artists_albums artalb ON alb.id = artalb.id_album
JOIN artist ast ON artalb.id_artist = ast.id
WHERE name = 'Cypress Hill'
GROUP BY collection_name;
""").fetchall()

# print(coll_art)

# 6 название альбомов, в которых присутствуют исполнители более 1 жанра;
gen_art_cnt = connection.execute("""SELECT album_title, count(id_genres) from albums alb
JOIN artists_albums artalb ON alb.id = artalb.id_album
JOIN artist ast ON artalb.id_artist = ast.id
JOIN artists_genres artge ON ast.id = artge.id_artists
GROUP BY album_title
HAVING COUNT(id_genres) > 1;
""").fetchall()

# print(gen_art_cnt)

# 7 наименование треков, которые не входят в сборники;
tr_d_col = connection.execute("""SELECT track_name from tracks t
WHERE track_name NOT IN (SELECT track_name from tracks JOIN collections_track ct ON t.id = ct.id_track);
""").fetchall()

# print(tr_d_col)

# 8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
min_dur_tr_ar = connection.execute("""SELECT name from artist ar
JOIN artists_albums artalb ON ar.id = artalb.id_artist
JOIN albums a ON artalb.id_album = a.id
JOIN tracks t ON a.id = t.id_album
WHERE track_duration = (SELECT MIN(track_duration) from tracks);
""").fetchall()

# print(min_dur_tr_ar)

# 9 название альбомов, содержащих наименьшее количество треков.
min_tr_alb = connection.execute("""SELECT album_title FROM albums a
JOIN tracks t ON a.id = t.id_album
GROUP BY album_title
HAVING COUNT(t.id) = (
    SELECT count(id) FROM tracks
    GROUP BY id_album
    ORDER BY count
    LIMIT 1);
""").fetchall()

# print(min_tr_alb)
