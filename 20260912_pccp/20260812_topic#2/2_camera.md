Camera Giám sát Giao thông

Chi tiết Bài tập

Mô tả

Chúng tôi dự định lắp đặt camera giám sát giao thông để đảm bảo mọi phương tiện lưu thông trên đường cao tốc đều gặp camera giám sát ít nhất một lần.

Cho các tuyến đường của phương tiện lưu thông trên đường cao tốc làm tham số, hãy hoàn thành hàm giải pháp để trả về số lượng camera tối thiểu cần thiết để đảm bảo mọi phương tiện đều gặp camera giám sát ít nhất một lần.

Ràng buộc

Số lượng phương tiện nằm trong khoảng từ 1 đến 10.000.

Các tuyến đường chứa đường đi của phương tiện; routes[i][0] chỉ ra điểm mà phương tiện thứ i đi vào đường cao tốc, và routes[i][1] chỉ ra điểm mà phương tiện thứ i đi ra khỏi đường cao tốc.

Một phương tiện được coi là đã gặp camera ngay cả khi có camera được lắp đặt tại điểm vào hoặc điểm ra của nó.

Điểm vào và điểm ra của phương tiện nằm trong khoảng từ -30.000 đến 30.000. Ví dụ về đầu vào/đầu ra

Các tuyến đường trả về

[[-20,-15], [-14,-5], [-18,-13], [-5,-3]] 2

Giải thích ví dụ về đầu vào/đầu ra

Nếu một camera được lắp đặt tại điểm -5, xe thứ hai và thứ tư sẽ gặp camera.

Nếu một camera được lắp đặt tại điểm -15, xe thứ nhất và thứ ba sẽ gặp camera.