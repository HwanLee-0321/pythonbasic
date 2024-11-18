#  1. 서브 메뉴 출력 기능! (아이스크림, 음료, 디저트)
def print_sub_menu(menu, price, menu_cnt):
    for i in range(1, menu_cnt + 1):   # 1, 2, 3
        print(f"{i}. {menu[i]} ({price[i]}원)")
        

#  2. 사용자 메뉴 선택 기능 
def input_menu_num(menu_cnt: int) -> int:
    while True:
        order = int(input("메뉴 : "))
        if order > menu_cnt or order < 1:
            print(">> WARNING: 올바른 번호를 입력해주세요.")
        else:
            break
    return order