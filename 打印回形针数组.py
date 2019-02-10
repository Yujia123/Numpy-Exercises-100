# 打印回形针（蛇形）数组
# import numpy as np
# num = 5
# k = 1
# a = np.zeros((num, num))
# for i in range(num//2):
    
#     j1 = i
#     for j1 in range(num-i):   # 遍历最上面一行
#         a[i][j1] = k
#         k += 1
        
#     j2 = i+1
#     while j2 <num-i:   # 遍历最右边一列
#         a[j2][num-i-1] = k
#         k += 1
#         j2 += 1
        
#     j3 = num-2-i
#     while j3>=i:    # 遍历最下面一行
#         a[num-i-1][j3] = k
#         k += 1
#         j3 -= 1
        
#     j4 = num-i-2
#     while j4>i:    # 遍历最左边一列
#         a[j4][i] = k
#         k += 1
#         j4 -= 1
    
# if num%2 == 1:   # 如果输入的数是奇数
#     a[num//2][num//2] = k  # 为最后一个数赋值
    
# print(a)




