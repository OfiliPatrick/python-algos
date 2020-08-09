test = [['Anne', 100, 1, "Boston"],
        ['Anne', 2000, 10, "Boston"],
        ['Bob', 50, 20, "Boston"],
        ['Cindy', 100, 50, "New York"],
        ['Bob', 50, 70, "New York"]

]

name = 0
price = 1
time = 2
location = 3

result = []
history = {}

def fraud(transactions):
    for i in range(len(transactions)):
        transaction = transactions[i]
        
        if transaction[price] > 1000:
            result.append(transaction)

        if transaction[name] in history:
            user_data = history[transaction[name]]

            user_time = user_data[2]
            user_location = user_data[3]

            if (transaction[time] - user_time) <= 60 and user_location != transaction[location]:
                result.append(transaction)
                result.append(transactions[user_data[4]])
                
        transaction.append(i)
        history[transaction[name]] = transaction

    return result

print(fraud(test))


        




