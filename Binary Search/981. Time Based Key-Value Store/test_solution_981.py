from random import random
import pytest
import inspect
import solution_981


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_981, predicate=inspect.isfunction)])
def test_example_1(f):
    timeMap = f()

    # store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.set("foo", "bar", 1)

    # return "bar"
    assert timeMap.get("foo", 1) == "bar"

    # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    assert timeMap.get("foo", 3) == "bar"

    # store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.set("foo", "bar2", 4)

    assert timeMap.get("foo", 4) == "bar2"  # return "bar2"
    assert timeMap.get("foo", 5) == "bar2"  # return "bar2"


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_981, predicate=inspect.isfunction)])
def test_lc_2(f):
    timeMap = f()

    timeMap.set("ctondw", "ztpearaw", 1)
    timeMap.set("vrobykydll", "hwliiq", 2)
    timeMap.set("gszaw", "ztpearaw", 3)
    timeMap.set("ctondw", "gszaw", 4)
    assert timeMap.get("gszaw", 5) == "ztpearaw"
    assert timeMap.get("ctondw", 6) == "gszaw"
    assert timeMap.get("ctondw", 7) == "gszaw"
    assert timeMap.get("gszaw", 8) == "ztpearaw"
    assert timeMap.get("vrobykydll", 9) == "hwliiq"
    assert timeMap.get("ctondw", 10) == "gszaw"
    timeMap.set("vrobykydll", "kcvcjzzwx", 11)
    assert timeMap.get("vrobykydll", 12) == "kcvcjzzwx"
    assert timeMap.get("ctondw", 13) == "gszaw"
    assert timeMap.get("vrobykydll", 14) == "kcvcjzzwx"
    timeMap.set("ztpearaw", "zondoubtib", 15)
    timeMap.set("kcvcjzzwx", "hwliiq", 16)
    timeMap.set("wtgbfvg", "vrobykydll", 17)
    timeMap.set("hwliiq", "gzsiivks", 18)
    assert timeMap.get("kcvcjzzwx", 19) == "hwliiq"
    assert timeMap.get("ztpearaw", 20) == "zondoubtib"


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_981, predicate=inspect.isfunction)])
def test_lc_30(f):
    timeMap = f()

    timeMap.set("rtzoj", "kuexwze", 1)
    timeMap.set("xcywxndnz", "herqmazp", 2)
    assert timeMap.get("xcywxndnz", 3) == "herqmazp"
    timeMap.set("rtzoj", "dgpguflin", 4)
    assert timeMap.get("xcywxndnz", 5) == "herqmazp"
    timeMap.set("dgpguflin", "lvrexco", 6)
    timeMap.set("xcywxndnz", "dgpguflin", 7)
    assert timeMap.get("xcywxndnz", 8) == "dgpguflin"
    timeMap.set("rtzoj", "wxqixmxs", 9)
    assert timeMap.get("xcywxndnz", 10) == "dgpguflin"
    timeMap.set("kuexwze", "lvrexco", 11)
    assert timeMap.get("dgpguflin", 12) == "lvrexco"
    timeMap.set("lvrexco", "wxqixmxs", 13)
    assert timeMap.get("xcywxndnz", 14) == "dgpguflin"
    timeMap.set("herqmazp", "vjfhio", 15)
    assert timeMap.get("dgpguflin", 16) == "lvrexco"
    assert timeMap.get("herqmazp", 17) == "vjfhio"
    assert timeMap.get("herqmazp", 18) == "vjfhio"
    assert timeMap.get("rtzoj", 19) == "wxqixmxs"
    assert timeMap.get("herqmazp", 20) == "vjfhio"
    assert timeMap.get("herqmazp", 21) == "vjfhio"
    timeMap.set("kuexwze", "vjfhio", 22)
    timeMap.set("dgpguflin", "qrkihrb", 23)
    timeMap.set("kuexwze", "dgpguflin", 24)
    assert timeMap.get("rtzoj", 25) == "wxqixmxs"
    assert timeMap.get("dgpguflin", 26) == "qrkihrb"
    timeMap.set("herqmazp", "rtzoj", 27)
    timeMap.set("lvrexco", "iztpo", 28)
    assert timeMap.get("lvrexco", 29) == "iztpo"
    timeMap.set("kuexwze", "lvrexco", 30)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_981, predicate=inspect.isfunction)])
# This is an aproximated test, see stress_test_lc_44.py for the full test
def test_lc_44(f):
    timeMap = f()
    timeMap.set("pp", "pp", 0)

    for i in range(1, 120001):
        if random() < 0.5:
            timeMap.set("pp", "pp", i)
        else:
            assert timeMap.get("pp", i) == "pp"


@pytest.mark.timeout(3)
@pytest.mark.parametrize("f", [f[1] for f in inspect.getmembers(solution_981, predicate=inspect.isfunction)])
def test_lc_46(f):
    timeMap = f()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    assert timeMap.get("love", 5) == ""
    assert timeMap.get("love", 10) == "high"
    assert timeMap.get("love", 15) == "high"
    assert timeMap.get("love", 20) == "low"
    assert timeMap.get("love", 25) == "low"
