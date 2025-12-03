#!/bin/bash

TARGETS=("10.0.0.2" "10.0.0.3" "10.0.0.4" "10.0.0.5" "10.0.0.6" "10.0.0.7")

while true; do
    NUM_FLOWS=$(( ( RANDOM % 3 ) + 1 ))
    
    echo "[$(date +%T)] Nowa seria: $NUM_FLOWS rownolegle polaczenia"

    for (( i=1; i<=NUM_FLOWS; i++ ))
    do
        RAND_IDX=$(( RANDOM % ${#TARGETS[@]} ))
        DEST_IP=${TARGETS[$RAND_IDX]}
        
        DURATION=$(( ( RANDOM % 4 ) + 3 ))

        TYPE=$(( RANDOM % 2 ))

        if [ $TYPE -eq 0 ]; then
            # TCP
            echo "   -> TCP do $DEST_IP ($DURATION s)"
            iperf -c $DEST_IP -t $DURATION &
        else
            # UDP
            BW=$(( ( RANDOM % 5 ) + 1 ))M
            echo "   -> UDP do $DEST_IP ($DURATION s, $BW)"
            iperf -c $DEST_IP -u -b $BW -t $DURATION &
        fi
    done

    sleep 1
done