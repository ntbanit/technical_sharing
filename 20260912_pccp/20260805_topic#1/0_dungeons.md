Trò chơi XX có hệ thống mệt mỏi (được biểu thị bằng các số nguyên lớn hơn hoặc bằng 0), và bạn có thể khám phá các hầm ngục bằng một lượng mệt mỏi nhất định. Mỗi hầm ngục có "Lượng Mệt mỏi Tối thiểu Cần thiết" để bắt đầu khám phá và "Lượng Mệt mỏi Đã Tiêu hao" khi hoàn thành khám phá. "Lượng Mệt mỏi Tối thiểu Cần thiết" cho biết lượng mệt mỏi tối thiểu cần thiết để khám phá hầm ngục, trong khi "Lượng Mệt mỏi Đã Tiêu hao" cho biết lượng mệt mỏi bị tiêu hao sau khi khám phá hầm ngục. Ví dụ, để khám phá một hầm ngục có "Lượng Mệt mỏi Tối thiểu Cần thiết" là 80 và "Lượng Mệt mỏi Đã Tiêu hao" là 20, lượng mệt mỏi hiện tại của người chơi phải từ 80 trở lên, và 20 mệt mỏi sẽ bị tiêu hao sau khi khám phá hầm ngục.

Trò chơi này chứa một số hầm ngục có thể được khám phá một lần mỗi ngày, và người chơi dự định khám phá càng nhiều hầm ngục càng tốt trong ngày hôm nay. Cho biết độ mệt mỏi hiện tại của người dùng là k và một mảng 2D `dungeons` chứa "độ mệt mỏi tối thiểu cần thiết" và "độ mệt mỏi đã tiêu hao" cho mỗi hầm ngục làm tham số, hãy hoàn thành hàm `solution` để trả về số lượng hầm ngục tối đa mà người dùng có thể khám phá.

Ràng buộc

k là một số tự nhiên nằm giữa 1 và 5000 (bao gồm cả 1 và 5000).

Chiều dài theo chiều dọc (hàng) của `dungeons` (tức là số lượng hầm ngục) nằm giữa 1 và 8 (bao gồm cả 1 và 8).

Chiều dài theo chiều ngang (cột) của `dungeons` là 2.

Mỗi hàng của `dungeons` đại diện cho ["độ mệt mỏi tối thiểu cần thiết", "độ mệt mỏi đã tiêu hao"] cho mỗi hầm ngục.

"Độ mệt mỏi tối thiểu cần thiết" luôn lớn hơn hoặc bằng "độ mệt mỏi đã tiêu hao".

"Độ mệt mỏi tối thiểu cần thiết" và "độ mệt mỏi đã tiêu hao" là các số tự nhiên nằm giữa 1 và 1000 (bao gồm cả 1 và 1000). Lượng ["Mức độ mệt mỏi tối thiểu cần thiết", "Mức độ mệt mỏi đã tiêu hao"] của các hầm ngục khác nhau có thể giống nhau.

Ví dụ đầu vào/đầu ra

Kết quả k hầm ngục

80 [[80,20],[50,40],[30,10]] 3

Giải thích ví dụ đầu vào/đầu ra

Mức độ mệt mỏi hiện tại là 80.

Nếu bạn khám phá các hầm ngục theo thứ tự Thứ nhất → Thứ hai → Thứ ba,

Mức độ mệt mỏi hiện tại là 80, và vì "Mức độ mệt mỏi tối thiểu cần thiết" để hoàn thành hầm ngục đầu tiên cũng là 80, bạn có thể khám phá hầm ngục đầu tiên. Vì "Mức độ mệt mỏi đã tiêu hao" cho hầm ngục đầu tiên là 20, mức độ mệt mỏi còn lại sau khi khám phá hầm ngục là 60.

Mức độ mệt mỏi còn lại là 60, và vì "Mức độ mệt mỏi tối thiểu cần thiết" để hoàn thành hầm ngục thứ hai là 50, bạn có thể khám phá hầm ngục thứ hai. Vì "Lượng tiêu hao thể lực" cho hầm ngục thứ hai là 40, nên thể lực còn lại sau khi khám phá hầm ngục này là 20.

Thể lực còn lại là 20, và "Lượng thể lực tối thiểu cần thiết" để vượt qua hầm ngục thứ ba là 30. Do đó, không thể khám phá hầm ngục thứ ba.

Tuy nhiên, nếu bạn khám phá theo thứ tự Hầm ngục thứ nhất → Hầm ngục thứ ba → Hầm ngục thứ hai:

Thể lực hiện tại là 80, và vì "Lượng thể lực tối thiểu cần thiết" để vượt qua hầm ngục thứ nhất cũng là 80, nên có thể khám phá hầm ngục thứ nhất. Vì "Lượng tiêu hao thể lực" cho hầm ngục thứ nhất là 20, nên thể lực còn lại sau khi khám phá hầm ngục này là 60.

Thể lực còn lại là 60, và vì "Lượng thể lực tối thiểu cần thiết" để vượt qua hầm ngục thứ ba là 30, nên có thể khám phá hầm ngục thứ ba. Vì "Lượng tiêu hao thể lực" cho hầm ngục thứ ba là 10, nên thể lực còn lại sau khi khám phá hầm ngục này là 50. Thể lực còn lại là 50, và vì "thể lực tối thiểu cần thiết" để vượt qua hầm ngục thứ hai là 50, bạn có thể khám phá hầm ngục thứ hai. Vì "thể lực tiêu hao" cho hầm ngục thứ hai là 40, nên thể lực còn lại sau khi khám phá hầm ngục này là 10.

Do đó, trong trường hợp này, bạn có thể khám phá cả ba hầm ngục, và số lượng hầm ngục tối đa mà người chơi có thể khám phá là 3.