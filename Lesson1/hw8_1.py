import random
import copy

max_barrel = 90
numbers_in_cart = 15
numbers_in_line = 5


def gen_card():
    num_comb = random.sample(range(1, max_barrel + 1), numbers_in_cart)
    card = [sorted(num_comb[i:i + numbers_in_line]) for i in range(0, len(num_comb), numbers_in_line)]
    return card


def gen_barr_list():
    return random.sample(range(1, max_barrel + 1), 90)


def get_barrel(barr_list):
    return barr_list.pop()


def show_card(card):
    card = copy.deepcopy(card)
    placeholders = ' '.join(['{:>2}' for i in range(9)])
    for line in card:
        for space in ' ' * 4:
            line.insert(random.randint(0, len(line) - 1), space)
    return [placeholders.format(*line) for line in card]


def update_card(card, barrel):
    for line in card:
        yield ['-' if x == barrel else x for x in line]


def is_empty(card):
    for line in card:
        for el in line:
            if el != '-':
                return False
    return True


def barr_in_card(card, barrel):
    return barrel in [barrel for line in card for barrel in line]


def play_round():
    print('Игра лото началась!\n')
    player_card, comp_card = gen_card(), gen_card()
    barrels = gen_barr_list()
    while True:
        next_barrel = get_barrel(barrels)
        print('Вышел баченок с номером: {}. Осталось в мешке: {}'.format(next_barrel, len(barrels)))
        print("{0} Ваша карта {0}\n{1}\n{2}\n{3}".format('-' * 6, *show_card(player_card)))
        print("{0} Карта противника {0}\n{1}\n{2}\n{3}".format('-' * 5, *show_card(comp_card)))
        answ = 'a'
        while answ not in 'ynq':
            answ = input("Этот баченок есть на твоей карте? 'у'= да, 'n'= нет и 'q' для выхода: ")
        if answ == 'q':
            break
        elif (answ == 'y' and barr_in_card(player_card, next_barrel)) or (answ == 'n' and not barr_in_card(player_card,
                                                                                                           next_barrel)):
            print("Все верно! \n\nСледующий ход...")
        else:
            print("Ты проиграл!")
            break
        player_card = list(update_card(player_card, next_barrel))
        comp_card = list(update_card(comp_card, next_barrel))
        if is_empty(player_card):
            print('Вы заполнили карту!')
            break
        if is_empty(comp_card):
            print('Противник заполнил карту!')
            break


play_round()