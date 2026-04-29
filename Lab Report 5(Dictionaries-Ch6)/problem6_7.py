first_person_info={'first_name':'sdratul','last_name':'muntaha','city':'feni'}
second_person_info={'first_name':'amrin','last_name':'hossain','city':'bogura'}
third_person_info={'first_name':'nabaneeta','last_name':'bhowmik','city':'noakhali'}

people=[first_person_info,second_person_info,third_person_info]
for information in people:
    print(f"\nFull Name: {information['first_name'].title()} {information['last_name'].title()} \nCity: {information['city'].title()}")

