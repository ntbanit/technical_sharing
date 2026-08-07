Cờ caro là một trò chơi hai người chơi trên bàn cờ 3x3, trong đó người chơi đầu tiên lần lượt đánh dấu "O" và người chơi thứ hai đánh dấu "X". Nếu ba dấu giống nhau được tạo thành theo chiều ngang, chiều dọc hoặc đường chéo, người chơi tạo ra các dấu giống nhau sẽ thắng và trò chơi kết thúc. Nếu cả chín ô đều được điền đầy và không thể đánh thêm dấu nào nữa, trò chơi kết thúc hòa.

Musuk, đang rảnh rỗi không có việc gì làm, định chơi cờ caro, một trò chơi hai người, một mình như sau:

Anh ta tự mình đảm nhận cả vai trò người chơi thứ nhất và thứ hai.

Sau khi bắt đầu trò chơi, anh ta lần lượt đánh dấu "O" và "X" một mình.

Vì cờ caro có luật chơi đơn giản và kết thúc nhanh chóng, Musuk chỉ đơn giản là vẽ lại bàn cờ 3x3 và lặp lại trò chơi mỗi khi một vòng kết thúc. Sau khi chơi hàng chục vòng như vậy, Musuk có thể đã mắc lỗi vi phạm luật chơi, như sau.

Đến lượt người chơi đánh dấu "O" nhưng người chơi lại đánh dấu "X", hoặc ngược lại, đến lượt người chơi đánh dấu "X" nhưng người chơi lại đánh dấu "O".

Trò chơi vẫn tiếp tục ngay cả khi người chơi thứ nhất hoặc thứ hai đã thắng và trò chơi đã kết thúc.

Trong khi chơi, Meoseuk bắt đầu tự hỏi liệu mình có mắc lỗi gì không. Vì anh ta chơi cờ caro một mình, không có ai quan sát nên anh ta không thể biết chắc chắn. Tuy nhiên, chỉ nhìn vào bàn cờ, anh ta tin rằng mình có thể xác định xem đây có phải là tình huống có thể xảy ra nếu tuân theo luật chơi cờ caro hay không, và nếu không có vấn đề gì, anh ta dự định tiếp tục trò chơi.

Cho một mảng chuỗi `board` làm tham số chứa thông tin về bàn cờ caro mà Meoseuk đã thắc mắc khi chơi một mình, hãy viết một hàm `solution` trả về 1 nếu tình huống đó là kết quả có thể xảy ra khi chơi cờ caro theo luật, và 0 nếu ngược lại.

Ràng buộc

Chiều dài của `board` = Chiều dài của `board[i]` = 3

Tất cả các phần tử của `board` chỉ bao gồm "O", "X" và "." `board[i][j]` biểu thị trạng thái của ô tương ứng với hàng i + 1 và cột j + 1.

"." biểu thị một ô trống, trong khi "O" và "X" biểu thị rằng ô đó được đánh dấu bằng ký tự tương ứng.

Ví dụ Nhập/Xuất

Kết quả bảng

["O.X", ".O.", "..X"] 1

["OOO", "...", "XXX"] 0

["...", ".X.", "..."] 0

["...", "...", "..."] 1

Giải thích Ví dụ Nhập/Xuất

Ví dụ Nhập/Xuất #1

Bảng trò chơi cho Ví dụ 1 như sau:

O.X

.O.

...X

Khi người chơi thứ nhất và thứ hai lần lượt đặt quân cờ như sau, bàn cờ này có thể được tạo ra.

Hàng 1 Cột 1 → Hàng 1 Cột 3 → Hàng 2 Cột 2 → Hàng 3 Cột 3

Hàng 1 Cột 1 → Hàng 3 Cột 3 → Hàng 2 Cột 2 → Hàng 3 Cột

Hàng 2 Cột 2 → Hàng 1 Cột 3 → Hàng 1 Cột 1 → Hàng 3 Cột

Hàng 2 Cột 2 → Hàng 3 Cột 3 → Hàng 1 Cột 1 → Hàng 3 Cột

Tất nhiên, không giống như trên, có khả năng Meoseuk đã mắc lỗi khi đánh dấu O ở Hàng 2 Cột 2, X ở Hàng 3 Cột 3, X ở Hàng 1 Cột 3 và O ở Hàng 1 Cột 1 theo thứ tự đó. Tuy nhiên, xin lưu ý rằng vấn đề không phải là hỏi "Liệu có khả năng xảy ra sai sót không?" mà là "Đây có phải là tình huống có thể xảy ra trong trò chơi Tic-Tac-Toe được chơi theo đúng luật không?". Do đó, trả về 1.

Ví dụ đầu vào/đầu ra #2

Bàn cờ trong Ví dụ 2 như sau:

OOO

...

XXX

Nếu trò chơi được chơi theo đúng luật, người chơi thứ nhất và thứ hai sẽ lần lượt đánh dấu hai ô vuông ở hàng 1 hoặc hàng 3, và trò chơi sẽ kết thúc khi người chơi thứ nhất hoàn thành ba ô O nằm ngang ở hàng 1 trong lượt thứ 5. Do đó, có thể suy ra rằng Meoseuk đã mắc lỗi khi tiếp tục chơi ngay cả sau khi trò chơi đã kết thúc, và tình huống này không thể xảy ra trong một trò chơi Tic-Tac-Toe bình thường. Do đó, trả về 0.

Ví dụ Nhập/Xuất #3

Trong Ví dụ 3, các ô X chỉ được đánh dấu ở hàng 2, cột 2. Vì chỉ có các ô X mà không có ô O của người chơi đầu tiên, nên có thể suy ra rằng Meoseuk đã mắc lỗi khi đánh dấu X thay vì O. Tình huống này không thể xảy ra khi trò chơi được chơi theo đúng luật. Do đó, trả về 0.

Ví dụ Nhập/Xuất #4

Ví dụ 4 là một bàn cờ 3x3 trống. Tình huống này có thể xảy ra trước khi người chơi đầu tiên đánh dấu bất kỳ ô trống nào. Do đó, trả về 1.