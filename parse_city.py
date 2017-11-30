import json

city_name = 'San Francisco'

json_data = open('business.json')
restaurants = json.loads(json_data)
json_data.close()

json_data = open('review.json')
reviews = json.loads(json_data)
json_data.close()

target_restaurants = []
target_reviews = []

for restaurant in restaurants:
	if (restaurant.city == city_name):
		target_restaurants.append(restaurant)
		for review in reviews:
			if review.business_id == restaurant.business_id:
				target_reviews.append(review)