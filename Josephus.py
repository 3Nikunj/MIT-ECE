# # lt = [1,2,3,4,5,6,7]
# # k = 3

# # n  = len(lt)
# # i = 0
# # while len(lt) > 1:
# #     i = (i + (k-1)) % len(lt)
# #     lt.pop(i)

# # print(lt[0])



# # With Recurrsion

# lt = [1,2,3,4,5,6,7]
# k = 3 

# def josephus(lt, cur):
#     if len(lt) == 1:
#         return lt[0]

#     cur = (cur +(k-1)) % len(lt)
#     lt.pop(cur)
#     return josephus(lt, cur)

# print(josephus(lt, 0))