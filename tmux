#!/bin/bash
DETACHED_SESSION=$(/usr/bin/tmux list-sessions  | grep -v attached | awk 'NR==1 {print $1}')

if [[ -n "$DETACHED_SESSION" ]]
then
    /usr/bin/tmux attach-session -t $DETACHED_SESSION
else
    /usr/bin/tmux
fi
