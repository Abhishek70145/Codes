
grades  = {
    "Hari": {"Maths":89 , "Science" : 87 } ,
    "Shyam": {"Maths":23 , "Science" : 47 } ,
    "Ram": {"Maths":64 , "Science" : 74 } 
}

def calculate_percentage (**grades):
    total = sum(grades.values())
    sub = len(grades)
    percentage = total / sub
    return percentage

for students , grades in grades.items():
    percentage =  calculate_percentage(**grades)
    print(f"{students}:{percentage}%")

