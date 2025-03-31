import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_login_yandex = os.getenv('MY_LOGIN_YANDEX')
my_password_yandex = os.getenv('MY_PASSWORD_YANDEX')

sender_email = 'angelina33520@yandex.ru'
recipient_email = 'angelina33520@yandex.ru'
subject = 'Приглашение!'
website = 'https://dvmn.org/profession-ref-program/angelina1906/LAwcI/'
friend_name = 'Аня'
my_name = 'Ангелина'
letter = '''\
from: {0} 
to: {1}
subject: {2}
Content-Type: text/plain; charset="UTF-8";

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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(sender_email, recipient_email, subject)
letter = letter.replace('%website%', website)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', my_name)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(my_login_yandex, my_password_yandex)
server.sendmail(sender_email, recipient_email, letter)
server.quit()
