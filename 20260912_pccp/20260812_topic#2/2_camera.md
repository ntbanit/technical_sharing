Chúng tôi dự định lắp đặt camera giám sát giao thông để đảm bảo mọi phương tiện lưu thông trên đường cao tốc đều gặp camera giám sát ít nhất một lần.

Ràng buộc
1 <= len(routes) <= 10000
routes[i][0] : điểm mà phương tiện thứ i đi vào đường cao tốc
routes[i][1] : điểm mà phương tiện thứ i đi ra khỏi đường cao tốc.

Một phương tiện được coi là đã gặp camera ngay cả khi có camera được lắp đặt tại điểm vào hoặc điểm ra của nó.

Điểm vào và điểm ra của phương tiện nằm trong khoảng từ -30.000 đến 30.000. 

Ví dụ 
Input:
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]] 
Ouput:
2

Giải thích :

Nếu một camera được lắp đặt tại điểm -5, xe thứ hai và thứ tư sẽ gặp camera.

Nếu một camera được lắp đặt tại điểm -15, xe thứ nhất và thứ ba sẽ gặp camera.