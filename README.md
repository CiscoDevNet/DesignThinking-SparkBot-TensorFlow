# GSX-DesignThinking-SparkBot-TensorFlow

## Description
In the workshop, you will build a prototype to show when customer uploads a photo of an object to Cisco spark, it will talk to an open source deep learning library (TensorFlow) to identify the object and return the related topics and options. 


## Prerequisites
1. Install docker from docker.com
2. Install Python 2.7
3. Install two Python packages Requests and Flask 


## Steps
1. In Terminal, set current path to the folder of downloaded files ```$ cd <your-folder-name>```
2. Build a deep-learning docker image based on TensorFlow with pre-training data ```$ docker build . -t dtimg```
3. Run ngrok for demo connection ```$ ./ngrok http 5000```
4. Register your Spark Bot - Login developer.ciscospark.com; go to “My Apps” and create your Bot
5. Update the token, account and ngrok URL in config.py ```$ open config.py```
(use cmd+T to open a new tab in Terminal)
6. Run ciscospark.py to create a direct room and add a webhook ```$ python ciscospark.py```
You will get a "Hello" message from the Spark Bot you created after this step
7. Run webhook.py to recognize image when webhook is triggered ```$ python webhook.py```
Now upload a image to your spark bot room and test it out!

