#  - 5층으로 제한
#  - 1층마다 차량 1대만 입고
#  - 차량번호는 숫자 4자리만
# 주차 타워(엘레베이터)

# 기능
#  1. 차량 입고
#  2. 차량 출고
#  3. 차량 조회
#  4. 종료

# 1. 공통 설정
max_car = 5  # 최대 주차 차량수
cnt_car = 0  # 현재 주차 되어있는 차량 수(count)

# 2. 주차 타워 생성 → list[] → "" 빈칸
# 방법1. 하드 코딩
# tower = ["", "", "", "", ""]
  
# 방법2. 리스트 컴프리헨슨
tower = [ "" for _ in range(max_car) ]

# 3. 초기 화면
print("=" * 50)
print("== 주차 타워 시스템 ver 1.0 ==")
print("=" * 50)
print("=1. 차량입고")
print("=2. 차량출고")
print("=3. 차량조회")
print("=4. 종료")
print("=" * 50)

# 4. 메뉴 선택
# 사용자로부터 1~4번까지 입력받는 코드 작성
# 사용자가 입력한 값은 select_num 변수에 저장
# 사용자가 1~4 이외의 값을 넣으면 경고 메세지 출력 후 다시 입력받기
while 1:
    select_num = int(input(">> 메뉴 선택: "))
    if 1 <= select_num <= 4:
        print()
    else:
        print(">> WARNINGS: 올바른 값을 입력하세요")
    
    # 5. 메뉴 서비스
    # select_num이 1,2,3,4인 경우
    if select_num == 1:
        print(">> [입고하길 원하는 층수와 차량번호를 입력해주세요]")
        while 1:
            in_car_floor = int(input(f">> 입고층수(1~{max_car}층까지 입력요망): "))
            if 0 <= in_car_floor <=max_car:
                if tower[in_car_floor-1] != "":
                    print(">> WARNING: 이미 차량이 입고되어 있는 층수입니다.")
                    print(">> WARNING: 다른 층수를 입력해주세요.")
                    break
            else:
                print(">> WARNING: 올바른 층수를 입력해주세요.")
            in_car_num = int(input(">> 차량번호: "))
            if len(str(in_car_num)) == 4:
                print(">> 차량입고 성공!")
            else:
                print(">> 올바른 차량번호를 입력해주세요.")
            break
        tower[in_car_floor-1] = in_car_num
    elif select_num == 2:
        out_car = int(input(">> 출고할 차량번호를 입력해주세요: "))
        if out_car in tower:
            for i in range(max_car):
                if out_car == tower[i]:
                    tower[i] = ""
                    print(">> 출고 성공!")
        else:
            print(">> 존재하지 않는 차량번호입니다.")
    elif select_num == 3:
        for i in range(max_car,0,-1):
            print(f"{i}층: {tower[i-2]}")
    elif select_num == 4:
        print(">> 프로그램을 종료합니다.")
        exit()