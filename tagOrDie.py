import boto3

# get id from lambda event

# i-0a0f29c2e338fc66f is my sample

#identify instance
newInstance = client.describe_instances(InstanceIds = ["i-0a0f29c2e338fc66f"])
print newInstance

#get tags attached to instance
print newInstance["Reservations"][0]["Instances"][0]["Tags"]
#turn those into a dict
myTagDict = {}
for pair in newInstance["Reservations"][0]["Instances"][0]["Tags"]:
    myTagDict[pair["Key"]] = pair["Value"]
print myTagDict

#instantiate approved values:
approvedUsers = ("Wes", "Kate", "Bill")
approvedNames = ("Scarif", "Sandbox", "Jakku", "Stardust")
approvedDepts = ("Monk", "Cosmotology", "Dwellers", "Catnip", "R&D")

#check if required values are present in the dict
if "User" in myTagDict:
    # check if required values are valid
    if myTagDict["User"] in approvedUsers:
        print myTagDict["User"]
    else:
        print "User not valid"
else:
    print "No User Specified"
