
import re  # import the regular expression module
# pyhton project class1 -->user
class User:  # define a class named User
    users = {}  # to save all users data in the format--> {user_id : [user_name,password,email,address]}
    def __init__(self):  # define the constructor method for the class
        # self.user_id = int(input("enter id : "))  # get the user id as an integer from the input
        # # if user_id not in User.users.keys():
        # self.user_name = input("enter your name : ")  # get the user name from the input
        # self.password = input("enter password : ")  # get the password from the input
        # self.email = input("enter email : ")  # get the email from the input
        def email_validation(mail):
            pattern = r'^\S+@\S+\.\S+$'
            return re.match(pattern, mail) is not None
        id =  0
        while True :
            try :
                id = float(input("enter id : "))
            except ValueError:
                    print("Please enter a number")
                    continue
            else :
                self.user_id = id
                break

        self.user_name = input("enter your name : ")
        self.password = input("enter password : ")     
        self.email = input("enter email : ")
        while True:
            if email_validation(self.email):
                self.address = input("enter address : ")  # get the address from the input
                break
                
            else:
                print("please Enter Valid mail.")
                self.email = input("enter email : ") 
                continue
                
        User.users["Enteries"] = [
            {"user id ": self.user_id, "user name": self.user_name, "password": self.password, "email ": self.email,"address ": self.address}]  # add the user data as a dictionary to the users attribute of the class
        import json  # import the json module
        with open('./User.users.json', 'w') as f:  # open a file named User.users.json in write mode
            json.dump(User.users, f)  # dump the users attribute of the class as a json object to the file
        f = open('User.users.json')  # open the same file in read mode
        data = json.load(f)  # load the json object from the file as a python dictionary

    @staticmethod  # declare the method as a static method, which means it can be called without creating an instance of the class
    def logining():  # define a method named logining for the class
        import json  # import the json module
        data = {}  # create an empty dictionary
        f = open('User.users.json')  # open the file named User.users.json in read mode
        data = json.load(f)  # load the json object from the file as a python dictionary
        user_name = input("enter your username : ")  # is the user email
        # check_in_email = re.search(r'[A-z0-9\.]+\@[A-z0-9]+(.com)',self.login_user_email).group()  # regix method to get the email
        for c in data:  # loop through the keys of the data dictionary
                for e in data["Enteries"]:  # loop through the values of the Enteries key of the data dictionary
                    while user_name == e['user name']:  # check if the user name matches the user name in the dictionary
                        print('Please enter your password.')  # prompt the user to enter the password
                        login_user_password = input("enter password : ")  # get the password from the input
                        if login_user_password == e['password']:  # check if the password matches the password in the dictionary
                            print('Welcome you are now logged in!')  # print a welcome message
                            break 
                        
                        else:
                            print('Wrong password,Try Again')  # print a wrong password message
                            continue  # continue the loop
                    

                    else:
                        print('Your name is not in the file.')  # print a message that the user name is not found
                        print('You need to register.')  # print a message that the user needs to register
                        customer1 = Customer()
                        customer1.logining()


    def register(self):  # a method to get user's data and save it in a dictionary called users
        User.users[self.user_id] = [self.user_name, self.password, self.email,self.address]  # a dictionary, the result of this like that {user_id:[user_name,password,email,address]}
        login_dictionary = {}  # used in login test to check only the email and password not the whole user's data
        login_dictionary[self.email] = self.password  # store the email and password as a key-value pair in the login dictionary
        return login_dictionary  # we will use it in login and update methods

    def update_profile(self):  # a method to update the user's profile
        # we will check if he is a user or not,if he is a user then he can modify his data
        old_email = input("enter user email: ")  # get the old email from the input
        old_password = input("enter user password: ")  # get the old password from the input
        user_data = User.register(self)  # call the register method to get the login dictionary
        if old_email in user_data.keys():  # check if the old email is in the login dictionary
            if str(user_data[old_email]) == old_password:  # check if the old password matches the one in the login dictionary
                print('you can modify your data')  # print a message that the user can modify the data
                print("please enter these items 1-user_id 2- user_name 3- password 4-email 5-address")  # print a message to prompt the user to enter the new data
                new_user_id = input("Enter user id: ")
                new_user_name = input("enter  user name: ")  # get the new user name from the input
                new_user_password = input("enter user password: ")  # get the new password from the input
                new_user_email = input("enter user email: ")  # get the new email from the input
                new_user_address = input("enter user address: ")  # get the new address from the input
                User.users["Enteries"] = [{"user id ": new_user_id, "user name": new_user_name, "password": new_user_password,"email ": new_user_email, "address ": new_user_address}]  #  save the data in users dictionary
                print(f'from update{User.users}')  # print the updated users dictionary

            else:
                print('wrong password')  # print a message that the password is wrong
        else:
            print('wrong email')  # print a message that the email is wrong

