ARG BASE_IMAGE=jetbot/jetbot:display-0.4.1-32.4.4.orig
FROM ${BASE_IMAGE}
RUN pip3 install sparkfun-qwiic
COPY sparkfun/stats.py /usr/local/lib/python3.6/dist-packages/jetbot-0.4.1-py3.6.egg/jetbot/apps/stats.py
CMD exec python3 -m jetbot.apps.stats

