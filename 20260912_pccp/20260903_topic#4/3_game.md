Mô tả

Bạn đang chơi một trò chơi giải đố, trong đó bạn phải giải n câu đố theo thứ tự trong thời gian giới hạn. Mỗi câu đố có độ khó và thời gian giới hạn cố định. Số lỗi bạn mắc phải khi giải câu đố thay đổi tùy thuộc vào trình độ của bạn. Nếu ta gọi diff là độ khó của câu đố hiện tại, time_cur là thời gian cần thiết cho câu đố hiện tại, time_prev là thời gian cần thiết cho câu đố trước đó, và level là trình độ của bạn, thì trò chơi diễn ra như sau:

- Nếu diff ≤ level, bạn giải câu đố mà không mắc lỗi nào và sử dụng time_cur.
- Nếu diff > level, bạn mắc tổng cộng diff - level lỗi. Mỗi lần mắc lỗi, bạn sử dụng time_cur và thêm time_prev để giải lại câu đố trước đó. Khi giải lại câu đố trước đó, bạn không mắc lỗi nào bất kể độ khó của câu đố trước đó. Sau khi mắc lỗi diff - level, bạn giải lại câu đố bằng cách sử dụng time_cur.

Ví dụ, nếu diff = 3, time_cur = 2 và time_prev = 4, thời gian cần thiết để giải câu đố sẽ thay đổi theo cấp độ như sau:

Nếu cấp độ = 1, bạn mắc 3 - 1 = 2 lỗi trong câu đố. Mỗi lỗi tiêu tốn 2 + 4 = 6 thời gian, và giải lại câu đố tiêu tốn 2 thời gian, tổng cộng là 6 × 2 + 2 = 14 thời gian.

Nếu cấp độ = 2, bạn mắc 3 - 2 = 1 lỗi, nên bạn tiêu tốn 6 + 2 = 8 thời gian.

Nếu cấp độ ≥ 3, bạn không mắc lỗi nào trong câu đố và tiêu tốn 2 thời gian.

Trò chơi giải đố có tổng thời gian giới hạn cố định. Chúng ta muốn tìm trình độ tối thiểu cần thiết để giải tất cả các câu đố trong thời gian giới hạn. Độ khó và thời gian yêu cầu đều là số nguyên dương, và trình độ cũng phải là số nguyên dương. Các tham số được cung cấp là một mảng số nguyên 1 chiều `diffs` chứa độ khó của các câu đố theo thứ tự, một mảng số nguyên 1 chiều `times` chứa thời gian giải các câu đố theo thứ tự, và tổng thời gian giới hạn `limit`. Hoàn thành hàm `solution` để trả về giá trị độ khó tối thiểu dưới dạng số nguyên cần thiết để giải tất cả các câu đố trong thời gian giới hạn.

Ràng buộc

1 ≤ độ dài của diffs = độ dài của times = n ≤ 300.000

diffs[i] biểu thị độ khó của câu đố thứ i, và times[i] biểu thị thời gian cần thiết cho câu đố thứ i.

diffs[0] = 1

1 ≤ diffs[i] ≤ 100.000

1 ≤ times[i] ≤ 10.000

1 ≤ limit ≤ 1015

Chỉ cung cấp dữ liệu đầu vào trong trường hợp tất cả các câu đố có thể được giải trong thời gian giới hạn. Ví dụ về đầu vào/đầu ra

số lần khác biệt giới hạn kết quả

[1, 5, 3] [2, 4, 7] 30 3

[1, 4, 4, 2] [6, 3, 8, 2] 59 2

[1, 328, 467, 209, 54] [2, 7, 1, 4, 3] 1723 294

[1, 99999, 100000, 99995] [9999, 9001, 9999, 9001] 3456789012 39354

Giải thích ví dụ về đầu vào/đầu ra

Ví dụ về đầu vào/đầu ra #1

Nếu trình độ là 3, hãy tiến hành như sau:

Giải câu đố thứ nhất bằng 2 lần.

Giải câu đố thứ 2 với 5 - 3 = 2 lần thử sai, tổng thời gian là (4 + 2) × 2 + 4 = 16.

Giải câu đố thứ 3 với 7 lần thử sai.

Bạn có thể giải tất cả các câu đố với tổng thời gian là 2 + 16 + 7 = 25. Nếu trình độ thành thạo nhỏ hơn 3, bạn không thể giải tất cả các câu đố trong thời gian giới hạn là 30.

Do đó, bạn phải trả về 3.

Ví dụ đầu vào/đầu ra #2

Nếu trình độ thành thạo là 2, hãy tiến hành như sau:

Giải câu đố thứ 1 với 6 lần thử sai.

Giải câu đố thứ 2 với 4 - 2 = 2 lần thử sai, tổng thời gian là (3 + 6) × 2 + 3 = 21.

Giải câu đố thứ 3 với 4 - 2 = 2 lần thử sai, tổng thời gian là (8 + 3) × 2 + 8 = 30.

Giải câu đố thứ 4 trong 2 lần. Bạn có thể giải tất cả các câu đố trong tổng thời gian là 6 + 21 + 30 + 2 = 59. Nếu trình độ thành thạo nhỏ hơn 2, bạn không thể giải tất cả các câu đố trong thời gian giới hạn là 59.

Do đó, bạn phải trả về 2.

Ví dụ đầu vào/đầu ra #3

Nếu trình độ thành thạo là 294, hãy tiến hành như sau:

Giải câu đố thứ nhất trong 2 lần.

Giải câu đố thứ hai với 328 - 294 = 34 lỗi, sử dụng tổng thời gian là (7 + 2) × 34 + 7 = 313.

Giải câu đố thứ ba với 467 - 294 = 173 lỗi, sử dụng tổng thời gian là (1 + 7) × 173 + 1 = 1385.

Giải câu đố thứ tư trong 4 lần.

Giải câu đố thứ 5 trong 3 lần.

Tất cả các câu đố có thể được giải trong tổng thời gian là 2 + 313 + 1385 + 4 + 3 = 1707. Nếu trình độ thành thạo nhỏ hơn 294, không thể giải tất cả các câu đố trong thời gian giới hạn là 1723.

Do đó, phải trả về 294.

Ví dụ đầu vào/đầu ra #4

Nếu trình độ thành thạo là 39354, quá trình diễn ra như sau:

Câu đố thứ nhất được giải trong 9999 lần.

Câu đố thứ hai được giải với 99999 - 39354 = 60645 lỗi, dẫn đến tổng thời gian là (9001 + 9999) × 60645 + 9001 = 1152264001 lần. Bạn giải câu đố thứ 3 bằng cách mắc 100.000 - 39.354 = 60.646 lỗi, sử dụng tổng cộng (9.999 + 9.001) × 60.646 + 9.999 = 1.152.283.999 lần thời gian.

Bạn giải câu đố thứ 4 bằng cách mắc 99.995 - 39.354 = 60.641 lỗi, sử dụng tổng cộng (9.001 + 9.999) × 60.641 + 9.001 = 1.152.188.001 lần thời gian.

Bạn có thể giải tất cả các câu đố với tổng thời gian là 9.999 + 1.152.264.001 + 1.152.283.999 + 1.152.188.001 = 3.456.746.000. Nếu trình độ của bạn thấp hơn 39.354, bạn không thể giải tất cả các câu đố trong thời gian giới hạn là 3.456.789.012. Do đó, bạn phải trả về 39354.