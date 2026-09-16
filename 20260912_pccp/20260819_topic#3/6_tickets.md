## Chúng ta dự định lập kế hoạch lộ trình di chuyển bằng cách sử dụng tất cả các vé đã cho. Chúng ta luôn khởi hành từ sân bay "ICN".

## Cho một mảng 2 chiều `tickets` chứa thông tin vé làm tham số, hãy viết một hàm `solution` trả về một mảng chứa lộ trình đi qua các sân bay đã ghé thăm.

## Ràng buộc:
- Tất cả các sân bay đều gồm 3 chữ cái viết hoa.
- Số lượng sân bay đã cho nằm trong khoảng từ 3 đến 10.000.
- Mỗi hàng [a, b] trong `tickets` cho biết có một vé từ sân bay a đến sân bay b.
- Tất cả các vé đã cho phải được sử dụng.
- Nếu có hai hoặc nhiều lộ trình khả thi, hãy trả về lộ trình xuất hiện đầu tiên theo thứ tự bảng chữ cái.
- Các trường hợp không thể ghé thăm tất cả các thành phố sẽ không được đưa ra. Ví dụ về nhập/xuất dữ liệu


|tickets |return|
|---|---|
|[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]| ["ICN", "JFK", "HND", "IAD"]
|[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] |["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

## Ví dụ #1 : Bạn có thể đến theo thứ tự ["ICN", "JFK", "HND", "IAD"].

## Ví dụ #2: Bạn có thể truy cập theo thứ tự ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"], nhưng ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] sẽ đứng đầu theo thứ tự bảng chữ cái.
