counties = ["Arapahoe", "Denver", "Jefferson"]

counties[0]
print(counties[2])
print(counties[-1])
len(counties)
counties[0:2]
counties.append("El Paso")
counties
#To specify where in a list to add a new item, select the location with an index
#by using the following syntax, list.insert(index, obj)

counties.insert(2, "El Paso")
counties.remove("El Paso")
counties
counties.pop(2)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict['Arapahoe']
voting_data = []
voting_data.append({"county" : "Arapahoe", "registered_voters" : 422829})
voting_data.append({"county" : "Denver", "registered_voters" : 463353})
voting_data.append({"county" : "Jefferson", "registered_voters" : 432438})
voting_data

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

