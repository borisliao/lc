class Naive:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        for letter in t:
            if letter not in s:
                return False
            
        return True

# Examples
solutions = [Naive()]

def assert_solutions(s, t, output):
    for solution in solutions: 
        assert solution.isAnagram(s, t) == output

def test_example_1():
    s = "anagram"
    t = "nagaram"
    output = True
    
    assert_solutions(s, t, output)

def test_example_2():
    s = "rat"
    t = "car"
    output = False
    
    assert_solutions(s, t, output)

# LC test cases

def test_lc_34():
    s = "aacc"
    t = "ccac"
    output = False
    
    assert_solutions(s, t, output)
