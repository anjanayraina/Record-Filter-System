# Assignment - 2
# Name - Anjanay Raina
# Roll No - 2020494

import json

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
    '''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters:
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''

    with open(file_path, 'r') as data:
        records = json.load(data)


    return records



def filter_by_first_name(records, first_name):
    '''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

    first_name=first_name.capitalize()
    cnt=[]
    for i in range(len(records)):
        if(records[i]["first_name"]==first_name):
            cnt.append(records[i]["id"])

    return cnt



def filter_by_last_name(records, last_name):
    '''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
    last_name = last_name.capitalize()
    cnt = []
    for i in range(len(records)):
        if (records[i]["last_name"] == last_name):
            cnt.append(records[i]["id"])

    return cnt

def filter_by_full_name(records, full_name):
    '''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

    l = full_name.split(' ')
    if (" " not  in  full_name):
        cnt = []
        for i in range(len(records)):
            if (records[i]["last_name"] == "" and records[i]["first_name"] == l):
                cnt.append(records[i]["id"])

        return cnt

    l=full_name.split(' ')
    l[0]=l[0].capitalize()
    l[1] =l[1].capitalize()

    cnt = []
    for i in range(len(records)):
        if (records[i]["last_name"] == l[1] and records[i]["first_name"] == l[0]):
            cnt.append(records[i]["id"])

    return cnt

def filter_by_age_range(records, min_age, max_age):

    '''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
    cnt = []
    for i in range(len(records)):
        if (records[i]["age"] >= min_age and records[i]["age"]<=max_age):
            cnt.append(records[i]["id"])

    return cnt


def count_by_gender(records):
    '''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
    cnt = {"male":0,"female":0}
    for i in range(len(records)):
        if (records[i]["gender"] == "male"):
            cnt["male"]+=1
        if(records[i]["gender"] == "female"):
            cnt["female"]+=1
    return cnt

#this must be looked at again
def filter_by_address(records, address):
    '''
	Description: Filters the person records whose address matches the given address.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {}
				=> All records match this case

			Case 2: { "block": "AD", "city": "Delhi" }
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)

			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
    l={}
    cnt = []
    if(address==l):
        for i in range(len(records)):
            cnt.append({"first_name": records[i]["first_name"], "last_name": records[i]["last_name"]})
        return cnt
    for i in address:
        if (i == "house_no" or i == "pincode"):
            l[i]=address[i]
            continue
        l[i]=address[i].lower()
    for i in range(len(records)):
        for j in records[i]["address"]:
            if (j != "house_no" and j != "pincode"):
                records[i]["address"][j] = records[i]["address"][j].lower()
    c=0
    for i in records:
        c=0
        for j in l:
            if(l[j]==i["address"][j]):
                c+=1

        if (len(l) == c):
            cnt.append({"first_name": i["first_name"], "last_name": i["last_name"]})


    return cnt
''' if "block" in address:
        address["block"]=address["block"].lower()
        for i in records
    if "town" in address:
        s=""
        m=address["town"].split()
        for i in range(len(m)):
            s+=m[i].capitalize()
        address["town"] = address["block"].lower()

    if "city" in address:
        s=""
        m=address["city"].split()
        for i in range(len(m)):
            s+=m[i].capitalize()
        address["city"] = s
    if "state" in address:
        s=""
        m=address["state"].split()
        for i in range(len(m)):
            s+=m[i].capitalize()
        address["state"] = s
        
        '''


def find_alumni(records, institute_name):
    '''
	Description: Find all the alumni of the given institute name (case-insensitive).

	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
    institute_name=institute_name.lower()

    cnt = []
    for i in range(len(records)):
        for j in range(len(records[i]["education"])):
            if ((records[i]["education"][j]["institute"].lower() == institute_name) and (not records[i]["education"][j]["ongoing"]) ):
                cnt.append({"first_name": records[i]["first_name"], "last_name": records[i]["last_name"], "percentage":records[i]["education"][j]["percentage"]})
    return cnt




def find_topper_of_each_institute(records):
    '''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs.
	The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''

    tpr={}
    tprid={}
    d={}
    for i in records:
        for j in i["education"]:
            clg=j["institute"]
            if (not j["ongoing"]):
                if clg in tpr:
                    if tpr[clg]<j["percentage"]:
                        tprid[clg]=i["id"]
                        tpr[clg]=j["percentage"]
                else:
                    tpr[clg]=j["percentage"]
                    tprid[clg]=i["id"]



    return tprid



def find_blood_donors(records, receiver_person_id):
    '''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note:
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
    if(receiver_person_id<0 or receiver_person_id>199):
        return {}

    ref={"A":["A","O"],"B":["B","O"],"AB":["AB","A","B","O"],"O":["O"]}
    d={}

    m =records[receiver_person_id]["blood_group"]

    if m ==None:
        return {}
    a = ref[records[receiver_person_id]["blood_group"]]
    for i in records:
        if (i["id"] == receiver_person_id):
            continue
        if (i["blood_group"] in ref[m]):
            d[i["id"]] = i["contacts"]

    return d



