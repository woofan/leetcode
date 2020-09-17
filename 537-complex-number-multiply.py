class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_cmp = a.split("+")
        b_cmp = b.split("+")
        part1 = int(a_cmp[0]) * int(b_cmp[0])
        part2 = int(a_cmp[0]) * int(b_cmp[1].replace('i',''))
        part3 = int(a_cmp[1][:-1]) * int(b_cmp[0])
        part4 = - int(a_cmp[1].replace('i','')) * int(b_cmp[1].replace('i',''))
        res = str(part1 + part4) + '+' + str(part2 + part3) + 'i'