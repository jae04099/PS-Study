# 생각한 풀이법
# 스트링으로 받고 리스트로 만듬
# 정렬 한다.
# 1이 시작되는 지점을 찾는다. 이전이 0이고 현재 1이면 됨.
# 1이 시작되는 지점부터 끝까지 1일테니 그 숫자를 리턴
# 0이라면 start를 다음부터 설정
# 1이라면(전이 0도 아니라면) end를 이전부터 설정


# def binsearch(n):
#     str_n = str(n)
#     sort_list = list(map(int, sorted(list(str_n))))
#     start, end = 0, len(sort_list) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if sort_list[mid] == 1 and sort_list[mid - 1] == 0:
#             return len(sort_list) - mid
#         else:
#             if sort_list[mid] == 0:
#                 start = mid + 1
#             else:
#                 end = mid - 1
# print(binsearch(byte(00000000000111)))

# binary string을 받는다는데 
# def hammingWeight(self, n: int) -> int:
#         str_n = str(n)
#         sort_list = list(map(int, sorted(list(str_n))))
#         start, end = 0, len(sort_list) - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if sort_list[mid] == 1 and sort_list[mid - 1] == 0:
#                 return len(sort_list) - mid
#             else:
#                 if sort_list[mid] == 0:
#                     start = mid + 1
#                 else:
#                     end = mid - 1
# print(hammingWeight(0,100010101100))

def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')

# 바이너리가 바이너리 서치가 아니고 이진법인 것 같습니다...