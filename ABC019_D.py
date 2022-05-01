import io
import sys

_INPUT = """\
1
2
1
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  a=1
  d=0
  for i in range(N-1):
    print("? {0} {1}".format(1, i+2))
    dist = int(input())
    if dist>d: a=i+2; d=dist
  b=a
  d=0
  for i in range(N):
    if b!=i+1:
      print("? {0} {1}".format(b, i+1))
      dist = int(input())
      if dist>d: d=dist
  print('!',d)