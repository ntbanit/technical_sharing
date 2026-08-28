Chỉ số H là một chỉ số đo lường năng suất và tầm ảnh hưởng của một nhà khoa học. Chúng ta muốn tính toán h, giá trị đại diện cho chỉ số H của một nhà khoa học. Theo Wikipedia, chỉ số H được tính như sau:

Trong số n bài báo được xuất bản bởi một nhà khoa học, nếu có h bài báo trở lên được trích dẫn h lần trở lên và các bài báo còn lại được trích dẫn h lần trở xuống, thì giá trị h lớn nhất chính là chỉ số H của nhà khoa học đó.

Cho một mảng `citations` chứa số lần trích dẫn của các bài báo được xuất bản bởi một nhà khoa học làm tham số, hãy viết một hàm `solution` trả về chỉ số H của nhà khoa học đó.

Ràng buộc:

Số lượng bài báo được xuất bản bởi nhà khoa học nằm trong khoảng từ 1 đến 1.000.

Số lần trích dẫn trên mỗi bài báo nằm trong khoảng từ 0 đến 10.000.

Ví dụ về đầu vào/đầu ra

Số trích dẫn trả về

[3, 0, 6, 1, 5] 3

Giải thích ví dụ về đầu vào/đầu ra

Nhà khoa học này đã công bố 5 bài báo, và 3 trong số đó đã được trích dẫn từ 3 lần trở lên. Và vì hai bài báo còn lại được trích dẫn ba lần hoặc ít hơn, nên chỉ số H của nhà khoa học này là 3.