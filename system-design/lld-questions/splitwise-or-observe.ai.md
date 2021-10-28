# Splitwise | observe.AI

## 2. Splitwise | observe.AI

{% tabs %}
{% tab title="main.py" %}
```python
'''

User
---------uid
---------name
---------ledger : {to_whom: how_much}
---------add_expense()
---------get_balance()

Group
---------group_id
---------users : {user: ratio}

Expense
--------expense_id
--------payers {user_id:share}
--------spenders {user_id:share}

'''

class User:
    
    user_id_count = 1       # hack for temp testing
    
    def __init__(self, name,email_id='abc@zyx.com'):
        self.user_id = User.user_id_count
        self.name = name
        self.email_id = email_id
        self.user_ledger = dict()
        self.passbook = []
        User.user_id_count += 1
        self.initialize_ledger()
        
        
    def generate_user_id(self):
        # return uuid.uuid4()
        pass

    def initialize_ledger(self):
        self.ledger = {}
        
    def add_user_owes_expense(self,u,amount):
        if u not in self.user_ledger:
            self.user_ledger[u] = -amount
        else:
            self.user_ledger[u] -= amount
            
    def add_user_gets_expense(self,u,amount):
        if u not in self.user_ledger:
            self.user_ledger[u] = amount
        else:
            self.user_ledger[u] += amount        
            
    def print_ledger(self):
        for k,v in self.user_ledger.items():
            print(f'{k.user_id} => {v}')
    
    def get_balance(self):
        print(f'\n=============== Printing Balance for UserID: {self.user_id} ==========================\n')
        total_owe_amt = 0
        total_get_amt = 0
        for u,amt in self.user_ledger.items():
            if amt > 0:
                total_get_amt += amt
                print(f' \t User {u.user_id} has to pay sum of {abs(round(amt,2))} to User {self.user_id}')
            elif amt < 0:
                total_owe_amt += amt
                print(f' \t User {u.user_id} gets sum of {round(amt,2)} to User {self.user_id}')
        print(f'\n ============== User: {self.user_id} ows total ${round(total_owe_amt,2)} & has lent total ${round(total_get_amt,2)} =========== \n')

    def get_total_balance_for_user(self):
        return sum([v for _,v in self.user_ledger.items()])
    
    def add_entry_to_passbook(self,entry):
        self.passbook.append(entry)
    
    def show_passbook(self):
        print(f'===================== Showing passbook for user_id : {self.user_id} =================')
        for entry in self.passbook:
            print('\t',entry)

class Expense:
    expense_id_count = 1
    '''
    payer: who has paid 
    payee: owes the money to payer
    '''
    
    def __init__(self, expense_amount,payers={}, spenders={}):
        self.expense_id = Expense.expense_id_count
        self.expense_amount = expense_amount
        self.payees = {}        #{user, ratio}
        self.payers = {}        #{user, ratio}
        Expense.expense_id_count += 1
        
    def add_payers(self, payers):
        self.payees = payers
        
    def add_spenders(self, spenders):
        self.payers = spenders

    def split_expense(self):
        # add the amount to payers
        
        total_payers_ratio = sum([x for _,x in self.payees.items()])
        total_spenders_ratio = sum([x for _,x in self.payers.items()])
        
        # print(f'>>>>>> total_payers_ratio = {total_payers_ratio}')
        # print(f'>>>>>> total_spenders_ratio = {total_spenders_ratio}')
        
        for payer,ratio in self.payees.items(): #user, ratio
            expense_paid_by_payer = self.expense_amount*(ratio/total_payers_ratio)
            # print(f'payer : {payer.user_id} has paid amt: {expense_paid_by_payer}')
            
            # update user_gets_ledger w.r.t. all the spenders
            for payee,r in self.payers.items(): #user, ratio
                balance_amount = expense_paid_by_payer*(r/total_spenders_ratio)
                # print(f'payee {payee.user_id} has to pay amt:{balance_amount} ')
                payee.add_user_owes_expense(payer,balance_amount)
                payer.add_user_gets_expense(payee,balance_amount)
                
                # update passbook
                payee_entry = str(payee.user_id) + ' owes ' + str(balance_amount) + ' from ' + str(payer.user_id)
                payer_entry = str(payer.user_id) + ' lends ' + str(balance_amount) + ' to ' + str(payee.user_id)

                payee.add_entry_to_passbook(payee_entry)
                payer.add_entry_to_passbook(payer_entry)
                
    def reset_expense(self):
        total_payers_ratio = sum([x for _,x in self.payees.items()])
        total_spenders_ratio = sum([x for _,x in self.payers.items()])
        
        for payer,ratio in self.payees.items(): #user, ratio
            expense_paid_by_payer = self.expense_amount*(ratio/total_payers_ratio)
            # print(f'payer : {payer.user_id} has paid amt: {expense_paid_by_payer}')
            
            # update user_gets_ledger w.r.t. all the spenders
            for payee,r in self.payers.items(): #user, ratio
                balance_amount = expense_paid_by_payer*(r/total_spenders_ratio)
                # print(f'payee {payee.user_id} has to pay amt:{balance_amount} ')
                payee.add_user_owes_expense(payer,-balance_amount)
                payer.add_user_gets_expense(payee,-balance_amount)
                
        
    def update_expense(self, new_payers={}, new_payees={}):
        print('\n***************************************** Rebalancing **********************************************\n ')
        # undo
        self.reset_expense()
        # add new payers & payees
        for u,new_ratio in new_payers.items():
            self.payers[u] = new_ratio  # update
        
        for u,new_ratio in new_payees.items():
            self.payees[u] = new_ratio  # update
        
        # rebalance
        self.split_expense()
            


u1 = User('User1')
u2 = User('User2')
u3 = User('User3')
u4 = User('User4')






# exp2 = Expense(100)

# payers2 = {u3:1}
# spenders2 = {u1:1,u2:1}

# exp2.add_payers(payers2)
# exp2.add_spenders(spenders2)

# exp2.split_expense()

# u1.get_balance()
# u2.get_balance()
# u3.get_balance()


u2.show_passbook()



'''
1000
payers=> u1:u2::1:1  , 
spenders=> u1:u3:u4::1:2:1

1000
payers=> u3:1
spends=> u1:u2::1:1
'''

exp1 = Expense(1000)

payers1 = {u1:1, u2:1}

spenders1 = {u1:1,u3:2,u4:1}
exp1.add_payers(payers1)
exp1.add_spenders(spenders1)
exp1.split_expense()
u1.get_balance()
u2.get_balance()
u3.get_balance()

# Update expense
# print('>>> original payees: ',exp1.payees)

new_payees = {u1:1, u2:2}
exp1.update_expense(new_payees=new_payees)
# print('>>> new payees(after rebalancing): ',exp1.payees)
u2.get_balance()
```
{% endtab %}

{% tab title="unit_test.py" %}
```python
from splitwise import Expense, User
import unittest

class TestSplitwise(unittest.TestCase):
    
    def test_user(self):
        u1 = User('User1')
        amt1 = u1.get_total_balance_for_user()
        self.assertEqual(amt1,0)
        
        
    def test_expense(self):
        ex1 = Expense(100)
        ex1.add_payers({User('User1'):1,User('User2'):1})
        ex1.add_spenders({User('User1'):1})
        
        payers_total_share = sum([v for _,v in ex1.payees.items()])
        spenders_total_share = sum([v for _,v in ex1.payers.items()])
        self.assertGreaterEqual(payers_total_share, 1)
        self.assertGreaterEqual(spenders_total_share, 1)
        
    def test_all(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
    
```
{% endtab %}
{% endtabs %}

##
