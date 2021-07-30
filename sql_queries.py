# DROP TABLESuser

songplay_table_drop = "drop table if exists songplay_table"
user_table_drop = "drop table if exists user_table"
song_table_drop = "drop table if exists song_table"
artist_table_drop = "drop table if exists artist_table"
time_table_drop = "drop table if exists time_table"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplay_table 
(songplay_id serial primary key not null, 
start_time timestamp, 
user_id int, 
level text, 
song_id text, 
artist_id text, 
session_id text, 
location text, 
user_agent text);""")

user_table_create = ("""
create table if not exists users_table 
(user_id int primary key not null, 
first_name varchar, 
last_name varchar, 
gender varchar, 
level text);""")

song_table_create = ("""
create table if not exists songs_table 
(song_id text primary key not null, 
title text, 
artist_id text, 
year int, 
duration float);""")

artist_table_create = ("""
create table if not exists artists_table 
(artist_id varchar primary key not null, 
name varchar, 
location varchar, 
latitude float, 
longitude float);""")

time_table_create = ("""create table if not exists time_table 
(start_time timestamp primary key not null, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplay_table 
(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
values(%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (songplay_id) DO NOTHING""")

user_table_insert = ("""insert into users_table 
(user_id, first_name, last_name, gender, level) values(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level""")

song_table_insert = ("""insert into songs_table 
(song_id, title, artist_id, year, duration) 
values(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""insert into artists_table 
(artist_id, name, location, latitude, longitude) 
values(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""insert into time_table 
(start_time, hour, day, week, month, year, weekday) 
values(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""select s.song_id, s.artist_id, a.name from songs_table as s 
join artists_table as a on (a.artist_id = s.artist_id) 
where s.title=%s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]