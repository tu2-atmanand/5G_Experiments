import requests
import param

def main():
	# address = input("NF address (default: 127.0.0.1): ")
	# if address == "":
	# 	address = "127.0.0.1"

	nf = input("Select NF: (smf / udr / udm / amf / ausf / nssf / pcf / nrf / upf)\n>> ")
	while nf == "":
		print("Please select a NF")
		nf = input("(smf / udr / udm / amf / ausf / nssf / pcf / nrf / upf)\n>> ")

	param_default = param.load_default(nf)
	filename = "src/" + nf
	
#       if nf=="amf":
#		address=""
	switcher={
		'smf': lambda: "127.0.0.2",
		'amf': lambda: "127.0.0.18",
		'udr': lambda: "127.0.0.4",
		'udm': lambda: "127.0.0.3",
		'ausf': lambda: "127.0.0.9",
		'nssf': lambda: "127.0.0.31",
		'pcf': lambda: "127.0.0.7",
		'nrf': lambda: "127.0.0.10",
		'upf': lambda: "127.0.0.8"
	}
	address = switcher.get(nf,lambda:"invalid")
	address = address()
	print(address)

	urls = []
	methods = []
	
	# Read URL
	with open(filename, 'r') as f:
		api = ""
		port = ""
		
		for line in f.readlines():
			if line[0] == ">":
				port = ":" + line.split(" ")[1]
			elif line[0] == "*":
				api = line.split(" ")[1][:-1]
			else:
				urls.append("http://" + address + port + api + line.split("|")[0])
				methods.append(line.split("|")[1][:-1])
	
	for i in range(len(urls)):
		# Replace parameter
		index = [0, 0]
		tmp = ""
		ii = 0
		while ii < len(urls[i]):
			if urls[i][ii] == "[":
				index[0] = ii
			elif urls[i][ii] == "]":
				index[1] = ii
				key = urls[i][index[0] + 1:index[1]]
				urls[i] = urls[i].replace(urls[i][index[0]:index[1] + 1], param_default[key])
				ii = index[0]
			ii += 1
#	print(urls)
	print("\nMETHOD" + " " * 2 + "URL" + " " * 147 + "RESPONSE" + "\n" + "-" * 166)
	for url, method in zip(urls, methods):
		result = method + " " * (8 - len(method)) + url + " " * (150 - len(url))
		try:	
			if method == "GET":
				Print(result, requests.get(url, timeout = 5).status_code)
			elif method == "POST":
				Print(result, requests.post(url, timeout = 5).status_code)
			elif method == "PUT":
				Print(result, requests.put(url, timeout = 5).status_code)
			elif method == "DELETE":
				Print(result, requests.delete(url, timeout = 5).status_code)
			elif method == "PATCH":
				Print(result, requests.patch(url, timeout = 5).status_code)
			else:
				Print("ERROR" + "   " + " " * 150, 0)
		except requests.exceptions.Timeout:
			Print(" " * 8 + "Time Out" + " " * 142, 0)
			continue
		except requests.exceptions.ConnectionError:
			Print(" " * 8 + "Server Crash" + " " * 138, 0)
			break

def Print(_result, _status):
	print(_result, end = "")
	
	div = _status // 100
	mod = _status % 100
	if div == 2:
		print("\033[1;42m %s \033[0m" % str(_status))
	elif div == 4 and mod == 0:
		print("\033[1;45m %s \033[0m" % str(_status))
	elif div == 4 and mod == 3:
		print("\033[1;43m %s \033[0m" % str(_status))
	elif div == 5:
		print("\033[1;41m %s \033[0m" % str(_status))
	else:
		print(" " + str(_status))

if __name__ == '__main__':
	main()
