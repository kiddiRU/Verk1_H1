print()
a = 0
while a != "q":
    print("\n" + '''    - - -User Path- - -
    Admin Page [b ap] -> Manage Tournaments [b mt] -> Manage Inactive Tournament [b mut]
    ————————————————————————————————————————————————————————————————————————————
                                    Edit Tournament
    ————————————————————————————————————————————————————————————————————————————
    - - - - - - - - - - - - - -  - -Tournament Name- - - - - - - - - - - - - - - - -

    Date: yyyy mm dd - yyyy mm dd
    Venue: 123 placename, cityname
    Contact Info:
        Email: somth@somth.com
        Phone number: 1234567

    ————————————————————————————————————————————————————————————————————————————
    1 Edit Time / Date
    2 Edit Info
    b Back
    ————————————————————————————————————————————————————————————————————————————
    Choose Action:
    ————————————————————————————————————————————————————————————————————————————''')


    a = input("    ")


    if a == "b ap":
        print("\n" + '''Admin Page
    —————————————
    1 Create Tournament
    2 Manage Tournaments
    3 Create Club
    b Back
    —————————————
    Choose Action:
    —————————————''')
        a = input("    ")

    elif a == "b mt":
        print("\n" + '''Manage Tournaments
——————————————————
- - - -List Of Tournaments - - - -

~~~~~~~~~~~
~~~~~~~~~~~
~~~~~~~~~~~
TheMuppetsVsDocHopper
~~~~~~~~~~~
~~~~~~~~~~~
——————————————————
Choose A Tournament To Manage:''')
        a = input("    ")


    elif a == "b" or a == "b mut":
        print("\n" + '''Manage Inactive Tournaments
——————————————————
- - -TheMuppetsVsDocHopper- - -

1 Manage Teams
2 Publish
3 Edit Tournament
b Back
——————————————————
Choose Action:
——————————————————''')
        
        a = input("    ")





