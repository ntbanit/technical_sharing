Nhân viên văn phòng Demi thỉnh thoảng làm thêm giờ, và sự mệt mỏi do làm thêm giờ tích lũy khi làm thêm giờ. Mệt mỏi do làm thêm giờ là tổng bình phương của khối lượng công việc còn lại tại thời điểm bắt đầu làm thêm giờ. Demi sẽ làm việc trong N giờ để giảm thiểu sự mệt mỏi do làm thêm giờ. Giả sử Demi có thể xử lý khối lượng công việc là 1 đơn vị mỗi giờ, hãy hoàn thành hàm `solution` trả về giá trị của sự mệt mỏi do làm thêm giờ được giảm thiểu khi biết N giờ còn lại cho đến giờ tan ca và khối lượng công việc `works` cho mỗi nhiệm vụ.

Ràng buộc

`works` là một mảng có độ dài từ 1 trở lên và nhỏ hơn hoặc bằng 20.000.

Các phần tử của `works` là các số tự nhiên nhỏ hơn hoặc bằng 50.000.

`n` là một số tự nhiên nhỏ hơn hoặc bằng 1.000.000. Ví dụ về đầu vào/đầu ra

|works | n | result|
|------|------|------|
|[4, 3, 3]| 4 |12|
|[2, 1, 2]| 1 |6|
|[1,1]| 3| 0|


Ví dụ về đầu vào/đầu ra #1

Khi n=4, nếu khối lượng công việc còn lại là [4, 3, 3], kết quả của việc làm việc 4 giờ để giảm thiểu chỉ số làm thêm giờ là [2, 2, 2]. Trong trường hợp này, chỉ số làm thêm giờ là 22 + 22 + 22 = 12.

Ví dụ về đầu vào/đầu ra #2

Khi n=1, nếu khối lượng công việc còn lại là [2, 1, 2], kết quả của việc làm việc 1 giờ để giảm thiểu chỉ số làm thêm giờ là [1, 1, 2]. Chỉ số làm thêm giờ là 12 + 12 + 22 = 6.

Ví dụ đầu vào/đầu ra #3

Vì không còn khối lượng công việc nào nữa, nên mức độ mệt mỏi là 0.