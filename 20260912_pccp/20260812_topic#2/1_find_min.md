Mảng A và B có cùng độ dài N
tìm tổng S nhỏ nhất

S = sum(A[i] * B[j])

với mọi phần tử trong 2 mảng

và nếu đã chọn số thứ k trong mảng rồi thì không được chọn lại nữa

ví dụ #1:
A = [1, 4, 2]
B = [5, 4, 4]
S = 1x5 + 4x4 + 2x4 = 5 + 16 + 8 = 29 là tổng nhỏ nhất

ví dụ #2:
A = [1, 2]
B = [3, 4]
S = 1x4 + 2x3 = 10

điều kiện :
N = len(A) = len(B)
1 <= N <= 1000
1 <= A[i], B[i] <= 1000



