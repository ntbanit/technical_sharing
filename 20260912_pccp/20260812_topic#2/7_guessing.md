Một cuộc thi đấu △△ đang được tổ chức. Trong cuộc thi này, N người chơi tham gia và trò chơi diễn ra theo thể thức giải đấu. N người tham gia được đánh số từ 1 đến N. Sau đó, người chơi theo thứ tự số 1↔số 2, số 3↔số 4, ..., số N-1↔số N sẽ chơi một ván. Người thắng mỗi ván sẽ tiến vào vòng tiếp theo. Những người chơi tiến vào vòng tiếp theo sẽ nhận được một số mới từ 1 đến N/2. Nếu người chơi số 2 thắng trong ván đấu giữa người chơi số 1↔người chơi số 2, số 1 sẽ được trao. Tương tự, nếu người chơi số 3 thắng trong ván đấu giữa người chơi số 3↔người chơi số 4, số 2 sẽ được trao. Cuộc thi sẽ tiếp tục cho đến khi chỉ còn người chơi cuối cùng.

Ở vòng đầu tiên, người chơi số A tự hỏi mình sẽ chơi vòng nào với người chơi số B, người được coi là đối thủ của mình. Cho số lượng người tham gia N, số đầu tiên được gán cho người tham gia A, và số đầu tiên được gán cho người tham gia B làm tham số, hãy viết một hàm để trả về vòng nào người tham gia số A sẽ chơi trò chơi với đối thủ của mình, người tham gia số B. Giả sử người tham gia số A và B luôn thắng cho đến khi họ gặp nhau.

Ràng buộc
N: một số tự nhiên nằm giữa 2^1 và 2^20 (Vì nó được cho là lũy thừa của 2, nên không có chiến thắng mặc định).

A, B: số tự nhiên nhỏ hơn hoặc bằng N (Tuy nhiên, A ≠ B).

Ví dụ
N A B câu trả lời
8 4 7 3
Ví dụ #1
Trong vòng đầu tiên, người tham gia số 4 chơi một trò chơi với người tham gia số 3 và người tham gia số 7 chơi một trò chơi với người tham gia số 8. Vì ta giả sử người tham gia số 4 và số 7 luôn thắng, nên người tham gia số 4 và số 7 sẽ nhận được số 2 và số 4 ở vòng tiếp theo, tương ứng. Ở vòng thứ hai, người tham gia số 2 chơi một ván với người tham gia số 1 và người tham gia số 4 chơi một ván với người tham gia số 3. Tương tự, người tham gia số 2 và số 4 được gán số 1 và số 2 tương ứng ở vòng tiếp theo. Vì những người tham gia này chơi một ván với tư cách là người tham gia số 1 và số 2 ở vòng thứ ba, nên trả về 3.-