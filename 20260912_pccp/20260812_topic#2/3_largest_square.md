Giả sử có một bảng gồm các số 1 và 0. Mỗi ô trong bảng là một hình vuông kích thước 1x1. Hãy viết hàm để tìm hình vuông lớn nhất chỉ chứa các số 1 trong bảng và trả về kích thước của nó (hình vuông này phải có các cạnh song song với các trục tọa độ).

Ví dụ #1, giả sử bảng được cho như sau.

|Index | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 1 |
| **1** | 1 | 1 | 1 | 1 |
| **2** | 1 | 1 | 1 | 1 |
| **3** | 0 | 0 | 1 | 0 |

Trả về kích thước hình vuông là 9 (3x3)


Ví dụ #2
|Index | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 0 | 0 | 1 | 1 |
| **1** | 1 | 1 | 1 | 1 |
Trả về kích thước hình vuông là 4 (2x2)

Các ràng buộc
Bảng được biểu diễn dưới dạng mảng hai chiều.
Số lượng hàng của bảng: số tự nhiên nhỏ hơn hoặc bằng 1.000.
Số lượng cột của bảng: số tự nhiên nhỏ hơn hoặc bằng 1.000.
Bảng chỉ chứa các giá trị 0 và 1.

