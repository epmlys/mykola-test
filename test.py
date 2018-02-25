""" Tests tricks for Python 2.7 """


def print_loals():
    print 'Locals: \n {}'.format(locals())

print_loals()

class Alpha(object):
    """ This is good class with 
    lot sof."""

    # init that shit
    def __init__(self):
        print 'init AAAA'
    
    def cars(self):
        pass

    def pay(slef):
        pass

    def dfdf(self):
        print_loals


a = Alpha()
print a

class C:

    def do():
        print 'class unbound method'

    def __new__(self):
        print 'New before init from C'

    def __init__(self):
        print 'Init of - {}'.format(self)
    
    def __repr__(self):
        return 'Class C'

    def meth(self):
        print 'Method 1'

    def meth(self, x=2):
        print 'Method 2 x = {}'.format(x)

print(C())

c = C()

C.meth(c, 3)


#  ---- Pizza Robot example

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_rise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print "{} does stuff".format(self.name)

    def __repr__(self):
        return "<Employee: name={}, salary={}>".format(self.name, self.salary)

class Chef(Employee):
    def work(self):
        print "{} makes food".format(self.name)

class PizzaRobot(Chef):
    def work(self):
        print "{} makes pizza".format(self.name)


bob = PizzaRobot("Bob", 50000)
print bob
bob.work()
bob.give_rise(0.20)
print bob

for cls in (Employee, Chef, PizzaRobot):
    obj = cls(cls.__name__)
    obj.work()


#  Piceria example

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print "{} orders pizza from {}".format(self.name, server)
    
    def pay(self, server):
        print "{} pays to {}".format(self.name, server)

class Oven:
    def bake(self):
        print "Oven bakes"

class PizzaShop:
    def __init__(self):
        self.server = Chef("Pat", 40000)
        self.chef = PizzaRobot("Bob", 5000)
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

print "----- strart Pizaa SHop day ----"
scene = PizzaShop()
scene.order("Nick")
print "............"
scene.order("Sandy")

# --- Processor example
class Processor:
    def __init__(self, reader, writter):
        self.reader = reader
        self.writter = writter

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writter.write(data)


    def converter(self, data):
        assert False, 'converted must be defined in subclass'

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


import sys
#up_conv = Uppercase(open("notes.txt"), sys.stdout)
#print ' ------------ Processing convertation -----'
#up_conv.process()


# --- pr3 scrapy spider
urls = [
    'https://www.polskieradio.pl/10/497/Artykul/1562240,Kluboteka-26122015-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1567980,Kluboteka-09012016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1570966,Kluboteka-16012016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1573828,Kluboteka-23012016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1577335,Kluboteka-30012016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1579608,Kluboteka-06022016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1582223,Kluboteka-13022016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1585560,Kluboteka-20022016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1588038,Kluboteka-27022016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1591329,Kluboteka-05032016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1599739,Kluboteka-26032016-2201',
    'https://www.polskieradio.pl/10/497/Artykul/1599743,Kluboteka-26032016-2301',
    'https://www.polskieradio.pl/10/497/Artykul/1602284,Kluboteka-02042016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1605316,Kluboteka-09042016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1608212,Kluboteka-16042016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1611519,Kluboteka-23042016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1616897,Kluboteka-07052016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1616901,Kluboteka-07052016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1619707,Kluboteka-14052016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1619712,Kluboteka-14052016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1624981,Kluboteka-28052016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1624986,Kluboteka-28052016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1627712,Kluboteka-04062016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1627716,Kluboteka-04062016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1633327,Kluboteka-18062016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1633333,Kluboteka-18062016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1636110,Kluboteka-25062016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1636115,Kluboteka-25062016-2300',
    'https://www.polskieradio.pl/10/497/Artykul/1640122,Kluboteka-02072016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1641399,Kluboteka-09072016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1646955,Kluboteka-23072016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1649467,Kluboteka-30072016-2205',
    'https://www.polskieradio.pl/10/497/Artykul/1652142,Kluboteka-06082016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1654885,Kluboteka-13082016-2155',
    'https://www.polskieradio.pl/10/497/Artykul/1657572,Kluboteka-20082016-2205',
    'https://www.polskieradio.pl/10/497/Artykul/1657572,Kluboteka-20082016-2205',
    'https://www.polskieradio.pl/10/497/Artykul/1660518,Kluboteka-27082016-2207',
    'https://www.polskieradio.pl/10/497/Artykul/1665124,Kluboteka-03092016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1669532,Kluboteka-17092016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1672365,Kluboteka-24092016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1675029,Kluboteka-01102016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1677728,Kluboteka-08102016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1680864,Kluboteka-15102016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1686590,Kluboteka-29102016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1689061,Kluboteka-05112016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1691498,Kluboteka-12112016-2205',
    'https://www.polskieradio.pl/10/497/Artykul/1694387,Kluboteka-19112016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1697124,Kluboteka-26112016-2203',
    'https://www.polskieradio.pl/10/497/Artykul/1702750,Kluboteka-10122016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1705688,Kluboteka-17122016-2204',
    'https://www.polskieradio.pl/10/497/Artykul/1715605,Kluboteka-24122016-2200',
    'https://www.polskieradio.pl/10/497/Artykul/1715606,Kluboteka-31122016-2200'
]


import requests
import re

def download_save(url):
    """ Finds mp3 link, downloads mp3 and saves file to disk."""
    resp = requests.get(url)
    mp3_re = re.search(r'\/\/.*.mp3', resp.content)
    furl = 'http:' + mp3_re.group(0)  # '//static.prsa.pl/3391c287-8f28-4b4a-a6a3-062018933e96.mp3'
    fname = resp.url.split(',')[1] + '.mp3'  # u'Funkadelia-29102017-1604'
    print 'Downloading file: {} ...'.format(furl)
    resp = requests.get(furl)
    with open(fname, 'wb') as f:
        f.write(resp.content)
        print 'Saved file: {}'.format(fname)
