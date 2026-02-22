from collections import defaultdict
from typing import List
def invalidTransactions(self, transactions: List[str]) -> List[str]:
    mostRecentTransaction = defaultdict(list)
    answerIndices = set()
    for transactionIndex in range(len(transactions)):
        name, time, amount, city = transactions[transactionIndex].split(",")
        if int(amount) > 1000:
            answerIndices.add(transactionIndex)
        if mostRecentTransaction[name]:
            for fruadsterPaymentIndex in mostRecentTransaction[name]:
                _, prevTime, _, prevCity, = transactions[fruadsterPaymentIndex].split(",")
                if abs(int(time) - int(prevTime)) <= 60 and not city == prevCity:
                    answerIndices.add(fruadsterPaymentIndex)
                    answerIndices.add(transactionIndex)
        mostRecentTransaction[name].append(transactionIndex)
    answer = []
    for index in answerIndices:
        answer.append(transactions[index])
    return answer