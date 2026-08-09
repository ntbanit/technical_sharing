# Học code 
## Bạn chuẩn bị cho coding test. Để giải quyết các bài toán cần có năng lực thuật toán và năng lực lập trình tối thiểu của bài toán đó 
- Năng lực thuật toán "alp" algorithm power 
- Năng lực lập trình "cop" coding power 
- alp, cop >= 0

## Ví dụ :
### Bạn đang có alp = 15, cop = 10
- Bài A cần alp 10, cop 10 -> bạn biết làm 
- Bài B cần alp 10, cop 20 -> bạn không biết làm 
### Cách để bạn lên trình 
1. Học thuật toán, alp tăng 1, tốn 1 giờ 
2. Học lập trình, cop tăng 1, tốn 1 giờ 
3. Làm các bài bạn đang biết làm, tăng alp_rwd (algorithm power reward), cop_rwd (coding power reward), tốn cost giờ 

### Input
- alp, cop : Trình lúc đầu của bạn 
- problems : mảng 2D, mỗi hàng gồm mảng [alp_req, cop_req, alp_rwd, cop_rwd, cost]
	- alp_req, cop_req : algorithm power required, coding power required
	- alp_rwd, cop_rwd : algorithm power reward, coding power reward
	- cost : giờ làm bài
### Output : Tìm thời gian tối thiểu bạn biết làm tất cả các bài toán 

## Constraints:
- 0 ≤ alp, cop ≤ 150
- 1 ≤ length of problems ≤ 100
- 0 ≤ alp_req, cop_req ≤ 150
- 0 ≤ alp_rwd, cop_rwd ≤ 30
- 1 ≤ cost ≤ 100

## Efficiency test constraints (smaller, for brute-force-safe testing):
- 0 ≤ alp, cop ≤ 20
- 1 ≤ length of problems ≤ 6
- 0 ≤ alp_req, cop_req ≤ 20
- 0 ≤ alp_rwd, cop_rwd ≤ 5
- 1 ≤ cost ≤ 10

###Example 1:
- alp=10, cop=10, problems=[[10,15,2,1,2],[20,20,3,3,4]] → answer: 15
- Step 1: Study coding, +5 → alp=10, cop=15 (takes 5 time)
- Step 2: Solve problem 1 five times → alp=20, cop=20 (takes 10 time)
- Total: 15 time, now able to solve both problems' requirements

###Example 2:
- alp=0, cop=0, problems=[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]] → answer: 13
- A sequence of solving problem 1 twice, studying coding +3, solving problem 2 twice, solving problem 4 once → total 13 time, reaches alp=10, cop=11 which satisfies all requirements