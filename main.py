def show_menu():
    print("\n=== 퀴즈 게임 ===")
    print("1. 퀴즈 풀기")
    print("2. 결과 보기")
    print("3. 종료")
    choice = input("선택: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = show_menu()
        if choice == "3":
            print("게임을 종료합니다.")
            break
        elif choice == "1":
            print("퀴즈 풀기 기능 (준비중)")
        elif choice == "2":
            print("결과 보기 기능 (준비중)")
        else:
            print("잘못된 선택입니다.")