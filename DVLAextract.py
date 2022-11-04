import requests

formatlist = []
title_list = []
data_list = []

regnum = ''
req_data = ['registrationNumber', 'make', 'colour', 'fuelType', 'yearOfManufacture']

reg = ''
make = ''
fuel = ''
colour = ''
year = ''
textdetails = ''
APIKey = open('APIKey.txt', 'r').read()


def requestvrn(vrn):
    global regnum
    regnum = str(vrn)

def getDVLAdata():
    #Test Environment    
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    
    payload = "{\n\t\"registrationNumber\": \"%s\"\n}" % (regnum)
    headers = {
      'x-api-key': APIKey,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    global formattedDVLA
    formattedDVLA = response.text.encode('utf8').decode('utf8').replace('"','').replace('{','').replace('}','').split(',')
    #print(formattedDVLA)



def append_data_list():
    global ec
    ec=200
    for i in range(len(formattedDVLA)):
        x = formattedDVLA[i-1]
        a = x.find('code:')
        if a == 0:
            b = x.find(':')
            ec = x[b+1:len(x)]
    if ec == 200:
        for x in range(len(req_data)):
            for i in range(len(formattedDVLA)):
                b = formattedDVLA[i-1].find(req_data[x-1])
                if b == 0:
                    a = formattedDVLA[i-1]
                    lTitle = a[0:a.find(':')]
                    lData = a[a.find(':')+1:len(a)]
                    global title_list
                    title_list.append(lTitle)
                    global data_list
                    data_list.append(lData)
    else:
        print('error')

def clear_list():
    global title_list
    title_list.clear()
    global data_list
    data_list.clear()

def transpose_data():
    global reg
    reg = data_list[title_list.index('registrationNumber')]
    global make
    make = data_list[title_list.index('make')]
    global fuel
    fuel = data_list[title_list.index('fuelType')]
    global colour
    colour = data_list[title_list.index('colour')]
    global year
    year = data_list[title_list.index('yearOfManufacture')]
    global textdetails
    textdetails = 'Please check the following is correct:\n\nRegistration: %s\nMake: %s\nColour: %s\nYear: %s\nFuel: %s' % (reg,make,colour,year,fuel)
    
def printData():
    if ec == 200:
        for i in range(len(req_data)):
            print('%s %s' % (title_list[i-1],data_list[i-1]))