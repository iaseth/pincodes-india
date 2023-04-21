import csv
import json


CSV_PATH = "data/Locality_village_pincode_final_mar-2017.csv"

def main():
	pincode_rows = []
	with open(CSV_PATH, encoding="ISO-8859-1") as f:
		reader = csv.reader(f)
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
			states[stateName] = {"districts": {}}

		state = states[stateName]
		districts = state["districts"]
		districtName = row[4]
		if not districtName in districts:
			districts[districtName] = {"pincodes": []}

		district = districts[districtName]
		pincodes = district["pincodes"]
		pincodes.append(row[2])

	for stateName in states:
		state = states[stateName]
		for districtName in state["districts"]:
			district = state["districts"][districtName]

			pincodes = sorted(district["pincodes"])
			district["pincodeStart"] = pincodes[0]
			district["pincodeEnd"] = pincodes[-1]
			del district["pincodes"]

	jo = {}
	jo["states"] = states
	districts_json_path = "districts.json"
	with open(districts_json_path, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"saved: {districts_json_path}")

	print(f"Total rows found: {len(pincode_rows)}")
	pincodes = [x[2] for x in pincode_rows]
	pincodes = list(set(pincodes))
	print(f"Unique pincodes found: {len(pincodes)}")


if __name__ == '__main__':
	main()
