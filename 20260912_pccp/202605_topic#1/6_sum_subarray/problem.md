Cho một dãy số được sắp xếp không giảm dần, ta cần tìm một dãy con thỏa mãn các điều kiện sau:

Dãy con phải chứa các phần tử tại bất kỳ hai chỉ số nào và tất cả các phần tử nằm giữa chúng.

Tổng của dãy con là k.

Nếu có nhiều dãy con có tổng bằng k, hãy tìm dãy con có độ dài ngắn hơn.

Nếu có nhiều dãy con có độ dài ngắn hơn, hãy tìm dãy con xuất hiện đầu tiên (chỉ số bắt đầu nhỏ hơn).

Cho một mảng số nguyên `sequence` biểu diễn dãy số và một số nguyên `k` biểu diễn tổng của dãy con làm tham số, hãy hoàn thành hàm `solution` để trả về một mảng chứa chỉ số bắt đầu và kết thúc của các dãy con thỏa mãn các điều kiện trên. Chỉ số của dãy bắt đầu từ 0.

Ràng buộc

5 ≤ độ dài dãy ≤ 1.000.000

1 ≤ phần tử của dãy ≤ 1.000

Dãy được sắp xếp theo thứ tự không giảm dần. 5 ≤ k ≤ 1.000.000.000

k luôn là một giá trị có thể tạo thành một dãy con của dãy.

Ví dụ về Nhập/Xuất

Kết quả dãy k

[1, 2, 3, 4, 5] 7 [2, 3]

[1, 1, 1, 2, 3, 4, 5] 5 [6, 6]

[2, 2, 2, 2, 2] 6 [0, 2]

Giải thích ví dụ về Nhập/Xuất

Ví dụ Nhập/Xuất #1

Vì [3, 4] là dãy con liên tiếp duy nhất có tổng bằng 7 trong [1, 2, 3, 4, 5], nên chỉ số bắt đầu là 2 và chỉ số kết thúc là 3 của dãy đó được lưu vào một mảng, và [2, 3] được trả về.

Ví dụ Nhập/Xuất #2

Trong [1, 1, 1, 2, 3, 4, 5], các dãy con liên tiếp có tổng bằng 5 là [1, 1, 1, 2], [2, 3] và [5]. Vì [5] là dãy ngắn nhất trong số này, nên [6, 6] chứa chỉ số bắt đầu và kết thúc của dãy đó được trả về.

Ví dụ Nhập/Xuất #3

Trong [2, 2, 2, 2, 2], các dãy con liên tiếp có tổng bằng 6 là [2, 2, 2], đây là một trong ba trường hợp. Khi có nhiều dãy có độ dài ngắn, dãy xuất hiện đầu tiên sẽ được tìm kiếm, vì vậy [0, 2] được trả về.