############# customer class 2
class Customer(User):  # define a class named Customer that inherits from the User class
    def init(self):  # define the constructor method for the class
        self.shopping_cart = ShoppingCart  # assign a ShoppingCart object to the shopping_cart attribute of the class
        self.purchase_history = []  # create an empty list for the purchase_history attribute of the class

    def add_to_cart(self, product):  # define a method to add a product to the shopping cart
        self.shopping_cart.add_item(product)  # call the add_item method of the shopping_cart object with the product as an argument
    def remove_from_cart(self, product):  # define a method to remove a product from the shopping cart
        self.shopping_cart.remove_item(product)  # call the remove_item method of the shopping_cart object with the product as an argument
    def view_purchase_history(self):  # define a method to view the purchase history
        return self.purchase_history  # return the purchase_history attribute of the class
class Seller(User):  # define a class named Seller that inherits from the User class
    def __init__(self,Store_Name):  # define the constructor method for the class
        super().__init__()  # call the constructor method of the parent class
        self.Store_Name = Store_Name  # assign a Store_Name object to the Store_Name attribute of the class
        self.products = []  # create an empty list for the products attribute of the class

    def add_product(self, product):  # define a method to add a product to the products list
        self.products.append(product)  # append the product to the products list

    def Update_Product_Information(self, Product_id, Product_new_description,Product_new_price):  # define a method to update the product information
        for Product in self.Products:  # loop through the products list
            if Product.Product_id == Product_id:  # check if the product id matches the given product id
                Product.description = Product_new_description  # update the product description with the new description
                Product.price = Product_new_price  # update the product price with the new price

    ### To update product info u need to enter mentioned above and func check for each item in products list and check for pid in pro class == pid or not found
    def view_sales_history(self):  # define a method to view the sales history
        return self.all_sales_istory  # return the all_sales_history attribute of the class
##############################class order rank 5
class Order():  # define a class named Order

    details = {}  # store all order details in a class attribute
    def __init__(self, order_id, user_name, products, total_cost,order_status):  # define the constructor method for the class
        '''
        here to check that user enter number for order_id and string for order_status also
        to detect that the order_id is unique.
        '''
        if not isinstance(order_id, int):  # check if the order_id is an integer
            raise TypeError("Order ID must be an integer.")  # raise an error if not

        if not isinstance(order_status, str):  # check if the order_status is a string
            raise TypeError("Order status must be a string.")  # raise an error if not

        if order_id in Order.details:  # check if the order_id already exists in the details dictionary
            raise ValueError("Order ID already exists. Please enter a unique ID.")  # raise an error if yes
        self.order_id = order_id  # assign the order_id to the instance attribute
        self.user_name = user_name  # assign the user_name to the instance attribute
        self.products = products  # assign the products to the instance attribute
        self.total_cost = total_cost  # assign the total_cost to the instance attribute
        self.order_status = order_status  # assign the order_status to the instance attribute
        # making all orders in nested dictionary
        Order.details[self.order_id] = {  # add the order details as a nested dictionary to the details dictionary
            'customer': user_name,  # a problem
            'products': self.products,
            'total_cost': self.total_cost,
            'order_status': self.order_status
        }
    def place_order(self):  # define a method to place the order
        while True:  # start an infinite loop
            place = input("Do you want to place order type (yes or no): ")  # get the user input for placing the order
            if place.lower() == 'yes':  # check if the user input is yes
                # place the order
                self.order_status = "Placed"  # change the order_status to Placed

                for product_name in self.products:
                    for product_id, product_info in Product.productsWithinfo.items():
                        if product_info[0] == product_name:
                            current_quantity = product_info[3]
                            Product.productsWithinfo[product_id][3] = current_quantity - 1
                return "Order placed successfully."  # return a success message
            elif place.lower() == 'no':  # check if the user input is no
                return "Order not placed."  # return a failure message
            else:  # check if the user input is something else
                continue  # continue the loop

    def cancel_order(self):  # define a method to cancel the order
        while True:  # start an infinite loop
            cancel = input(
                "Do you want to cancel your order type (yes or no):")  # get the user input for canceling the order
            if cancel.lower() == 'yes':  # check if the user input is yes
                # place the order
                self.order_status = "Canceled"  # change the order_status to Canceled
                for product_name in self.products:
                    for product_id, product_info in Product.productsWithinfo.items():
                        if product_info[0] == product_name:
                            current_quantity = product_info[3]
                            Product.productsWithinfo[product_id][3] = current_quantity + 1
                return "Order Canceled successfully."  # return a success message
            elif cancel.lower() == 'no':  # check if the user input is no
                return "Order not Canceled."  # return a failure message
            else:  # check if the user input is something else
                continue  # continue the loop

    def view_order_details(self):  # define a method to view the order details
        for order_id, order_info in Order.details.items():  # loop through the items of the details dictionary
            print(f"Order ID: {order_id}")  # print the order id
            print(f"Customer: {order_info['customer']}")  # print the customer name
            print(f"Products: {order_info['products']}")  # print the products
            print(f"Total Cost: {order_info['total_cost']}")  # print the total cost
            # print(f"Order Status: {order_info['order_status']}") # print the order status

