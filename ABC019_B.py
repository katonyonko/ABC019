import io
import sys

_INPUT = """\
6
aabbbaad
aabbbbbbbbbbbbxyza
edcba
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  s=input()
  ans=[]
  i=0
  while i<len(s):
    ans.append([s[i],1])
    while i+1<len(s) and s[i]==s[i+1]:
      ans[-1][1]+=1
      i+=1
    i+=1
  print(*[ans[i][0]+str(ans[i][1]) for i in range(len(ans))],sep='')