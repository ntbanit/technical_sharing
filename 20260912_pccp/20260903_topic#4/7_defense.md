Trò chơi phòng thủ

Junho hiện đang rất thích các trò chơi phòng thủ. Trò chơi phòng thủ là trò chơi mà Junho sử dụng n binh lính của mình để chặn các đòn tấn công liên tiếp của kẻ thù theo trình tự. Trò chơi phòng thủ diễn ra theo các quy tắc sau:

Junho bắt đầu với n binh lính.

Kẻ thù[i] xuất hiện trong mỗi vòng.

Bạn có thể chặn kẻ thù[i] bằng cách sử dụng kẻ thù[i] binh lính từ số quân còn lại của mình.

Ví dụ, nếu bạn còn 7 binh lính và có 2 kẻ thù, việc chặn vòng hiện tại sẽ còn lại 7 - 2 = 5 binh lính.

Trò chơi kết thúc nếu số lượng kẻ thù trong vòng hiện tại vượt quá số lượng binh lính còn lại.

Trò chơi có một kỹ năng gọi là "Bất khả xâm phạm". Sử dụng Bất khả xâm phạm cho phép bạn chặn toàn bộ một vòng tấn công mà không cần sử dụng bất kỳ binh lính nào.

Bất khả xâm phạm có thể được sử dụng tối đa k lần.

Junho muốn sử dụng Bất khả xâm phạm vào những thời điểm thích hợp để tiến qua càng nhiều vòng càng tốt. Các tham số được cho là n, số lượng binh lính mà Junho bắt đầu; k, số lượt di chuyển bất khả xâm phạm có sẵn; và một mảng số nguyên `enemy` chứa số lượng kẻ thù tấn công trong mỗi vòng, theo thứ tự đó. Hoàn thành hàm `solution` để trả về số vòng mà Junho có thể phòng thủ.

Ràng buộc

1 ≤ n ≤ 1.000.000.000

1 ≤ k ≤ 500.000

1 ≤ độ dài của enemy ≤ 1.000.000

1 ≤ enemy[i] ≤ 1.000.000

enemy[i] chứa số lượng kẻ thù tấn công trong vòng i + 1.

Nếu có thể phòng thủ trong tất cả các vòng, hãy trả về độ dài của enemy[i]. Ví dụ về đầu vào/đầu ra

|n |k|enemy|result|
|---|---|---|---|
|7| 3| [4, 2, 4, 5, 3, 3, 1] |5|
|2| 4 |[3, 3, 3, 3] |4|

Ví dụ về đầu vào/đầu ra #1

Bằng cách chặn vô điều kiện các đòn tấn công ở vòng 1, 3 và 5, và tiêu hao 2 lính ở vòng 2 và 5 lính ở vòng 4, bạn có thể chặn các đòn tấn công đến vòng 5. Tương tự, bằng cách chặn vô điều kiện các đòn tấn công ở vòng 1, 3 và 4, và tiêu hao 2 lính ở vòng 2 và 3 lính ở vòng 5, bạn có thể chặn các đòn tấn công đến vòng 5. Vì không có cách nào chặn được nhiều vòng hơn, hãy trả về 5.

Ví dụ về đầu vào/đầu ra #2

Junho có thể chặn các đòn tấn công đến vòng 4 bằng cách sử dụng chặn vô điều kiện cho tất cả các đòn tấn công.