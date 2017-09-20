# GSX-DesignThinking-SparkBot-TensorFlow

## Description
In the exercise, you will build a prototype to show when customer uploads a photo of an object to Cisco spark, it will talk to an open source deep learning library (TensorFlow) to identify the object and return the related topics and options. 
The instructions are based on Mac computer. You may need to modify some steps if you are using windows.


## Prerequisites
1. Install [docker](https://www.docker.com/). You will see a running docker on your system bar after completion. [docker screen](https://github.com/CiscoDevNet/GSX-DesignThinking-SparkBot-TensorFlow/blob/master/Docker.png)
2. Install Python 2.X. We used Python 2.7 during GSX workshop. You can check your python version by put this command in Terminal ```$ python --version```
3. Install Python packages "Requests" ```$ sudo pip install Flask``` Check [this page](http://docs.python-requests.org/en/master/user/install/) for more information if you run into any issues.
4. Install Python packages "Flask" ```$ sudo pip install Flask``` Check [this page](http://flask.pocoo.org/docs/0.12/installation/) for more information if you run into any issues.


## Steps
1. Download all files from this repo to you local computer if you have not yet.
2. We need to set the current path to the folder of downloaded files. In Terminal, you can use the **cd** command ```$ cd <your-folder-path>```
3. Now let's build a deep-learning docker image based on TensorFlow with pre-training data. We will need to use **docker build** command, and set the image title as **dtimg**. ```$ docker build . -t dtimg```
4. We will use [ngrok](https://ngrok.com/) tool to set up connection tunnel between your computer and public cloud. ```$ ./ngrok http 5000``` You will get a screen like this [ngrok screen](https://github.com/CiscoDevNet/GSX-DesignThinking-SparkBot-TensorFlow/blob/master/ngrok.png) after completion. You will need the http forwarding url for step 6.
5. You will need to register your Spark Bot - login to developer.ciscospark.com, and then go to “My Apps” tab to create your Bot. Once you created your Bot, you will be able to copy the access token of your Bot.
6. Now we need to update the Bot access token, your Spark account email and ngrok forwarding URL in config.py ```$ open config.py```
(use cmd+T to open a new tab in Terminal)
7. We will run our prewritten script to create a direct room in Spark with your Bot and add a webhook to that room. ```$ python ciscospark.py``` You will get a "Hello" message from the Spark Bot you created after this step. If you want to learn how to write this script, you can visit Spark Learning Modules on [Cisco DevNet](https://learninglabs.cisco.com/modules/beginning-apis). 
8. We also need to run another prewritten services to recognize image when webhook is triggered in your Spark Bot room. ```$ python webhook.py```You will need to keep this service running to enable the image recognition capality for your Spark Bot room.
Now upload a image to your Spark Bot room and test it out!

