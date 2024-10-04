
class employee():
    def __init__(self,name,id,salary,department,year_of_joining) :
        self.id=id
        self.name=name
        self.salary=salary
        self.department=department
        self.year_of_joining=year_of_joining
    def employee_name (self):
        return f'the name of  employee is : {self.name}'
    def employee_id (self):
        return f'the {self.name} id is : {self.id}'
    def employee_salary(self):
        return f'the salary for {self.id} is : $ {self.salary}'
    def employee_department (self):
        return f'the  {self.name } is department of : {self.department}'
    def employee_year_of_joining(self):
        return f'the {self.name } was joined in : {self.year_of_joining}'

employee1=employee('TEJASH','NIJA0222',14000,'PRODUCTION TEAM','MAY 21st 2024')
employee2=employee('ROHITH','NIJA0224',13000,'QULITY TEAM',2023)
employee1.employee_department()
print(employee1.employee_name())
print(employee1.employee_id())
print(employee1.employee_salary())
print(employee1.employee_department())
print(employee1.employee_year_of_joining())
print()
print('ANOTHER ONE PERSON')
print()
print(employee2.employee_name())
print(employee2.employee_id())
print(employee2.employee_salary())
print(employee2.employee_department())
print(employee2.employee_year_of_joining())
