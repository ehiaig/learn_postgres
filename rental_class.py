#2a. create a python class to represent a Rental with a movie_name, renter and rental_date
#2b. Take the data returned from question 1 and convert it into a list of Rental objects

import dvdrental

class Rental:

    def __init__(self, movie_titl, rentr, rentl_date ):
        self.movie_titl = movie_titl
        self.rentr = rentr
        self.rentl_date = rentl_date

    def rental_objects(self):
        rent_list = []
        for con in dvdrental.get_movies_rented():

            return (rent_list.append(con['Renter Name'], con['Movie Title'], con['Rental date']))

if __name__ == '__main__':
    ren = Rental()
    ren.rental_objects()