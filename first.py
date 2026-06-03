# a = 100
# sum = sum + 100
# sum += 100

'''
Operators:
Arithmetic Operators : + - * / % // ** : numerical
Assignment Operators : = += -= *= /= //= **= &= |= ^= <<= >>= : numerical
Comparison Operators : == != > >= < <=  : boolean
Logical Operators : and or not : boolean
Bitwise Operators : & | ^ ~ << >> : numerical
Identity Operators : is , is not : boolean
Member Operators : in , not in : boolean
'''

# lt =[10, 20, 30]
# lt[1] = 200
# print(lt)

# t =(10, 20, 30)
# t[1] = 200
# print(t)

# lt =[10, 20, 30]
# lt1 =[10, 20, 30]

# t =(10, 20, 30)
# t1 =(10, 20, 30)

# print(id(lt), id(lt1))
# print(id(t), id(t1))

# print(lt is not lt1)
# print(t is not t1)


# t2 =(10, 20, 30)
# print(10 not in t2)
# print(40 not in t2)


'''
COnditional Statements
if 
elif 
if-else 
nested if
'''


# if (b+c)>=a and (a+b)>=c and (a+c)>=b:
#     print("triangle formed")
# else:
#     print("triangle not formed")

# if (b+c)>=a:
#     if (a+b)>=c:
#         if (a+c)>=b:
#             print("triangle formed")
#         else:
#             print("triangle not formed")
#     else:
#         print("triangle not formed")
# else:
#     print("triangle not formed")

# n = 11
# if n%2==0:
#     print("divisible by 2")
# elif n%3==0:
#     print("divisible by 3")
# elif n%5==0:
#     print("divisible by 5")
# else :
#     print("not divisible by 2, 3, 5")


# wt = int(input("Enter the weight: "))
# if wt>0 and wt<=2000:
#     print("15 min")
# elif wt>2000 and wt<=4000:
#     print("25 min")
# elif wt>4000 and wt<=7500:
#     print("35 min")
# else:
#     print("OVERWEIGHT")

'''
Looping Statements
for :  range()  , for-each
while :
'''

# range(start, stop, step)
# start: 0,
# step : 1
# range(2,10,2): 2 4 6 8
# range(5,35,5)
# range(-10,-15,-3): -10 -13

# range(-20,-10,2)
# range(-10,-50,5)

# range(10)

# lt = [10,20,30,40,50]
# for i in range(5):  # 0 1 2 3 4
#     print(lt[i])

# for i in lt:
#     print(i)

# i = 0
# while i<10:
#     print(i)
#     i += 1

# print all the prime number between 10 to 50

# for j in range(10,51):
#     flag = True
#     for i in range(2,j):
#         if j%i == 0:
#             flag = False
#             break
#     if flag:
#         print(j,"prime")
#     else:
#         print(j,"composite")


'''
Collections in Python
List : mutable, can contain any data type, ordered, allows duplicates, []
Tuple : immutable, can contain any data type, ordered, allow duplicates, ()
Set : mutable, can contain any data type, unordered, no duplicates, {}
Dictionary : mutable, can contain any data type, key-value pairs,
             key must be unique, unordered, no duplicates, {}
'''

# lt = [10, 20, 30]
# print(lt[-2], lt[1])

# for i in range(-1,-4,-1):
#     print(lt[i])


# s = {78,908,345,234,7,67654,345566,75645,43}
# s1 = [1,2,3,3,2,1]
# print(s1)
# print(s)


# lt = []
# lt.append(10)
# lt.append(20)
# lt.append(30)
# print(lt)

# n = 4
# lt1=[]
# for i in range(n):
#     val = int(input())
#     lt1.append(val)
# print(lt1)

# nums = [4,1,2,1,2,4,3]

# def singleNumber( nums):
#     s = set(nums)
#     for i in s:
#         if nums.count(i) == 1:
#             return i
# print(singleNumber( nums))


# d = {}
# s = set()
# print(type(d))
# print(type(s))


# d = {
#     "name":"male",
#     "gender":"male",
#     "age": 10
# }
# print(d)

# d["contact"] = "9876543210"
# print(d)


# sort() : sort with-in the list
# nums.sorted() : return a new sorted list


'''
Object Oriented Programming

Class: a blueprint for creating objects.
Object: a real-world entity or concept.

4 pillars of OOPs:
1. Encapsulation: _var (protected, same class, same package) 
                , __var (private, only within the class)
2. Inheritance: a class can inherit properties from methods of 
                another class.
3. Polymorphism: a method can have different implementations for 
                 different objects.
4. Abstraction: - a class can have abstract methods, 
                which are not implemented in the class.
                - Subclasses must implement these methods.
                - Abstract methods are declared with the @abstractmethod decorator.
                - Abstract classes are declared with the @abstractclass decorator.
'''

# class Sample:
#     bank = "BOI"

#     def __init__(self,ac,bal):
#         self.account = ac
#         self.balance = bal

#     def func1(self, name, age=100):
#         print("balance:", self.balance, "name:", name, "age:", age)

# s =Sample(1001,10000000)
# s1 =Sample(1002,100)

# s.func1( age=27, name="Nikunj")
# s1.func1(name="Raj")
# print(s.bank, s1.bank)

# Encapsulation

# class Sample:
#     bank = "BOI"

#     def __init__(self,ac,bal):
#         self.__account = ac
#         self.balance = bal
    
#     def get_account(self):
#         return self.__account

#     def set_account(self, ac):
#         self.__account = ac

#     def __func2 (self):
#         print("private method func2()")

#     def func1(self, name, age=100):
#         self.__func2()
#         print("balance:", self.balance, "name:", name, "age:", age)

# s =Sample(1001,10000000)
# s1 =Sample(1002,100)

# s.func1( age=27, name="Nikunj")
# s1.func1(name="Raj")
# print(s.get_account(), s1.get_account())
# s.set_account(11)
# s1.set_account(22)

# print(s.get_account(), s1.get_account())

# class Sample:
#     bank = "BOI"

#     def __init__(self,ac,bal):
#         self.account = ac
#         self._balance = bal

#     def func1(self, name, age=100):
#         print("balance:", self._balance, "name:", name, "age:", age)

# s =Sample(1001,10000000)
# s1 =Sample(1002,100)

# s.func1( age=27, name="Nikunj")
# s1.func1(name="Raj")
# print(s._balance, s1._balance)


class Sample:
    bank = "BOI"

    def __init__(self,ac,bal):
        self.account = ac
        self._balance = bal

    def func1(self, name, age=100):
        print("balance:", self._balance, "name:", name, "age:", age)

class Mapple (Sample) :
    def __init__(self,ac,bal,branch):
        super().__init__(ac,bal)
        self.branch = branch

    def greet(self):
        print("Welcome to User")
        print("branch:", self.branch)
m = Mapple(11, 50000,"MIT")
m.greet()
m.func1("Nikunj", 27)