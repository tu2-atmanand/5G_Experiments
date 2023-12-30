 ![[Pasted image 20230927173412.jpg]]

> Main link for this simulation : <https://github.com/s5uishida/free5gc_ueransim_snssai_upf_sample_config>
>
## Network Configuration

### In Core Plane - 5NR-Core (192.168.56.101)
>
> ip addr add 192.168.56.142/24 dev enp0s8
> ip addr add 192.168.56.143/24 dev enp0s8
> ip addr

## Running the Simulation

### 0. Start all the VM

And run :
> tmux
> ctrl + b
> shift + %

To switch to different windows :
> ctrl + b
> arrow key where you want to go

> ifconfigure

To verfiy their ip address.

### 1. Go in User Plane 1 - 5NR-UP1 (192.168.56.102)
>
>iptables -t nat -A POSTROUTING -s 10.60.0.0/16 ! -o upfgtp -j MASQUERADE
> cd 5Nr-Core/
> sudo ./run_upf.sh

> sudo tcpdump -i upfgtp -n
And if you want to save as pcap files
> sudo tcpdump -i any -w netSlicing-up1.pcap

### 2. Go in User Plane 2 - 5NR-UP2 (192.168.56.105)

If you want to save as pcap files
> sudo tcpdump -i any -w netSlicing-up2.pcap

>iptables -t nat -A POSTROUTING -s 10.60.0.0/16 ! -o upfgtp -j MASQUERADE
> cd 5Nr-Core/
> sudo ./run_upf.sh

> sudo tcpdump -i upfgtp -n

### 3. Go in Core Plane - 5NR-Core (192.168.56.101)
>
>sudo tcpdump -i any -w netSlicing-Core.pcap

>cd 5Nr-Core/
>sudo ./configure-snssai.sh
>sudo ./run_upf_expt.sh

### 4. Go in gNB - gNB1 (192.168.56.104)
>
> sudo tcpdump -i any -w netSlicing-gNB.pcap

> sudo ./start_gNB.sh

### 5. Go in User Equipment - UE1 (192.168.56.4)
>
> sudo tcpdump -i any -w netSlicing-UE1.pcap

> sudo ./start_UE_UPF_Expt.sh

- Permission : if we can use the cow monitoring device in our project.
- Permission : Can we have a video from the farm for cow monitoring, so that we can show that in our project.
- Learn about if we can control drone using 4g testbed.

> Learn testbed

Paper reserach
Motor Connection
MQTT




