"Supoja" là từ viết tắt của người đã từ bỏ môn toán. "Bộ ba Supoja" dự định đoán đúng tất cả các câu hỏi toán học trong bài kiểm tra thử. Supoja đoán các câu hỏi từ đầu đến cuối như sau:

Phương pháp đoán của Học sinh #1: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...

Phương pháp đoán của Học sinh #2: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...

Phương pháp đoán của Học sinh #3: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

Cho một mảng `answers` chứa các câu trả lời đúng từ câu hỏi 1 đến câu hỏi cuối cùng theo thứ tự, hãy viết một hàm `solution` trả về một mảng chứa người trả lời đúng nhiều câu hỏi nhất.

Ràng buộc

Bài kiểm tra gồm tối đa 10000 câu hỏi.

Đáp án đúng là một trong các số 1, 2, 3, 4 hoặc 5.

Nếu có nhiều người đạt điểm cao nhất, hãy sắp xếp các giá trị trả về theo thứ tự tăng dần.

Ví dụ đầu vào/đầu ra

Đáp án trả về

[1,2,3,4,5] [1]

[1,3,2,4,2] [1,2,3]

Giải thích ví dụ đầu vào/đầu ra

Ví dụ đầu vào/đầu ra #1

Người sợ toán 1 trả lời đúng tất cả các câu hỏi.

Người sợ toán 2 trả lời sai tất cả các câu hỏi.

Người sợ toán 3 trả lời sai tất cả các câu hỏi.

Do đó, người trả lời đúng nhiều câu hỏi nhất là Người sợ toán 1.

Ví dụ đầu vào/đầu ra #2

Mọi người đều trả lời đúng 2 câu hỏi.
