# Python - list

**배열과 연결리스트** 

- 배열 : 여러데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조

  배열의 길이는 변경 불가능 -> 길이를 고정 하고 싶다면 새로 생성

  데이터 타입은 고정 

   

- 연결 리스트 : 데이터가 담신 여러 노드들이 순차 적으로 연결된 형태의 자료구조 

  맨처음 노드부터 순차적으로 탐색 

  연결리스트의 길이 자유롭게 변경 가능 -> 삽입 삭제가 편리 

  다양한 데이터 타입 저장 

  데이터가 메모리에 연속적으로 저장되지 않음 

**파이썬 리스트 메서드**

``` python
append() : 리스트 맨끝에 새로운 원소 삽입
a = [1,2,3]
a.append(4)
# a = [1,2,3,4] 

pop() : 특정 인덱스에 있는 원소를 삭제 반환 
a = [1,2,3]
b = a.pop()
#a = [1,2] b = 3
a = [1,2,3]
b = a.pop(1)
#a = [1,3] b = 2

count() : 리스트에서 해당 원소의 개수를 반환
a = [1,2,2,2,3,3,3,3,3]
print(a.count(2))
# 3

index() : 리스트에서 처음으로 원소가 등장하는 인덱스 반환
a = [1,2,3]
print(a.index(2))
# 1

sort() : 리스트를 오름차순으로 정렬 reverse = True  옵션을 통해 내림차순으로 정렬 
a = [5,2,4,0,-1]
a.sort()
print(a)
# [-1,0,2,4,5]
a.sort(reverse = True)
#[5,4,2,0,-1]

reverse() :리스트의 원소들의 순서를 거꾸로 뒤집기
a=[1,2,3,4,5]
a.reverse()
#[5,4,3,2,1]

```

**자주 쓰이는 리스트 관련 내장함수**

```python
len(iterable) : 리스트의 길이를 반환
a = [1,2,3,4,5]
len(a)
# 5

sum(iterable) : 리스트의 모근 원소의 합을 반환 
a = [1,2,3,4,5]
sum(a)
#15

max(iterable) : 리스트의 원소중 최대값을 반환 
a = [1,2,3,4,5]
max(a)
#5

min(iterable) : 리스트의 원소중 최소값을 반환 
a = [1,2,3,4,5]
min(a)
#1

sorted(iterable) : 오름차순으로 정렬된 새로운 리스트 반환 원본리스트는 변화 없음 
a = [5,2,-1,0,1]
b = sorted(a)
c = sorted(a, reverse =True)
# a = [5,2,-1,0,1]
# b = 오름차순 정렬 [-1,0,1,2,5]
# c = 내림차순 정렬 [5,2,1,0,-1]

```

**리스트 컴프리헨션**

``` python
numbers = []
for i in range(5):
    numbers.append(i)
    
numbers = [i for i in range(5)]

# 같은 결과 

odd_numbers = [i for i in range(10) if i%2 == 1]
#if문으로 필터링 가능
```

