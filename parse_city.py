import simplejson as json

city_name = 'San Francisco'
city_initial = 'SF'

restaurants = []
reviews = []
with open('dataset/business.json') as fin:
	for line in fin:
		line_contents = json.loads(line)
		restaurants.append(line_contents)
print(len(restaurants))

with open('dataset/review.json') as fin:
	for line in fin:
		line_contents = json.loads(line)
		reviews.append(line_contents)

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