##############Online Marketplace Class:
class Online_Marketplace: # define a class named Online_Marketplace
    def __init__(self,Marketplace_name, list_of_customers, list_of_sellers, list_of_products): # define the constructor method for the class
        self.Marketplace_name =Marketplace_name # assign the Marketplace_name to the instance attribute
        self.list_of_customers = list_of_customers # assign the list_of_customers to the instance attribute
        self.list_of_sellers = list_of_sellers # assign the list_of_sellers to the instance attribute
        self.list_of_products = list_of_products # assign the list_of_products to the instance attribute
        self.customer_names = [] # create an empty list for the customer_names attribute
        self.seller_names = [] # create an empty list for the seller_names attribute
        self.product_names = [] # create an empty list for the product_names attribute

        for item in self.list_of_customers: # loop through the list_of_customers
            c = Customer(item[0],item[1],item[2],item[3],item[4]) # create a Customer object with the item as an argument
            self.customer_names.append(item[1]) # append the user name of the Customer object to the customer_names list
        for item in self.list_of_sellers: # loop through the list_of_sellers
            c = Seller(item[0],item[1],item[2],item[3],item[4],item[4]) # create a Seller object with the item as an argument
            self.seller_names.append(item[1]) # append the user name of the Seller object to the seller_names list
        for item in self.list_of_products: # loop through the list_of_products
            c = Product(item[0],item[1],item[2],item[3],item[4]) # create a Product object with the item as an argument
            self.product_names.append([item[1],item[3]]) # append the product name and price of the Product object to the product_names list
        print(f"Available Products & Item's price : {self.product_names}") # print the product_names list with a formatted string
    def Display_marketplace_information(self): # define a method to display the marketplace information
        print(self.Marketplace_name) # print the Marketplace_name attribute
    def add_remove(self, new, type, action): # define a method to add or remove a customer, seller, or product
        self.new = new # assign the new parameter to the instance attribute
        status = False  # status = false if there is no a customer or seller or product
        if type == 'customer': # check if the type parameter is customer
            for i in self.list_of_customers: # loop through the list_of_customers
                if i[1] == self.new: # check if the user name of the customer matches the new attribute
                    status = True # set the status to True
                    if action== 'add': # check if the action parameter is add
                        if new not in self.list_of_customers: # check if the new attribute is not in the list_of_customers
                            self.list_of_customers.append(i) # append the customer to the list_of_customers
                        else:
                            print('the customer already in the system') # print a message that the customer already exists
                    elif action == 'remove': # check if the action parameter is remove
                        self.list_of_customers.remove(i) # remove the customer from the list_of_customers
                    else:
                        print('error deleting the customer') # print a message that there is an error in deleting the customer
                    # print(self.list_of_customers) # print the updated list_of_customers
            if status == False: # check if the status is still False
                print('no customers with this name ') # print a message that there is no customer with the given name

        elif type == 'seller': # check if the type parameter is seller
            for i in self.list_of_sellers: # loop through the list_of_sellers
                if i[1] == self.new: # check if the user name of the seller matches the new attribute
                    status = True # set the status to True
                    if action== 'add': # check if the action parameter is add
                        if self.new not in self.list_of_sellers: # check if the new attribute is not in the list_of_sellers
                            self.list_of_sellers.append(i) # append the seller to the list_of_sellers
                        else:
                            print('the seller already in the system') # print a message that the seller already exists
                    elif action == 'remove': # check if the action parameter is remove
                        self.list_of_sellers.remove(i) # remove the seller from the list_of_sellers
                    else:
                        print('error deleting the seller') # print a message that there is an error in deleting the seller
                    # print(self.list_of_sellers) # print the updated list_of_sellers
            if status == False: # check if the status is still False
                print('no seller with this name ') # print a message that there is no seller with the given name

        elif type == 'product': # check if the type parameter is product
            for i in self.list_of_products: # loop through the list_of_products
                if i[1] == self.new: # check if the product name of the product matches the new attribute
                    status = True # set the status to True
                    if action== 'add': # check if the action parameter is add
                        if self.new not in self.list_of_products: # check if the new attribute is not in the list_of_products
                            self.list_of_products.append(i) # append the product to the list_of_products
                        else:
                            print('the product already in the system') # print a message that the product already exists
                    elif action == 'remove': # check if the action parameter is remove
                        self.list_of_products.remove(i) # remove the product from the list_of_products
                    else:
                        print('error deleting the product') # print a message that there is an error in deleting the product
                    print(self.list_of_products) # print the updated list_of_products
            if status == False: # check if the status is still False
                print('no product with this name ') # print a message that there is no product with the given name
        Online_Marketplace.__init__(self,self.Marketplace_name,self.list_of_customers,self.list_of_sellers,self.list_of_products) # call the constructor method of the class with the updated attributes
