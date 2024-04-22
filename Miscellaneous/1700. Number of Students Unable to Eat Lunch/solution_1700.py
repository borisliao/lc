from collections import Counter, deque


def lunch(students, sandwiches):
    """
    Mochi 4-21-24
    """
    students = deque(students)
    sandwiches = deque(sandwiches)

    while students:
        prev = students.copy()
        for _ in range(len(students)):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                s = students.popleft()
                students.append(s)
        if students == prev:
            return len(students)
    return 0


def neetcode(students: list[int], sandwiches: list[int]) -> int:
    result = len(students)
    count = Counter(students)

    for s in sandwiches:
        if count[s] > 0:
            result -= 1
            count[s] -= 1
        else:
            return result
    return 0
