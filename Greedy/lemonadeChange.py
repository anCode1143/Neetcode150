from typing import List
def lemonadeChange(self, bills: List[int]) -> bool:
    tens = 0
    fives = 0
    for transaction in bills:
        if transaction == 5:
            fives += 1
        elif transaction == 10:
            fives -= 1
            tens += 1
            if fives < 0: return False
        else:
            if fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            elif fives >= 2:
                fives -= 2
            else:
                return False
    return True 