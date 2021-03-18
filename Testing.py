# Tema 1
def adresaDeRetea(IP, MASK):
	# se descompun cei doi parametrii
	if isinstance(IP, str) and isinstance(MASK, str):
		lv_IP = IP.split(".") 
		lv_MASK = MASK.split(".")
	else:
		lv_IP = IP
		lv_MASK = MASK
	# stringurile in care o sa fie compuse rezultatele
	result_bin = ""
	result_dec = ""

	if len(lv_IP) == len(lv_MASK):
		for looper in range(len(lv_IP)):
			# stringurile sunt convertite la INTEGER, se aplica un bitwise AND
			# se reconvertesc la BIN, si se aplica un zfill(8) pentru a scapa
			# de formatarea in binar, si de asigura paddingul pana la al 8-lea bit.
			result_bin += (bin(int(lv_IP[looper]) & int(lv_MASK[looper]))[2:].zfill(8))
			result_dec += str((int(lv_IP[looper]) & int(lv_MASK[looper])))
			# se adauga 1 punct dupa fiecare element compus
			result_bin += "."
			result_dec += "."
	# se returneaza un tuple, in functia main se selecteaza fct[0] pentru binar si fct[1] pentru decimal
	return result_bin, result_dec


# Tema 2
def adresaDeBroadCast(IP, MASK, IP_type = "A"):
	if isinstance(IP, str) and isinstance(MASK, str):
		lv_IP = IP.split(".") 
		lv_MASK = MASK.split(".")
	else:
		lv_IP = IP
		lv_MASK = MASK
	result_broad_addres_bin = ""
	result_broad_addres_dec = ""

	if IP_type == "A":
		# pe configuratia de tip A, primii 3 octeti sunt conf. de retea si ultimul conf. de host
		identificatori_retea = [bin(int(lv_MASK[looper]))[2:].zfill(8) for looper in range(3)]
		identificatori_host = str(bin(int(lv_MASK[3])))[2:].zfill(8)
		# ultimul octet este completat cu 1 (@todo XOR 1?)
		identificatori_host_bitwB = "11111111"
		identificatori_host_bitwD = "255"
		for looper in range(3):
			# primii 3 octeti sunt copiati in rezultat, nefiind modificati
			result_broad_addres_bin += (bin(int(lv_IP[looper])))[2:].zfill(8)
			result_broad_addres_dec += str(int(lv_IP[looper]))

			result_broad_addres_bin += "."
			result_broad_addres_dec += "."
		else:
			# ultimul octet este inlocuit cu cel modificat
			result_broad_addres_bin += identificatori_host_bitwB
			result_broad_addres_dec += str(int(identificatori_host_bitwD))

	if IP_type == "B":
		# todo
		pass

	return result_broad_addres_bin, result_broad_addres_dec
	# prototip functie mai simplu fara formatare
	# lv_IP = IP.split(".")
	# lv_IP[3] = "11111111"
	# return lv_IP

# Tema 3
def IP_posibile(IP, MASK):
	# se alege tip de IP A
	lv_IP = IP.split(".") 
	lv_MASK = MASK.split(".")

	result_addr = list()
	result_broad = list()
	for looper in range(1, 0xFF):
		lv_IP[3] = str(looper)
		result_addr.append(adresaDeRetea(lv_IP, lv_MASK)[1])
		result_broad.append(adresaDeBroadCast(lv_IP, lv_MASK)[1])

	return result_addr, result_broad

if __name__ == "__main__":
	#print(adresaDeRetea("134.141.7.33", "255.255.255.0")[1])
	#print(adresaDeBroadCast("134.141.7.33", "255.255.255.0")[1])
	IP_posibile("193.193.7.7", "255.255.172.142")