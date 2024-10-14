######################################################################
## Project: 조선벅스                                                 ##
## Wirter:  HwanLee                                                 ##     
## Company: 조선대학교                                               ##
## Reg_date: 2024.10.14                                             ## 
## Update_date: 2024.10.14                                          ## 
## License: None                                                    ##     
## Contents: 콘솔 프로그래밍을 활용한 커피 점문점에서 사용하는 키오스크  ##
######################################################################

# 키오스크

# 1. 메인 메뉴 출력(커피, 스무디, 베이커리)
# 2. 메인 메뉴 선택(사용자)
# 3. 서브 메뉴 출력(커피 or 스무디 or 베이커리)
# 4. 서브 메뉴 선택(사용자)
# 5. 고객 주문 메뉴 목록에 저장(서브 메뉴)
# 6. 추가 주문 여부(Yes or No)
# 7-1. Yes: 1번으로 보내기
# 7-2. No: 최종주문 내역으로 보내기
# 8. 최종주문 내역 출력

from service_kiosk import print_menu, select_menu

###################
## 1. 메뉴 만들기 ##
###################

main_menu = {
    1: "커피",
    2: "스무디",
    3: "베이커리"
} 
coffee_menu = {
    1: "에스프레소",
    2: "아메리카노"
}
coffee_price = {
    1: 3500,
    2: 4000,
}
smoothie_menu = {
    1: "딸기 스무디",
    2: "망고 스무디",
    3: "블루베리 스무디",
    4: "키위 스무디",
}
smoothie_price = {
    1: 5500,
    2: 6000,
    3: 5000,
    4: 6500,
}
bakery_menu = {
    1: "조각 케이크",
    2: "롤 케이크",
    3: "샌드위치",
}
bakery_price = {
    1: 6500,
    2: 5500,
    3: 5000,
}

order_list = []  # 고객 주문 기록

while True:
    # 1. 메인메뉴 출력 
    print("★" * 50)
    print("★★ 별다방 조선")
    print_menu(main_menu, 3)

    # 2. 메뉴 선택 기능
    order = select_menu(3)

    # 3.4. 서브메뉴 출력 및 선택
    if order == 1:      # 커피
        print_menu(coffee_menu, 2)
        sub_order = select_menu(2)
        order_list.append([coffee_menu[sub_order], coffee_price[sub_order]])
                
    elif order == 2:    # 스무디
        print_menu(smoothie_menu, 4)
        sub_order = select_menu(4)
        order_list.append([smoothie_menu[sub_order], smoothie_price[sub_order]])
        
    elif order == 3:    # 베이커리
        print_menu(bakery_menu, 3)
        sub_order = select_menu(3)
        order_list.append([bakery_menu[sub_order], bakery_price[sub_order]])
        
    for item in order_list:
        print(f"주문기록: {item}")
        
    
        