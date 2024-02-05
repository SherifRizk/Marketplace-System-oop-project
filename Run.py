from Classes import User, Customer, Online_Marketplace, Order, ShoppingCart, Payment, \
    Product  # import the classes from the first module

print("*************************************************")  # print a line of asterisks
print("           Welcome to Our Market System           ")  # print a welcome message
print("*************************************************")  # print another line of asterisks
m = Online_Marketplace('marhaba', [], [], \
                       [[1, "meat", "It's meat.", 180, 150], [2, "rice", "It's Rice.", 30, 100],[6, "oil", "It's oil.", 40, 80],[6, "tomato", "It's tomato.", 40,80]])  # create an Online_Marketplace object with the given name and lists of customers, sellers, and products

print("Please regitser or If you have acount , login")  # print a message to prompt the user to register or login
inputs = input("choose login or register  :")  # get the user input for the choice
while True :
    if inputs.lower() == "register":  # check if the user input is register
        customer1 = Customer()  # create a Customer object with the default values
        print(
            f"                Hello {customer1.user_name} you ready to login !!            ")  # print a message to greet the customer and ask for login
        User.logining()  # call the login method of the customer object
        print("       Successfully Login    ")  # print a message to confirm the login
        print("*************************************************")  # print a line of asterisks
        print("                 Market Products                  ")  # print a message to show the market products
        print("*************************************************")  # print another line of asterisks

        Answer = input(" ready to start shopping ? yes or no ")  # get the user input for the shopping
        if Answer == "yes":  # check if the user input is yes
            print(
                "**************************************************************************************************************")  # print a long line of asterisks
            print(
                "          Please Enter your products and Enter done when you finished shoping       ")  # print a message to instruct the user to enter the products and done
            print(
                "**************************************************************************************************************")  # print another long line of asterisks
            sc = ShoppingCart()  # create a ShoppingCart object
            # meet = Product(1, "meat", "It's meet.", 180, 150)  # create a Product object for meat
            # rice = Product(2, "rice", "It's Rice.", 30, 100)  # create a Product object for rice
            # oil = Product(6, "oil", "It's oil.", 40, 80)  # create a Product object for oil

            print("Products and Price: ",Product.productsWithinfo)  # print the products and price from the productsWithinfo dictionary
            sc.add_item()  # call the add_item method of the shopping cart object
            # print(sc.calculate_total_cost()) # print the total cost of the items in the cart
            order = Order(9, customer1.user_name, sc.items, sc.calculate_total_cost(),'Pending')  # create an Order object with the given id, customer name, items, total cost, and status

            if order.place_order() == "Order placed successfully.":  # check if the order is placed successfully
                payment1 = Payment(1, order.order_id, 'cash','Pending')  # create a Payment object with the given id, order id, method, and status
                print(payment1.process_payment())  # print the result of processing the payment
                print('*' * 40)  # print a line of asterisks
                print("Your Order details")  # print a message to show the order details
                order.view_order_details()  # view the order details
                sc.calculate_total_cost()  # calculate the total cost of the items in the cart
                break
            else:  # check if the order is something else
                print("Order not placed")  # print a message to indicate the order is not placed
                print(order.cancel_order())  # print the result of canceling the order
                break
        else:  # check if the user input is not yes
            print("Products and Price: ",Product.productsWithinfo)  # print the products and price from the productsWithinfo dictionary

    elif inputs.lower() == "login":  # check if the user input is login

        User.logining()  # call the login method of the User class
        print("       Successfully Login    ")  # print a message to confirm the login
        print("*************************************************")  # print a line of asterisks
        print("                 Market Products                  ")  # print a message to show the market products
        print("*************************************************")  # print another line of asterisks

        Answer = input(" ready to start shopping ? yes or no ")  # get the user input for the shopping
        if Answer == "yes":  # check if the user input is yes
            if Answer == "yes":  # check if the user input is yes
                print(
                    "**************************************************************************************************************")  # print a long line of asterisks
                print(
                    "          Please Enter your products and Enter done when you finished shoping       ")  # print a message to instruct the user to enter the products and done
                print(
                    "**************************************************************************************************************")  # print another long line of asterisks
                sc = ShoppingCart()  # create a ShoppingCart object
                meet = Product(1, "meat", "It's meet.", 180, 150)  # create a Product object for meat
                rice = Product(2, "rice", "It's Rice.", 30, 100)  # create a Product object for rice
                oil = Product(6, "oil", "It's oil.", 40, 80)  # create a Product object for oil

                print("Products and Price: ",
                    Product.productsWithinfo)  # print the products and price from the productsWithinfo dictionary
                sc.add_item()  # call the add_item method of the shopping cart object
                # print(sc.calculate_total_cost()) # print the total cost of the items in the cart
                order = Order(9," ", sc.items, sc.calculate_total_cost(),'Pending')  # create an Order object with the given id, customer name, items, total cost, and status

                
                if order.place_order() == "Order placed successfully.":  # check if the order is placed successfully
                    payment1 = Payment(1, order.order_id, 'cash','Pending')  # create a Payment object with the given id, order id, method, and status
                    print(payment1.process_payment())  # print the result of processing the payment
                    print('*' * 40)  # print a line of asterisks
                    print("Your Order details")  # print a message to show the order details
                    order.view_order_details()  # view the order details
                    sc.calculate_total_cost()  # calculate the total cost of the items in the cart
                    break
                else:  # check if the order is something else
                    print("Order not placed")  # print a message to indicate the order is not placed
                    print(order.cancel_order())  # print the result of canceling the order
                    break


            else:  # check if the user input is not yes
                print("Products and Price: ",Product.productsWithinfo)  # print the products and price from the productsWithinfo dictionary
    else :
        print("Please regitser or If you have acount , login")  # print a message to prompt the user to register or login
        inputs = input("choose login or register  :")  # get the user input for the choice 
        continue