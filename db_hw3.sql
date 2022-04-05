create table if not exists Artist (
	id serial primary key,
	artist_name varchar (40) unique not null
);

create table if not exists Albums (
	id serial primary key,
	album_title varchar (40)  not null,
	edition_year integer not null
);

create table if not exists Tracks (
	id serial primary key,
	track_name varchar (40)  not null,
	track_duration serial  not null,
	id_album  integer references Albums (id)
);

create table if not exists Artists_albums (
	id_artist serial references Artist(id),
	id_album serial references Albums(id),
	constraint pk  primary key (id_artist, id_album)
);

create table if not exists Genres (
	id serial primary key,
	name_genre varchar (100)
);

create table if not exists Artists_genres (
	id_artists serial references Artist(id),
	id_genres serial references Genres(id),
	constraint pc primary key (id_artists, id_genres)
);

create table if not exists Collection (
	id serial primary key,
	collection_name varchar (100) not null,
	edition_year integer
);

create table if not exists Collections_track (
	id_collection serial references Collection(id),
	id_track serial references Tracks(id),
	constraint ps primary key (id_collection, id_track)
);