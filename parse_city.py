import json

city_name = 'San Francisco'
city_initial = 'SF'

json_data = open('business.json')
restaurants = json.loads(json_data)
json_data.close()
print(len(restaurants))

json_data = open('review.json')
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

with open('business_'+city_initial+'.json', 'w+') as business_out:
	json.dumps(target_restaurants, business_out)

with open('review_'+city_initial+'.json', 'w+') as reviews_out:
	json.dumps(target_reviews, reviews_out)