# 5G Experiments

This repository contains all the work i carried out in 5G.

The different task which includes sub projects and simulations of 5G architecture has been placed in the respective folders in this repository.

Following is the brief on each task :

1. [Network Slicing Using 2 UPFs Setup]()
    This is a simulation setup which uses 2 UPFs and 1 UE, this is to demostrate how the network resource allocation changes, when the UE switches between one UPF to another.
<br>

2. [Network Slicing Using 3 UPFs Setup]()
    This project is same as above but scaled from 2 UPFs to 3 UPFs. Few challanges were faced during the scaling, the whole procedure how to scale has been documented in this project.
<br>

3. [Network Slicing Using Host Machines]()
    This project is basically simulating the second one, but using mulitple PC. The above project was completely inside one single Host Machine, inside a virtualbox. But this project uses VMs from different Host machines which are connected to each other after few network configuration from virtualbox. This project also demonstrates how a bare Host OS of Raspberry PI can be configured as UPF. The whole procedure on how to setup this environment has been documented in this prject.
<br>

4. [Interconnects Threats in 5G]()
    This project is to understand what are the threats associated with the 5G Architecture which used HTTP/2 as its protocol in 5G Core System to communicate between different Network Functions (NFs).
<br>

5. [5GC API Requester]()
    This is a project forked from [here](). It helps to send the HTTP request to the different NFs in 5G Core system.
