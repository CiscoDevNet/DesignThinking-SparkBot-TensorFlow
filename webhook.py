# import Flask
from flask import Flask, request
import re, os, time, subprocess
import config, ciscospark

# Create an instance of Flask
app = Flask(__name__)

# Index page will trigger index() function
@app.route('/')
def index():
    return 'OK'

# Webhook page will trigger webhooks() function
@app.route("/webhook", methods=['POST'])
def webhooks():
    # Get the json data
    json = request.json
    person_email = json["data"]["personEmail"]

    if person_email != config.email:
        return ""

    print("[MESSAGE] %s" % json)
    # parse the message id, person id, person email, and room id
    message_id = json["data"]["id"]
    person_id = json["data"]["personId"]
    room_id = json["data"]["roomId"]
    files = json["data"]["files"]

    # convert the message id into readable text
    # message = ciscospark.get_message(message_id)
    # print(message)
    ret = []
    for f in files:
        is_image, cd = ciscospark.is_image_attachment(f)
        if is_image:
            m = re.search('"(.+)"', cd)
            name = m.group(0)
            print("%s is an image: %s" % (f, name))
            ciscospark.post_message("Analyzing")
            name = "%d-%s" % (int(time.time()), name[1:-1])
            ciscospark.download_attachment(f, name)
            ret.append(tf_analysis(name))
            ciscospark.post_message("\n".join(ret))
        else:
            print("%s is not an image" % f)

    return ""


def tf_analysis(name):
    p = subprocess.Popen(["docker", "run", "--rm", "-v", os.getcwd()+":/img/", config.docker_image_name,
                          "python", "classify_image.py", "--image=/img/" + name], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out


# run the application
if __name__ == "__main__":
    app.run()
