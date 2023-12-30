# 5GC API Requester
This is a simple tool to send HTTP request to the different Network Functions (NF) in 5G Core Component and get valuable information about the different data sharing happening between them. This project is to demonstrate that, if we can get valuable information about the UEs from the HTTP or HTTPs requests, the 5G network can be at risk. So to overcome all this threats, we can analyze each component and the information sharing between them and improve the security of the network.

## How to Setup

* This project is developed by python 3.x.
* Testing Environment: Free5GC
* Usage
 ```bash
 python requester.py
 ```

	1.Select the testing network function (NF), all the IP addresses have been already configured inside the requster.py file, you can change it from the file.

## Functionality

* `requester.py`
 	* The main program
 	* Send request to 5GC API
* `src`
 	* The url of 5GC API
* `param.py`
 	* Default parameter for 5GC API
