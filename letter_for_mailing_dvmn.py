import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

from_mail = 'angelina33520@yandex.ru'
to_mail = 'angelina33520@yandex.ru'
subject = 'Приглашение!'
website = 'https://dvmn.org/profession-ref-program/angelina1906/LAwcI/'
friend_name = 'Аня'
my_name = 'Ангелина'
letter = '''\
from: {0} 
to: {1}
subject: {2}
content-type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(from_mail, to_mail, subject)
letter = letter.replace('%website%', website)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', my_name)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail('angelina33520@yandex.ru', 'angelina33520@yandex.ru', letter)
server.quit()
