#!/bin/bash

TARGETS=("10.0.0.2" "10.0.0.3" "10.0.0.4" "10.0.0.5" "10.0.0.6" "10.0.0.7")

while true; do
    NUM_FLOWS=$(( ( RANDOM % 3 ) + 1 ))
    
    echo "--- Nowa seria: uruchamiam $NUM_FLOWS rownolegle przeplywy ---"

    for (( i=1; i<=NUM_FLOWS; i++ ))
    do
        RAND_IDX=$(( RANDOM % ${#TARGETS[@]} ))
        DEST_IP=${TARGETS[$RAND_IDX]}

        DURATION=$(( ( RANDOM % 6 ) + 3 ))

        TYPE=$(( RANDOM % 2 ))

        if [ $TYPE -eq 0 ]; then
            # --- TCP ---
            echo "   [Flow $i] TCP -> $DEST_IP (czas: ${DURATION}s)"
            iperf -c $DEST_IP -t $DURATION &
        else
            # --- UDP ---
            # bandwidth 1M - 10M
            BW=$(( ( RANDOM % 10 ) + 1 ))M
            echo "   [Flow $i] UDP -> $DEST_IP (czas: ${DURATION}s, bw: $BW)"
            iperf -c $DEST_IP -u -b $BW -t $DURATION &
        fi
    done

    SLEEP_TIME=$(( ( RANDOM % 2 ) + 1 ))
    echo "--- Czekam ${SLEEP_TIME}s przed kolejna seria... ---"
    sleep $SLEEP_TIME
done