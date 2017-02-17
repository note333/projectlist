class school:
    def __init__(name,year,address):
        self.name=name
        self.year=year
        self.address=address

school.name=input("이름을 입력해주세요")
school.year=input("설립년도을 입력해주세요")
school.address=input("주소을 입력해주세요")

print("제 이름은 "+school.name+"이구요 설립년도는 "+school.year+"년도 입니다 또한 제 주소는 "+school.address+"입니다")
