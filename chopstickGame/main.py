player_cs_left = 1
player_cs_right = 1
computer_cs_left = 1
computer_cs_right = 1


def game():
    if player_cs_left >= 5:
        print("GameOver")
    elif player_cs_right >= 5:
        print("GameOver")
    elif computer_cs_left >= 5:
        print("GameOver")
    elif computer_cs_right >= 5:
        print("GameOver")


def get_player_input():
    hand = str(input("[플레이어1, 당신의 왼손, 오른손 중에 하나를 입력해주세요]"))

    if hand == "왼손":
        atk_hand = str(input("[플레이어1, 이제, 공격할 상대의 왼손, 오른손 중에 하나를 입력해주세요]"))
        if atk_hand == "왼손":
            add_cs("left", "left", "player1")
        elif atk_hand == "오른손":
            add_cs("left", "right", "player1")
    elif hand == "오른손":
        atk_hand = str(input("[플레이어1, 이제, 공격할 상대의 왼손, 오른손 중에 하나를 입력해주세요]"))
        if atk_hand == "왼손":
            add_cs("right", "left", "player1")
        elif atk_hand == "오른손":
            add_cs("right", "right", "player1")
    else:
        print("[올바른 입력이 아닙니다. 다시 입력해주세요]")
        get_player_input()


def get_second_player_input():
    hand = str(input("[플레이어2, 당신의 왼손, 오른손 중에 하나를 입력해주세요]"))

    if hand == "왼손":
        atk_hand = str(input("[플레이어2, 이제, 공격할 상대의 왼손, 오른손 중에 하나를 입력해주세요]"))
        if atk_hand == "왼손":
            add_cs("left", "left", "player2")
        elif atk_hand == "오른손":
            add_cs("left", "right", "player2")
    elif hand == "오른손":
        atk_hand = str(input("[플레이어2, 이제, 공격할 상대의 왼손, 오른손 중에 하나를 입력해주세요]"))
        if atk_hand == "왼손":
            add_cs("right", "left", "player2")
        elif atk_hand == "오른손":
            add_cs("right", "right", "player2")
    else:
        print("[올바른 입력이 아닙니다. 다시 입력해주세요]")
        get_player_input()


def add_cs(selected_hand, target_hand, now_turn):
    global computer_cs_left, player_cs_left, computer_cs_right, player_cs_right

    if selected_hand == "left" and target_hand == "left":
        if now_turn == "player1":
            computer_cs_left += player_cs_left
        elif now_turn == "player2":
            player_cs_left += computer_cs_left
    elif selected_hand == "left" and target_hand == "right":
        if now_turn == "player1":
            computer_cs_right += player_cs_left
        elif now_turn == "player2":
            player_cs_left += computer_cs_right
    elif selected_hand == "right" and target_hand == "left":
        if now_turn == "player1":
            computer_cs_left += player_cs_right
        elif now_turn == "player2":
            player_cs_left += computer_cs_right
    elif selected_hand == "right" and target_hand == "right":
        if now_turn == "player1":
            computer_cs_right += player_cs_right
        elif now_turn == "player2":
            player_cs_right += computer_cs_right

    print("내 손가락:", player_cs_left, player_cs_right, "상대 손가락:", computer_cs_left, computer_cs_right)
    game()


get_player_input()
get_second_player_input()
