import random

def start_adventure():
    print("🪱 Привет, маленький червячок! Сегодня у тебя важная миссия.")
    print("Твоя цель - найти самое вкусное яблоко в саду.")
    choose_path()

def choose_path():
    print("\nТы видишь перед собой три дороги:")
    print("1. 🌳 Лесная тропа")
    print("2. 🌷 Поле цветов")
    print("3. 🏙️ Дорога в город")
    choice = input("Куда ты пойдешь? Введи 1, 2 или 3: ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        flower_field()
    elif choice == "3":
        city_path()
    else:
        print("Неверный выбор. Попробуй снова.")
        choose_path()

def forest_path():
    print("\nТы выбрал лесную тропу 🌳.")
    print("В лесу прохладно и влажно, тебе нравится тут ползать.")
    if encounter_enemy():
        battle()
    print("Ты находишь две ягоды:")
    print("1. 🍓 Красная ягода")
    print("2. 🍇 Синяя ягода")
    choice = input("Какую ягоду ты съешь? Введи 1 или 2: ")

    if choice == "1":
        print("\nТы съел красную ягоду 🍓. Она оказалась ядовитой! 😵")
        print("К сожалению, ты проиграл. Начни сначала.")
        start_adventure()
    elif choice == "2":
        print("\nТы съел синюю ягоду 🍇. Она дала тебе силу и энергию!")
        print("Ты продолжаешь свой путь и находишь вкусное яблоко 🍏. Победа! 🎉")
    else:
        print("Неверный выбор. Попробуй снова.")
        forest_path()

def flower_field():
    print("\nТы выбрал поле цветов 🌷.")
    print("Здесь очень красиво и пахнет цветами.")
    if encounter_enemy():
        battle()
    print("Ты видишь двух друзей:")
    print("1. 🐝 Пчела")
    print("2. 🐞 Божья коровка")
    choice = input("Кого ты выберешь в спутники? Введи 1 или 2: ")

    if choice == "1":
        print("\nТы выбрал пчелу 🐝. Она показывает тебе путь к медовой поляне, но яблока там нет.")
        print("Ты возвращаешься к началу пути.")
        choose_path()
    elif choice == "2":
        print("\nТы выбрал божью коровку 🐞. Она ведет тебя к яблоневому саду.")
        print("Ты находишь самое вкусное яблоко 🍎. Победа! 🎉")
    else:
        print("Неверный выбор. Попробуй снова.")
        flower_field()

def city_path():
    print("\nТы выбрал дорогу в город 🏙️.")
    print("В городе много шума и машин. Ты находишь магазин:")
    if encounter_enemy():
        battle()
    print("1. 🛒 Магазин фруктов")
    print("2. 🍭 Кондитерский магазин")
    choice = input("В какой магазин ты заползешь? Введи 1 или 2: ")

    if choice == "1":
        print("\nТы заполз в магазин фруктов 🛒. Там много яблок!")
        print("Ты находишь самое вкусное яблоко 🍎. Победа! 🎉")
    elif choice == "2":
        print("\nТы заполз в кондитерский магазин 🍭. Там много сладостей, но яблок нет.")
        print("Ты возвращаешься к началу пути.")
        choose_path()
    else:
        print("Неверный выбор. Попробуй снова.")
        city_path()

def encounter_enemy():
    # Случайное событие встречи с врагом
    return random.choice([True, False])

def battle():
    print("\nТы встретил врага! 🕷️")
    print("Бой начинается!")
    player_health = 10
    enemy_health = 10

    while player_health > 0 and enemy_health > 0:
        print(f"\nТвое здоровье: {player_health}")
        print(f"Здоровье врага: {enemy_health}")
        action = input("Выбери действие: 1. Атака 2. Уклонение: ")

        if action == "1":
            damage = random.randint(1, 4)
            enemy_health -= damage
            print(f"Ты нанес врагу {damage} урона!")
        elif action == "2":
            print("Ты попытался уклониться!")
            if random.choice([True, False]):
                print("Успешное уклонение!")
                continue
            else:
                print("Не удалось уклониться!")

        if enemy_health > 0:
            enemy_damage = random.randint(1, 4)
            player_health -= enemy_damage
            print(f"Враг нанес тебе {enemy_damage} урона!")

    if player_health > 0:
        print("\nТы победил врага! 🎉")
    else:
        print("\nТы проиграл в бою. Начни сначала.")
        start_adventure()

# Запуск игры
start_adventure()
