ARG BASE_IMAGE=jetbot/jetbot:jupyter-0.4.1-32.4.4.orig
FROM ${BASE_IMAGE}
RUN pip3 install sparkfun-qwiic
RUN pip3 install evdev
COPY ../../../sparkfun/robot.py /usr/local/lib/python3.6/dist-packages/jetbot-0.4.1-py3.6.egg/jetbot/robot.py
COPY ../../../sparkfun/motor.py /usr/local/lib/python3.6/dist-packages/jetbot-0.4.1-py3.6.egg/jetbot/motor.py
