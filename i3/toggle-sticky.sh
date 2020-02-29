#!/bin/sh

FOCUSED=$(xprop -root _NET_ACTIVE_WINDOW | awk -F' ' '{print $NF}')

if xprop -id $FOCUSED _NET_WM_STATE | grep -q "_NET_WM_STATE_STICKY"; then
    i3 "sticky disable, border normal 0"
else
    i3 "sticky enable, border none"
fi

