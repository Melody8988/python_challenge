# vim: ts=4:sw=4:expandtabs


__author__ = 'zach.mott@oppsource.com'
__doc__ = """
OppSource Python programming test v0.1.2 2018-05-30.

Consider the following classes, which make up the foundation of a
(very) simple account-based marketing platform. This programming 
test will require you to modify and extend its behavior to meet
certain business goals.

If you find any of the questions below to be ambiguous, use your
best judgement to decide how to proceed, then explain why you
made that choice in comments.

Your final submissions should:
- Be syntactically valid Python 3.6.5 code.
- Follow the PEP 8 style guide.
- Be PEP 20 compliant.
- Be reasonably free from errors.
- Contain lots of comments and docstrings.
- Employ a DRY programming style.
"""


class SalesRep(object):
    """
    Models a sales representative. Sales representatives know
    their own names and which accounts are assigned to them.
    """
    def __init__(self, first_name, last_name, accounts=None):
        self.first_name = first_name
        self.last_name = last_name
        self._accounts = []

        if accounts:
            self._accounts.extend(accounts)

    def __str__(self):
        return "{self.first_name} {self.last_name}".format(self=self)

    def get_accounts(self):
        return self._accounts

    def add_account(self, account):
        self._accounts.append(account)
        account.set_sales_rep(self)
        return self._accounts

    def remove_account(self, account):
        self._accounts.remove(account)
        account.set_sales_rep(None)
        return self._accounts

    # def set_accounts(self, accounts)
    #     self._accounts = accounts
    # setting accounts in the SalesRep class to be the current accounts array



     

   

        
# +----------------------------------------------------------------------------+
# |                                                                            |
# | Q1-1. Management has determined that it would be useful to organize        |
# |       Accounts by market segments, so that SalesReps can specialize        |
# |       in selling to particular segments and thus improve the number        |
# |       of sales opportunities they generate.                                |
# |                                                                            |
# |       Implement the MarketSegment class. A MarketSegment must be           |
# |       instantiated with a name, but it may also receive an iterable of     |
# |       Accounts which will be associated with it. MarketSegments must       |
# |       keep track of which Accounts they're associated with. Additionally,  |
# |       the MarketSegment class must know how to add and remove Accounts     |
# |       from itself.                                                         |
# |                                                                            |
# |       Additionally, modify the Account class so that it supports the       |
# |       following MarketSegment-related use cases:                           |
# |       - An Account may be instantiated with an iterable of MarketSegments  |
# |         to which it's related.                                             |
# |       - An Account can provide an iterable of the MarketSegments it's      |
# |         related to.                                                        |
# |       - An Account can be related to a new MarketSegment.                  |
# |       - An Account can be removed from one of the MarketSegments it's      |
# |         related to.                                                        |
# |                                                                            |
# |       A MarketSegment may be associated with more than one Account, and    |
# |       and Account may be associated with more than one MarketSegment.      |                                                   
# |                                                                            |
# +----------------------------------------------------------------------------+
       
class MarketSegment(object):
    def __init__(self, name, accounts=None):
        self.name = name
        self._accounts = []

        if accounts:
            self._accounts.extend(accounts)
    
    def __str__(self):
        return "{self.name}".format(self=self)

    def add_account(self, account):
        if account in self._accounts:
            # ^check if account is already in current segment array
            raise ValueError ('Accounts cannot be assigned to the same Market Segment more than once.') 
             
        else:
            self._accounts.append(account)
            account.set_market_segments(self)
            return self._accounts 

    def remove_account(self, account):
        self._accounts.remove(account)
        account.set_market_segments(None)
        return self._accounts 

    def set_accounts(self, accounts):
        self._accounts = accounts
    # replacing accounts in the marketSegment class to be the current accounts array 


class Account(object):
    """
    Models an account. Accounts know their name, the sales rep they're
    assigned to, and the market segments they're a part of.
    """
    def __init__(self, name, sales_rep, segments=None):
        self.name = name
        self._sales_rep = sales_rep
        self._segments = []

        if segments:
            self._segments.extend(segments)
        
    def __str__(self):
        return "{self.name}".format(self=self)

    def get_sales_rep(self):
        return self._sales_rep
    
    def set_sales_rep(self, sales_rep):
        self._sales_rep = sales_rep

    def set_market_segments(self, segments):
        self._segments = segments
        # might have to be self._segments = []

    def add_segment(self, segment):

        if segment in self._segments:
             # ^check if segment is already in current account array
            raise ValueError ('This segment cannot be assigned to the same Account more than once.') 
        
        else:
            self._segments.append(segment)
            segment.set_accounts(self)
            # update accounts to have new segments by calling set_accounts

    def remove_segment(self, segment):
        self._segments.remove(segment)
        segment.set_accounts(None)
        # update accounts to have new segments by calling set_accounts

        # """
        # Q1-2. Implement this method, which takes an iterable of MarketSegments to
        #       which this Account will be attached. This method REPLACES all
        #       MarketSegment associations, so be sure to update each MarketSegment's
        #       internal representation of associated Accounts appropriately.
        # """
        # raise NotImplementedError()






