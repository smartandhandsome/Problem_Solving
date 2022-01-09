def solution(table, languages, preference):
    score = {}
    for lang, pref in zip(languages, preference):
        for job in table:
            checklist = job.split()
            if lang in checklist:
                score[checklist[0]] = score.get(checklist[0], 0) + (6 - checklist.index(lang)) * pref
    print(score.items())
    return sorted(score.items(), key=lambda x: [[-x[1], x[0]]])


# sorted(score.items(), key=lambda x: [[-x[1], x[0]]])[0][0]
# 다음에 또 볼것


print(solution(
    ["SI JAVA JAVASCRIPT SQL PYTHON C#",
     "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
     "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
     "GAME C++ C# JAVASCRIPT C JAVA"],
    ["JAVA", "JAVASCRIPT"],
    [7, 5]
))
