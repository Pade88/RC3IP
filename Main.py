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
		if int(self.IP[0]) in range(class_A_IP_Range[0], class_A_IP_Range[1]):
			self.NetAddr   = [self.IP[0], str(0), str(0), str(0)]
			self.BroadAddr = [self.IP[0], str(255), str(255), str(255)]
			self.IPClass   = "A"
			return
		if int(self.IP[0]) in range(class_B_IP_Range[0], class_B_IP_Range[1]):
			self.NetAddr   = [self.IP[0], self.IP[1], str(0), str(0)]
			self.BroadAddr = [self.IP[0], self.IP[1], str(255), str(255)]
			self.IPClass   = "B"
			return
		if int(self.IP[0]) in range(class_C_IP_Range[0], class_C_IP_Range[1]):
			self.NetAddr   = [self.IP[0], self.IP[1], self.IP[2], str(0)]
			self.BroadAddr = [self.IP[0], self.IP[1], self.IP[3], str(255)]
			self.IPClass   = "C"
			return
		if int(self.IP[0]) in range(class_D_IP_Range[0], class_D_IP_Range[1]):
			# pentru clasa D, 28 de biti sunt host, deci in primul octect se face un XOR 11110000 ca sa setam
			# ultimii 4 biti pe 0 (xxxx xxxx ^ 0xF0) = xxxx 00000

			# pentru a seta ultimii 4 biti din primul octet pe 1, se face un OR cu 0xF (1111)
			# (xxxx xxxxx | 0xFF ) = xxxx 1111
			self.NetAddr   = [str(int(self.IP[0]) ^ 0xF0), str(0), str(0), str(0)]
			self.BroadAddr = [str(int(self.IP[0]) | 0x3), str(1), str(1), str(1)]
			self.IPClass   = "D"
			return

		self.NetAddr   = [str(int(self.IP[0]) ^ 0xF0), str(0), str(0), str(0)]
		self.BroadAddr = [str(int(self.IP[0]) | 0xF), str(1), str(1), str(1)]
		self.IPClass = "E"

	def join(self):
		self.NetAddr = '.'.join(self.NetAddr)
		self.BroadAddr = '.'.join(self.BroadAddr)

if __name__ == "__main__":
	ex1list = ["191.022.123.233", "97.200.015.000", "168.192.000.000", "244.234.100.9", "126.255.255.255",
			   "224.111.234.012", "173.202.000.000", "199.168.100.1", "225.192.111.5", "250.190.200.123"]

	# for IP in ex1list:
	# 	current_IP = IPinfo(IP) #dummy mask
	# 	print("IP-ul " + IP + ": face parte din " + current_IP.checkIPClass())

	ex2list = ["127.0.0.0", "168.192.255.255", "192.168.074.189", "223.123.0.12", "244.123.34.0", "90.100.76.22",
			   "225.200.021.210", "171.255.222.100"]

	for IP in ex2list:
		current_IP = IPinfo(IP)
		print("IP-ul " + IP + ": este in clasa de IP-uri " + current_IP.IPClass + ", adresa de retea " + current_IP.NetAddr
			  + ", adresa de broadcast: " + current_IP.BroadAddr)