import database

database=database.Connection('dvdrental', 'postgres', '$Make2016$')
def get_actor_named_penelope():
    actor = database.query('select first_name, last_name from actor '
                           'where first_name = \'Penelope\'').fetch_one()
    first_name, last_name = actor

    print('First Name:{}\n Last Name: {}'.format(first_name, last_name))
    print(' ')


if __name__ == '__main__':
    get_actor_named_penelope()