import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://py48user:12345@localhost:5432/py48db')
connection = engine.connect()

connection.execute("""INSERT INTO artist VALUES
    (1,'Enter Shikari'),
    (2, 'AC/DC'),
    (3, 'Slipknot'),
    (4, 'Bring Me The Horizon'),
    (5, 'Parkway Drive'),
    (6, 'Linkin Park'),
    (7, 'Cypress Hill'),
    (8, 'Crystal Castles');
""")

connection.execute("""INSERT INTO albums VALUES
    (1, 'Common Dreads', 2009),
    (2, 'Back in Black', 1980),
    (3, 'Iowa', 2001),
    (4, 'Count Your Blessings', 2006),
    (5, 'Reverence', 2018),
    (6, 'Meteora', 2003),
    (7, 'Black Sunday', 1993),
    (8, 'Alice Practice', 2006);
""")

connection.execute("""INSERT INTO genres VALUES
    (1, 'Rock'),
    (2, 'Post-Hardcore'),
    (3, 'Electronic'),
    (4, 'Nu metal'),
    (5, 'Rap');
""")

connection.execute("""INSERT INTO tracks VALUES
    (1, 'Zzzonked', 32700, 1),
    (2, 'Havoc B', 25200, 1),
    (3, 'Back in Black', 41600, 2),
    (4, 'My plague', 40100, 3),
    (5, 'A lot like Vegas', 21000, 4),
    (6, 'Slow Dance', 11600, 4),
    (7, 'Prey', 41500, 5),
    (8, 'The Void', 35300, 5),
    (9, 'Hit The Floor', 24400, 6),
    (10, 'Numb', 30800, 6),
    (11, 'Insane in the Brain', 33000, 7),
    (12, 'Hand on the Glock', 33300, 7),
    (13, 'Alice Practice', 24400, 8),
    (14, 'Air War', 34400, 8),
    (15, 'Love and Carring', 21900, 8),
    (16, 'Juggernauts', 44400, 1);
""")

connection.execute("""INSERT INTO collection VALUES
    (1, 'Rock Hits', 2019),
    (2, 'Electro Top', 2020),
    (3, 'Best Sellers', 2013),
    (4, 'Worse', 2015),
    (5, 'On the Road', 2017),
    (6, 'Country Rock', 2005),
    (7, 'Legendary Rap', 2010),
    (8, 'Old Hits', 2007);
""")


connection.execute("""INSERT INTO artists_genres VALUES
    (1, 3),
    (2, 1),
    (3, 4),
    (4, 2),
    (5, 2),
    (6, 1),
    (7, 5),
    (8, 3),
    (1, 2);
""")

connection.execute("""INSERT INTO artists_albums VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8);
""")

connection.execute("""INSERT INTO collections_track VALUES
    (1, 3),
    (1, 9),
    (2, 13),
    (2, 14),
    (2, 15),
    (3, 11),
    (4, 8),
    (5, 1),
    (5, 2),
    (5, 5),
    (5, 6),
    (6, 3),
    (7, 11),
    (7, 12),
    (8, 1),
    (8, 4),
    (8, 7);
""")
