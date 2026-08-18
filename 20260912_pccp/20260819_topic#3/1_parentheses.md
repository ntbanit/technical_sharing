# Dấu ngoặc đơn chính xác
Định nghĩa về cặp dấu ngoặc hợp lệ là: nếu chuỗi bắt đầu bằng ký tự '(', thì nó phải kết thúc bằng ký tự ')'.
Ví dụ:

"()()" hoặc "(())()" là chuỗi dấu ngoặc hợp lệ.
")()(" hoặc "(()(" là chuỗi dấu ngoặc không hợp lệ.
Cho một chuỗi s chỉ bao gồm các ký tự '(' hoặc ')', hãy hoàn thiện hàm giải quyết bài toán trả về giá trị true nếu chuỗi s hợp lệ và false nếu không hợp lệ.

Ràng buộc:
Độ dài chuỗi s: số tự nhiên nhỏ hơn 100.000
Chuỗi s chỉ bao gồm các ký tự '(' hoặc ')'.
Ví dụ:
| s | kết quả |
|---|---|
|"()()" | true |
|"(())()" | true |
|")()("| false |
|"(()("| false |

Ví dụ #1
Giống như ví dụ trên.