#SOLUTION DAY 2 - PART A (What is the checksum for your list of box IDs?)
input = open("/home/utente/Scrivania/input.txt", "r")

data = []
for line in input:
	splitted_line = line.split(' ')
	for values in splitted_line:
		data.append(values.rstrip())


IDs_letters = {}
for i in range(len(data)):
	match_2 = []
	match_3 = []
	for j in set(data[i]):
		count = data[i].count(j)
		if (count == 2): 
			match_2.append(j)
		if (count == 3):
			match_3.append(j)
	IDs_letters[i] = [len(match_2), len(match_3)]


count_2=0
count_3=0
for i in IDs_letters.keys():
	if IDs_letters[i][0] != 0:
		count_2 += 1
	if IDs_letters[i][1] != 0:
		count_3 += 1
checksum = count_2 * count_3
print(checksum)

#SOLUTION DAY 2 - PART B (What letters are common between the two correct box IDs?)
import stringutils as su
input = open("/home/utente/Scrivania/input.txt", "r")

data = []
for line in input:
	splitted_line = line.split(' ')
	for values in splitted_line:
		data.append(values.rstrip())

count = 0
for i in range(0,len(data)):
	for z in range(i+1,len(data)):
		count=0
		for k in range(0,len(data[i])):
			if data[i][k] != data[z][k]:
				count += 1 
		if count == 1:
			print("Solution are string:\n" + data[i] + "\nand\n" + data[z])
			break

