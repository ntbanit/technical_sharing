# Tiến hành bài tập
Sau khi nhận bài tập, Ru đã lập kế hoạch hoàn thành theo thứ tự sau:
- Bài tập bắt đầu khi đến thời gian bắt đầu đã định.
- Khi đến thời gian bắt đầu một bài tập mới, nếu có một bài tập đang thực hiện, bài tập hiện tại sẽ bị tạm dừng và bài tập mới bắt đầu.
- Khi một bài tập đang thực hiện kết thúc, nếu có một bài tập bị tạm dừng, bài tập bị tạm dừng sẽ được tiếp tục.
- Nếu cả bài tập mới cần bắt đầu và bài tập bị tạm dừng đều tồn tại tại thời điểm kết thúc bài tập, bài tập mới cần bắt đầu sẽ được thực hiện trước.
- Nếu có nhiều bài tập bị tạm dừng, bài tập bị tạm dừng gần đây nhất sẽ được bắt đầu trước.
#### Cho một mảng chuỗi 2 chiều `plans` chứa các kế hoạch bài tập làm tham số, hãy hoàn thành hàm `solution` để trả về một mảng chứa tên các bài tập theo thứ tự chúng được hoàn thành.

#### Ràng buộc
- 3 ≤ len(`plans`) ≤ 1.000
- Các phần tử của `plans` bao gồm cấu trúc [name, star, playtime].
- name: Đại diện cho tên của nhiệm vụ. 2 ≤ len(name) ≤ 10
- name chỉ bao gồm các ký tự chữ cái viết thường.
- Không có phần tử trùng lặp trong name.
- start: Đại diện cho thời gian bắt đầu của nhiệm vụ.
- Chỉ các giá trị thời gian nằm giữa "00:00" và "23:59" được lưu trữ dưới dạng "giờ:phút".
- Vì thời gian bắt đầu của tất cả các nhiệm vụ đều khác nhau, nên không có sự chồng chéo.
- Các nhiệm vụ nên bắt đầu theo thứ tự "00:00" ... "23:59". Nói cách khác, giá trị giờ và phút càng nhỏ thì nhiệm vụ bắt đầu càng sớm.
- playtime: Đại diện cho thời gian cần thiết để hoàn thành một nhiệm vụ, tính bằng phút.
- 1 ≤ playtime ≤ 100
- Thời gian chơi không bắt đầu từ 0.
- Mảng có thể không được sắp xếp theo thứ tự thời gian.
- Nếu thời gian kết thúc của một tác vụ đang thực hiện trùng khớp với - thời gian bắt đầu của một tác vụ mới, thì tác vụ đang thực hiện được coi là đã hoàn thành.

#### Ví dụ về đầu vào/đầu ra
| plans | result |
|---|---|
| `[["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]` | `["korean", "english", "math"]` |
| `[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]` | `["science", "history", "computer", "music"]` |
| `[["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]` | `["bbb", "ccc", "aaa"]` |
Giải thích các ví dụ về nhập/xuất dữ liệu

Ví dụ nhập/xuất dữ liệu #1
- Các nhiệm vụ được bắt đầu theo thứ tự "tiếng Hàn", "tiếng Anh" và "toán". 
- Nhiệm vụ "tiếng Hàn" bắt đầu lúc "11:40", kết thúc 30 phút sau đó lúc "12:10", và ngay lập tức bắt đầu nhiệm vụ "tiếng Anh". 
- Nhiệm vụ "tiếng Anh" kết thúc 20 phút sau đó lúc "12:30", và ngay lập tức bắt đầu nhiệm vụ "toán". 
- Nhiệm vụ "toán" kết thúc 40 phút sau đó lúc "01:10". Do đó, vì các nhiệm vụ được hoàn thành theo thứ tự "tiếng Hàn", "tiếng Anh" và "toán", chúng được lưu trữ trong một mảng và được trả về theo thứ tự đó.

Ví dụ nhập/xuất dữ liệu #2
- Các nhiệm vụ được bắt đầu theo thứ tự "âm nhạc", "máy tính", "khoa học" và "lịch sử".

| Thời gian | Nhiệm vụ đang thực hiện | Nhiệm vụ tạm dừng | Giải thích |
|---|---|---|---|
| `"12:20"` | `"music"` | `[]` | Bắt đầu `"music"`. |
| `"12:30"` | `"computer"` | `["music"]` | Tạm dừng `"music"` (còn 30 phút) và bắt đầu `"computer"`. |
| `"12:40"` | `"science"` | `["music", "computer"]` | Tạm dừng `"computer"` (còn 90 phút) và bắt đầu `"science"`. |
| `"13:30"` | `"computer"` | `["music"]` | Hoàn thành `"science"` và tiếp tục lại `"computer"` — nhiệm vụ được tạm dừng gần nhất. |
| `"14:00"` | `"history"` | `["music", "computer"]` | Tạm dừng `"computer"` (còn 60 phút) và bắt đầu `"history"`. |
| `"14:30"` | `"computer"` | `["music"]` | Hoàn thành `"history"` và tiếp tục lại `"computer"` — nhiệm vụ được tạm dừng gần nhất. |
| `"15:30"` | `"music"` | `[]` | Hoàn thành `"computer"` và tiếp tục lại `"music"` — nhiệm vụ được tạm dừng gần nhất. |
| `"16:00"` | `-` | `[]` | Hoàn thành `"music"`. |

Do đó, hãy hoàn thành bài tập theo thứ tự ["khoa học", "lịch sử", "máy tính", "âm nhạc"].

Ví dụ Nhập/Xuất #3

(Phần giải thích đã được lược bỏ)