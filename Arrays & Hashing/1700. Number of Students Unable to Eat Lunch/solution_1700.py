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


def review1(students: list[int], sandwiches: list[int]) -> int:
    amount = {1: 0, 0: 0}
    for s in students:
        amount[s] += 1

    for sw in sandwiches:
        if amount[sw] == 0:
            return amount[1-sw]
        amount[sw] -= 1
    return 0


def review2(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 4-22-24
    """
    count = Counter(students)

    for s in sandwiches:
        if count[s] == 0:
            return count[1-s]
        count[s] -= 1
    return 0


def review3(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 4-24-24
    """
    count = {}

    for s in students:
        count[s] = 1 + count.get(s, 0)

    for s in sandwiches:
        count[s] = count.get(s, 0) - 1
        if count[s] < 0:
            return count[1 - s]

    return 0


def review4(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 6-23-24
    """
    count = {}

    for s in students:
        count[s] = 1+count.get(s, 0)

    for s in sandwiches:
        count[s] = count.get(s, 0)-1
        if count[s] < 0:
            return count[1-s]

    return 0


def review5(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 10-5-24
    This solution is not optimal.
    We do not need to do a full simulation, as only the order of the sandwiches matter, not the students.
    """
    prevStudents = []
    while students != prevStudents:
        prevStudents = students
        if students:
            if sandwiches[0] == students[0]:
                sandwiches = sandwiches[1:]
                students = students[1:]
            else:
                students = students[1:] + students[:1]  # d1 students[0]

    return len(students)


def review6(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 10-5-24
    """
    count = [0, 0]
    for s in students:
        count[s] += 1

    for f in sandwiches:
        if count[f] == 0:
            return count[abs(f-1)]
        else:
            count[f] -= 1

    return 0


def review7(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 10-9-24
    """
    count = {0: 0, 1: 0}

    for s in students:
        count[s] += 1

    for s in sandwiches:
        if count[s]:
            count[s] -= 1
        else:
            return count[abs(s-1)]
    return max(count.values())


def review8(students: list[int], sandwiches: list[int]) -> int:
    """
    Mochi 12-1-24
    """
    st = {0: 0, 1: 0}
    for s in students:
        st[s] += 1

    for sw in sandwiches:
        if st[sw] > 0:
            st[sw] -= 1
        else:
            return st[abs(sw-1)]

    return 0
