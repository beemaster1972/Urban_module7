team1_num = 5
print('В команде Мастера кода участников: %s ! ' % team1_num)
team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
score_2 = 42
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team1_time = 18015.2
team1_name = 'Волшебники данных'
print("{name} решили задачи за {time} с !".format(name=team1_name,time=team1_time))
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач.")
victory = 'победа'
team2_name = 'Мастера кода'
final_string = f"Результат битвы: {victory} команды {team2_name if score_2 > score_1 else team1_name}!"
print(final_string)
tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
