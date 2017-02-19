# # first attempt
#
# def pre_check(x, y):
#     if x < y:
#         return True
#     else:
#         return False
#
#
# def check_range(arr):
#     for x in arr:
#         if x > 2147483647 or x < -2147483647:
#             return False
#
#     return True
#
#
# def get_area(x1, y1, x2, y2):
#     return (x2 - x1) * (y2 - y1)
#
#
# def get_each_point(K, L, M, N):
#     return [Point(K, L), Point(K, N), Point(M, L), Point(M, N)]
#
#
# def check_each_point(point, P, Q, R, S):
#     if point.x < P or point.x > R:
#         return False
#     elif point.y < Q or point.y > S:
#         return False
#     else:
#         return True
#
#
# def check_cover(K, L, M, N, P, Q, R, S):
#     for p in get_each_point(K, L, M, N):
#         if check_each_point(p, P, Q, R, S):
#             return p
#
#     return None
#
#
# def get_cover_area(x1, y1, x2, y2):
#     area = get_area(x1, y1, x2, y2)
#     if area < 0:
#         return -area
#     else:
#         return area
#
#
# def pre_checks(K, L, M, N, P, Q, R, S):
#     if pre_check(K, M) and pre_check(L, N) and pre_check(P, R) and pre_check(Q, S) and check_range(
#             [K, L, M, N, P, Q, R, S]):
#         return True
#     else:
#         return False
#
#
# def solution(K, L, M, N, P, Q, R, S):
#     # write your code in Python 2.7
#     area = -1
#     if pre_checks(K, L, M, N, P, Q, R, S):
#         r1 = Rect(Point(K, L), Point(M, N))
#         r2 = Rect(Point(P, Q), Point(R, S))
#         area = r1.area() + r2.area()
#         r3 = Rect(check_cover(K, L, M, N, P, Q, R, S), check_cover(P, Q, R, S, K, L, M, N))
#         if r3.check():
#             area -= r3.area1()
#
#
#
# # final form( which is not so clear at that time)
#
# class Rect:
#     def __init__(self, point1, point2):
#         self.p1 = point1
#         self.p2 = point2
#
#     def area(self):
#         return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)
#
#     def check(self):
#         if self.p1 and self.p2:
#             return True
#         else:
#             return False
#
#     def area1(self):
#         area = self.area()
#         if area < 0:
#             return -area
#         else:
#             return area
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# def pre_check(x, y):
#     if x < y:
#         return True
#     else:
#         return False
#
#
# def check_range(arr):
#     for x in arr:
#         if x > 2147483647 or x < -2147483647:
#             return False
#
#     return True
#
#
# def get_area(x1, y1, x2, y2):
#     return (x2 - x1) * (y2 - y1)
#
#
# def get_each_point(K, L, M, N):
#     return [Point(K, L), Point(K, N), Point(M, L), Point(M, N)]
#
#
# def check_each_point(point, P, Q, R, S):
#     if point.x < P or point.x > R:
#         return False
#     elif point.y < Q or point.y > S:
#         return False
#     else:
#         return True
#
#
# def check_cover(K, L, M, N, P, Q, R, S):
#     for p in get_each_point(K, L, M, N):
#         if check_each_point(p, P, Q, R, S):
#             return p
#
#     return None
#
#
# def get_cover_area(x1, y1, x2, y2):
#     area = get_area(x1, y1, x2, y2)
#     if area < 0:
#         return -area
#     else:
#         return area
#
#
# def pre_checks(K, L, M, N, P, Q, R, S):
#     if pre_check(K, M) and pre_check(L, N) and pre_check(P, R) and pre_check(Q, S) and check_range(
#             [K, L, M, N, P, Q, R, S]):
#         return True
#     else:
#         return False
#
#
# def solution(K, L, M, N, P, Q, R, S):
#     # write your code in Python 2.7
#     area = -1
#     if pre_checks(K, L, M, N, P, Q, R, S):
#         r1 = Rect(Point(K, L), Point(M, N))
#         r2 = Rect(Point(P, Q), Point(R, S))
#         area = r1.area() + r2.area()
#         r3 = Rect(check_cover(K, L, M, N, P, Q, R, S), check_cover(P, Q, R, S, K, L, M, N))
#         if r3.check():
#             area -= r3.area1()
#
#     return area

class Rect:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
        self.p3 = Point(self.p1.x, self.p2.y)
        self.p4 = Point(self.p2.x, self.p1.y)
        self.all_points = [self.p1, self.p2, self.p3, self.p4]

    def area(self):
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)

    def check(self):
        if self.p1 and self.p2:
            return True
        else:
            return False

    def cover_area(self):
        area = self.area()
        if area < 0:
            return -area
        else:
            return area

    def get_each_point(self):
        return self.all_points

    def check_each_point(self, point):
        if point.x < self.p1.x or point.x > self.p2.x:
            return False
        elif point.y < self.p1.y or point.y > self.p2.y:
            return False
        else:
            return True


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def pre_check(x, y):
    if x < y:
        return True
    else:
        return False


def check_range(arr):
    for x in arr:
        if x > 2147483647 or x < -2147483647:
            return False

    return True


def check_cover(r1, r2):
    for p in r1.get_each_point():
        if r2.check_each_point(p):
            return p

    return None


def pre_checks(K, L, M, N, P, Q, R, S):
    if pre_check(K, M) and pre_check(L, N) and pre_check(P, R) and pre_check(Q, S) and check_range(
            [K, L, M, N, P, Q, R, S]):
        return True
    else:
        return False


def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 2.7
    area = -1
    if pre_checks(K, L, M, N, P, Q, R, S):
        r1 = Rect(Point(K, L), Point(M, N))
        r2 = Rect(Point(P, Q), Point(R, S))
        area = r1.area() + r2.area()
        r3 = Rect(check_cover(r1, r2), check_cover(r2, r1))
        if r3.check():
            area -= r3.cover_area()

    return area
