from flask import Flask, json, jsonify, request
import requests

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
random = {
	"random": "22",
	"random float": "19.396",
	"bool": "true",
	"date": "1992-04-28",
	"regEx": "hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo to you",
	"enum": "online",
	"firstname": "Stacey",
	"lastname": "Radu",
	"city": "Tamale",
	"country": "Togo",
	"countryCode": "CU",
	"email uses current data": "Stacey.Radu@gmail.com",
	"email from expression": "Stacey.Radu@yopmail.com",
	"array": [
		"Georgina",
		"Shirlee",
		"Leia",
		"Leanna",
		"Max"
	],
	"array of objects": [
		{
			"index": "0",
			"index start at 5": "5"
		},
		{
			"index": "1",
			"index start at 5": "6"
		},
		{
			"index": "2",
			"index start at 5": "7"
		}
	],
	"Jere": {
		"age": "23"
	}
}

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/random', methods=['GET'])
def get_random():
  return json.dumps(random)

@api.route('/tasks', methods=['GET'])
def get_tasks():
  return jsonify({'tasks': tasks})

# @api.route('/tasks', methods=['POST'])
# def create_task():
# 	tasks = {
# 		'id': tasks[-1]['id'] + 1,
# 		'title': requests.json['title'],
# 		'description': requests.json.get('description', ""),
# 		'done': False
# 	}
# 	return jsonify({'tasks': tasks})

@api.route('/test', methods=['POST'])
def post_test():
	comp = {"id": request.json["id"], "name": request.json["name"]}
	# companies.append(comp)
	print(type(comp))
	print(comp)


	return jsonify({'companies': companies}), 'Success!'



if __name__ == '__main__':
    api.run(debug=True)
