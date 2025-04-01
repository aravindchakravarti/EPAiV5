class Person:
    """
    Represents a generic person with basic attributes like name, age, and job.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        job (str): The job or occupation of the person.
    """
    def __init__(self, name, age, job):
        """
        Initializes a Person object with the given name, age, and job.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            job (str): The job of the person.
        """
        self.name = name
        self.age = age
        self.job = job

    def get_details(self):
        """
        Returns a formatted string with the person's details.

        Returns:
            str: A string containing the person's name, age, and job.
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"


class Student(Person):
    """
    Represents a student, inheriting from Person and adding a grade attribute.

    Attributes:
        grade (str): The grade of the student.
    """
    def __init__(self, name, age, job, grade):
        """
        Initializes a Student object with the given attributes.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            job (str): The job or occupation of the student (e.g., part-time work).
            grade (str): The grade of the student.
        """
        super().__init__(name, age, job)
        self.grade = grade

    def get_details(self):
        """
        Returns a formatted string with the student's details, including grade.

        Returns:
            str: A string containing the student's name, age, job, and grade.
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Grade: {self.grade}"


class Professor(Person):
    """
    Represents a professor, inheriting from Person and adding a courses attribute.

    Attributes:
        courses (list): A list of courses taught by the professor.
    """
    def __init__(self, name, age, job, courses):
        """
        Initializes a Professor object with the given attributes.

        Args:
            name (str): The name of the professor.
            age (int): The age of the professor.
            job (str): The job title of the professor.
            courses (list): A list of courses taught by the professor.
        """
        super().__init__(name, age, job)
        self.courses = courses

    def get_details(self):
        """
        Returns a formatted string with the professor's details, including courses.

        Returns:
            str: A string containing the professor's name, age, job, and courses.
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Courses: {self.courses}"


class Employee(Person):
    """
    Represents an employee, inheriting from Person and adding a department attribute.

    Attributes:
        department (str): The department where the employee works.
    """
    def __init__(self, name, age, job, department):
        """
        Initializes an Employee object with the given attributes.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            job (str): The job title of the employee.
            department (str): The department of the employee.
        """
        super().__init__(name, age, job)
        self.department = department

    def get_details(self):
        """
        Returns a formatted string with the employee's details, including department.

        Returns:
            str: A string containing the employee's name, age, job, and department.
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Department: {self.department}"


class StudentProfessor(Student, Professor):
    """
    Represents an individual who is both a student and a professor.

    Attributes:
        courses (list): A list of courses taught by the individual.
        grade (str): The grade of the individual as a student.
    """
    def __init__(self, name, age, job, courses, grade):
        """
        Initializes a StudentProfessor object with the given attributes.

        Args:
            name (str): The name of the individual.
            age (int): The age of the individual.
            job (str): The job title of the individual.
            courses (list): A list of courses taught by the individual.
            grade (str): The grade of the individual as a student.
        """
        # Initialize Person directly to avoid duplicate initialization
        Person.__init__(self, name, age, job)
        self.courses = courses
        self.grade = grade

    def get_details(self):
        """
        Returns a formatted string with details from both student and professor roles.

        Returns:
            str: A string containing the individual's name, age, job, courses, and grade.
        """
        return (f"Name: {self.name}, Age: {self.age}, Job: {self.job}, "
                f"Courses: {self.courses}, Grade: {self.grade}")


class Location:
    """
    Represents a physical location with a name and coordinates.

    Attributes:
        name (str): The name of the location.
        latitude (float): The latitude coordinate of the location.
        longitude (float): The longitude coordinate of the location.
    """
    __slots__ = ('name', 'latitude', 'longitude')

    def __init__(self, name, latitude, longitude):
        """
        Initializes a Location object with the given attributes.

        Args:
            name (str): The name of the location.
            latitude (float): The latitude coordinate of the location.
            longitude (float): The longitude coordinate of the location.
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        """
        Returns the coordinates of the location as a tuple.

        Returns:
            tuple: A tuple containing the latitude and longitude of the location.
        """
        return (self.latitude, self.longitude)
