Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"

----------------------------------------------------------------

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
    
    
 =================================================================
def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])
    
==================================================================
def DNA_strand(dna):
  return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])
 
===================================================================
import string

TABLE = string.maketrans('ATCG', 'TAGC')


def DNA_strand(dna):
    return dna.translate(TABLE)
===================================================================
将一个字符串的大写换成小写，小写换成大写
"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"

def to_alternating_case(string):
    return string.swapcase()

