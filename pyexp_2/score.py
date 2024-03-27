score_students = [89, 70, 90, 50]
score_sum = 0

for score_student in score_students:
    score_sum += score_student

score_aver = score_sum / len(score_students)
score_max = max(score_students)
score_min = min(score_students)

print(f"""该班级平均成绩为：{score_aver}
最大值：{score_max}
最小值：{score_min}""")


