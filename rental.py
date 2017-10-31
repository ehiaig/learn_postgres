from peewee import PostgresqlDatabase, BooleanField, IntegerField, Model, CharField, DateField

my_db = PostgresqlDatabase('dvdrental',
                           host = 'localhost',
                           user = 'postgres',
                           password = '$Make2016$',
                           port = '5432')
class Rental_one(Model):
    class Meta:
        database = my_db

    renter_name = CharField(50)
    movie_name = CharField(100)
    rental_date = DateField(null = False)
    return_date = DateField(null=True)