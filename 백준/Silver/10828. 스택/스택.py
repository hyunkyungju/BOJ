import sys


'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

input = sys.stdin.readline

n = int(input())
st = list()
commands = ["push", "pop", "size", "empty", "top"]
for _ in range(n):
  s = input()
  if s.startswith("push"):
    st.append(int(s.lstrip("push ")))
  elif s.startswith("pop"):
    if st:
      print(st.pop())
    else:
      print(-1)
  elif s.startswith("size"):
    print(len(st))
  elif s.startswith("empty"):
    if st:
      print(0)
    else:
      print(1)
  else:
    if st:
      print(st[-1])
    else:
      print(-1)
    
