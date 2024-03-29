class Person:
    def __init__(self, name, age, height):  # 생성자 메서드
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):   # 클래스가 문자열 타입으로 호출될 때 사용되는 메서드
        return "Person 설명, 이름은 " + self.name + " 키는" + str(self.height)

    def __len__(self):   #
        return self.height

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None

p = Person("철수", 18, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])