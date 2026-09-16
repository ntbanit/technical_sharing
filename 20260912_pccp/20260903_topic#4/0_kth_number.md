Số thứ K

Chi tiết bài nộp

Mô tả

Tôi muốn tìm số thứ k khi mảng được cắt từ phần tử thứ i đến phần tử thứ j và được sắp xếp.

Ví dụ: nếu mảng là [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3,

Cắt từ phần tử thứ 2 đến phần tử thứ 5 của mảng ta được [5, 2, 6, 3].

Sắp xếp mảng kết quả ta được [2, 3, 5, 6].

Số thứ 3 trong mảng kết quả là 5.

Cho mảng `array` và một mảng 2D `commands` chứa các phần tử [i, j, k] làm tham số, hãy viết một hàm `solution` áp dụng phép toán đã mô tả ở trên cho tất cả các phần tử của `commands` và trả về kết quả trong một mảng.

Ràng buộc

Độ dài của mảng nằm giữa 1 và 100.

Mỗi phần tử của mảng nằm giữa 1 và 100. Độ dài của
mảng commands nằm giữa 1 và 50.

Mỗi phần tử của mảng commands có độ dài là 3.

Ví dụ đầu vào/đầu ra

Mảng commands trả về

[1, 5, 2, 6, 3, 7, 4]

[[2, 5, 3], [4, 4, 1], [1, 7, 3]] [5, 6, 3]

Giải thích ví dụ đầu vào/đầu ra

Cắt mảng [1, 5, 2, 6, 3, 7, 4] từ phần tử thứ 2 đến phần tử thứ 5 và sắp xếp nó. Số thứ ba trong dãy [2, 3, 5, 6] là 5.

Cắt dãy [1, 5, 2, 6, 3, 7, 4] từ phần tử thứ 4 đến phần tử thứ 4 và sắp xếp lại. Số đầu tiên trong dãy [6] là 6.

Cắt dãy [1, 5, 2, 6, 3, 7, 4] từ phần tử thứ 1 đến phần tử thứ 7. Số thứ ba của dãy [1, 2, 3, 4, 5, 6, 7] là 3.