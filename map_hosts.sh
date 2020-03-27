#!/bin/bash
file=/home/stack/map_hosts
if [ -f $file ]
then
rm $file
fi
. /home/stack/stackrc
for i in `nova list | grep overcloud|awk -F" " '{ print $2 }'`
do
par1=`nova list|grep $i|awk -F" " '{ print $4 }'`
par2=`ironic node-list | grep $i | awk -F" " '{ print $2 }'`
#par3=`ironic node-show $par2 | grep ipmi_address | awk -F"'" '{ print $8 }'`
par3=`ironic node-show $par2 --fields driver_info| grep 'ipmi_address' | grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'`
echo $par3" "$par1 >> $file
done
echo $file | sort

