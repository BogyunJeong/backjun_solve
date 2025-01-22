number_of_books = 100


def decrease_books(num):
    global number_of_books
    number_of_books -= num
    print('남은 책의 수 :', number_of_books)


def rental_book(info):
    num = info['age'] % 10
    decrease_books(num)
    print(f"{info['name']}님이 {num}권의 책을 대여하였습니다")
    #num = user['age'] % 10
    #map(decrease_books,user['age'])
    #map(lambda x: f"{user['name']}님이 {num}권의 책을 대여하였습니다",user)
 
def create_user(info):
    name,age,address = info
    print(f"{name}님 환영합니다")
    return {'name': name, 'age': age, 'address': address}


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
many_user = zip(name,age,address)
info = list(map(create_user,many_user))
user = list(map(lambda x: {'name': x['name'], 'age': x['age'],'address': x['address']},info))

list(map(rental_book,user))
