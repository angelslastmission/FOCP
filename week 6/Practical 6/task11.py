names = ["Eric", "anna", "Sophie", "sam"] 
names.sort(key=lambda x: x.upper()) 
names_in_uppercase = [name.upper() for name in names] 
print(names_in_uppercase)  

