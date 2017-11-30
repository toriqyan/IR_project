import json

city_name = 'San Francisco'
city_initial = 'SF'

with open('dataset/business.json') as json_data:
	restaurants = json.loads(json_data)
print(len(restaurants))

json_data = open('dataset/review.json')
reviews = json.loads(json_data)
json_data.close()
print(len(reviews))

target_restaurants = []
target_reviews = []

for restaurant in restaurants:
	if (restaurant.city == city_name):
		target_restaurants.append(restaurant)
		for review in reviews:
			if review.business_id == restaurant.business_id:
				target_reviews.append(review)

with open('dataset/business_'+city_initial+'.json', 'w+') as business_out:
	json.dumps(target_restaurants, business_out)

with open('dataset/review_'+city_initial+'.json', 'w+') as reviews_out:
	json.dumps(target_reviews, reviews_out)