#1. Return in python, the last 10 movies rented, who rented them and rental date
import database
import rental

database=database.Connection('dvdrental', 'postgres', '$Make2016$')

def get_movies_rented():

    renters = database.query("SELECT CONCAT(first_name,' ',last_name) as renter_name, title, rental_date FROM rental "
                             "JOIN customer ON (customer.customer_id = rental.customer_id)"
                             "JOIN inventory ON (inventory.inventory_id = rental.inventory_id)"
                             "JOIN film ON (film.film_id = inventory.film_id)"
                             "ORDER BY rental_date DESC LIMIT 10").fetch_all()

    for renter in renters:
        renter_name, title, rental_date = renter

        """To print the renter"""
        # print(' Renter Name: {}\n Movie Title:{}\n Rental date: {}'.format(renter_name, title, rental_date))
        # print(' ')

        """To save the renters objects in the Rental table"""
        rental.Rental_one(renter_name=renter_name, title = title, rental_date=rental_date).save()

if __name__ == '__main__':
    # get_movies_rented()
    rental.Rental_one.create_table(fail_silently=True)
