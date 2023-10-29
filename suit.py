import random
import os

class main:
	def show(self):
		print("*"*30,"\n"," "*7,"Simple Suit")
		print("*"*30)
		print("1. Suit indonesia(Gajah, Orang, Semut)")
		print("2. Suit Jepang(Batu, Gunting, Kertas)")
	def choice(self):
		try:
			inp = int(input("Pilih jenis Suit: "))
			if(inp == 1 or inp == 2):
				return inp
			else:
				return False
		except:
			return False
	def choice_indonesia(self):
		os.system("clear")
		list = ["Gajah", "Orang", "Semut","Gajah", "Orang", "Semut"]
		rand = random.randint(0,5)
		print("Pilihan:\n1. Gajah\n2. Orang\n3. Semut")
		try:
			# print(list[0])
			inp_raw = int(input("Masukan pilihan(Angka): "))
			inp = inp_raw-1
			value_input = str(list[inp])
			value_random = str(list[rand])
			if inp_raw > 3:
				exit()
			if value_input == value_random:
				return "[ Seri ] Pilihan sama, Anda {} bot {}".format(value_input,value_random)
			else:
				if value_input == "Gajah" and value_random == "Orang": #Gajah dan orang
					return "[ Menang ] Anda gajah Bot orang"
				elif value_input == "Gajah" and value_random == "Semut": #Gajah dan semut
					return "[ Kalah ] Anda Gajah Bot semut"
				elif value_input == "Orang" and value_random == "Gajah":
					return "[ Kalah ] Anda orang Bot gajah" # orang dan gajah
				elif value_input == "Orang" and value_random == "Semut":
					return "[ Menang ] Anda orang Bot semut" # orang dan semut
				elif value_input == "Semut" and value_random == "Orang":
					return "[ Kalah ] Anda semut Bot orang" # semut dan orang
				elif value_input == "Semut" and value_random == "Gajah": #semut dan gajah
					return "[ Menang ] Anda semut Bot gajah"
				else:
					return "Mohon untuk memasukan pilihan ulang:)"
		except:
			return "Pilihan mohon untuk dicek kembali:)"

	def choice_jepang(self):
		os.system("clear")
		list = ["Batu", "Gunting", "Kertas","Batu", "Gunting", "Kertas"]
		rand = random.randint(0,2)
		print("Pilihan:\n1. Batu\n2. Gunting\n3. Kertas")
		try:
			# print(list[0])
			inp_raw = int(input("Masukan pilihan(Angka): "))
			inp = inp_raw-1
			value_input = str(list[inp])
			value_random = str(list[rand])
			if inp_raw > 3:
				exit()
			if value_input == value_random:
				return "[ Seri ] Pilihan sama, Anda {} bot {}".format(value_input,value_random)
			else:
				if value_input == "Batu" and value_random == "Gunting": #batu dan gunting
					return "[ Menang ] Anda batu Bot gunting"
				elif value_input == "Batu" and value_random == "Kertas": #Batu dan kertas
					return "[ Kalah ] Anda batu Bot kertas"
				elif value_input == "Gunting" and value_random == "Batu":
					return "[ Kalah ] Anda gunting Bot batu" # gunting dan batu
				elif value_input == "Gunting" and value_random == "Kertas":
					return "[ Menang ] Anda gunting Bot kertas" # gunting dan kertas
				elif value_input == "Kertas" and value_random == "Batu":
					return "[ Menang ] Anda kertas Bot batu" # kertas dan batu
				elif value_input == "Kertas" and value_random == "Gunting": #kertas dan gunting
					return "[ Kalah ] Anda kertas Bot gunting"
				else:
					return "Mohon untuk memasukan pilihan ulang:)"
		except:
			return "Pilihan mohon untuk dicek kembali:)"

	def proc(self):
		choice = self.choice()
		if choice == False:
			print("Masukan pilihan yang sesuai(Angka)!!!")
			exit()
		if choice == 1:
			print(self.choice_indonesia())
		elif choice == 2:
			print(self.choice_jepang())
		else:
			print("Pilih sesuai pilihan yang tepat:)")
	def __init__(self):
		self.show()
		self.proc()
main()
