from peewee import *

my_db = PostgresqlDatabase('dvdrental',
                           host = 'localhost',
                           user = 'postgres',
                           password = '$Make2016$',
                           port = '5432')
class BaseModel(Model):
    class Meta:
        database = my_db

class Customer(BaseModel):
    active = IntegerField(null=True)
    activebool = BooleanField()
    # address = ForeignKeyField(db_column='address_id', rel_model=Address, to_field='address_id')
    create_date = DateField()
    customer = PrimaryKeyField(db_column='customer_id')
    email = CharField(null=True)
    first_name = CharField()
    last_name = CharField(index=True)
    last_update = DateTimeField(null=True)
    store = IntegerField(db_column='store_id', index=True)

    class Meta:
        db_table = 'customer'

class Film(BaseModel):
    description = TextField(null=True)
    film = PrimaryKeyField(db_column='film_id')
    # fulltext = TSVectorField(index=True)
    # language = ForeignKeyField(db_column='language_id', rel_model=Language, to_field='language')
    last_update = DateTimeField()
    length = IntegerField(null=True)
    # rating = UnknownField(null=True)  # USER-DEFINED
    release_year = IntegerField(null=True)
    rental_duration = IntegerField()
    rental_rate = DecimalField()
    replacement_cost = DecimalField()
    # special_features = UnknownField(null=True)  # ARRAY
    title = CharField(index=True)

    class Meta:
        db_table = 'film'

class Inventory(BaseModel):
    film = ForeignKeyField(db_column='film_id', rel_model=Film, to_field='film')
    inventory = PrimaryKeyField(db_column='inventory_id')
    last_update = DateTimeField()
    store = IntegerField(db_column='store_id')

    class Meta:
        db_table = 'inventory'
        indexes = (
            (('film', 'store'), False),
        )

class Rental(BaseModel):
    customer = ForeignKeyField(db_column='customer_id', rel_model=Customer, to_field='customer')
    inventory = ForeignKeyField(db_column='inventory_id', rel_model=Inventory, to_field='inventory')
    last_update = DateTimeField()
    rental_date = DateTimeField()
    rental = PrimaryKeyField(db_column='rental_id')
    return_date = DateTimeField(null=True)
    # staff = ForeignKeyField(db_column='staff_id', rel_model=Staff, to_field='staff')

    class Meta:
        db_table = 'rental'
        indexes = (
            (('rental_date', 'inventory', 'customer'), True),
        )

if __name__=='__main__':

    Q = Rental.select(Rental, Customer, Inventory,Film). \
        join(Customer, on=(Customer.customer == Rental.customer)). \
        join(Inventory, on=(Inventory.inventory == Rental.inventory)). \
        join(Film, on=(Film.film == Inventory.film)). \
        order_by(Rental.rental_date.desc()).limit(10)

    for u in Q:
        # print(u._data['rental_date']) #This prints the result as object
        # print(u.__dict__)#This prints the result as dictionary
        print(" Name: {}\n Movie Title:{}\n Return Date:{}".format(u.customer.first_name+' '+u.customer.last_name, u.inventory.film.title,
                                                                   u._data['rental_date']))
        print(' ')