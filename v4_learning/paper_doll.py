"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

def paper_doll(arg1):
    result = ''
    for i in arg1:
        result += (i * 3)
    return result

print(paper_doll('Hello'))