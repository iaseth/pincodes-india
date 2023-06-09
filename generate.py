import csv
import json


CSV_PATH = "data/Locality_village_pincode_final_mar-2017.csv"

def main():
	pincode_rows = []
	with open(CSV_PATH, encoding="ISO-8859-1") as f:
		reader = csv.reader(f)
		next(reader, None)
		for row in reader:
			if len(row) == 6:
				pincode_rows.append(row)
				continue
			else:
				print(f"Line {len(pincode_rows)} is Not Ok!")
				break


	states = {}
	for row in pincode_rows:
		stateName = row[5]
		if not stateName in states:
			states[stateName] = {"stateName": stateName, "districts": {}}

		state = states[stateName]
		districts = state["districts"]
		districtName = row[4]
		if not districtName in districts:
			districts[districtName] = {"stateName": stateName, "districtName": districtName, "pincodes": []}

		district = districts[districtName]
		pincodes = district["pincodes"]
		pincodes.append(row[2])

	states = [states[x] for x in states]
	for state in states:
		state["districts"] = [state["districts"][x] for x in state["districts"]]

	for state in states:
		for district in state["districts"]:
			pincodes = sorted(district["pincodes"])
			district["pincodeStart"] = pincodes[0]
			district["pincodeEnd"] = pincodes[-1]
			del district["pincodes"]

	statesJson = {}
	statesJson["states"] = states
	states_json_path = "states.json"
	with open(states_json_path, "w") as f:
		json.dump(statesJson, f, indent="\t")
	print(f"Saved: {states_json_path}")


	districtsJson = {}
	districtsJson["districts"] = []
	for state in states:
		for district in state["districts"]:
			districtsJson["districts"].append(district)

	districts_json_path = "districts.json"
	with open(districts_json_path, "w") as f:
		json.dump(districtsJson, f, indent="\t")
	print(f"Saved: {districts_json_path}")


	print(f"Total rows found: {len(pincode_rows)}")
	pincodes = [x[2] for x in pincode_rows]
	pincodes = sorted(list(set(pincodes)))
	print(f"Unique pincodes found: {len(pincodes)}")

	jo = {}
	jo["pincodes"] = pincodes
	pincodes_json_path = "pincodes.json"
	with open(pincodes_json_path, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"Saved: {pincodes_json_path}")


if __name__ == '__main__':
	main()
