# from collections import defaultdict


# def carFleet(target: int, position: list[int], speed: list[int]) -> int:
#     """
#     Anki 1-8-24
#     Time: 2h
#     Used: debugger 3
#     """
#     in_target = 0
#     fleets = 0
#     car = []
#     for i in range(len(position)):
#         if position[i] >= target:
#             in_target += 1
#         car.append([position[i], speed[i]])
#     car.sort()

#     while in_target < len(position):  # d3 len(car)
#         i = len(car) - 1  # d1 moved in while loop
#         while i >= 0:
#             car[i][0] += 1
#             if i != len(car) - 1:
#                 car[i][0] = min(car[i][0], car[i+1][0])  # d3 car[i+1]
#             i -= 1

#         distance = set()
#         while car and car[-1][0] >= target:  # d2 car and
#             c = car.pop()
#             distance.add(c[0])
#             in_target += 1
#         fleets += len(distance)

#     return fleets


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    # Sort cars by position in descending order
    cars = sorted(zip(position, speed), reverse=True)
    time_taken = [float(target - p) / s for p, s in cars]

    fleets = 0
    while len(time_taken) > 1:
        lead_time = time_taken.pop(0)
        if lead_time < time_taken[0]:
            fleets += 1
        else:
            time_taken[0] = lead_time  # Update the next car's arrival time

    return fleets + bool(time_taken)  # Add 1 if there's any remaining car


def neetcode(target: int, position: list[int], speed: list[int]) -> int:
    """
    1-8-24
    [Car Fleet - Leetcode 853 - Python](https://www.youtube.com/watch?v=Pr6T-3yB9RM)
    """
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


def review1(target: int, position: list[int], speed: list[int]) -> int:
    """
    Anki 1-9-24
    Used: [Car Fleet - Leetcode 853 - Python](https://www.youtube.com/watch?v=Pr6T-3yB9RM)
    """
    cars = [(p, s) for p, s in zip(position, speed)]
    cars = sorted(cars, reverse=True)
    stack = []

    for p, s in cars:
        mph = (target - p) / s
        stack.append(mph)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


def review2(target: int, position: list[int], speed: list[int]) -> int:
    """
    Anki 1-9-24
    Time: 14 min
    """
    cars = [(p, s) for p, s in zip(position, speed)]
    # d2 seperate line, .sort returns None, making cars = None
    cars.sort(reverse=True)
    stack = []

    for p, s in cars:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:  # d1 len(stack)
            stack.pop()

    return len(stack)


# def review3(target: int, position: list[int], speed: list[int]) -> int:
#     """
#     Anki
#     """
