from openpyxl import Workbook
import openpyxl

# storing all of the states into a dict
# where state: id
states = {}

stateCSV = open("statesCSV.csv", "r")
stateCSV.__next__()
for s in stateCSV:
	id = s.split(",")[0]
	state = s.split(",")[1]
	states[state] = id

stateCSV.close()

#reading us cities

path = "UScities&states.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active


end_city = "El Monte Mobile Village\n"
trigger = True
count = 1
cities = []

while(trigger):
	city = sheet_obj.cell(row = count+1, column=1)
	state = sheet_obj.cell(row = count+1, column = 3)
	# print(count, city.value, state.value)
	count = count+1
	# to hold state_id & city

	if(city.value == None):
		trigger = False
		break

	temp = []
	state_id = states.get(state.value + "\n")
	temp.append(state_id)
	temp.append(city.value)
	temp.append(state.value)
	cities.append(temp)


workbook = Workbook()
sheet = workbook.active


total = []

sheet["A1"] = "id"
sheet["B1"] = "city"
sheet["C1"] = "state"

count = 2
for l in cities:
	sheet["A${count}".format(count=count)] = l[0]
	sheet["B${count}".format(count=count)] = l[1]
	sheet["C${count}".format(count=count)] = l[2]
	count = count + 1
print("count: ", count)
workbook.save(filename="cities.xlsx")