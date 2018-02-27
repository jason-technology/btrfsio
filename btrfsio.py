#!/usr/bin/python
import re
import subprocess

IOStatOps="-x -m -H -d "

#Add ARGS to collect iteration time
IOStatOps+="2"


#Test for prerequisites

#return = subprocess.Popen(['command',options ], stdout = subprocess.PIPE).communicate()[0]

#Rewrite to grab this info from /proc/mounts
#mount = all mounted file systems
mounts = subprocess.Popen('mount', stdout = subprocess.PIPE).communicate()[0]

#btrfs_mounts = all mounted filesystems of type btrfs
btrfs_mounts = re.findall('.+btrfs.+',mounts)

#btrfs_filesystems = the actual mount points of the filesystem which we need to interact with them
btrfs_filesystems = []
for mount in btrfs_mounts:
	btrfs_filesystems.append(re.findall('\/\w+\/\w+',mount)[1])

#Create a 2Darray with each BTRFS filesystems label and constituent drives.
#if there is no label, use the mount point
diskarray ={} 
for fs in btrfs_filesystems:
	#Grab output from btrfs fi
	fi  = subprocess.Popen(['btrfs','fi', 'show', fs], stdout = subprocess.PIPE).communicate()[0]
	#Extract the label
	label2=re.findall('Label\:\s.[^\s]+',fi)[0]
	label1=re.findall('\'\S+',label2)[0]
	label=re.findall('\w+',label1)[0]
	#Extrct the member devices
	members=re.findall('\/\w+\/\w+',fi)

	diskarray[label]=members

#Build groups for IOstat
groups = ""
for fs in diskarray:
	groups+=" -g "+fs+" "
	for device in diskarray[fs]:
		groups+=device+" "

IOStatOps+=groups

subprocess.call("iostat "+IOStatOps,shell=True)
