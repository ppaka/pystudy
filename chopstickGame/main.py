player_cs_left = 1
player_cs_right = 1
computer_cs_left = 1
computer_cs_right = 1

player_turn = 1
gameOver = False


def game():
    global gameOver

    if player_cs_left == 0 and player_cs_right == 0:
        gameOver = True
    elif player_cs_right == 0 and player_cs_left == 0:
        gameOver = True
    elif computer_cs_left == 0 and computer_cs_right == 0:
        gameOver = True
    elif computer_cs_right == 0 and computer_cs_left == 0:
        gameOver = True


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
    global computer_cs_left, player_cs_left, computer_cs_right, player_cs_right, player_turn

    if selected_hand == "left" and target_hand == "left":
        if now_turn == "player1":
            computer_cs_left += player_cs_left
        elif now_turn == "player2":
            player_cs_left += computer_cs_left
    elif selected_hand == "left" and target_hand == "right":
        if now_turn == "player1":
            computer_cs_right += player_cs_left
        elif now_turn == "player2":
            player_cs_right += computer_cs_left
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

    if player_cs_left >= 5:  player_cs_left = 0
    if player_cs_right >= 5:  player_cs_right = 0
    if computer_cs_left >= 5:  computer_cs_left = 0
    if computer_cs_right >= 5:  computer_cs_right = 0

    print("내 손가락:", player_cs_left, player_cs_right, "상대 손가락:", computer_cs_left, computer_cs_right)
    if now_turn == "player1":
        player_turn = 2
    elif now_turn == "player2":
        player_turn = 1
    
    game()


def separate():
    selected = input("[나눠질 결과를 적어주세요(각 손은 ,로 구분)]")
    splited = selected.split(',')
    both = splited[0] + splited[1]
    if both == (player_cs_left + player_cs_right):
        player_cs_left = splited[0]
        player_cs_right = splited[1]
        print("내 손가락:", player_cs_left, player_cs_right, "상대 손가락:", computer_cs_left, computer_cs_right)


def start():
    while gameOver == False:
        if player_turn == 1:
            get_player_input()
        elif player_turn == 2:
            get_second_player_input()


start()
