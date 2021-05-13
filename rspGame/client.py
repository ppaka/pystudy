import socket

HOST = '127.0.0.1'
PORT = 9999

client_socket = None


def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))


def checking():
    global client_socket
    # msg = 'checking'
    # data = msg.encode()
    # length = len(data)
    # client_socket.sendall(length.to_bytes(4, byteorder="little"))
    # client_socket.sendall(data)

    data = client_socket.recv(4)
    length = int.from_bytes(data, "little")
    data = client_socket.recv(length)
    msg = data.decode()
    print("(수신)", msg)
    if msg == "꽉찬 방입니다.":
        return


def send_to_host():
    global client_socket
    # 10번의 루프로 send receive를 한다.
    for i in range(1, 10):
        # 메시지는 hello로 보낸다.
        msg = 'hello'
        # 메시지를 바이너리(byte)형식으로 변환한다.
        data = msg.encode()
        # 메시지 길이를 구한다.
        length = len(data)
        # server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
        client_socket.sendall(length.to_bytes(4, byteorder="little"))
        # 데이터를 전송한다.
        client_socket.sendall(data)

        # server로 부터 전송받을 데이터 길이를 받는다.
        data = client_socket.recv(4)
        # 데이터 길이는 리틀 엔디언 형식으로 int를 변환한다.
        length = int.from_bytes(data, "little")
        # 데이터 길이를 받는다.
        data = client_socket.recv(length)
        # 데이터를 수신한다.
        msg = data.decode()
        # 데이터를 출력한다.
        print('Received from : ', msg)

    client_socket.close()
