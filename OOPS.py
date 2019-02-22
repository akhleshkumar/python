class person:
    pass

p=person()
print(p)

class person:
    def say_hi(self):
        print('hello how are you')

p=person()
p.say_hi()

class person:
    def __init__(self,name):
                self.classname=name

    def say_hi(self):
        print('Hello my name is',self.classname)

p=person('akhlesh')
p.say_hi()

class robot:
    population=0
    def __init__(self,name):
        self.name=name
        print("(Initializing {})".format(self.name))
        robot.population+=1

    def die(self):
        print("{} is being destroyed".format(self.name))
        robot.population-=1

        if robot.population==0:
            print("{} was the last one".format(self.name))
        else:
            print("there are still {:d} robots working".format(robot.population))

    def say_hi(self):
        print("Greatings, my masters call me {}. ".format(self.name))

    @classmethod
    def how_many(cls):
        print("we have {:d} robots".format(cls.population))

driod1=robot("R2-D2")
driod1.say_hi()
robot.how_many()

driod2=robot("C-3PO")
driod2.say_hi()
robot.how_many()

driod1.die()
robot.how_many()

driod2.die()
robot.how_many()

#Inheritance

class schoolmember:
    def __init__(self,name, age):
        self.name=name
        self.age=age
        print('(Initialzied SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class teacher(schoolmember):
    def __init__(self, name, age, salary):
        schoolmember.__init__(self,name, age)
        self.salary=salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        schoolmember.tell(self)
        print('salary : {:d}'.format(self.salary))


class student(schoolmember):
    def __init__(self, name, age, marks):
        schoolmember.__init__(self,name, age)
        self.marks=marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        schoolmember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t=teacher('akhlesh',30,40000)
s=student('aman',6,75)

members=[t,s]
print()

for member in members:
    member.tell()

#File
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

f=open('poem.txt', 'w')
f.write(poem)
f.close()

f=open('poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line, end='')
f.close()

#pickle
import pickle
shoplistfile='shoplist.data'

shoplist=['apple','mango','carrot']
f=open(shoplistfile,'wb')

pickle.dump(shoplist, f)
f.close()

del shoplist

f=open(shoplistfile,'rb')
storedlist=pickle.load(f)
print(storedlist)

# Handling Exception
try:
    text=input('Enter Something --->')
except EOFError:
    print('why did you do an EOF on me')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You Entered {}'.format(text))

class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    text=input('Enter Something ----->')
    if len(text)<3:
        raise ShortInputException(len(text), 3)

except EOFError:
      print('Why did you do an EOF on me?')
except ShortInputException as ex:
      print(('ShortInputException: The input was ' +
'{0} long, expected at least {1}')
.format(ex.length, ex.atleast))
else:
     print('No exception was raised.')

