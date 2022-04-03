create table if not exists artist (
	id serial primary key,
	name varchar (40) unique not null
);

create table if not exists albums (
	id serial primary key,
	album_title varchar (40)  not null,
	edition_year integer not null,
	id_artist integer references artist (id)
);

create table if not exists tracks (
	id serial primary key,
	track_name varchar (40)  not null,
	track_duration serial  not null,
	id_album  integer references albums (id)
);