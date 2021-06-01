import hello_func
import greeting_func

def main():
    print("insa_func 모듈입니다.")
    print("__name__ : ", __name__)
    hello_func.hello()
    greeting_func.greeting()

main()