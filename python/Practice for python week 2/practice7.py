name="Abdullah"
def call():
    print(name)
print(name)
call()


def make_total():
    sub_total=100000
    return sub_total
print(make_total())


marks=[12,13,14,13,16,17,]
new_marks=[]
for i in marks:
    new_marks.append(i+2)
print(new_marks)


                 # Kitna index tak print krwaa chata ho
marks=[12,13,14,13,16,17,]
new_marks=[]
for i in marks[:3]:
    new_marks.append(i+2)
print(new_marks)

                 # Reduced comperhension
marks=[12,13,14,13,16,17,]
new_marks=[x+2 for x in marks]
print(new_marks)

                # find cube of even numbers


cube=[]
for i in range(11):
    if i % 2 == 0:
       cube.append(i**3)
print(cube)
        
cube=[i**3 for i in range(11) if i % 2 == 0]
print(cube)