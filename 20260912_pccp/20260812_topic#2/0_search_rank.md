[Bài toán này có điểm số riêng cho bài kiểm tra độ chính xác và hiệu quả.]

Kakao hiện đang tuyển dụng các lập trình viên giàu kinh nghiệm cho nửa cuối năm nay, và việc nộp đơn cũng như làm bài kiểm tra lập trình đã kết thúc. Đối với đợt tuyển dụng này, ứng viên được yêu cầu chọn bốn mục sau khi điền đơn:

Bạn phải chọn một trong các ngôn ngữ lập trình C++, Java hoặc Python cho bài kiểm tra lập trình.

Bạn phải chọn Backend hoặc Frontend cho vị trí công việc bạn đang ứng tuyển.

Bạn phải chọn Junior hoặc Senior cho cấp độ kinh nghiệm của mình.

Bạn phải chọn Gà hoặc Pizza là món ăn khoái khẩu của mình.

Niniz, người làm việc trong Nhóm Tuyển dụng Nhân tài, đang phát triển một công cụ để phân tích kết quả kiểm tra lập trình và cung cấp kết quả cho các nhóm phát triển tham gia tuyển dụng. Công cụ này cho phép người dùng dễ dàng xác định có bao nhiêu ứng viên đáp ứng các tiêu chí cụ thể chỉ bằng cách chọn các điều kiện ứng tuyển của ứng viên.

Ví dụ, các câu hỏi từ các nhóm phát triển có thể có dạng như sau: Có bao nhiêu ứng viên đạt điểm kiểm tra lập trình từ 50 trở lên trong số những người tham gia kiểm tra lập trình bằng Java, chọn vai trò backend, có kinh nghiệm junior và chọn pizza là món ăn khoái khẩu?

Tất nhiên, tùy thuộc vào tình hình của từng nhóm phát triển, có thể có nhiều loại câu hỏi khác nhau như sau:

Có bao nhiêu người đạt điểm kiểm tra lập trình từ 100 trở lên trong số những người tham gia kiểm tra lập trình bằng Python, chọn vai trò frontend, có kinh nghiệm senior và chọn gà là món ăn khoái khẩu?

Có bao nhiêu người đạt điểm kiểm tra lập trình từ 100 trở lên trong số những người tham gia kiểm tra lập trình bằng C++, có kinh nghiệm senior và chọn pizza là món ăn khoái khẩu?

Có bao nhiêu người đạt điểm kiểm tra lập trình từ 200 trở lên trong số những người chọn vai trò backend và có kinh nghiệm senior?

Có bao nhiêu người đạt điểm kiểm tra lập trình từ 250 trở lên trong số những người chọn gà là món ăn khoái khẩu?

Có bao nhiêu người đạt điểm kiểm tra lập trình từ 150 trở lên? Nói cách khác, câu hỏi từ nhóm phát triển có dạng như sau:

* Trong số những người đáp ứng điều kiện [condition], có bao nhiêu người đạt điểm kiểm tra lập trình từ X trở lên?

[Bài toán]

Cho một mảng `info` gồm một chuỗi duy nhất đại diện cho bốn thông tin mà ứng viên đã nhập trong đơn xin việc và điểm kiểm tra lập trình đạt được, và một mảng `query` chứa các điều kiện kiểm tra mà nhóm phát triển muốn biết dưới dạng chuỗi,

hãy hoàn thành hàm `solution` để trả về một mảng chứa số người tương ứng với mỗi điều kiện kiểm tra theo thứ tự.

[Ràng buộc]

Kích thước của mảng `info` nằm trong khoảng từ 1 đến 50.000.

Giá trị của mỗi phần tử trong mảng `info` có định dạng "Ngôn ngữ lập trình Nhóm công việc Kinh nghiệm Tâm hồn Ẩm thực Điểm số", là tổng của bốn giá trị mà ứng viên đã nhập trong đơn xin việc và điểm kiểm tra lập trình.

