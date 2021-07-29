import random
import requests
import json

#API details
url = "http://127.0.0.1:5000/api/the_eye"
headers = {'Content-Type': 'application/json'}

tests = [
    {
      "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
      "category": "page interaction",
      "name": "pageview",
      "data": {
        "host": "www.consumeraffairs.com",
        "path": "/",
      },
      "timestamp": "2021-01-01 09:15:27.243860"
    },
    {
      "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
      "category": "page interaction",
      "name": "cta click",
      "data": {
        "host": "www.consumeraffairs.com",
        "path": "/",
        "element": "chat bubble"
      },
      "timestamp": "2021-01-01 09:15:27.243860"
    },
    {
      "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
      "category": "form interaction",
      "name": "submit",
      "data": {
        "host": "www.consumeraffairs.com",
        "path": "/",
        "form": {
          "first_name": "John",
          "last_name": "Doe"
        }
      },
      "timestamp": "2021-01-01 09:15:27.243860"
    }
]


for x in range(100):
    #Making http post request
    body = json.dumps(tests[random.randint(0,2)])
    response = requests.post(url, headers=headers, data=body, verify=False)
    print(response.text)
