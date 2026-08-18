Chia tách lưới điện
Lịch sử nộp bài
Mô tả
Có *n* trạm điện được kết nối bằng các đường dây tạo thành một cấu trúc cây duy nhất. Bạn dự định cắt một trong những đường dây này để chia mạng lưới điện hiện tại thành hai mạng lưới riêng biệt. Mục tiêu của bạn là làm cho số lượng trạm điện trong hai mạng lưới thu được chênh lệch ít nhất có thể.

Bạn được cung cấp số lượng trạm điện *n* và thông tin về các đường dây *wires* dưới dạng tham số. Hãy hoàn thiện hàm `solution` để trả về giá trị tuyệt đối của hiệu số trạm điện giữa hai mạng lưới sau khi cắt một đường dây để chia tách chúng một cách cân bằng nhất có thể.

Ràng buộc
*n* là số tự nhiên trong khoảng từ 2 đến 100 (bao gồm cả 2 và 100).
*wires* là mảng số nguyên hai chiều có độ dài *n*-1.
Mỗi phần tử của *wires* bao gồm hai số tự nhiên [v1, v2], biểu thị rằng trạm v1 và trạm v2 được kết nối bằng một đường dây.
1 ≤ v1 < v2 ≤ *n*.
Dữ liệu đầu vào luôn biểu diễn một mạng lưới có cấu trúc cây duy nhất.
Ví dụ Đầu vào/Đầu ra
n|wires | result |
9|[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]|3
4|[[1,2],[2,3],[3,4]]|0
7|[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]|1
Giải thích Ví dụ
Ví dụ #1

Hình ảnh dưới đây minh họa một cách giải quyết cho dữ liệu đầu vào đã cho.
ex1.png
Nếu bạn cắt đường dây nối trạm 4 và trạm 7, hai mạng lưới sẽ có lần lượt 6 và 3 trạm; không thể chia mạng lưới cân bằng hơn mức này. Ngoài ra, việc cắt đường dây nối trạm 3 và trạm 4 cũng mang lại kết quả tối ưu.
Ví dụ Đầu vào/Đầu ra #2

Hình ảnh dưới đây minh họa phương pháp giải quyết cho dữ liệu đầu vào đã cho.
ex2.png
Việc cắt đường dây nối trạm 2 và trạm 3 dẫn đến kết quả là mỗi lưới điện đều có hai trạm; đây là cách tiếp cận tối ưu. Ví dụ về Đầu vào/Đầu ra số 3

Hình ảnh dưới đây minh họa phương pháp giải quyết cho dữ liệu đầu vào đã cho.
ex3.png
Việc cắt dây nối giữa tháp số 3 và tháp số 7 sẽ chia hệ thống thành hai lưới điện với số lượng tháp lần lượt là 4 và 3; đây là phương án tối ưu.