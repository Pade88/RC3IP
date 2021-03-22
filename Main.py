class_A_IP_Range = (0x0, 0x7F) # Primul bit al primului octet e 0, adresele disponibile sunt intre 00000000 (0) si 01111111 (127)
class_B_IP_Range = (0x80,0xBF) # Primi 2 biti ai primului octet sunt 1 si 0, adresele disponibile sunt intre 1000000 (128) si 1011111 (191)
class_C_IP_Range = (0xC0,0xDF) # Primi 3 biti ai primului octet sunt 1, 1, 0, adresele disponibile sunt intre 11000000 (192) si 11011111 (223)
class_D_IP_Range = (0xE0,0xEF) # Primi 4 biti ai primului octet sunt 1, 1, 1, 0, adresele disponibile sunt intre 1110000 (224) si 11101111 (239)

class IPinfo():
	def __init__(self, IP):
		self.IP = IP.split(".")
		self.checkIPClass()
		self.join()

	def checkIPClass(self):
		if int(self.IP[0]) in range(class_A_IP_Range[0], class_A_IP_Range[1]+1):
			self.NetAddr   = [self.IP[0], str(0), str(0), str(0)]
			self.BroadAddr = [self.IP[0], str(255), str(255), str(255)]
			self.HostOctals = 24
			self.IPClass   = "A"
			return
		if int(self.IP[0]) in range(class_B_IP_Range[0], class_B_IP_Range[1]+1):
			self.NetAddr   = [self.IP[0], self.IP[1], str(0), str(0)]
			self.BroadAddr = [self.IP[0], self.IP[1], str(255), str(255)]
			self.HostOctals = 16
			self.IPClass   = "B"
			return
		if int(self.IP[0]) in range(class_C_IP_Range[0], class_C_IP_Range[1]+1):
			self.NetAddr   = [self.IP[0], self.IP[1], self.IP[2], str(0)]
			self.BroadAddr = [self.IP[0], self.IP[1], self.IP[3], str(255)]
			self.HostOctals = 8
			self.IPClass   = "C"
			return
		if int(self.IP[0]) in range(class_D_IP_Range[0], class_D_IP_Range[1]+1):
			self.NetAddr   = None
			self.BroadAddr = None
			self.HostOctals = 28
			self.IPClass   = "D"
			return

		self.NetAddr   = None
		self.BroadAddr = None
		self.HostOctals = 28
		self.IPClass = "E"

	def getSubNetMask(self, value):
		if value > self.HostOctals:
			self.LoanBits = value - self.HostOctals
			self.LeftBits = 16 - self.LoanBits

		computed_value = list()
		append_value = 256
		for looper in range(self.LoanBits):
			computed_value.append(append_value / 2)
			append_value /= 2

		self.noSubNets = pow(2, self.LoanBits) - 2
		self.noSubNetsHosts = pow(2, self.LeftBits) - 2
		self.subNetMask = ["255", "255", int(sum(computed_value)), "0"]

		self.subNetsDomain = list()
		for subNet in range(self.noSubNets):
			for subNetHost in range(self.noSubNetsHosts):
				self.subNetsDomain.append([self.IP[0], self.IP[1], subNet, subNetHost])

		# ToDo si pentru restul claselor de IP?

		return self.subNetMask

	def getBinIP(self):
		looper = 0
		for octet in self.IP:
			self.IP[looper] = str(bin(int(octet)))[2:].zfill(8)
			looper += 1

	def join(self):
		self.NetAddr = '.'.join(self.NetAddr)
		self.BroadAddr = '.'.join(self.BroadAddr)

if __name__ == "__main__":
	print (" ---------------------> EXERCITIUL 1 <-----------------")
	ex1list = ["191.022.123.233", "97.200.015.000", "168.192.000.000", "244.234.100.9", "126.255.255.255",
			   "224.111.234.012", "173.202.000.000", "199.168.100.1", "225.192.111.5", "250.190.200.123"]

	for IP in ex1list:
		current_IP = IPinfo(IP)
		print("IP-ul " + IP + ": face parte din " + current_IP.IPClass)

	print (" ---------------------> EXERCITIUL 2 <-----------------")
	ex2list = ["127.0.0.0", "168.192.255.255", "192.168.074.189", "223.123.0.12", "244.123.34.0", "90.100.76.22",
			   "225.200.021.210", "171.255.222.100"]

	for IP in ex2list:
		current_IP = IPinfo(IP)
		if (current_IP.IPClass in ["A", "B", "C"]):
			print("IP-ul " + IP + ": este in clasa de IP-uri " + current_IP.IPClass + ", adresa de retea " + current_IP.NetAddr
				  + ", adresa de broadcast: " + current_IP.BroadAddr)
		else:
			print("IP-ul " + IP + ": este in clasa de IP-uri " + current_IP.IPClass +
				  " adresa de retea si de broadcast nu exista pentru aceasta clasa")

	print (" ---------------------> EXERCITIUL 3 <-----------------")
	test_IP = IPinfo("190.232.10.211")
	test_IP.getSubNetMask(24)
	print("IP-ul este in clasa " + test_IP.IPClass + ", are un numar de " + str(test_IP.noSubNets)
		+ " subretele utilizabile, un numar de " + str(test_IP.noSubNetsHosts) + " gazde utlizabile pe o subretea. In proces am imprumutat "
		+ str(test_IP.LoanBits) + " biti si am ramas cu " + str(test_IP.LeftBits))

	print("Intervalul adreselor de subretea este: " + str(test_IP.subNetsDomain[0]) + " - " + str(test_IP.subNetsDomain[test_IP.noSubNets-1]))
	print("Intervalul adreselor de gazde pentru fiecare subretea este: " + str(test_IP.subNetsDomain[0]) + " - " +
		  str(test_IP.subNetsDomain[(test_IP.noSubNets-1 * test_IP.noSubNetsHosts-1)]))

	print (" ---------------------> EXERCITIUL 4 <-----------------")
	ex4list = ["95.0.0.0", "128.0.0.0", "193.0.0.0", "224.0.0.0", "240.0.0.0"]
	for IP in ex4list:
		current_IP = IPinfo(IP)
		print("Un IP din clasa " + current_IP.IPClass + " poate avea maxim " + str(pow(2, (current_IP.HostOctals-2))) + " subretele")
		#pow(2, (current_IP.HostOctals-2)) 2 la puterea biti imprumutati (numar total de biti gazda - 2, este cel mai mare numar de biti imprumutati posibil)