from customer import Customer
from restaurant import Restaurant
from review import Review


customer1 = Customer("Justin", "Bieber")
customer2 = Customer("Selena", "Gomez")

restaurant1 = Restaurant("McDonald's")
restaurant2 = Restaurant("Krabby Patty")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

print(f"Name :  {customer1.full_name()}")
print(f"Rating : {restaurant2.average_star_rating()}")
print(f"Review : {customer2.num_reviews()}")
