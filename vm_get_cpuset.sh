#!/bin/bash

#function to show VNF name
show_vnf_name () {
compute=$1
vm_id=$2
nova_name=$(ssh heat-admin@${compute} sudo virsh dumpxml ${vm_id} |grep 'nova:name')
echo $nova_name|cut -d '>' -f2|cut -d '<' -f1
}

#function to check number of vcpus assigned to a VM
get_num_vcpus () {
compute=$1
vm_id=$2
num_vcpu=$(ssh heat-admin@${compute} sudo virsh dumpxml ${vm_id} | grep 'nova:vcpus')
echo $num_vcpu|cut -d '<' -f2|cut -d '>' -f2
}

#function to list CPUsets of a VM
get_cpu_list () {
compute=$1
vm_id=$2
vcpu_list=$(ssh heat-admin@${compute} sudo virsh dumpxml ${vm_id} | grep 'vcpu='|awk '{print $3}'|cut -d'=' -f2 |cut -d '/' -f1)
echo $vcpu_list
}


for i in $(cat /etc/hosts | grep -i compute | awk '{print $2}'); do for j in $(ssh heat-admin@$i sudo virsh list --all| grep instance | awk '{print $2}'); do echo -e "${i} \t ${j} \t $(show_vnf_name ${i} ${j}) \t $(get_num_vcpus ${i} ${j}) \t $(get_cpu_list ${i} ${j})" ;done ;done


