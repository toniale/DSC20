"""
DSC 20 Final Project
Name: Tonia Le
PID:  A15662706
"""
from util import Stack, Queue
from datetime import datetime


def doctest():
    """
    ------------------------ PRODUCT TEST ------------------------

    >>> p1 = Product("iphone",399)
    >>> p2 = Special_Product("macbook air",999)
    >>> p3 = Limited_Product("free iphone", 0, 10)
    >>> p1, p2, p3
    (PRODUCT <0>, PRODUCT <1>, PRODUCT <2>)
    >>> print(p1)
    <0> iphone - 399$
    >>> print(p2)
    <1> macbook air - 999$ (special)
    >>> print(p3)
    <2> free iphone - 0$ (10 left)

    ------------------------ WAREHOUSE TEST ------------------------

    >>> wh = Warehouse()
    >>> st = Store(wh)
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> print(wh)
    Warehouse with 3 products
    >>> print(wh.get_product(1))
    <1> macbook air - 999$ (special)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <0> iphone - 399$
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (10 left)
    ============================
    >>> wh.export_product(3)
    >>> wh.export_product(2)
    PRODUCT <2>
    >>> wh.remove_product(0)
    True
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (9 left)
    ============================
    >>> st.view_products(sort = True)
    ============================
    <ID> Product - Price
    <2> free iphone - 0$ (9 left)
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.remove_product(0)
    False
    >>> [wh.export_product(2) for i in range(9)]
    [PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>,\
 PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>]
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.show_log()
    Product <0> imported - 2020-11-26 07:09:17.709522
    Product <1> imported - 2020-11-26 07:09:17.709584
    Product <2> imported - 2020-11-26 07:09:17.709612
    Product <2> exported - 2020-11-26 07:09:17.709745
    Product <0> removed  - 2020-11-26 07:09:17.709776
    Product <2> exported - 2020-11-26 07:09:17.709886
    Product <2> exported - 2020-11-26 07:09:17.709893
    Product <2> exported - 2020-11-26 07:09:17.709897
    Product <2> exported - 2020-11-26 07:09:17.709901
    Product <2> exported - 2020-11-26 07:09:17.709905
    Product <2> exported - 2020-11-26 07:09:17.709909
    Product <2> exported - 2020-11-26 07:09:17.709913
    Product <2> exported - 2020-11-26 07:09:17.709916
    Product <2> exported - 2020-11-26 07:09:17.709920
    Product <2> removed  - 2020-11-26 07:09:17.709924

    ------------------------ USER TEST ------------------------

    >>> u1 = User( 'Jerry', st)
    >>> u2 = Premium_User( 'FYX', st)
    >>> u1
    USER<0>
    >>> u2
    USER<1>
    >>> print(u1)
    standard user: Jerry - 0$
    >>> u2.add_balance(2000)
    >>> print(u2)
    premium user: FYX - 2000$

    >>> wh.import_product(p1)
    >>> u1 = User("A",st)
    >>> u1.add_cart(0)
    >>> u1.add_cart(0)
    >>> u1.view_cart()
    (front) <0> iphone - 399$ -- <0> iphone - 399$ (rear)
    >>> u1.checkout()
    STORE: Not enough money QQ
    []
    >>> u1.add_balance(1000)
    >>> u1.checkout()
    STORE: A ordered iphone. A has 562$ left.
    STORE: A ordered iphone. A has 124$ left.
    [PRODUCT <0>, PRODUCT <0>]
    >>> p4 = Limited_Product("Ipad", 600, 5)
    >>> wh.import_product(p4)
    >>> u2.buy_all(3)
    STORE: FYX ordered Ipad. FYX has 1400$ left.
    STORE: FYX ordered Ipad. FYX has 800$ left.
    STORE: FYX ordered Ipad. FYX has 200$ left.
    STORE: Not enough money QQ
    [PRODUCT <3>, PRODUCT <3>, PRODUCT <3>]

    ------------------- HISTORY / UNDO TEST -------------------

    >>> u1.view_history()
    (bottom) <0> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903632 -- \
<1> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903658 (top)
    >>> u1.undo_purchase()
    STORE: A refunded iphone. A has 523$ left.

    -------------------------- EC TEST ------------------------
    >>> p1 = Product("A",20)
    >>> p2 = Special_Product("B",7)
    >>> p3 = Limited_Product("C", 1, 2)
    >>> wh = Warehouse()
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> st = Store(wh)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <4> A - 20$
    <5> B - 7$ (special)
    <6> C - 1$ (2 left)
    ============================
    >>> st.so_rich(45)
    1
    >>> st.so_rich(61)
    0
    >>> st.so_rich_recursive(45)
    1
    >>> st.so_rich_recursive(61)
    0
    """
    pass


