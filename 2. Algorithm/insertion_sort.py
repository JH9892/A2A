# -----------------------------------
#   A2A Study
#   Algorithm - Insertion Sort
# -----------------------------------

# Insertion Sort
# 반복조건(xs != [])
#     xs[1:].sort (-> recursive)
#     xs[0]를 적절한 위치에 끼워넣는다.

#     head = smallest
#     tail = xs.sort
#     return xs

# 종료조건(xs==[])
#     return xs

# def insert(x, ss):
#     if ss!=[]:
#         if x<=ss[0]:
#             return [x] + ss
#         else:
#             return [ss[0]]+insert(x, ss[1:])
#     else:
#         return [x]

def insert(x, ss):
    if ss == [] or x<= ss[0]:
        return [x]+ss
    else:
        return [ss[0]]+insert(x, ss[1:])

def insertion_sort(xs):
    if xs!=[]:
        return insert(xs[0], insertion_sort(xs[1:]))
    else:
        return xs

# def insert_T(x, ss):
#     def loop(ss, left):
#         if ss!=[]:
#             if x <= ss[0]:
#                 left.append(x)
#                 return left +  ss
#             else:
#                 left.append(ss[0])
#                 return loop(ss[1:], left)
#         else:
#             left.append(x)
#             return left
#     return loop(ss, [])

def insert_T(x, ss):
    def loop(ss, left):
        if ss == [] or x<= ss[0]:
            left.append(x)
            return left + ss
        else:
            left.append(ss[0])
            return loop(ss[1:], left)
    
    return loop(ss, [])

def insertion_sort_T(xs):
    pass

def insert_W(x, ss):
    pass

def insertion_sort_W(xs):
    pass