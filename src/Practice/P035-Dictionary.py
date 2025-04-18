#Dictionary
# unordered collection of data with Key and value

student_info = { "name" : "Alex",
                  "age" : 34,
                  "address" : "HYD"
               }

print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

#-------------------------------------------
#Other way of using dictionary
stud_info = dict( name ="Alex", age = 34, address = "HYD")

print(stud_info)
print(stud_info["name"])
print(stud_info["age"])
print(stud_info["address"])

#-------------------------------------------
#Multiple values of a key in dictionary
st_info = { "name" : "Alex",
                  "age" : 34,
                  "address" : {
                      "home_address" : "HYD",
                      "office_address" : "TN"
                                   }
               }

print(st_info)
print(st_info["name"])
print(st_info["age"])
print(st_info["address"])
