import client

# client.HOST = '127.0.0.1'
your_select = ""


def connect_game():
    client.HOST = str(input("호스트의 IP 주소를 입력해주세요: "))
    client.start_client()
    client.checking()


def plz_input():
    global your_select

    your_select = str(input("가위, 바위, 보 중에 하나 입력해주세요: "))

    if your_select == "가위":
        return
    elif your_select == "바위":
        return
    elif your_select == "보":
        return
    else:
        plz_input()


def start_game():
    global your_select

    plz_input()
    print(your_select)


connect_game()
# start_game()
