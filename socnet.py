class User:
    def __init__(self, name, id_num):
        self.name = name
        self.connections = []
        self.id_num = id_num
    def add_connection(self, connect):
        self.connections.append(connect)
    def get_connections(self):
        return self.connections
class Network:
    def __init__(self):
        self.users = []
    def add_users(self, user):
        new_id = len(self.users)
        u = User(user, new_id)
        self.users.append(user)
    def get_users(self):
        return self.users
    def id_find(self):
        
    # write a function that will find the ID of



def main():
    initial = "What would you like to do?\n\tAdd a user (u), print users (p),\n\tadd connections (c),print connections (pc),\n\tquit (q)? \n\t"
    done = False
    net = Network()
    while not done:
        user_input = input(initial)
        if user_input == "u":
            x = input("What username?\t")
            net.add_users(x)
        if user_input == "p":
            userList = net.get_users()
            for eachUser in userList:
                print(eachUser.name)
        if user_input == "c":
            x = input("First Username:\t")
            y = input("Second Username: ")
            for i in range(len(net.users)):
                if net.users[i].name == x:
                    ne.add_connection(y)
                    y.add_connection(x)

        if user_input == "pc":
            for eachConnection in connections():
                print(eachConnection.uname)
        if user_input == "q":
            quit()
            done = True
main()
