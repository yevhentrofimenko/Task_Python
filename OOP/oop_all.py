class Department(object):
    def __init__(self, list_managers):
        self.list_managers = list_managers

    def print_list_managers(self):
        for i in self.list_managers:
            print(i.list_of_managers())

    def give_salary(self):
        if (self.experiance > 2):
            self.salary += 200
        elif (self.experiance > 5):
            self.salary = self.salary * 1.2 + 500
        elif(self.__class__ == Designer):
            self.salary *= self.coef_effect
        elif(self.__class__ == Manager):
            if(len(self.team)>5):
                self.salary += 200
            elif(len(self.team) > 10):
                self.salary += 300
            elif(float(len(self.team))/2 < float(self.count_of_developers())):
                self.salary *= 1.1
        print('%s %s:\ngot salary: %s$' % (self.first_name, self.second_name, self.salary))


class Emploee(Department):
    def __init__(self, first_name, second_name, salary, experiance, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experiance = experiance
        self.manager = manager

    def __str__(self):
        return ('%s %s,\nmanager: %s,\nexperiance:%s')%(self.first_name,
                                                        self.second_name,
                                                        self.manager,
                                                        self.experiance)

class Developer(Emploee):
    def __init__(self, first_name, second_name, salary, experiance, manager):
        Emploee.__init__(self, first_name, second_name, salary, experiance, manager)

class Designer(Emploee):
    def __init__(self, first_name, second_name, salary, experiance, manager, coef_effect):
        Emploee.__init__(self, first_name, second_name, salary, experiance, manager)
        self.coef_effect = coef_effect

class Manager(Emploee):

    def __init__(self, first_name, second_name, salary, experiance , manager, team):
        Emploee.__init__(self, first_name, second_name, salary, experiance, manager)
        self.team = team

    def list_of_managers(self):
        team_list = []
        for i in self.team:
            team_list.append(i.first_name)
        return '%s Team: %s'%(self.first_name, team_list)

    def count_of_developers(self):
        dev = 0
        for i in self.team:
            if(i.__class__ == Developer):
             dev += 1
        return dev


dev1 = Developer('Jack','Nickolson', 500, 2, 'Kristin')
dev2 = Developer('Nini','Miras', 1400, 5, 'Kristin')
dev3 = Developer('Rick','Strange', 1000, 3, 'Kristin')
dev4 = Developer('Rick','Strange', 1000, 3, 'Kristin')
dev5 = Developer('FF','Nickolson', 500, 4, 'Julia')
dev6 = Developer('KK','Miras', 400, 2, 'Julia')
des = Designer('Mira', 'Polson', 500, 2, 'Lili', 0.3)
des1 = Designer('Lesli', 'Weson', 1400, 5, 'Lili', 0.7)
manager = Manager('Lili', 'Krabs', 500, 2, 'Lili', [dev1, dev2, dev3, des, des1, dev3])
manager1 = Manager('Julia', 'Krabs', 500, 2, 'Julia', [dev5, dev6])

# print(des1)
# dev1.give_salary()
# des.give_salary()
# print(manager.count_of_developers())
# manager.give_salary()
# manager.list_of_managers()
dep = Department([manager1, manager])
dep.print_list_managers()

# 2) -----------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def put(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    def delete(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def size(self):
        size = 1
        p = self.head
        if p != None:
            while p.next != None:
                size +=1
                p = p.next
        return size

    def get(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    print(p.data)
                p = p.next
            if (p.data == k):
                print(p.data)
        return None

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s



# l = LinkedList()
#
# l.put('a')
# l.put('b')
# l.put('c')
# l.get('b')
# print(l.size())
# print(l)
# l.delete(l.search('b'))
# print(l)
# print(l.size())
