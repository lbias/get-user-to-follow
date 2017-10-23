import json


# Removes the extra characters that get returned with every JSON request on Medium endpoints
# json to dictionary
def clean_json_response(response):
    return json.loads(response.text.replace('])}while(1);</x>', '', 1))
