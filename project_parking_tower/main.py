# 주차 타워 (엘리베이터
#   - 1 ~ 5층 (1층당 1대만 주차
#   - 차량번호: 정수 숫자 4자리만 입력

#  기능
#   1. 차량입고
#   2. 차량출고
#   3. 차량조회
#   4. 프로그램 종료

# 1. 공통 설정값
max_car = 5         # 최대 주차 5
cnt_car = 0         # 현재 주차 대수(count)

# 2. 주차 타워 생성 → List
#tower = ["", "", "", "", "",]       # 방법 1 : 하드코딩 (절대 지양)

# 방법 2 : for 문 활용
# tower = []
# for i in range(5):
#     tower.append('')
    
# 방법 3 : List Comprehension 활용
tower = ["" for i in range(max_car)]

# 방법 2와 방법 3은 동일한 기능의 코드
# 방법 3을 사용하면 좀더 효율적으로 코드 개발 가능
# 모든 for 문을 "List Comprehesion"으로 변경 불가
# (심플한 for 문만 가능)

# 3. 주차타워 메뉴 출력
while True:
    print("=" * 50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("=" * 50)
    print("1. 입고")
    print("2. 출고")
    print("3. 조회")
    print("4. 종료")
    print('=' * 50)
    
    # 사용자에게 1 ~ 4번까지 값을 입력받는 코드 작성(+유효성 체크)
    #   - 올바른 값이 들어오지 않으면 경고 메세지 출력 후 다시 입력
    #   - 사용자에게 입력 받는 변수는 select_num에 저장
    while True:
        while True:
            select_num = input(">> 입력하시오: ")
            try:
                select_num = int(select_num)
                if select_num < 1 or select_num > 4:
                    print(">> WARNING 없는 번호 입니다. 다시 입력해 주세요.")
                else:
                    break
            except:
                print(">> WARNING 숫자가 아닙니다. 다시 입력해 주세요.")
        
        
        if select_num == 1:         # 입고
            # 도메인 지식 → 비지니스 로직
            
            # 1. 주차 타워 만차 여부 확인
            if cnt_car < max_car:
                # 2. 주차 번호 (4자리) 입력
                #  + 유효성 체크(숫자만 입력, 4자리 입력)
                car_num = input(">> 차량번호: ")
            else:
                print(">> 만차입니다. 다음에 이용해주세요.")
            for i, car in enumerate(tower):
                if(car == ""): # 빈 주차 공간
                    # 3. 주차타워 입고 → tower[] 저장
                    tower[i] = car_num
                    # 4. cnt_car + 1 : 현재 주차 차량 최신화
                    cnt_car += 1
                    break
        elif select_num == 2:       # 출고
            # 1. 차량번호 입력(출고)
            if cnt_car > 0:
                car_num = input(">> 차량 번호: ")
            else:
                print(">> 주차되어있는 차가 없습니다. 다음에 이용해주세요.")
            
            for i in tower:
                pass
                
            # 2. 주차타워에 주차 여부 확인 
            #   y : 다음 단계로
            #   n : 주차 되지 않은 차량입니다.
            # 3. 차량 출고 → tower → "" 변경
            # 4. 현재 차량수 - 1
        elif select_num == 3:       # 조회
            print("■" * 20)
            for i in range(len(tower)):
                print(f"■ {i + 1}층 : {tower[i]}")
            print("■" * 20)
        elif select_num == 4:       # 종료
            print(">> 프로그램을 종료합니다.")
            exit()