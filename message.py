import random
def not_result():
    message = ['Упс... похоже у онлайнера здесь пусто...',
               'У меня не получилось найти...(',
               'К сожалению, удача сегодня не на нашей стороне...',
               'Придется мне сказать другую цифру, а то онлайнер ничего не выдает по такому запросу',
               '...',
               'А мы точно именно на такую сумму ищем!?',
               'Давай персмотрим цену, пожалуйста',
               'Ну же, я хочу поискать тебе хороший вариант, давай посмотрим выше!']
    return random.choice(message)