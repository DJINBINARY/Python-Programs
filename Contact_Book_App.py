contacts = {}

while True:
    print("\n Contact Book App")
    print('1.Create Contact')
    print('2.View  Contact')
    print('3.Update Contact')
    print('4.Delete  Contact')
    print('5.Search  Contact')
    print('6.Count  Contact')
    print('7.Exit')

    choice = int(input("Enter your choice : "))
if choice == '1':
    name = input("Enter Your Name :")
    if name in contacts:
        print(f"Contact name {name} already Exists !")
    else:
        age = input("Enter age :")
        mobile_no = int(input("Enter your Mobile number :"))
        Email_id = int(input("Enter your Email id"))
        contacts[name] = {'age':int(age),'email':Email_id,'mobile':mobile_no}
        print(f"Contact Name{name} has been  !")

elif choice == '2':
    name : input("Enter contact name to view :")
    if name in contact:
        contact = contacts[name]
        print('Name: {')

