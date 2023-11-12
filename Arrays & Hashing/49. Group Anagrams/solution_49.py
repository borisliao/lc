from collections import defaultdict
from typing import List


def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


def review1(strs):
    """
    https://www.youtube.com/watch?v=vzdNOK2oB2E
    Anki review 10/17/23
    """
    anagram_sets = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord("a")] += 1
        anagram_sets[tuple(count)].append(word)

    return anagram_sets.values()


def review2(strs):
    """
    Anki review 10/18/23
    """
    groups = {}
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        if tuple(count) in groups:
            groups[tuple(count)].append(count)
        else:
            groups[tuple(count)] = [word]
    return groups.values()


def review3(strs):
    """
    Anki review 10/18/23
    same as first solution above
    """
    groups = {}
    for word in strs:
        if ''.join(sorted(word)) in groups:
            groups[''.join(sorted(word))].append(word)
        else:
            groups[''.join(sorted(word))] = [word]
    return groups.values()


def review4(strs: List[str]) -> List[List[str]]:
    """
    Anki 11-12-23
    Time: 20 min
    """
    anagrams = defaultdict(list)

    for s in strs:
        hash = [0] * 26
        for c in s:
            hash[ord(c) - ord('a')] += 1
        anagrams[tuple(hash)].append(s)

    return anagrams.values()
