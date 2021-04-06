# Name - Anjanay Raina
# Roll No - 2020494
import a2d as a
import json

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
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
r=input("Enter the name or path of the file:")
records = read_data_from_file(r)

print('''Type 1 to run filter_by_first_name
Type 2 to run by last name
Type 3 to run by full name
Type 4 to run by age range
Type 5 to run by gender
Type 6 to run by adddress
Type 7 to run alumini
Type 8 to run topper of each institute
Type 9 to run blood donos
Type 10 to run Get common friends
Type 11 to run Is Related
Type 12 to run Delete id
Type 13 to run Add friend
Type 14 to run Remove friend
Type 15 to run Add education
Type -1 to exit the loop''')

# Write the code here for creating an interactive program
i=0
while True:
    n=int(input('Enter Your The function to be executed:'))
    if n==-1:
        exit()
    elif n==1:
        first_name=input("Enter the first name:")
        first_name = first_name.capitalize()
        cnt = []
        for i in range(len(records)):
            if (records[i]["first_name"] == first_name):
                cnt.append(records[i]["id"])
        print(cnt)
    elif n==2:
        last_name=input('Enter the last name:\t')
        ls=a.filter_by_last_name(records, last_name)
        print(ls)
    elif n==3:
        full_name=input('Enter the full name:\t')
        fun=a.filter_by_last_name(records, full_name)
        print(fun)
    elif n==4:
        min_age=int(input('Enter the minimum age:\t'))
        max_age=int(input('Enter the minimum age:\t'))
        age=a.filter_by_age_range(records, min_age, max_age)
        print(age)
    elif n==5:
        gender=a.count_by_gender(records)
        print(gender)
    elif n==6:
        dictionary={}
        hno=input('Enter house no:')
        b=input('Enter block:')
        t=input('Enter Town:')
        c=input('Enter city:')
        s=input('Enter state:')
        pin=input('Enter pincode:')

        if len(hno)>0:
            dictionary['house_no']=hno
        if len(b)>0:
            dictionary['block']=b
        if len(t)>0:
            dictionary['town']=t
        if len(c)>0:
            dictionary['city']=c
        if len(s)>0:
            dictionary['state']=s
        if len(pin)>0:
            dictionary['pincode']=int(pin)
        add=a.filter_by_address(records, dictionary)
        print(add)

    elif n==7:
        institute_name=input('Enter the institute name:')
        ins=a.find_alumni(records, institute_name)
        print(ins)

    elif n==8:
        tpr=a.find_topper_of_each_institute(records)
        print(tpr)

    elif n==9:
        receiver_person_id=int(input('Enter thr reciever person id:'))
        b=a.find_blood_donors(records, receiver_person_id)
        print(b)

    elif n==10:
        list_of_ids=[]
        while True:
            inp=input('Enter the ids (Leave blank to stop):')
            if inp=='':
                break
            else:
                list_of_ids.append(inp)

        cmn=a.get_common_friends(records, list_of_ids)
        print(cmn)

    elif n==11:
        person_id_1=int(input('Enter ID of person 1:'))
        person_id_2 = int(input('Enter ID of person 2:'))
        related=a.is_related(records, person_id_1, person_id_2)
        print(related)


    elif n==12:
        person_id=int(input('Enter the person id:'))
        d=a.delete_by_id(records, person_id)
        print(d)

    elif n==13:
        person_id=int(input('Enter the person id:'))
        friend_id=int(input('Enter the friend id:'))
        afr=a.add_friend(records, person_id, friend_id)
        print(afr)

    elif n==14:
        person_id=int(input('Enter the person id:'))
        friend_id=int(input('Enter the friend id:'))
        rem=a.remove_friend(records, person_id, friend_id)
        print(rem)

    elif n==15:
        person_id=int(input('Enter the person id:'))
        institute_name=input('Enter the institue name:')
        ongoing=(input('Enter ongoing:'))
        percentage=input('Enter the percentage:')
        education=a.add_education(records, person_id, institute_name, ongoing, percentage)
        print(education)
    print(f"Loop {i} ended")
    i+=1
print()