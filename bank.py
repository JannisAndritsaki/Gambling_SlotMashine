#This will be the Bank, where the player's money will be saved

class Bank:
    __instance = None;
    def __init__(self, balance):
        self.balance = balance;
    balance = 0;

    def __init__(self):
        if Bank.__instance != None:
            raise Exception("There can only be one Bank")
        else:
            Bank.__instance = self

    def get_instance():
        if Bank.__instance == None:
            Bank();
        return Bank.__instance;

    

    def add_money(amount, self):
        self.balance + amount;


    def remove_money(amount, self):
        self.balance - amount;


    def show_amount(amount, self):
        print(self.amount);