# +----------------------------------------------------------------------------+
# |                                                                            |
# | Q2-1. After reviewing your work on Q1, your manager provides you with      |
# |       a new requirement: Account-MarketSegment relations must be unique.   |
# |       An informative ValueError should be raised if a user tries to relate |
# |       an Account to a MarketSegment it is already a part of.               |
# |                                                                            |
# |       Write a test suite that validates that this requirement is           |
# |       enforced correctly (or not).                                         |
# |                                                                            |
# | Q2-2. If necessary, modify the MarketSegment and Account classes so        |
# |       that the the tests you wrote in Q2-1 pass.                           |
# |                                                                            |
# | Q2-Bonus. If necessary, modify your solution to Q2-2 so that it            |
# |           uses the Account's name as the basis for determining             |
# |           whether a particular Account-MarketSegment relation is           |
# |           unique.                                                          |
# |                                                                            |
# +----------------------------------------------------------------------------+

class ChildAccount(Account):
    
    def __init__(self, child_account_name, name, sales_rep, segments=None):
        super(ChildAccount, self).__init__(name, sales_rep, segments=None)

        if segments:
            self._segments.extend(segments)

        # child accounts have their own names, name represents parent account
        self._child_account_name = child_account_name
        
    
      

# Dummy Data
acc1 = Account('acc1', 'Leslie', ['Consumer Goods'])
acc2 = Account ('acc2', 'Leslie', ['Consumer Goods'])
acc3 = Account ('acc3', 'Leslie', ['Services', 'Advertising'])

c_acc1  = ChildAccount ('c_acc1', 'acc2', 'Leslie should be here', ['SHould be consumer goods'])

print(c_acc1)
rep_1 = SalesRep('Leslie', 'Knope', [acc1, acc2, acc3])

seg_1 = MarketSegment('Consumer Goods', [acc1, acc2])
seg_2 = MarketSegment('Services', [acc3])
seg_3 = MarketSegment('Advertising', [acc3])


# rep_1.remove_account(acc1)
# acc1.add_segment('Consumer Goods')
# print (acc1._sales_rep)

# seg_1.add_account(acc1)
# print (seg_1._accounts)

# print(c_acc1._sales_rep)
        

# +----------------------------------------------------------------------------+
# |                                                                            |
# | Q3. Create a new kind of Account, called a ChildAccount. A ChildAccount    |
# |     behaves exactly like an Account, but its constructor takes an          |
# |     additional "parent" argument, which represents the Account which       |
# |     this ChildAccount is a child of.                                       |
# |                                                                            |
# |     During initialization, A ChildAccount should be assigned to its        |
# |     parent's SalesRep if no SalesRep is provided. Likewise, a ChildAccount |
# |     should be added to its parent's MarketSegments if no MarketSegments    |
# |     are provided.                                                          |
# |                                                                            |
# |     It is permissible for a ChildAccount to have another ChildAccount as   |
# |     its parent.                                                            |
# |                                                                            |
# +----------------------------------------------------------------------------+


# +----------------------------------------------------------------------------+
# |                                                                            |
# |  Q4. Implement the following function "print_tree".  This function must    |
# |      take an Account as input, though you may modify its signature to      |
# |      take other parameters as well. This function prints the Account's     |
# |      name, SalesRep and MarketSegments, as well as each of its children,   |
# |      their name, SalesReps and MarketSegments (and their children, etc.)   |
# |                                                                            |
# |      The output should visually indicate the parent/child relationships.   |
# |                                                                            |
# +----------------------------------------------------------------------------+

def print_tree(account):
    """ In the example output below, "GE" is the root account, "Jet Engines"
        and "Appliances" are first-degree ChildAccounts, and "DoD Contracts"
        and "Washing Machines" are second-degree ChildAccounts.

    > print_tree(general_electric)
    GE (Manufacturing, R&D): Daniel Testperson
        Jet Engines (Manufacturing, R&D, Aerospace): Daniel Testperson
            DoD Contracts (Defense, R&D, Aerospace): William Testperson
        Appliances (Manufacturing, Consumer Goods): Janet Testperson
            Washing Machines (Consumer Goods): Janet Testperson
    """
    raise NotImplementedError()


# +----------------------------------------------------------------------------+
# |                                                                            |
# |  Q5-1. Devise a SQL schema that could be used to persist the data          |
# |        represented by the SalesRep, MarketSegment, and Account classes     |
# |        above. Do not consider the ChildAccount class for this exercise.    |
# |        Make sure to preserve relationships between the classes as well as  |
# |        the data contained within each class.                               |
# |                                                                            |
# |  Q5-2. Write a SQL statement that uses the schema you devised in Q5-1 to   |
# |        fetch the name and SalesRep name for all of the accounts that are   |
# |        related to the "Consumer Goods" market segment.                     |
# |                                                                            |
# +----------------------------------------------------------------------------+
