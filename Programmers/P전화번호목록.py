def solution(phone_book):
    dic = {}
    for p in phone_book:
        dic[p] = 1
        temp = ""
        for n in p:
            temp += n
            if temp in dic and temp != p:
                return False
    return True


if __name__ == "__main__":
    # __name__ = "__main__" 의 뜻은 직접 실행 했을 때만 실행한다는 뜻
    # 다른 모듈에서 import 되어 실행 되었을 때는 아래 코드가 실행되지 않음
    # __name__ 은 interpreter 가 실행 전에 만든 global 변수임
    print(solution(["119", "97674223", "1195524421"]))
