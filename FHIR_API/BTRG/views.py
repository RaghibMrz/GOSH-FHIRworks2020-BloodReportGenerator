from django.http import HttpResponse
from fhir_parser import FHIR
import json


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def getAttributes(uuid, obType, requiredAttributes):
    fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)
    obs = fhir.get_patient_observations(uuid)
    count = 0
    attribList = []
    for ob in obs:
        if ob.type == obType:
            for i in ob.components:
                if count in requiredAttributes:
                    attribList.append(str(i))
                count += 1
    return attribList


def makeDict(fbcAttributes):
    myDict = {}
    for attribute in fbcAttributes:
        myDict[str(attribute.split(": ")[0])] = str(attribute.split(": ")[1])
    return myDict


def get_report(request, uid):
    fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)
    if request.method == 'GET':
        try:
            patient = fhir.get_patient(uid)
            fbcReqAttributes = ("laboratory", [2, 13, 5, 3, 15, 16, 17, 6])
            bpReqAttributes = ("vital-signs", [3, 4, 5])
            otherReqAttributes = ("laboratory", [22, 23, 24, 25, 26, 27, 28, 33, 55])
            fbcAttributes = getAttributes(uid, fbcReqAttributes[0], fbcReqAttributes[1])
            bpAttributes = getAttributes(uid, bpReqAttributes[0], bpReqAttributes[1])
            otherAttributes = getAttributes(uid, otherReqAttributes[0], otherReqAttributes[1])
            myDict = {
                'UID': patient.uuid,
                'Name': patient.name.full_name,
                'Address': str(patient.addresses[0]),
                'Full-Blood Count Attributes': makeDict(fbcAttributes),
                'Blood Pressure Values': makeDict(bpAttributes),
                'Other blood readings': makeDict(otherAttributes)
            }
            response = json.dumps(myDict)
            return HttpResponse(response, content_type='text/json')
        except ConnectionError:
            response = json.dumps([{'Error': 'No patient found'}])
            return HttpResponse(response, content_type='text/json')