def get_common_friends(records, list_of_ids):
    for i in list_of_ids:
        if (i < 0 or i > 199):
            return []

    def common(x,y):
        z=[]
        for b in y:
            if b in x:
                z.append(b)
        return z



    '''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
    if(list_of_ids==[]):
        return []
    cmn={}
    temp={}
    cmn=(records[list_of_ids[0]]["friend_ids"])

    for i in list_of_ids:
        cmn=common(cmn,records[i]["friend_ids"])

    l=[]
    l.extend(cmn)
    return l


def is_related(records, person_id_1, person_id_2):
    if (person_id_2<0 or person_id_2>199 or person_id_1<0 or person_id_1>199):
        return False
    '''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D)
	'''
    d={}
    if(person_id_2==person_id_1):
        return False
    for i in ((records[person_id_1]["friend_ids"])):

        if (person_id_2 in records[i]["friend_ids"]):
            return True
        for j in ((records[i]["friend_ids"])):

            if (person_id_2 in records[j]["friend_ids"]):
                return True
            for k in ((records[j]["friend_ids"])):

                if (person_id_2 in records[k]["friend_ids"]):
                    return True
                for l in ((records[k]["friend_ids"])):

                    if (person_id_2 in records[l]["friend_ids"]):
                        return True
                    for n in ((records[l]["friend_ids"])):

                        if (person_id_2 in records[n]["friend_ids"]):
                            return True
                        for q in ((records[n]["friend_ids"])):

                            if (person_id_2 in records[q]["friend_ids"]):
                                return True
                            for z in ((records[q]["friend_ids"])):

                                if (person_id_2 in records[z]["friend_ids"]):
                                    return True
                                for a1 in ((records[z]["friend_ids"])):

                                    if (person_id_2 in records[a1]["friend_ids"]):
                                        return True
                                    for a2 in ((records[a1]["friend_ids"])):

                                        if (person_id_2 in records[a2]["friend_ids"]):
                                            return True
                                        for a3 in ((records[a2]["friend_ids"])):

                                            if (person_id_2 in records[a3]["friend_ids"]):
                                                return True

    return False





def delete_by_id(records, person_id):
    '''
	Description: Given a person ID, this function deletes them from the records.
	Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list.
	If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
    if(person_id<0 or person_id>199):
        return records
    temp=-1
    for i in records:
        if (person_id == i["id"]):
            records.remove(i)
            break

    for i in range(len(records)):
        if( person_id in records[i]["friend_ids"]):
            records[i]["friend_ids"].remove(person_id)
    return records
'''
    l=[]
    
    x=len(records)
    for i in range(x):
        if(records[i]["id"]==person_id):
            temp=i
            continue
        else:
            q=len(records[i]["friend_ids"])
            for j in range(q):
                if(records[i]["friend_ids"][j]==person_id):
                    records[i]["friend_ids"].remove(records[i]["friend_ids"][j])
            l.append(records[i])
    return l

'''

def add_friend(records, person_id, friend_id):
    if (person_id==friend_id):
        return records
    '''
	Description: Given a person ID and a friend ID, this function makes them friends of each other.
	If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
    if(person_id<0 or person_id>199 or friend_id<0 or friend_id>199 ):
        return records
    for i in range(len(records)):
        if(records[i]["id"]==person_id):
            if (friend_id not in records[i]["friend_ids"]):
                records[i]["friend_ids"].append(friend_id)

        if(records[i]["id"]==friend_id):
            if(person_id not in records[i]["friend_ids"]):
                records[i]["friend_ids"].append(person_id)

    return records

def remove_friend(records, person_id, friend_id):

    '''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
    if (person_id < 0 or person_id > 199 or friend_id < 0 or friend_id > 199):
        return records

    for i in range(len(records)):
        if(records[i]["id"]==person_id):
            if (friend_id  in records[i]["friend_ids"]):
                records[i]["friend_ids"].remove(friend_id)
        if(records[i]["id"]==friend_id):
            if(person_id in records[i]["friend_ids"]):
                records[i]["friend_ids"].remove(person_id)

    return records


def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
	Description: Adds an education record for the person with the given person ID.
	The education record constitutes of insitute name, the person's percentage and if that
	education is currently ongoing or not. Please look at the format of an education field from the PDF.
	If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
    if(person_id<0 or person_id>199):
        return records
    d={}
    for i in range(len(records)):
        if (records[i]["id"] == person_id):
            if(institute_name!=None):
                d["institute"]=institute_name
            if(ongoing!=None):
                d["ongoing"] = ongoing
            if(percentage!=0):
                d["percentage"]= percentage

            records[i]["education"].append(d)

    return records


n=read_data_from_file()
print(filter_by_first_name(n,""))
#print(find_blood_donors(n, 0))
#print(find_topper_of_each_institute(n))
print(get_common_friends(n,[1,2,3,1000]))

