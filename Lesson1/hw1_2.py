# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_var = int(input('Введите время в секундах? : '))
hours = user_var // 3600
minutes = (user_var - (hours * 3600)) // 60
seconds = (user_var - (hours * 3600)) - (minutes * 60)
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

print(f'{user_var} секунд это {hours}:{minutes}:{seconds}')


