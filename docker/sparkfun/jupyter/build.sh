sudo docker build \
    -t $JETBOT_DOCKER_REMOTE/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .
