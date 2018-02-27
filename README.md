# btrfsio
Python script for displaying IO Stats of each BTRFS filesystem mounted on the host

Currently uses iostat but will rewrite in native python.

Locates every mounted BTRFS file system and creates a group command line to pass to iostat.

The script groups every member device under the label of the btrfs filesystem.
**I have not tested what happend when there's no label but I will rewrite to make it use the mount point if there is no label"


