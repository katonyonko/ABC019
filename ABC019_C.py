import io
import sys

_INPUT = """\
6
3
1 2 3
4
2 4 8 16
4
2 3 5 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  ans=set()
  for i in range(N):
    t=A[i]
    while t%2==0: t//=2
    ans.add(t)
  print(len(ans))