class Product:  # define a class named Product
    products = []  # create a class attribute to store the product names
    productsWithinfo = {}  # create a class attribute to store the product details as a nested dictionary

    def __init__(self, productId, productName, description, price,
                 quantityInStock):  # define the constructor method for the class
        self.productId = productId  # assign the productId to the instance attribute
        self.productName = productName  # assign the productName to the instance attribute
        self.description = description  # assign the description to the instance attribute
        self.price = price  # assign the price to the instance attribute
        self.quantityInStock = quantityInStock  # assign the quantityInStock to the instance attribute

        if productId not in Product.products:  # check if the productId is not in the products list
            Product.products.append(self.productName)  # append the productName to the products list
            Product.productsWithinfo[
                self.productId] = []  # create an empty list for the productId key in the productsWithinfo dictionary

        Product.productsWithinfo[self.productId].extend([self.productName, self.description, self.price,self.quantityInStock])  # extend the list with the product details
    def display_product_info(self):  # define a method to display the product information
        print(
            f"Product ID: {self.productId}\nProductName: {self.productName}\nDescription: {self.description}\nPrice: {self.price}\nQuantity In Stock: {self.quantityInStock}.")  # print the product information with a formatted string

    def update_quantity(self):  # define a method to update the quantity in stock
        new_quantity = input("Enter new Quantity In Stock: ")  # get the new quantity from the input
        self.quantityInStock = int(new_quantity)  # assign the new quantity to the instance attribute
class ShoppingCart():  # define a class named ShoppingCart

    items = []

    def init(self):
        pass

    def add_item(self):
        while True:
            product = input("Enter Product and type 'done' to finish: ")
            if product.lower() != "done":
                ShoppingCart.items.append(product.lower())

            else:
                break
        return ShoppingCart.items  # return the items list

    def display_cart(self):
        print("Products in the cart:")
        for product in ShoppingCart.items:
            print(product)
    def calculate_total_cost(self):  # define a method to calculate the total cost of the items in the cart
        sum = 0  # initialize a variable to store the sum
        for product_id, product_info in Product.productsWithinfo.items():  # loop through the items of the productsWithinfo dictionary

            product_name = product_info[0]  # get the product name from the product info list
            product_price = product_info[2]  # get the product price from the product info list
            for product in ShoppingCart.items:  # loop through the items list
                if product in product_name:  # check if the product name matches the product in the items list
                    sum += product_price  # add the product price to the sum

        return sum  # return the sum
#########################################################
class Payment():  # define a class named Payment

    def __init__(self, payment_id, order_id, payment_method,payment_status):  # define the constructor method for the class
        self.order_id = order_id  # assign the order_id to the instance attribute
        self.payment_id = payment_id  # assign the payment_id to the instance attribute
        self.payment_method = payment_method  # assign the payment_method to the instance attribute
        self.payment_status = payment_status  # assign the payment_status to the instance attribute

    def process_payment(self):  # define a method to process the payment
        # the logic for processing the payment here
        # and update the payment status based on the response
        while True:  # start an infinite loop
            payment = input(
                "What type of payment you want.\n Choose the payment type: (cash or visa)")  # get the payment type from the input
            if payment.lower() == 'cash':  # check if the payment type is cash
                return 'Payment processed successfully!'  # return a success message
            elif payment.lower() == 'visa':  # check if the payment type is visa
                return 'Payment processed successfully!'  # return a success message
            else:  # check if the payment type is something else
                print("Error please Choose the payment type: (cash or visa): ")  # print an error message
                continue  # continue the loop
    def update_payment_status(self, new_status):
        self.payment_status = new_status
        print(f"Payment status updated to {new_status} for Payment ID {self.payment_id}")
