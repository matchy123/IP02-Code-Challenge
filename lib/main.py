from customer import Customer
from restaurant import Restaurant
from review import Review


customer1 = Customer("Justin", "Bieber")
customer2 = Customer("Justin", "Bieber")

restaurant1 = Restaurant("McDonald's")
restaurant2 = Restaurant("Krabby Patty")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

print(customer1.full_name())
print(restaurant2.average_star_rating())
print(customer2.num_reviews())
