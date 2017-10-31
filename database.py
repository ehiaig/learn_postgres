import psycopg2
import psycopg2.extras

class Connection:
    '''docstring for Connection'''
    def __init__(self, database, user, password='', host='localhost', port = 5432):
        # config = dict(database = database, user = user, password=password, host=host, port=port)
        con = psycopg2.connect(database = database,
                               user = user,
                               password=password,
                               host=host,
                               port=port)

        self.cursor = con.cursor(cursor_factory = psycopg2.extras.DictCursor)

    def query(self, query):
        self.cursor.execute(query)
        return self

    def fetch_one(self): #This method returns only the first line of whatever you ask it to return
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()

if __name__ == '__main__':
    database = Connection('dvdrental', 'postgres', '$Make2016$')
    # print(database.query('select version()').fetch_one())
    # print(database.query('select * from actor').fetch_one())
    actors = database.query('select * from actor').fetch_all()
    for act in actors:
        id, first_name, last_name, last_update = act
        print('First Name:{} \n Last Name:{} \n Last Update:{}'.format(first_name, last_name, last_update))