#######################################################################
#                               PRODUCT                               #
#######################################################################
class Product:
    """
    A class that provides abstraction to the products available in our system.
     """
    product_counter = 0
    ##### Part 1.1 #####
    def __init__(self, name, price):
        """
        Constructor of Product.
        Parameters:
            name (str): name of product
            price (int): price of product
        """
        self.name = name
        self.price = price
        self.id = Product.product_counter
        Product.product_counter += 1

    def __str__(self):
        """ String representation of Product """
        # result = '<' + str(self.id) + '> ' + str(self.name) + ' - ' + str(self.price) +'$'
        result = ('<{}> {} - {}$'.format(str(self.id), str(self.name), str(self.price)))
        return result
    def __repr__(self):
        """ String representation of Product """
        # return 'PRODUCT ' + '<' + str(self.id) + '> '
        return ('PRODUCT <{}>'.format(str(self.id)))

class Limited_Product(Product):
    """ A class that abstracts a limited product """

    ##### Part 1.2 #####
    def __init__(self, name, price, amount):
        """
        Constructor of Limited_Product.
        Parameters:
            name (str): name of product
            price (int): price of product
            amount (int): amount of items available for this product
         """
        super().__init__(name, price)
        self.amount = amount

    def __str__(self):
        """ String representation of Limited_Product """
        # “<{id}> {name} - {price}$ ({amount} left)”
        return '<{}> {} - {}$ ({} left)'.format(str(self.id), self.name, str(self.price), str(self.amount))

class Special_Product(Product):
    """ A class that abstracts a special product """

    ##### Part 1.3 #####
    def __init__(self, name, price, description="special"):
        """
        Constructor of Special_Product.
        Parameters:
            name (str): name of product
            price (int): price of product
        """
        super().__init__(name, price)
        if description == "":
            return self.description
        else:
            self.description = description

    def __str__(self):
        """ String representation of Special_Product """
        #“<{id}> {name} - {price}$ ({description})”
        return '<{}> {} - {}$ ({})'.format(str(self.id), self.name, str(self.price), self.description)


#######################################################################
#                              WAREHOUSE                              #
#######################################################################


class Warehouse:
    """ A class that provides abstraction to the warehouses. """

    ##### Part 2 #####
    def __init__(self):
        """
        Constructor of Warehouse
        """
        self.inventory = {}
        self.log = []

    def __str__(self):
        """
        String representation of Warehouse
        """
        # “Warehouse with {number of products stored} products”
        return "Warehouse with {} products".format(len(self.inventory))


    def get_product(self, product_id):
        """
        Returns the product instance with the given id (int) from
        the inventory. Returns None if the product is not found,.
        """
        if product_id not in self.inventory.keys():
            return None
        else:
            return self.inventory[product_id]

    def list_products(self):
        """
        A list of all actual product instances stored in
        the inventory.
        """
        return list(self.inventory.values())

    def remove_product(self, product_id):
        """
        Removes the product instance with the given id (int) from
        the inventory. Will return True if it’s successfully removed,
        and False if the product is already not in the inventory.
        """
        if product_id not in self.inventory:
            return False
        else:
            self.inventory.pop(product_id)
            self.log.append("Product <{}> removed  - {}".format(str(product_id), datetime.now()))
            return True

    def import_product(self, product):
        """
        Imports the product instance (Product) to the inventory
        """
        prod_id = product.id
        self.inventory[prod_id] = product
        self.log.append("Product <{}> imported - {}".format(prod_id, datetime.now()))

    def export_product(self, product_id):
        """
        Exports the product instance with the given id (int) from
        the inventory. It will return None if the specified product
        does not exist in the inventory.
        """
        if product_id not in self.inventory:
            return None

        prod = self.inventory[product_id]
        if isinstance(prod, Limited_Product):
                prod.amount -= 1
                self.log.append("Product <{}> exported - {}".format(product_id, datetime.now()))
                if prod.amount <= 0:
                    self.remove_product(product_id)
                return prod
                    # self.log.append("Product <{}> removed  - {}".format(product_id, datetime.now()))
        else:
            self.log.append("Product <{}> exported - {}".format(product_id, datetime.now()))
            return prod

    def size(self):
        """
        Returns the number of products stored in the inventory
         """
        return len(self.inventory)

    def show_log(self):
        """
        Prints time logs
        """
        for log in self.log:
            print (log)

