Kiểm tra an ninh nhập cư

N người đang xếp hàng chờ kiểm tra an ninh nhập cư. Thời gian kiểm tra cho mỗi nhân viên tại mỗi quầy kiểm tra là khác nhau.

Ban đầu, tất cả các quầy kiểm tra đều trống. Chỉ một người được kiểm tra tại một quầy. Người đứng đầu hàng có thể đến quầy trống để được kiểm tra. Tuy nhiên, nếu có quầy nào hoàn thành sớm hơn, họ có thể chờ và đến đó để được kiểm tra.

Chúng ta muốn giảm thiểu thời gian cần thiết để tất cả mọi người được kiểm tra.

Cho số người chờ kiểm tra an ninh nhập cư là n và một mảng `times` chứa thời gian mỗi nhân viên kiểm tra một người làm tham số, hãy viết một hàm `solution` trả về thời gian tối thiểu cần thiết để tất cả mọi người được kiểm tra.

Ràng buộc

Số người chờ kiểm tra an ninh nhập cư nằm trong khoảng từ 1 đến 1.000.000.000.
Thời gian mỗi nhân viên kiểm tra một người là từ 1 phút đến 1.000.000.000 phút.
Có từ 1 đến 100.000 nhân viên kiểm tra.

Ví dụ đầu vào/đầu ra

n lần trả về

6 [7, 10] 28

0 0  7   10    14   20 21 28    30
1 2  3   4     5       6  end

Giải thích ví dụ đầu vào/đầu ra

T=mid ?? check N ng k

nhân viên i
dùng times[i]
T // times[i]

left = 1
right = N * max(times)



Hai người đầu tiên đi thẳng đến khu vực kiểm tra.
Sau 7 phút, bàn kiểm tra đầu tiên trống, và người thứ 3 được kiểm tra.
Sau 10 phút, bàn kiểm tra thứ hai trống, và người thứ 4 được kiểm tra.
Sau 14 phút, bàn kiểm tra đầu tiên trống, và người thứ 5 được kiểm tra.
Sau 20 phút, bàn kiểm tra thứ hai trống, nhưng nếu người thứ 6 không kiểm tra ở đó và đợi thêm một phút trước khi được kiểm tra tại bàn kiểm tra đầu tiên, thì việc kiểm tra tất cả mọi người sẽ hoàn tất sau 28 phút.
