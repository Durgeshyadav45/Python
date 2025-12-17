student = {
    "name" : "durgesh",
    "age": 22,
    "course": "MCA"
}
print(student["name"])  # using key 


#adding and updating values single value
student["age"] = 23,
student["city"] = "delhi"

#miltiple value add and updates
student.update({
    "age": 23, #update value
    "course": "BBA",
    "city": "noida",  #add new value
    "phone": 97877899,
    "marks": 77.4
})
print(student)


