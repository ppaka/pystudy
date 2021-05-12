import client

# client.HOST = '127.0.0.1'

# client.StartClient()
your_select = ""

def ConnectGame():
    client.HOST = str(input("호스트의 IP 주소를 입력해주세요: "))
    client.StartClient()

    client.Checking()


def PlzInput():
    global your_select

    your_select = str(input("가위, 바위, 보 중에 하나 입력해주세요: "))

    if your_select == "가위":
        return
    elif your_select == "바위":
        return
    elif your_select == "보":
        return
    else: PlzInput()


def StartGame():
    global your_select

    PlzInput()
    print(your_select)


ConnectGame()
StartGame()
