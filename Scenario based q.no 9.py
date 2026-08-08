class Course:
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
        self.category = self.get_category()

    def get_category(self):
        if self.duration <= 6:
            return "Short-Term"
        else:
            return "Long-Term"


class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print("Course added successfully.")

    def display_courses(self):
        print("\n===== Course Details =====")

        if not self.courses:
            print("No courses available.")
            return

        for course in self.courses:
            print("Course Name:", course.course_name)
            print("Duration:", course.duration, "months")
            print("Fee: ₹", course.fee)
            print("Category:", course.category)
            print("------------------------")


# Create Institute object
institute = Institute()

while True:
    print("\n===== Course Management System =====")
    print("1. Add Course")
    print("2. Display All Courses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        course_name = input("Enter course name: ")
        duration = int(input("Enter duration in months: "))
        fee = float(input("Enter course fee: ₹"))

        course = Course(course_name, duration, fee)
        institute.add_course(course)

    elif choice == "2":
        institute.display_courses()

    elif choice == "3":
        print("Thank you for using Course Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
