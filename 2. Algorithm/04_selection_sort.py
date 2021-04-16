# -----------------------------------
#   A2A Study
#   Algorithm - Selection Sort
# -----------------------------------

# Selection Sort
# 반복조건(xs != [])
#     smallest = min(xs)
#     xs.remove(smallest)
#     xs.sort (-> recursive)

#     head = smallest
#     tail = xs.sort
#     return xs

# 종료조건(xs==[])
#     return xs

# 사용되는 메모리 공간이 입력되는 list길이에 비례.
# 즉, 공간복잡도가 O(n)
def selection_sort(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selection_sort(xs)
    else:
        return []

# 꼬리 재귀로 구현한 선택정렬
def selection_sort_T(xs):
    def loop(xs, ss):
        if xs!=[]:
            smallest = min(xs)
            xs.remove(smallest)
            ss.append(smallest)
            # return loop(xs, ss+[smallest])
            return loop(xs, ss)
        else:
            return ss
    return loop(xs, [])

# 반복문으로 구현한 선택정렬
def selection_sort_W(xs):
    ss = []
    while xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        ss.append(smallest)
    return ss


#-----------------------------------------
# python list의 remove()를 오버라이딩 해보자!
#-----------------------------------------
# 1. list.remove(x)를 하면 list에서 가장 처음 나타나는 x를 제거.
# 2. 단, 제거할 대상이 없는 경우 에러를 내는 것이 아니라 그냥 그대로 유지.
    # - params : 리스트xs와 리스트에서 제거할 원소
    # - return : 리스트에서 제거할 원소가 제거된 리스트

def remove_overriding(xs, v):
    if xs != []:
        if xs[0] == v:
            # print("xs!=[] and xs[0] == v -> ", xs)
            return xs[1:]
        else:
            # print("xs!=[] and xs[0] != v -> ", xs)
            return [xs[0]]+remove_overriding(xs[1:], v)
    else:
        # print("xs==[] -> ", xs)
        return xs


def remove_proc(xs, v):
    xs[:] = remove(xs, v)


if __name__=="__main__":
    lx = [1,2,3,4,5]
    print(min(lx))
    # result = 1
    print(min(lx, key=(lambda x:x)))
    # result = 1
    lx = remove_overriding(lx, 5)
    print(lx)