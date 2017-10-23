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


# Returns the list of Usernames from a user's Followings list
def get_list_of_followings(user_id):
    print('Retrieving users from Followings...')
    
    next_id = False
    followings = []

    while True:
        if next_id:
            # If this is not the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following?limit=8&to=' + next_id
        else:
            # If this is the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following'

        response = requests.get(url)
        response_dict = clean_json_response(response)

        for user in response_dict['payload']['value']:
            followings.append(user['username'])

        try:
            # If the "to" key is missing, we've reached the end of the list and an exception is thrown
            next_id = response_dict['payload']['paging']['next']['to']
        except:
            break
    return followings
