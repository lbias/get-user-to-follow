import json
import requests

MEDIUM = 'https://medium.com'


# Removes the extra characters that get returned with every JSON request on Medium endpoints
# json to dictionary
def clean_json_response(response):
    return json.loads(response.text.replace('])}while(1);</x>', '', 1))


# Returns the User ID of a Medium Username
def get_user_id(username):
    print('Retrieving user ID...')

    url = MEDIUM + '/@' + username + '?format=json'
    response = requests.get(url)
    response_dict = clean_json_response(response)
    return response_dict['payload']['user']['userId']