#######################################################################
#                               HISTORY                               #
#######################################################################
class History:
    """
    A class that provides abstraction to the purchase history records.
    """
    history_counter = 0
    ##### Part 3 #####
    def __init__(self, product, user):
        """
        Constructor of History
            Parameters:
            product(Product): product being purchased
            user(User): user who purchased the product
            """
        self.product = product
        self.user = user
        self.id = History.history_counter
        History.history_counter += 1
        self.time = datetime.now()

    def __str__(self):
        """
        String representation of History class
        """
        return "<{}> {} bought {} at {}".format(str(self.id), \
                str(self.user.id), self.product, self.time)

    def __repr__(self):
        """ String representation of History class
        """
        return "HISTORY<{}> - {}".format(str(self.id), self.time)


#######################################################################
#                                USER                                 #
#######################################################################
class User:
    """
    A class that provides abstraction to the users.
    """
    user_counter = 0

    ##### Part 4.1 #####
    def __init__(self, name, store):
        """
        Constructor for User
            Parameters:
            name: name of the user
            store: name of the store the user is registered to
        """
        self.name = name
        self.store = store
        self.balance = 0
        self.id = User.user_counter
        User.user_counter += 1
        self.purchase_history = Stack()
        self.cart = Queue()
        self.store.add_user(self)

    def __str__(self):
        """
        String representation of User
        """
        return "standard user: {} - {}$".format(self.name, str(self.balance))

    def __repr__(self):
        """
        String representation of User
        """
        return "USER<{}>".format(str(self.id))

    def set_name(self, new_name):
        """
        Sets to the given new name
        """
        self.name = new_name

    def get_name(self):
        """
        Gets the name attribute
        """
        return self.name

    def set_balance(self, amount):
        """
        Sets balance equal to given amount
        """
        self.balance = amount

    def get_balance(self):
        """
        Gets the balance amount
        """
        return self.balance

    def add_balance(self, amount):
        """
        Adds a given amount to the balance
        """
        self.balance += amount

    def last_purchase(self):
        """
        Returns the last purchased history instance (of type History).
        If the purchase history is empty, None is returned.
        """
        if self.purchase_history.is_empty():
            return None
        else:
            return self.purchase_history.peek()

    def view_history(self):
        """
        Prints the purchase history of the user
        """
        print(self.purchase_history)

    def view_cart(self):
        """
        Prints the cart of this user
        """
        print(self.cart)

    def clear_cart(self):
        """
        Remove all products in the cart
        """
        self.cart.clear()

    ##### Part 5.2 #####
    def add_cart(self, product_id):
        """
        Adds the product to the user’s shopping cart based on the
        given product id
        """
        product = self.store.get_product(product_id)
        if product in self.store.warehouse.list_products():
            self.cart.enqueue(product)
        else:
            pass

    def checkout(self):
        """
        Returns a list of purchased products
        """
        purchased_products = []
        for i in range(self.cart.size()):
            product = self.cart.peek()
            if self.store.get_product(product.id) is None:
                break
            ordered_items = self.store.order(self.id, product.id)
            if ordered_items is False:
                break
            else:
                product = self.cart.dequeue()
                self.purchase_history.push(ordered_items)
                purchased_products.append(product)
        return purchased_products

    ##### Part 5.3 #####
    def undo_purchase(self):
        """
        Undoes the user's last purchase
        """
        if self.purchase_history.is_empty():
            print ("USER: no purchase history")
            return
        else:
            last_purch = self.last_purchase().product
            if self.store.undo_order(self.id, last_purch) is True:
                self.purchase_history.pop()
            elif self.store.undo_order(self.id, last_purch) is False:
                pass

class Premium_User(User):
    """
    A class that abstracts a premium user
    """

    ##### Part 4.2 #####
    def __str__(self):
        """
        String representation of Premium_User
        """
        return "premium user: {} - {}$".format(self.name, str(self.balance))


    ##### Part 5.4 #####
    def buy_all(self, product_id):
        """
        Repeatedly orders the product corresponding to the given product id
        only if it is a limited product. Ordering will stop when there are
        no more offerings or the user does not have enough in their balance.
        This purchase history will be added to the user's purchase
        history and a list of purchased products will be returned.
        """
        purchased_products = []
        product = self.store.get_product(product_id)
        if not isinstance(product, Limited_Product):
            print ("USER: not a limited product")
            return []
        else:
            while self.store.order(self.id, product_id):
                purchased_products.append(product)
                self.purchase_history.push(product)
            return purchased_products

    def undo_all(self):
        """
        Cancels the last purchases until the user does not have any records
        in purchase history, or if the last purchase is a limited product.
        """
        last_purch = self.last_purchase().product
        while not self.purchase_history.is_empty() and not \
        isinstance(last_purch, Limited_Product):
            self.undo_purchase()
            break

