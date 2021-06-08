import socket
import threading

player_1_ready = False
player_2_ready = False
player_1_client = ""
player_2_client = ""


def binder(client_socket, addr):
    print('연결됨: ', addr)

    try:
        # 접속 상태에서는 클라이언트로 부터 받을 데이터를 무한 대기한다.
        # 만약 접속이 끊기게 된다면 except가 발생해서 접속이 끊기게 된다.
        while True:
            # socket의 recv함수는 연결된 소켓으로부터 데이터를 받을 대기하는 함수입니다. 최초 4바이트를 대기합니다.
            data = client_socket.recv(4)
            # 최초 4바이트는 전송할 데이터의 크기이다. 그 크기는 little 엔디언으로 byte에서 int형식으로 변환한다.
            length = int.from_bytes(data, "little")
            # 다시 데이터를 수신한다.
            data = client_socket.recv(length)
            # 수신된 데이터를 str형식으로 decode한다.
            msg = data.decode()
            # 수신된 메시지를 콘솔에 출력한다.
            print('수신됨: ', addr, msg)

            # 수신된 메시지 앞에 「echo:」 라는 메시지를 붙힌다.
            msg = "메세지: " + msg
            # 바이너리(byte)형식으로 변환한다.
            data = msg.encode()
            # 바이너리의 데이터 사이즈를 구한다.
            length = len(data)
            # 데이터 사이즈를 little 엔디언 형식으로 byte로 변환한 다음 전송한다.
            client_socket.sendall(length.to_bytes(4, byteorder="little"))
            client_socket.sendall(data)
    except:
        print("접속 오류 : ", addr)
    finally:
        client_socket.close()


def check_clients(client_socket, addr):
    global player_1_client
    global player_1_ready
    global player_2_client
    global player_2_ready

    try:
        while True:
            if not player_1_ready and not player_2_ready:
                print("플레이어1 접속")
                player_1_ready = True
                player_1_client = client_socket

                msg = "플레이어1로 접속하셨습니다."
                data = msg.encode()
                length = len(data)
                client_socket.sendall(length.to_bytes(4, byteorder="little"))
                client_socket.sendall(data)
            elif not player_1_ready and player_2_ready:
                print("플레이어1 접속")
                player_1_ready = True
                player_1_client = client_socket

                msg = "플레이어1로 접속하셨습니다."
                data = msg.encode()
                length = len(data)
                client_socket.sendall(length.to_bytes(4, byteorder="little"))
                client_socket.sendall(data)
            elif player_2_ready and not player_2_ready:
                print("플레이어2 접속")
                player_2_ready = True
                player_2_client = client_socket

                msg = "플레이어2로 접속하셨습니다."
                data = msg.encode()
                length = len(data)
                client_socket.sendall(length.to_bytes(4, byteorder="little"))
                client_socket.sendall(data)
            elif player_1_ready and player_2_ready:
                print("(전송)", addr, "꽉찬 방입니다.")
                msg = "꽉찬 방입니다."
                data = msg.encode()
                length = len(data)
                client_socket.sendall(length.to_bytes(4, byteorder="little"))
                client_socket.sendall(data)

                client_socket.close()
    except:
        print("접속 오류 : ", addr)
        if player_1_client == client_socket:
            print("플레이어1 끊김")
            player_1_ready = False
            player_1_client = None
        elif player_2_client == client_socket:
            print("플레이어2 끊김")
            player_2_ready = False
            player_2_client = None

        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 9999))
server_socket.listen()

try:
    while True:
        # client로 접속이 발생하면 accept가 발생한다.
        # 그럼 client 소켓과 addr(주소)를 튜플로 받는다.
        client_socket, addr = server_socket.accept()
        # 쓰레드를 이용해서 client 접속 대기를 만들고 다시 accept로 넘어가서 다른 client를 대기한다.
        # th = threading.Thread(target=binder, args=(client_socket, addr))
        # th.start()
        th1 = threading.Thread(target=check_clients, args=(client_socket, addr))
        th1.start()
except:
    print("서버")
finally:
    server_socket.close()
