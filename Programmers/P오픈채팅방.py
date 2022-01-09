def solution(record):
    temp = []
    id_list = {}
    for data_line in record:
        data = data_line.split()
        if data[0] == "Enter":
            temp.append(f"{data[1]}님이 들어왔습니다.")
            id_list[data[1]] = data[2]
        elif data[0] == "Leave":
            temp.append(f"{data[1]}님이 나갔습니다.")
        else:
            id_list[data[1]] = data[2]
    answer = []
    for info in temp:
        answer.append(info.replace(info[:info.find('님')], id_list[info[:info.find('님')]]))

    return answer


print(solution(
    ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"]))
