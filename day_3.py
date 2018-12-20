#SOLUTION DAY 3 - PART A (How many square inches of fabric are within two or more claims?)
import numpy as np
import pandas as pd

fabric = pd.DataFrame(np.zeros((1000, 1000)))

input = open("/home/utente/Scrivania/input.txt", "r")
for line in input:
	coord = pd.DataFrame(np.zeros((1,2)))
	area = pd.DataFrame(np.zeros((1,2)))
	coord.iloc[0,0] = int(line.rsplit(" ")[2].rstrip(":").rsplit(",")[0])
	coord.iloc[0,1] = int(line.rsplit(" ")[2].rstrip(":").rsplit(",")[1])
	area.iloc[0,0] = int(line.rsplit(" ")[3].rstrip("\n").rsplit("x")[0])
	area.iloc[0,1] = int(line.rsplit(" ")[3].rstrip("\n").rsplit("x")[1])
	fabric.iloc[int(coord.iloc[0,0]):int(coord.iloc[0,0]+area.iloc[0,0]), int(coord.iloc[0,1]):int(coord.iloc[0,1]+area.iloc[0,1])] += 1

print("The number of square inches of fabric that are within two or more claims is: " + str(fabric[fabric > 1.0].count().sum()))


#SOLUTION DAY 3 - PART B (What is the ID of the only claim that doesn't overlap?)
import numpy as np
import pandas as pd

fabric = pd.DataFrame(np.zeros((1000, 1000)))
coord_list = []
area_list = []
IDs = []

input = open("/home/utente/Scrivania/input.txt", "r")
for line in input:
	coord = pd.DataFrame(np.zeros((1,2)))
	area = pd.DataFrame(np.zeros((1,2)))
	ID = int(line.rsplit(" ")[0].lstrip("#"))
	coord.iloc[0,0] = int(line.rsplit(" ")[2].rstrip(":").rsplit(",")[0])
	coord.iloc[0,1] = int(line.rsplit(" ")[2].rstrip(":").rsplit(",")[1])
	area.iloc[0,0] = int(line.rsplit(" ")[3].rstrip("\n").rsplit("x")[0])
	area.iloc[0,1] = int(line.rsplit(" ")[3].rstrip("\n").rsplit("x")[1])
	coord_list.append(coord)
	area_list.append(area)
	IDs.append(ID)
	fabric.iloc[int(coord.iloc[0,0]):int(coord.iloc[0,0]+area.iloc[0,0]), int(coord.iloc[0,1]):int(coord.iloc[0,1]+area.iloc[0,1])] += 1

	
for i in range(len(coord_list)):
	if (fabric.iloc[int(coord_list[i][0]):int(coord_list[i][0]+area_list[i][0]), int(coord_list[i][1]):int(coord_list[i][1]+area_list[i][1])] == 1).all(axis=None):
		print("The number of square inches of fabric that are within two or more claims is: " + str(IDs[i]))

