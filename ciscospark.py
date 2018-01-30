# import the requests library so we can use it to make REST calls
import requests
import sys
import config

# globally disable warnings about using certificate verification
requests.packages.urllib3.disable_warnings()


# create_room function
def create_room():
    # add authorization to the header
    header = {"Authorization": "Bearer %s" % config.token}

    # create request url
    rooms_api = "https://api.ciscospark.com/v1/rooms"

    # create request body
    payload = {
        "title": "%s with Spark Bot" % config.email
    }

    # send POST request and do not verify SSL certificate for simplicity
    api_response = requests.post(rooms_api, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    if response_status == 200:
        # parse the response in json
        response_json = api_response.json()

        # print the response
        print("room %s created" % response_json['id'])
        return response_json['id']
    else:
        print("%d: error creating room, please check your access token" % response_status)
        sys.exit(0)


# create_membership function
def create_membership(room_id):
    # add authorization to the header
    header = {"Authorization": "Bearer %s" % config.token}

    # create request url
    memberships_api = "https://api.ciscospark.com/v1/memberships"

    # create request body
    payload = {
        "roomId": room_id,
        "personEmail": config.email
    }

    # send POST request and do not verify SSL certificate for simplicity
    api_response = requests.post(memberships_api, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    if response_status == 200:
        # print the response
        print("%s joined room %s" % (config.email, room_id))
    else:
        print("%d: error adding you to room, please check your email address" % response_status)
        sys.exit(0)


# create_webhook function
def create_webhook(room_id):
    # add authorization to the header
    header = {"Authorization": "Bearer %s" % config.token}

    # create request url
    webhooks_api = "https://api.ciscospark.com/v1/webhooks"

    # create request body
    payload = {
        "resource": "messages",
        "event": "created",
        "filter": "roomId=%s" % room_id,
        "targetUrl": "%s/webhook" % config.ngrok_url,
        "name": "tf_workshop"
    }

    # send POST request and do not verify SSL certificate for simplicity
    api_response = requests.post(webhooks_api, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    if response_status == 200:
        # print the response
        print("%s registered" % config.ngrok_url)
    else:
        print("%d: error registering webhook to cisco spark, please check your ngrok_url" % response_status)
        sys.exit(0)


# get_message function
def get_message(message_id):
    header = {"Authorization": "Bearer %s" % config.token}

    # create request url using message ID
    messages_api = "https://api.ciscospark.com/v1/messages/"

    # send the GET request and do not verify SSL certificate for simplicity of this example
    api_response = requests.get(messages_api + message_id, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    if response_status == 200:
        # parse the response in json
        response_json = api_response.json()

        # get the text value from the response
        text = response_json["text"]

        # return the text value
        return text
    else:
        print("%d: error retrieve message, please check your message_id: %s" % (response_status, message_id))
        sys.exit(0)


# post_message function
def post_message(text):
    # add authorization to the header
    header = {"Authorization": "Bearer %s" % config.token}

    # create request url
    messages_api = "https://api.ciscospark.com/v1/messages"

    # create message in Spark room
    payload = {
        "toPersonEmail": config.email,
        "text": text
    }

    # create POST request do not verify SSL certificate for simplicity of this example
    api_response = requests.post(messages_api, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    if response_status == 200:
        # parse the response in json
        response_json = api_response.json()
        room_id = response_json['roomId']

        # print the response
        print("message [%s] sent in room %s" % (text, room_id))
        return room_id
    else:
        print("%d: error sending message please check your network connection" % response_status)
        sys.exit(0)


# is_image_attachment function
def is_image_attachment(attachment):
    # add authorization to the header
    header = {"Authorization": "Bearer %s" % config.token}

    # send the head request and do not verify SSL certificate for simplicity of this example
    api_response = requests.head(attachment, headers=header, verify=False)
    return api_response.headers['Content-Type'].startswith("image/"), api_response.headers['content-disposition']


# download_attachment function
def download_attachment(attachment, target):
    # add authorization to the header
    header = {"Authorization": "Bearer %s" % config.token}

    # send the head request and do not verify SSL certificate for simplicity of this example
    api_response = requests.get(attachment, headers=header, verify=False)
    with open(target, 'wb') as f:
        f.write(api_response.content)


# check_webhook function
def check_webhook():
    # send the GET request and do not verify SSL certificate for simplicity of this example
    api_response = requests.get(config.ngrok_url, verify=False)

    # get the response status code
    response_status = api_response.status_code

    if response_status == 404:
        print("%d: error hitting webhook, please check your ngrok instance is up and running: %s" % (
            response_status, config.ngrok_url))
        sys.exit(0)


if __name__ == '__main__':
    check_webhook()

    room_id = post_message("Welcome")
    create_webhook(room_id)
