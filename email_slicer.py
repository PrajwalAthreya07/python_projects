#simple email slicer using python to get username and the domain address

#creating a variable that takes the input(email addess)
emailadd = input(f"\n please enter the email address \n").strip()

#slicing the emailadress into 2 parts,alphabets/numeric till @ is the email address and the the rest is the domain
username = emailadd[:emailadd.index('@')]
domain = emailadd[emailadd.index('@') + 1:]

#priting the output
print()
print(f"The username is : {username}")
print(f" The domain is  : {domain}")