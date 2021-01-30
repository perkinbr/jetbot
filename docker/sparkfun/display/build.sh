sudo docker build \
    -t $JETBOT_DOCKER_REMOTE/jetbot:display-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile ../../../
