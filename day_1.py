#SOLUTION DAY 1 - PART A (Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?)
input = open("/home/utente/Scrivania/input.txt", "r")
sum = 0
data = []
for line in input:
	splitted_line = line.split(' ')
	for values in splitted_line:
		value_as_int = int(values)
		sum += value_as_int
		data.append(value_as_int)

print(sum)

#SOLUTION DAY 1 - PART B (What is the first frequency your device reaches twice?)
import itertools

freq = 0
seen = {0}
for i in itertools.cycle(data):
	freq += i
	if freq in seen:
		print(freq)
		break
	seen.add(freq)
