Test.describe("Basic tests")
Test.assert_equals(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
Test.assert_equals(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
Test.assert_equals(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
Test.assert_equals(triple_trouble("Bm", "aa", "tn"), "Batman")
Test.assert_equals(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")
E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

def triple_trouble(one, two, three):
    return ''.join(''.join(sub) for sub in zip(one, two, three))
