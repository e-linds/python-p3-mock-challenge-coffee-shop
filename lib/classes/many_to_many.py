class Coffee:
    all = []

    def __init__(self, name):
        self.name = name

        Coffee.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and len(value) >= 3 and hasattr(self, "name") == False:
            self._name = value
        else: print("not valid name")


    name = property(get_name, set_name)
        
    def orders(self):
        orders= []
        for each in Order.all:
            if each.coffee == self:
                orders.append(each)
        return orders
    
    def customers(self):
        customers = []
        for each in self.orders():
            customers.append(each.customer)
        return list(set(customers))
    
    def num_orders(self):
        if len(self.orders()) > 0:
            return len(self.orders())
        else:
            return 0
    
    def average_price(self):
        individual_prices = []
        for each in self.orders():
            individual_prices.append(each.price)
        avg = sum(individual_prices)/len(individual_prices)
        return avg

    def __repr__(self):
        return f"{self.name}"

#------------------------------------------------------------------------------------------------    
class Customer:
    all = []

    def __init__(self, name):
        self.name = name

        Customer.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 1 <= len(value) <= 15:
            self._name = value
        else: print("not valid name")
        
    name = property(get_name, set_name)
        
    def orders(self):
        orders = []
        for each in Order.all:
            if each.customer == self:
                orders.append(each)
        return orders
    
    def coffees(self):
        coffees = []
        for each in self.orders():
            coffees.append(each.coffee)
        return list(set(coffees))
    
    def create_order(self, coffee, price):
        newinstance = Order(self, coffee, price)
        return newinstance
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers = []
        customer_count = []
        all_customer_counts = []

        for each in Order.all:
            if each.coffee == coffee:
                customers.append(each.customer)
                if customers:
                    count = customers.count(each.customer)
                    individual_count = [count, each.customer]
                    all_customer_counts.append(individual_count)
                else: return None 
            all_customer_counts.sort(reverse=True)
        for each in Customer.all:
            if all_customer_counts and each == all_customer_counts[0][1]:
                return each
        

    def __repr__(self):
        return f"{self.name}"


#------------------------------------------------------------------------------------------------    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if type(price) is float and 1.0 <= len(str(price).replace('.','')) <= 10.0:
            self._price = price

        Order.all.append(self)


    def get_price(self):
        return self._price
    
    def set_price(self, value):
            print("cannot change price")

    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer
    
    def set_customer(self, value):
        if type(value) is Customer:
            self._customer = value
        else: print("not valid Customer object")

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    
    def set_coffee(self, value):
        if type(value) is Coffee:
            self._coffee = value
        else: print("not valid Coffee object")
       

    coffee = property(get_coffee, set_coffee)
    



    
    
# customer1 = Customer("Teri")
# customer2 = Customer("Dee")
# coffee1 = Coffee("Black")
# coffee2 = Coffee("Latte")
# coffee3 = Coffee("Cappucino")
# order1 = Order(customer1, coffee1, 5.50)
# order2 = Order(customer2, coffee2, 10.0)
# order_mixed = Order(customer1, coffee2, 3.5)
# order3 = Order(customer2, coffee2, 10.0)
# order4 = Order(customer2, coffee2, 10.0)
# order5 = Order(customer2, coffee2, 10.0)
# order6 = Order(customer1, coffee1, 5.50)

# order7 = Order(customer1, coffee1, 5.50)






# print(Customer.most_aficionado(coffee1))

