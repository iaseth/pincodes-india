import districtsJson from './districts.json';
import statesJson from './states.json';
import pincodesJson from './pincodes.json';

interface DistrictType {
	stateName: string,
	districtName: string,
	pincodeStart: string,
	pincodeEnd: string
}

interface StateType {
	stateName: string,
	districts: DistrictType[]
}

export const states: StateType[] = statesJson.states;
export const districts: DistrictType[] = districtsJson.districts;
export const pincodes: string[] = pincodesJson.pincodes;
