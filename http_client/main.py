import requests, json, jsonify


dec = ''
api_url4 = "http://127.0.0.1:5000/tasks"
api_url5 = "http://127.0.0.1:5000/test"
test = ''
company = [{"id": 3, "name": "Company Three"}]

task = {
    "description": "",
    "done": False,
    "id": 3,
    "title": "Read a book"
  }



def decider():
    dec = input('Was willst du machen? \n get or post? ')




    if dec == 'get':
        dec2 = input('Was willst du getten? \n companies or random? ')
        if dec2 == 'companies':
            api_url = "http://127.0.0.1:5000/companies"
            response = requests.get(api_url)
            print(response.json())
            rerunner()

        elif dec2 == 'random':
            api_url = "http://127.0.0.1:5000/random"
            response = requests.get(api_url)
            print(response.json())
            rerunner()

        else:
            print('Error, next try')
            decider(dec)

    # return dec



def rerunner ():
    s = input('Willst du nochmal eine Aktion machen? \n y or n? ')
    if s == 'y':
        decider()
    elif s == 'n':
        print('Okay viel spass noch')
    else:
        print('Error try again')
        rerunner()



def get_task():
    response = requests.get(api_url4)
    print(response.json())
    print(type(response.json()))

def post_task():
    r=requests.post(api_url4, )
    print(r.json())

def post_test():
    r=requests.post(api_url5, json=company)
    r_json = r.json()
    print(r_json)

post_test()