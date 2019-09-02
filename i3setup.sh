#!/bin/sh

# [[ -f ~/.i3/i3-config-name ]] && . ~/.i3/i3-config-name

# assemble config from specific and shared parts
# echo > ~/.i3/config
# cat ~/.i3/config-$I3_CONFIG-pre >> ~/.i3/config
# cat ~/.i3/config-shared >> ~/.i3/config
# cat ~/.i3/config-$I3_CONFIG-post >> ~/.i3/config

# give plasma (and networkmanager) some time to start up 
sleep 10

i3 --shmlog-size=26214400 &

# just block here :D
read
