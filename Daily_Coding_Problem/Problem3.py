# Problem #16

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API :
# - record(order_id): adds the order_id to the log
# - get_last(i): gets the ith last element from the log. i is guaranteed
#                to be smaller than or equal to N.

# You should be as efficient with time and space as possible.

class Order:
    def __init__(self):
        # self --> used to access variables
        # that belong to the class
        # We initialise an empty orders list
        self.order_ids_log = []

    # This Function adds order_id to the log
    def record(self, order_id):
        return self.order_ids_log.append(order_id)

    # this function return the id of the last log
    def get_last(self, i):
        return self.order_ids_log[-(1+i)]

if __name__=="__main__":
    # Initiating the class Order --> to eCommerceOrders
    # Which initiates the order_ids_log at the same time
    eCommerceOrders = Order()

    # add order ids to the list eCommerce
    # adds 100 orders to the log
    for j in range(1, 101):
        eCommerceOrders.record(j)

    # returns 50
    Api_command = eCommerceOrders.get_last(50)
    print(Api_command)

    # returns 90
    Api_command2 = eCommerceOrders.get_last(10)
    print(Api_command2)
