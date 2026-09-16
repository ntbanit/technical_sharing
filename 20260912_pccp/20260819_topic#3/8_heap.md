Hàng đợi hai cấp

Hàng đợi hai cấp là một cấu trúc dữ liệu có khả năng thực hiện các thao tác sau:

| Lệnh | Tác vụ nhận được |
|------|------------------|
| I `số` | Chèn `số` đã cho vào hàng đợi. |
| D 1 | Xóa giá trị lớn nhất khỏi hàng đợi. |
| D -1 | Xóa giá trị nhỏ nhất khỏi hàng đợi. |

Khi các thao tác cần thực hiện bởi hàng đợi hai cấp được đưa ra dưới dạng tham số, vui lòng triển khai hàm giải pháp để trả về [0,0] nếu hàng đợi trống sau khi xử lý tất cả các thao tác, và [max, minimum] nếu ngược lại.

Ràng buộc

operations là một mảng chuỗi có độ dài từ 1 đến 1.000.000.

Các phần tử của operations đại diện cho các thao tác cần thực hiện bởi hàng đợi.

Các phần tử được đưa ra ở định dạng “dữ liệu lệnh”.

- Trong thao tác xóa giá trị lớn nhất/nhỏ nhất, nếu có hai hoặc nhiều giá trị lớn nhất/nhỏ nhất, chỉ một giá trị bị xóa.

Nếu một thao tác xóa dữ liệu được đưa ra cho một hàng đợi trống, thao tác đó sẽ bị bỏ qua. Ví dụ về Nhập/Xuất

|operations| return|
|---|---|
|["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"] |[0,0]|
|["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] |[333, -45]|


Ví dụ Nhập/Xuất #1

Chèn 16 và -5643.

Xóa giá trị nhỏ nhất. -5643 bị xóa và 16 còn lại.

Xóa giá trị lớn nhất. 16 bị xóa và hàng đợi ưu tiên kép trống.

Vì hàng đợi ưu tiên trống, thao tác xóa giá trị lớn nhất bị bỏ qua.

Chèn 123.

Xóa giá trị nhỏ nhất. 123 bị xóa, và hàng đợi ưu tiên kép trống.

Do đó, [0, 0] được trả về.

Ví dụ Nhập/Xuất #2

Sau khi chèn -45 và 653, giá trị lớn nhất (653) bị xóa. -45 còn lại.

Sau khi chèn -642, 45 và 97, giá trị lớn nhất (97) và giá trị nhỏ nhất (-642) bị xóa. -45 và 45 còn lại.

333 được chèn.

Vì -45, 45 và 333 vẫn còn trong hàng đợi ưu tiên kép, nên [333, -45] được trả về.