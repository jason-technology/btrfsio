#!/usr/bin/python
# Python IOstat
# https://www.kernel.org/doc/Documentation/block/stat.txt
 
import time
import os
import sys
 
#if len(sys.argv) > 0 :
# timer = float(sys.argv[1])
#else :
# timer = 5


timer = 5
 
stats = os.popen("cat /sys/block/sda/stat").read()
stats_split = stats.split(' ')
stats_array = filter(None, stats_split)
 
time.sleep(timer)
stats_2 = os.popen("cat /sys/block/sda/stat").read()
stats_split_2 = stats_2.split(' ')
stats_array_2 = filter(None, stats_split_2)
 
iototal = [
int(stats_array_2[0]) - int(stats_array[0]),
int(stats_array_2[1]) - int(stats_array[1]),
int(stats_array_2[2]) - int(stats_array[2]),
int(stats_array_2[3]) - int(stats_array[3]),
int(stats_array_2[4]) - int(stats_array[4]),
int(stats_array_2[5]) - int(stats_array[5]),
int(stats_array_2[6]) - int(stats_array[6]),
int(stats_array_2[7]) - int(stats_array[7]),
int(stats_array_2[8]) - int(stats_array[8]),
int(stats_array_2[9]) - int(stats_array[9]),
int(stats_array_2[10]) - int(stats_array[10])
]
 
description = [
"IO stats over last "+str(timer)+" seconds \n\n",
"read I/Os : " + iototal[0],
"read merges : " + iototal[1],
"read sectors : " + iototal[2],
"read ticks (ms) : " + iototal[3],
"write I/Os : " + iototal[4],
"write merges : " + iototal[5],
"write sectors : " + iototal[6],
"write ticks (ms) : " + iototal[7],
"in_flight : " + iototal[8],
"io_ticks (ms) : " + iototal[9],
"time_in_queue (ms) : " + iototal[10]
]
for d in description:
 print(d)
