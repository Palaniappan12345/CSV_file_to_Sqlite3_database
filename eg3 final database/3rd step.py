import csv,sqlite3

conn = sqlite3.connect('kapi1.3-swaggers.db')
c = conn.cursor()

#create table
c.execute('''CREATE TABLE IF NOT EXISTS NEW_ACTOR_SCORE
             (ARTIST_NAME text,YEAR integer,MOVIE text,CRITIC_SCORE integer,AUDIENCE_SCORE integer,BOX_OFFICE_SCORE integer,UPDATED_BY text)''')

with open('kapiActorScore.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ARTIST_NAME'], i['YEAR'],i['MOVIE'],i['CRITIC_SCORE'],i['AUDIENCE_SCORE'],i['BOX_OFFICE_SCORE'],i['UPDATED_BY']) for i in dr]

c.executemany("INSERT INTO NEW_ACTOR_SCORE (ARTIST_NAME,YEAR,MOVIE,CRITIC_SCORE,AUDIENCE_SCORE,BOX_OFFICE_SCORE,UPDATED_BY) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)

			
#commit the changes to db			
conn.commit()
#close the connection
conn.close()
