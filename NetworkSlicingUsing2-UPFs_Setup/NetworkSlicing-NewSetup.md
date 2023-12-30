# Steps to Simulate network Slicing on Free5GC

# AIM

To verify the throughput and jitter values for different UPF plane using free5GC configuration

# System Requirements

- Virtual box with Ubuntu

- Free5GC .ova file contains five ubuntu OS (control plane, two user plane, gNb, UE)

# Procedure to setup 5G testbed using Free5GC

- Import the .ova file

![](https://lh7-us.googleusercontent.com/WZLvnyGhzHAc9_uq9UXuQvPimSzpnLv_QYVbO4cdQDfd4NwHrsVkKjRdmP6obThH3ts5NqiYDWq8g9EYUQgeulfYcBjXEbLlXNLUeI3RH3SXppXXB3ReXf2biBkrpuV_dJoud9E-fR7n7MtrLnPtORI)

- Open the 5NRCore-CP, UP1, UP2, gNB, UE and in each screen

- Give the login credentials as follows
  User name: chandharlabs
  Password:99999radio

![](https://lh7-us.googleusercontent.com/CmB2z2j25H6Ggfe6Mo4GQvBfMt8q-y0mJfND1Y6x8J5wzT_LhzeP_-SQkYodjkr5iZMh8Fvg8O8FdYHtw5CRzQoCqWIqDdtIXTXZ0QsDKhZxbz3XyygAJ-aTNT0fUQ0CxOwQhvGwv0Tc_BIivkQ10ag)

- Start the 5NRCore-CP and execute the following command “sudo bash startIPConfiguration.sh”
- Note down the ip address using “ifconfig” command: 192.168.56.141
![](https://lh7-us.googleusercontent.com/-uqPNMOvAdfVc-bt_NTFm0KFSXxS-hEs40sADHX3Y0DyKtkZw0vPd7ok7FNBiX42pLeUzHX51M8OXqxTqh2iDhhDQctcelwK1PUevmHwHT5U1g7p2zMGeiACn-cZQjUmOdz-eVkF9rE8t_7o3TmF4nw)

- Start the 5NRCore-UP1 and execute the following command “sudo bash startIPConfiguration.sh”
- Note down the ipaddress using “ifconfig”command: 192.168.56.144
![](https://lh7-us.googleusercontent.com/vW5X7t8S5lowFZ8DFbjTWF8c403YaSrnZRnbrPMqj0C-bSGnz5bXu-K4AGiZEE7dVibY4yAAblJqt4dqpuOFmMikVX2ugqMt1DAYvfaZW7yxchjNG5u0gSYsU3We5kQiMUQnxSL3LQJ0aQ7m2V45cjs)

- Start the 5NRCore-UP2 and execute the following command “sudo bash startIPConfiguration.sh”
- Note down the ipaddress using “ifconfig”command: 192.168.56.145
![](https://lh7-us.googleusercontent.com/WCnryoWMug9Jamxs26-TNMS8hO8aO0NoyRNnIwNNKLHDk49SF2NNpDgJ3V1Aewdu25aCBBAlRPP8JpGmJ44Zziilmo66rdS0Q-RlLi7PYYIrqnQFSBL1ksgrL4vt6FUH-g7WjvXWlfcsgEtP9GlCkyM)

- Start the 5NR-gNB and execute the following command “sudo bash startIPConfiguration.sh”  
- Note down the ipaddress using “ifconfig”command: 192.168.56.131
![](https://lh7-us.googleusercontent.com/zGYKcab2H_6lEnbaD3QQ0607KUK1PhnMH9uis7hWEUej8KiWCoay6LSFaXf6fcZ2yKunp29G-aJzkwAw9uZY0fMUwcXD3iUJcHW1Z-ERWblPqCg26fxPbia5hYsVbdZ101JvkKrB3Cyl45hDCGVPwGU)

- Start the 5NR-UE and execute the following command “sudo bash startIPConfiguration.sh”  
- Note down the ipaddress using “ifconfig”command: 192.168.56.132
![](https://lh7-us.googleusercontent.com/u9NSsFmkRIkcpaP-b37MMScBwDkbmCXWqbLSya1bMQs3u2JW9ysSNBMkwPCWuCWya7BZgbeP6X7q5nVFAetrWS7eGIHiL-MHFCLNd6x2hLC761Rs606EJ9Rud8arUkD4oABxyOZnYCTypzJIueuhmzU)

- Open the terminal window in the main Linux OS (Host): Using the new tab option open 4 terminals for CP, UPF, gNB, UE and SSH into all the 4 machines.

- In UPF2 terminal
![](https://lh7-us.googleusercontent.com/AwANk2dBx02aEBFXjrYfroVdy0W036C5kWo6vmdkWMR-mVqj0pMT5xXDLBUkbxAeCdqCOWTiQ7_MYESjE5wNAf_hWAWOxftTeAPADnWia5wfh1yz7ih2UCnynHdeUld5q3z1rUBLSxxMN-myY-D_rMk)

- In CP terminal
![](https://lh7-us.googleusercontent.com/EBRDxs63plIZciyV6LiAiMY4s-nPYwNvMQBV5l1mfNNe5QGvEGP-tp4093MPjyqLI1il5UGQ0sdzD3o-QkBIdRMvfCgNUgsUjndJeRhMo4tTnPjfXDxjO9FAXE4pc6HXCHBbvx3qgq3OntD6j0KSAMM)

- In gNB terminal
![](https://lh7-us.googleusercontent.com/EromV__fpWeXyjWO6DSeTNgtw5cQd1WVMxkBBr7fPJanbVUu2nLOwcrTk4qxRKmDtm1HGjkACqGcL2VYMFgU6gxpR8ZBlyhYDhGRk1Ny1UBQNyZkr1xnZslLtRXLHo8deyblnRoUOuJ4uPTAtMawG_Q)

- In CP
 	- Enter 'cd 5NRcore/webconsole',
 	- then run the command “go run server.go”
![](https://lh7-us.googleusercontent.com/gTzst1bf5OuYNTw9VdzSInVgAuAKJ2_OP0Y_IIKwzMELR1NsFRtU6TRR9axnyZTdxU9DDm0bqkFZUdvK6PU9JZ4bbMCWbLWEvHTHI30-oubcEeJ5fssDx8JMYzUiEV2r4UISWPTUfMdJk5of6Uu8dLU)

- Wait until to get the message HTTP on:5000
![](https://lh7-us.googleusercontent.com/-a0ZMbUuLtNmRJq_f0l3PUKbm966ll1SCSrAlj_2YeTeLre22zPprg5NfZFP7_sqqynW23XaZ2AMPiR3-eig6Yvl7W-hrdOjZT2a4mB7GfcMRZkEkrXp5fFbJDmGNSHP09Ijwo9y2aJiPD4DOLh7dP8)

- Go to the browser and type 192.168.56.141:5000, then type admin as a username and free5gc as  password.
![](https://lh7-us.googleusercontent.com/8mZ0UGZE9PWxl7ShsQi2wt11GeVIizMyWcZw8sYFYSox7mnKs_XfWIS3ed4kkc7ClP2z40AvMP4HfVlBu4JLRB7M19nvbqtPCHVpaYl7T7SRDSCwac7vBGgRf57Hn6_1NTQ3wRfNhj52zVbt5Hw4jJ8)

![](https://lh7-us.googleusercontent.com/kYe6P3O8Np3Tp-ObrEMxIkcl1-mIUrX1Q-QyIrRnk9FezLS1UG5ZxG0GWoMxM52QbqyUZ8cUgnZo8P8SgEY9neau2C5Cf93KrEUI8ZBvsLUpWJDP1TMy-FUUyfijVrNEz2fuKz-Ob4dTHROLklYsZhw)

![](https://lh7-us.googleusercontent.com/Bdrz_5qLc4cpYUiAXNWZO4KwqYE7U7yjGvehBb4IIdW_C1VmOZm0nia6Henqyd5YOSs6otlxciO2k3TjjgsAEfU38YEKeNeiNDfb7G6JDuCCrEIVzbaJ1hjgqmx9lBd2tUcPf0pItJKy81YFJRPUQBE)

![](https://lh7-us.googleusercontent.com/vul0atBjLj8y_I2AlJWrHHmR8wDEbyG2nwLKb2NX8MvaX1-w81rvL4pmpwTsCjG3Cqg7eaqMzGAIhsLuVPzJwYvHpaKNF7KIgaFCCNa2J9C0YDqBOZ7CMkodCgFD_gq7FMC5s8cCvsoZaQ1hCY6-3yo)

- At UE terminal

         ![](https://lh7-us.googleusercontent.com/m9zkBc8ncjRj6eXTS219l6QNe1icJYRdEuZKakNCV5nV8R8HNGS-7qY-MhPVnVsRGHNYt5DxsMnE_yzMeyHcGbkC0PPFbydinsS51GpDdaYd1cXQOZmDf72To9dq5b7vGclG3Jn9bL141Ey-bN1-otM)

- Check the web browser

![](https://lh7-us.googleusercontent.com/4h-AwrlVB77M7DYQhGL77buPSWRvDaTrvjZV_yroxp4_uI8x59EGqyUrLuooEEJyluUsLFxeT_tdezV4wkvud2LUOuIDlvLBz7E8FxRb3XQA0qoxI-dsRIK8GT4qliwGHGjZZFDr7XGiZ7ErHE8-IuY)

- Click the show info

![](https://lh7-us.googleusercontent.com/8fcOTKDteLHlzdlhKfKfuS-ztmUkkAImlGyB1ZDzSx_SoPxH58GcirzmnxHd_C7oDS7Po-ZHmq2ocRovW1iN6YeJmaDBqPtpdZ4XXkvy_ohr5-jn_0ViogfCnOOqGCeX6ldVB4mD_ztHFjBtT8AW-qk)

![](https://lh7-us.googleusercontent.com/IHFVaqYy6uvjtaR2MbsW5tqNVKicHGETYiBa_Xa9TNhDVC6gHgVAlGOp5q-jc7dgLnifvX3j1jG6v2bn_Ys20dMNBTOIr7vR4bmCFc0C9lKKa4ZnX7q9dWoVfpJDa_lDGYbOuBnl51lkl3-guezfb5U)  
  
- For throughput calculation in the UP1 machine type “iperf3 -s”

- In the UE terminal,

![](https://lh7-us.googleusercontent.com/X2gtjkd6yq3FEfd2sea7McqL9miQgwkvXpllZILm-0DSRGOl7X6GTEtyfG76ISTCf676HaM_tpjboXV9swO24rW3SK8MGwCCLLhyZF5JNkyZ35bv-bTdreb1eWecKX_ubA_7VeID4Kz2uuiXl9TFPWo)

- Calculate the throughput and latency using file transfer command (send the file)

![](https://lh7-us.googleusercontent.com/1g_mM2-VFO4m1Bna4DvvUEwTcTX2Qhq7eX2zJDPcIGjeCbh3P15Xn3m-szooFCU7hb7g1Ux2Ge6GYx1g4h5JOPp7SQ4Q3i0k7urUYnidH6GC7O_JUzt2vQj7RQoiwk6_Napf3PNYrGFlG-mAURGqfy0)

- Introducing the delay and releasing the delay value from the network in the UPF plane![](https://lh7-us.googleusercontent.com/4t14EjlxBlDR31C71upsQ3IgfCsbHebIpaPVRwHnU2OdTzJkSRy6oUFhN2dhn5HdyKPIKlLeDIJmZvIs-xOocz-wgYQHIk_IqEU0_bcXxDM0_GgxXM40i97HJ6eeoq7X9YiOap2QZAtkBeqyRgDwm90)

- Calculating the delay value at UE side before and after introducing latency “ping google.com -I uesimtun0”
    ![](https://lh7-us.googleusercontent.com/JWpSFBErRxp29s7nTq-YD1kIIiwXqynU94ER-mDB-3Fxp6eP92eiuLGXWwQ88kQudva-PMn21ELiRoMuFAVqreG57I_fRwHa_DV3xb3EawFp3FL6dXrK7cJ9SU2WpZJOFW_OjqMHdzoYcO5hlsgz1Vc)

![](https://lh7-us.googleusercontent.com/phTj_KHLUbJislgcgp_m0h52NzXt3wXDMzdrOzsTksCHtqDCiovOE5yTRzwZyFHs14EmO_pgAGzEXsqY9T1g3DpCgAN8SxVh2gBkgrLzWYRcX_UroiE5xriiHiPX6nUrBXMyzdjZQYRpmj1QV_ni1Kk)

# EXP2: DDOS effects in the free5GC network

# AIM

Analyse the with and without attacks in the free5GC network using the captured packets.

# System Requirements

- Broker VB (gNB) - 192.168.56.131

- Publisher VB (UE) - 192.168.56.132

- Subscriber VB (UP1) - 192.168.56.144

- Attacker VB (CP) - 192.168.56.141

#       Procedure

- Start all the virtual systems (UP1, gNB, and UE) using “sudo bash startIPConfiguration.sh”

- Install mosquitto in all the systems using following comments:

- sudo apt-get update

- sudo apt-get install mosquitto

- sudo apt-get install mosquitto-clients

- sudo apt clean

- Open the gNB in the terminal using its ip address and enter this command to start the broker

“sudo systemctl start mosquitto”

- Check the status using “sudo systemctl status mosquitto”

![](https://lh7-us.googleusercontent.com/cIWQPph7lQIZwFDPm7jtdi2bgS2wk03obvPr1j1QFFzsJk_znQ7vUCbqBtYAaTKm899VEMBkPf-lDFAByB70ZDBUuMibtGkhi_wELXWw3b4N4jpEX_Ei3_KfIQHGR8zpW1egtjOqUw-jCvg5KNOfln0)

- Verify Mosquitto by  running “netstat -tuln | grep 1883” ![](https://lh7-us.googleusercontent.com/EWc7Wh2bSD7ZJwXsehVZiwFLxtMqF41s7Xcu15FYOCY1wZegI0non1jsIOX1_WeczNrJevLm1ABDkBDCB0hiL0d5fT4y3gkolvSN7cSrA_5hHkm4WjoFt7sBCtbDuEKuMLnIJPmwr6spOReOK6vL9-s)

- Still if you get connection refused, then in the broker system do the following steps

![](https://lh7-us.googleusercontent.com/mR3E8aNiZZrVzuRi_cXNRjBtP5dDyzdpe75u14Rt1VdvGqsKhiMZO6GwYwzKEMvDwZqprMh4VZIHmjM6LCp3Q22uXl4WklBRLjSiiw0eKY4ZhmUM24uKp6idNCBhc1tzX2swzlbly65RYZbvJXcCZHI)

- Open the UE in the other tab of terminal using its ip address and change the directory:cd IoT-Security-DoS-main

- Using “sudo nano publish.py”, change the ipaddress as 192.168.56.131

- Run the code: “sudo python3 publish.py”

![](https://lh7-us.googleusercontent.com/azoJAlgsVKYzBWnDbnOTbR4_vCqthon9emEvIGZtbbBwSmknPxcYnyLJW4zGKz3vgtDKoL1zCGxHe5TRCZfRUr04wcxwhFkiF97qfW6dbVGDxicHJja4BRdTKxuKgmo9MYwQ1J5vWp86Psds3MOHcgw)

- Open the UP1 in the other tab of terminal using its ip address and change the directory:cd IoT-Security-DoS-main

- Using “sudo nano subscribe.py”, change the ipaddress as 192.168.56.131

- Run the code: “sudo python3 subscribe.py”

![](https://lh7-us.googleusercontent.com/QVgzX51Lpfjn2U77kZnQpNDxFyHfyAD-nngpbRAv7qsNIVtdtarrLPeOnaAEV5MW8ZqLjyUUOYgJzNJpx_8dntCk8LTm-R1ws1UhRV9AXfoTf0X6MCTlMpj0hL4ItUGlv8FpIAc1Wn5GBzlHgkKwABc)
