# 4 Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is 
# the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day 
# to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        sell = sell + 1
    return max_profit

prices = [7,1,5,3,6,4]
print("max_profit :",maxProfit(prices))



# Non working solution 
prices = [7,1,5,3,6,4]
def list_to_pair_list(list):
    res = [((i), (i + 1) % len(list)) for i in range(len(list))]
    return res

def Best_time(price_list):
    profit_list=[]
    list_result=[]
    index_list = []
    for i in price_list:
        for j in range(1,len(price_list),1):
            profit_list.append(i-price_list[j])
            index_I = price_list.index(i)
            index_J = price_list[j]
            index_list.append(index_I)
            index_list.append(index_J)
    # print("index_list",index_list)
    # print("index_list",list_to_pair_list(index_list))
    # print("len indexL",len(list_to_pair_list(index_list)))
    # print("max_profit =",max(profit_list))
    # print("len profitL",len(profit_list))
    return profit_list