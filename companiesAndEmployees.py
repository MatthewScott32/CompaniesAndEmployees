class Employee:
    def __init__(self, name, job_title, employement_start_date):
        self.name = name
        self.job_title = job_title
        self.employment_start_date = employement_start_date

class Company:
    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.industry_type =industry_type
        self.employees = list()

company_1 = Company("MattCo", "1st Avenue", "Real Estate")
company_2 = Company("Art Vandelay Inustries", "2nd Street", "Import/Export")

employee_1 = Employee("Jim", "Manager", "2020/01/17")
employee_2 = Employee("James", "Assistant Manager", "2020/01/16")
employee_3 = Employee("Jimmy", "Secretary", "2020/01/15")
employee_4 = Employee("Bill", "Janitor", "2020/01/14")
employee_5 = Employee("Will", "Security Guard", "2020/01/13")

company_1.employees.append(employee_1)
company_1.employees.append(employee_2)
company_2.employees.append(employee_3)
company_2.employees.append(employee_4)
company_2.employees.append(employee_5)

employee_string = ""
for employee in company_1.employees:
    employee_string += f"{employee.name} "  

for employee in company_1.employees:
    print(f'{employee.name} works at {company_1.name}, started on {employee.employment_start_date} and is a {employee.job_title}')

for employee in company_2.employees:
    print(f'{employee.name} works at {company_2.name}, started on {employee.employment_start_date} and is a {employee.job_title}')

for employee in company_1.employees:
    print(f"{company_1.name}'s employees are {employee_string}")