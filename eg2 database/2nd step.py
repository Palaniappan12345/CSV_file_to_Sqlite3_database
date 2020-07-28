import csv,sqlite3

conn = sqlite3.connect('sample_importing_csv_file.db')
c = conn.cursor()

#create table
c.execute('''CREATE TABLE IF NOT EXISTS ACTOR_SCORE
             (Year integer,Movie text)''')
with open('actor_score.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Year'],i['Movie']) for i in dr]
c.executemany("INSERT INTO ACTOR_SCORE (Year,Movie) VALUES ( ?, ?);", to_db)


			
#commit the changes to db			
conn.commit()
#close the connection
conn.close()
