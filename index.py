def name(ls):
    for element in ls:
        name= ""
        for value in element.itervalues():
            name+=value + " "
        print name
    
def name2(ls):
    for user,names in ls.iteritems():
        print user
        num_of_users=0
        for name in names:
            userName = ""
            num_of_users+=1
            length = 0
            for person in name.itervalues():
                length += len(person)
                userName+=person + " "
            print "{} - {} - {}".format(num_of_users, userName, length)
            
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# name(students)
name2(users)