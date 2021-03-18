class_A_IP_Range = (0x0, 0x7F) # Primul bit al primului octet e 0, adresele disponibile sunt intre 00000000 (0) si 01111111 (127)
class_B_IP_Range = (0x80,0xBF) # Primi 2 biti ai primului octet sunt 1 si 0, adresele disponibile sunt intre 1000000 (128) si 1011111 (191)
class_C_IP_Range = (0xC0,0xDF) # Primi 3 biti ai primului octet sunt 1, 1, 0, adresele disponibile sunt intre 11000000 (192) si 11011111 (223)
class_D_IP_Range = (0xE0,0xEF) # Primi 4 biti ai primului octet sunt 1, 1, 1, 0, adresele disponibile sunt intre 1110000 (224) si 11101111 (239)

def checkIPClass(IP):
	lv_IP = IP.split(".")
	if int(lv_IP[0]) in range(class_A_IP_Range[0], class_A_IP_Range[1]):
		return "Clasa A"
	if int(lv_IP[0]) in range(class_B_IP_Range[0], class_B_IP_Range[1]):
		return "Clasa B"
	if int(lv_IP[0]) in range(class_C_IP_Range[0], class_C_IP_Range[1]):
		return "Clasa C"
	if int(lv_IP[0]) in range(class_D_IP_Range[0], class_D_IP_Range[1]):
		return "Clasa D"
	return "Clasa E"

if __name__ == "__main__":
	print(checkIPClass("225.192.111.5"))