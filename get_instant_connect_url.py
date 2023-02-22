#!/usr/bin/env python

import requests
import json
import os
import sys

authToken = os.getenv("AUTHTOKEN")
endPointUri1 = os.getenv("ENDPOINTURI1")
endPointUri2 = os.getenv("ENDPOINTURI2")
endPointUri3 = os.getenv("ENDPOINTURI3")
endPointUri4 = os.getenv("ENDPOINTURI4")
visitUri = os.getenv("VISITURI")
brokerUri = os.getenv("BROKERURI")

### GET VIRTUAL ROUNDING LINKS


def getInstantConnectUriRoom1():
    payload = json.dumps({
    "jwt": {
        "sub": "002b3d63-2bd4-41df-b659-6144b062f3d6",
        "flow": {
        "id": "sip-no-knock",
        "data": [
            {
            "uri": endPointUri1
            }
        ]
        }
    },
    "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
    "provideShortUrls": True,
    "verticalType": "hc", #set to "gen" for general instant connect or "hc" for healthcare, changes the webex meeting template. "start consultation vs start meeting"
    "loginUrlForHost": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {authToken}'
    }

    response = requests.request("POST", brokerUri, headers=headers, data=payload)

    resp_dict = response.json()
    


    values = dict();
    values['host'] = host
    values['guest'] = guest 
    return values;


def getInstantConnectUriRoom2():
    payload = json.dumps({
    "jwt": {
        "sub": "002b3d63-2bd4-41df-b659-6144b062f3d6",
        "flow": {
        "id": "sip-no-knock",
        "data": [
            {
            "uri": endPointUri2
            }
        ]
        }
    },
    "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
    "provideShortUrls": True,
    "verticalType": "hc", #set to "gen" for general instant connect or "hc" for healthcare, changes the webex meeting template. "start consultation vs start meeting"
    "loginUrlForHost": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {authToken}'
    }

    response = requests.request("POST", brokerUri, headers=headers, data=payload)

    resp_dict = response.json()
    
    for i in resp_dict['host']:
        host = visitUri + I['short']
    for i in resp_dict['guest']:
        guest = visitUri + I['short']

    values = dict();
    values['host'] = host
    values['guest'] = guest 
    return values;


def getInstantConnectUriRoom3():
    payload = json.dumps({
    "jwt": {
        "sub": "002b3d63-2bd4-41df-b659-6144b062f3d6",
        "flow": {
        "id": "sip-no-knock",
        "data": [
            {
            "uri": endPointUri3
            }
        ]
        }
    },
    "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
    "provideShortUrls": True,
    "verticalType": "hc", #set to "gen" for general instant connect or "hc" for healthcare, changes the webex meeting template. "start consultation vs start meeting"
    "loginUrlForHost": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {authToken}'
    }

    response = requests.request("POST", brokerUri, headers=headers, data=payload)

    resp_dict = response.json()
    
    for i in resp_dict['host']:
        host = visitUri + I['short']
    for i in resp_dict['guest']:
        guest = visitUri + I['short']

    values = dict();
    values['host'] = host
    values['guest'] = guest 
    return values;

def getInstantConnectUriRiles():
    payload = json.dumps({
    "jwt": {
        "sub": "002b3d63-2bd4-41df-b659-6144b062f3d6",
        "flow": {
        "id": "sip-no-knock",
        "data": [
            {
            "uri": endPointUri4
            }
        ]
        }
    },
    "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
    "provideShortUrls": True,
    "verticalType": "hc", #set to "gen" for general instant connect or "hc" for healthcare, changes the webex meeting template. "start consultation vs start meeting"
    "loginUrlForHost": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {authToken}'
    }

    response = requests.request("POST", brokerUri, headers=headers, data=payload)

    resp_dict = response.json()
    
    for i in resp_dict['host']:
        host = visitUri + I['short']
    for i in resp_dict['guest']:
        guest = visitUri + I['short']

    values = dict();
    values['host'] = host
    values['guest'] = guest 
    return values;

def getInstantConnectUriAllRooms():
    payload = json.dumps({
    "jwt": {
        "sub": "002b3d63-2bd4-41df-b659-6144b062f3d6",
        "flow": {
        "id": "sip-no-knock",
        "data": [
            {
            "uri": endPointUri1
            },
            {
            "uri": endPointUri2
            },
           {
            "uri": endPointUri3
            },
           {
            "uri": endPointUri4
            }
        ]
        }
    },
    "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
    "provideShortUrls": True,
    "verticalType": "hc", #set to "gen" for general instant connect or "hc" for healthcare, changes the webex meeting template. "start consultation vs start meeting"
    "loginUrlForHost": False
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {authToken}'
    }

    response = requests.request("POST", brokerUri, headers=headers, data=payload)

    resp_dict = response.json()
    
    for i in resp_dict['host']:
        host = visitUri + I['short']
    for i in resp_dict['guest']:
        guest = visitUri + I['short']

    values = dict();
    values['host'] = host
    values['guest'] = guest 
    return values;

#testing
#result = getInstantConnectUriAllRooms()

#print(result['host'])

#print("End Get Instant Rounding URL")