#######################################################################
#                               STORE                                 #
#######################################################################
class Store:
    """
    A class that abstracts stores
    """

    ##### Part 4.3 #####
    def __init__(self, warehouse):
        """
        Constructor of Store
            Parameters:
            warehouse(Warehouse): all of the products of the store
        """
        self.users = {}
        self.warehouse = warehouse

    def __str__(self):
        """
        String representation of Store
        """
        return "STORE: store with {} users and {} products".format(len(users), self.warehouse.size())


    def get_product(self, product_id):
        """
        Returns the product instance given the product_id
        """
        prod = self.warehouse.get_product(product_id)
        return prod

    def view_products(self, sort=False):
        """
        Views the products
        """
        print ('============================')
        print('<ID> Product - Price')
        if sort == False:
            for prod in self.warehouse.list_products():
                print ("{}".format(prod))
        elif sort == True:
            for sorted_price in sorted(self.warehouse.list_products(), key = lambda x: x.price):
                 print ("{}".format(sorted_price))
        print ('============================')


    ##### Part 5.1 #####
    def add_user(self, user):
        """
        Adds a user to the users dictionary unless the user is already
        present in the dictionary than False will be returned
        """
        if user in self.users:
            print ("STORE: User already exists")
            return False
        else:
            self.users[user.id] = user
            return True

    ##### Part 5.2 #####
    def order(self, user_id, product_id):
        """
        Takes the ids of the user who makes the order and the product they
        order, and handles the order after checking against the following
        requirements:
            1) The product should be available in the store.
            2) Non-Premium users will be denied Special Products
            3) The user’s balance should be enough to pay for this product.
            4) Premium users will only need to pay the full price of the
               product.
            5) Non-Premium users will also have to pay a shipping fee ontop
               of their product price.
        """
        user = self.users[user_id]
        product = self.warehouse.get_product(product_id)

        if product_id not in self.warehouse.inventory:
            print ("STORE: Product not found")
            return False
        # non- premium user trying to purchase a special product
        if not isinstance(user, Premium_User) and isinstance(product, Special_Product):
            print ("STORE: Special product is limited to premium user")
            return False
        # if the user doesn't have enough money for the product
        if user.balance < product.price:
            print ("STORE: Not enough money QQ")
            return False
        # premium user only pays full price of product
        if isinstance(user, Premium_User):
            cost = product.price
            user.balance -= cost
        # non-premium users pay full product price + shipping fee
        if not isinstance(user, Premium_User):
            ten_percent = .1
            shipping_fee = int(ten_percent * product.price)
            cost = product.price + shipping_fee
            user.balance -= cost
        # export the product id
        self.warehouse.export_product(product_id)
        print("STORE: {} ordered {}. {} has {}$ left.".format(user.name, product.name, user.name, user.balance))
        # create a history instance
        payment_history = History(product, user)
        return payment_history

    ##### Part 5.3 #####
    def undo_order(self, user_id, product):
        """
        Refunds the user by adding the price of the product back to their
        balance if the product is not limited
        """
        user = self.users[user_id]
        if isinstance(product, Limited_Product):
            print ("STORE: can’t refund Limited_Product")
            return False
        else:
            user.balance += product.price
            print ("STORE: {} refunded {}. {} has {}$ left.".format(user.name, product.name, user.name, user.balance))
            return True

    ##### Part 6 #####
    def so_rich(self, money):
        """
        Returns the least amount of money a user will have left after
        their purchases
        """
        # YOUR CODE GOES HERE #

        # suppose you haven't seen any product yet
        # the only possible amount of money left is "money"
        # this is a set to record the possible money left
        left = set([money])

        # get products
        lst = self.warehouse.list_products()

        for product in lst:

            # a temporary set to save the updates of "left"
            # you don't want to modify the set you're iterating through
            tmp_left = set()

            for m in left: #(45, 25, 5)
                # update tmp_left
                if type(product) != Limited_Product:
                    new_left = m
                    while new_left >= 0:
                        tmp_left.add(new_left) #new_left = 5
                        new_left = new_left - product.price #new_left = 5-7
                else:
                    # handle limited product
                    amt_prod = product.amount
                    new_left = m
                    while new_left >= 0 and amt_prod >= 0:
                        amt_prod -= 1
                        tmp_left.add(new_left)
                        new_left = new_left - product.price

            left = tmp_left

        return min(left)

    def so_rich_recursive(self, money):
        """
        Recursively returns the least amount of money a user will have
        left after their purchases
        """

        # get products
        lst = self.warehouse.list_products()

        def helper(lst, money):
            # base case
            if money == 0:
                return 0

            cur_min = money
            product = lst[0][1]
            if type(product) != Limited_Product:
                tmp = money
                while tmp >= 0:
                    return helper(lst[:product], money)
            else:
                tmp = money
                amt_prod = len(lst)
                while tmp >= 0 and amt_prod >= 0:
                    return helper(lst, money - product)

            return

        return helper(lst, money)
