# laiba haroon
#sp24-bba-113
# assignment 3


# 1. Simple Function
def welcome_message():
    print("Welcome to the Student Registration System!")

welcome_message()


# 2. Function with Parameter (positional)
def greet_student(name):
    print(f"Hello, {name.title()}! Let's get you registered.")

greet_student("zainab")


# 3. Positional Arguments
def register_student(name, course):
    print(f"{name.title()} has registered for the {course.upper()} course.")

register_student("zainab", "python")


# 4. Keyword Arguments
register_student(course="ai", name="hamza")


# 5. Default Values
def register_student_v2(name, course="Python"):
    print(f"{name.title()} has registered for the {course.upper()} course.")

register_student_v2("saad")  
register_student_v2("fatima", "data science")  

# 6. Return Values
def create_email(name):
    email = f"{name.lower()}@university.com"
    return email

student_email = create_email("Ahsan")
print("Generated Email:", student_email)


# 7. Optional Argument
def get_full_name(first, last, middle=""):
    if middle:
        return f"{first} {middle} {last}".title()
    else:
        return f"{first} {last}".title()

print(get_full_name("fatima", "ali"))
print(get_full_name("fatima", "ali", "bano"))


# 8. Return Dictionary
def build_student_profile(name, age=None):
    profile = {"name": name.title()}
    if age:
        profile["age"] = age
    return profile

print(build_student_profile("osman", age=21))


# 9. Function with a While Loop
def get_username(first, last):
    return f"{first} {last}".title()


# 10. Passing a List
def greet_all_students(names):
    for name in names:
        print(f"Hello, {name.title()}! Welcome.")

students = ["usman", "fatima", "nimra"]
greet_all_students(students)


# 11. Modifying a List
def process_registration(pending, confirmed):
    while pending:
        current = pending.pop()
        print(f"Registering {current.title()}")
        confirmed.append(current)

def show_registered(confirmed):
    print("Registered Students:")
    for name in confirmed:
        print(name.title())

pending_students = ["omer", "danish", "maria"]
confirmed_students = []

process_registration(pending_students[:], confirmed_students)
show_registered(confirmed_students)


# 12. Preventing List Modification (using [:])
print("Original Pending List:", pending_students)


# 13. *args (Arbitrary Arguments)
def enroll_courses(*courses):
    print("Student enrolled in the following courses:")
    for course in courses:
        print("-", course)

enroll_courses("Math", "AI", "Web Development")


# 14. Mixed Positional and *args
def enroll_student(name, *courses):
    print(f"\n{name.title()} enrolled in:")
    for course in courses:
        print("-", course)

enroll_student("bilal", "Python", "Cybersecurity")


# 15. **kwargs (Arbitrary Keyword Arguments)
def student_info(name, **details):
    details["name"] = name
    return details

info = student_info("laiba", age=20, department="CS", semester=3)
print(info)


