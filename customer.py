'''
C1

ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom.full_name()  # "Tom Ford" という値を返す
'''


class Customer:
    def __init__(self,first_name,family_name):
        self.first_name=first_name.capitalize()
        self.family_name=family_name.capitalize()

    def full_name(self):
        return self.first_name + ' ' +self.family_name


ken = Customer(first_name="ken",family_name="tanaka")
tom = Customer(first_name="tom",family_name="ford")

ken.full_name()  
tom.full_name() 


'''
C2

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す
'''

class Customer:
    def __init__(self,first_name,family_name,age):
        self.first_name=first_name.lower()
        self.family_name=family_name.lower()
        self.age = age


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)



'''
C3

料金の計算ルール
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す
'''

class Customer:
    def __init__(self,first_name,family_name,age):
        self.first_name=first_name.lower()
        self.family_name=family_name.lower()
        self.age = age

    def entry_fee(self):
        if self.age < 20:
            return str(1000)
        elif 20 <= self.age < 65:
            return str(1500)
        else:
            return str(1200)


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

ken.entry_fee()
tom.entry_fee()
ieyasu.entry_fee()



'''
C4
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
'''

class Customer:
    def __init__(self,first_name,family_name,age):
        self.first_name=first_name
        self.family_name=family_name
        self.age = age

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        return self.first_name + ',' + self.family_name + ',' + str(self.age) + ',' + str(self.entry_fee())


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)


ken.info_csv() 
ken.info_csv()
ieyasu.info_csv()

