import io
import sys

_INPUT = """\
6
2 3 4
5 100 5
3 3 3
3 3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a=list(map(int,input().split()))
  a.sort()
  print(a[1])