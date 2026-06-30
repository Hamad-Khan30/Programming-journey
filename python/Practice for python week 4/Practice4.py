import json
student={"Name":"Hamad khan", 
        "age":22, 
        "class":"CS-B",
        "subjects":["Phy", "Math", "Urdu", "English"]
        }

with open("student.json", "w") as f:
    json.dump(student, f)

with open("student.json","r") as f:
    Load = json.load(f)
print(Load["Name"], "Studied", Load["subjects"])