Ngôn ngữ lập trình là một trong các ngôn ngữ C++, Java hoặc Python.

Nhóm công việc là một trong các nhóm: backend hoặc frontend.

Kinh nghiệm là một trong các cấp độ: junior hoặc senior.

Món ăn khoái khẩu là một trong các món: gà hoặc pizza. "Điểm số" đề cập đến điểm kiểm tra lập trình và là một số tự nhiên nằm giữa 1 và 100.000.

Mỗi từ được phân cách bởi một dấu cách.

Kích thước của mảng truy vấn nằm giữa 1 và 100.000.

Mỗi chuỗi trong truy vấn có định dạng "[Điều kiện] X".

[Điều kiện] là một chuỗi có định dạng "Ngôn ngữ lập trình và Nhóm công việc và Kinh nghiệm và Món ăn khoái khẩu".

Ngôn ngữ là một trong các ngôn ngữ C++, Java, Python hoặc -.

Nhóm công việc là một trong các nhóm: backend, frontend hoặc -.

Kinh nghiệm là một trong các cấp độ: junior, senior hoặc -.

Món ăn khoái khẩu là một trong các món: gà, pizza hoặc -.

Ký hiệu '-' cho biết điều kiện tương ứng sẽ không được xem xét.

X đề cập đến điểm số bài kiểm tra lập trình và cho biết tổng số người đạt điểm X trở lên trong số những người đáp ứng điều kiện.

Mỗi từ được phân cách bởi một dấu cách. Ví dụ: "cpp and - and senior and pizza 500" có nghĩa là "Trong số các ứng viên đã tham gia bài kiểm tra lập trình bằng C++, có kinh nghiệm cấp cao và chọn pizza là món ăn khoái khẩu, có bao nhiêu người đạt điểm bài kiểm tra lập trình từ 500 trở lên?" [Ví dụ Nhập/Xuất]

Kết quả truy vấn thông tin

["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"] ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] [1,1,1,1,2,4]

Giải thích Ví dụ Nhập/Xuất

Thông tin của người ứng tuyển được trình bày trong bảng như sau.

Ngôn ngữ Chức vụ Kinh nghiệm Món ăn khoái khẩu Điểm số

java backend junior pizza 150

python frontend senior chicken 210

python frontend senior chicken 150

cpp backend senior pizza 260

java backend junior chicken 80

python backend senior chicken 50

"java và backend và junior và pizza 100": Trong số các ứng viên tham gia bài kiểm tra lập trình bằng Java, chọn vai trò backend, có kinh nghiệm junior và chọn pizza là món ăn khoái khẩu, có 1 ứng viên đạt điểm kiểm tra lập trình từ 100 trở lên.

"python và frontend và senior và chicken 200": Trong số các ứng viên tham gia bài kiểm tra lập trình bằng Python, chọn vai trò frontend, có kinh nghiệm senior và chọn gà là món ăn khoái khẩu, có 1 ứng viên đạt điểm kiểm tra lập trình từ 200 trở lên.

"cpp và - và cấp cao và pizza 250": Trong số các ứng viên tham gia bài kiểm tra lập trình bằng C++, có kinh nghiệm cấp cao và chọn pizza là món ăn khoái khẩu, có 1 ứng viên đạt điểm kiểm tra lập trình từ 250 trở lên.

"- và backend và cấp cao và - 150": Trong số các ứng viên chọn vai trò backend và có kinh nghiệm cấp cao, có 1 ứng viên đạt điểm kiểm tra lập trình từ 150 trở lên.

"- và - và - và gà 100": Trong số các ứng viên chọn gà là món ăn khoái khẩu, có 2 ứng viên đạt điểm kiểm tra lập trình từ 100 trở lên.

"- và - và - và - 150": Có 4 ứng viên đạt điểm kiểm tra lập trình từ 150 trở lên.