#!/bin/bash

TARGETS=("10.0.0.2" "10.0.0.3" "10.0.0.4" "10.0.0.5" "10.0.0.6")

echo "Startuje generator ruchu z hosta h1..."

while true; do
    echo "[$(date +%T)] Wysylam..."

    # [h2] TCP port 5001
    iperf -c 10.0.0.2 -p 5001 -t 5 &
    
    # [h3] UDP port 5002
    iperf -c 10.0.0.3 -u -p 5002 -b 1M -t 5 &
    
    # [h4] TCP port 8080
    iperf -c 10.0.0.4 -p 8080 -t 5 &

    # [h5] TCP na losowym default porcie
    iperf -c 10.0.0.5 -t 5 &
    
    # [h6] UDP streaming danych
    iperf -c 10.0.0.6 -u -b 5M -t 5 &

    sleep 7 # 7 nie 5 na wszelki wypadek
done