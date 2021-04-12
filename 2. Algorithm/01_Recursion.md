--- 
#   A2A Study
#   Algorithm - Recursive
--- 

## 구조 귀납(Structural Induction)
- 개념
    - 빈 리스트 []는 리스트이다.
    - x가 임의의 원소이고, xs가 임의의 리스트이면, x :: xs도 리스트이다.
    ( ps. 여기서 ::는 리스트 생성 연산자로 constructor라고 한다. 또한 x는 선두원소(head)라 하고 xs는 후미리스트(tail)라 한다.)
- 파이썬 문법
    - 빈 리스트 []는 리스트이다.
    - x가 임의의 원소이고, xs가 임의의 리스트이면, [x] + xs도 리스트이다.
    ( ps. 여기서 ::는 리스트 생성 연산자로 constructor라고 한다. 또한 x는 선두원소(head)라 하고 xs는 후미리스트(tail)라 한다.)

## Recursive란?
재귀(Recursive)는 하나의 함수를 정의하고 해당 함수내부에서 본인함수를 재호출하는 기법을 말한다.
즉, A라는 함수가 있다면 A함수안에서 다시 A함수를 부르는것이라 할 수 있다.

```python
def hello():
    print("Hello Recursion!")
    hello()

hello()
````

함수가 종료되지 않은 상태에서 본인을 호출하기 때문에 종료되지 않은 함수들이 계속해서 내부 Stack에 쌓이게 된다.
즉, 이는 과하게 많은 호출이 일어날 경우 stack memory가 overflow될 수 있다.
( 파이썬에선 이를 권하지도 않거니와 이러한 문제를 방지하기 위해 recursionlimit를 지정해놓았다. )

