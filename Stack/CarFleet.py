import math
def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    fleets = []
    cars_with_speed = list(zip(position, speed))
    cars_with_speed.sort(key=lambda x: x[0], reverse=True)
    for position, speed in cars_with_speed:
        eta = (target-position) / speed
        if not fleets or fleets[-1] < eta:
            fleets.append(eta)
    return len(fleets)

print(carFleet(10, [6,8], [3,2]))