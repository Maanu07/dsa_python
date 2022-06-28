#Oops in python
#Whenver i am creating a method inside a class, the first parameter must be 'self'
#Every object of a class has its own space in the memory 
#The size of the object is decided by the number of variables and size of each variable
#Two types of variables in a class => 1.Instance variable  2.Class variable(static variable)
#Instance variable is only accessed using the instance/object, we cannot use class to access instance variable
#Class variable is used when we want to have a common property value for every objects
#There are 3 types of methods in a class => 1.Instance method  2.Class method  3.Static method 
#Instance method are of 2 types => 1.accessor methods  2.mutator methods
#Static method is not used with instance or class variables 
#Class inside a class(inner class)


""" class Employee:
  'this is a employee class'  #docstring(brief description of class)
  company_name='Facebook'   #class variable 
  def __init__(self):
    self.name='Ashish'
    self.age=21
    #creating object of inner class 
    self.lap=self.Laptop()
  
  def display(self):
    print(Employee.company_name,self.company_name)

  @classmethod                   #decorator 
  def show(cls):     #use cls with the class method
    print(cls.company_name)

  @staticmethod
  def info():
    print('This is a employee class and i am a static method...')


  class Laptop:
    def __init__(self):
      self.brand='Dell'
      self.cpu='i7'
      self.ram=8
  
    def show(self):
      print(self.brand,self.cpu,self.ram) """

    


""" e1=Employee()
e2=Employee()
# e1.company_name='Apple'
# e1.lap.show()
# lap1=Employee.Laptop()
# lap1.show()
# Employee.info()
# Employee.show()
# print(Employee.__doc__) """


#MULTIPLE INHERITANCE
""" class Parent:
  def show(self):
    print('Parent show method')


class Parent2:
  def show(self):
    print('Parent2 show method')

class Child(Parent2,Parent):
  def show(self):
    print('Child show method')
    Parent.show(self)

# print(Child.__mro__)                  #mro => method resolution order
c=Child()
c.show() """



#MULTI LEVEL INHERITANCE 
""" class A:
  def Ashow(self):
    print('show method inside A')

class B(A):
    def Bshow(self):
      print('show method inside B')

class C(B):
  def show(self):
    print('show method inside C')

c=C()
c.show()
c.Bshow()
c.Ashow() """





#super() method represents the super class 
#super().__init__()  => calls super class init method 



""" class Vehicle:
  color='White'   #class atribute 

  def __init__(self,name,max_speed,mileage,capacity=50):
    self.name=name
    self.max_speed=max_speed
    self.mileage=mileage
    self.capacity=capacity


  def seating_capacity(self,capacity):
    return f"The seating capacity of a {self.name} is {capacity} passengers. "

  def fare(self):
    return self.capacity * 100

class Bus(Vehicle):
   def seating_capacity(self, capacity=50):
       return super().seating_capacity(capacity=50)

   def fare(self):
     bus_fare=super().fare()
     total_fare=.1 * bus_fare + bus_fare
     return total_fare

class Car(Vehicle):
  pass

# modelX=Vehicle(240,24)
busX=Bus('TATA',180,34)
# carX=Car('Tesla',240,16,4)
print(busX.fare())
print(type(busX))
# print(carX.color)
# print(busX.color)
# print(busX.seating_capacity())
# print(busX.name,busX.max_speed,busX.mileage) """



""" class Student:
  def __init__(self):
    self.name='Manas'
    self.age=21

s1=Student()
print(s1.name,s1.age)
del s1.name
print(s1.name) """




