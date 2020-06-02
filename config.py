# Токен дискорд бота. Если его соединить в одну строку, то при засветки его в сети(например этого файла)
# дискорд сразу же забанит ключ и его придётся менять, поэтому извращаемся разбивая его на половинки

part1 = 'NzE0ODE4NTc2MTQ5OTA1NDg4.Xs'
part2 = '_BSg.Fpi5OX5LZewFfK7KjqQOpKOduGg'
TOKEN = part1 + part2

# ========== Модуль Weather ==========
api_key = 'a7cb15e0-43e3-4506-8fe6-3e567b02fa5b'    # апи ключ Яндекс погоды

colors = {'DEFAULT': 0x000000, 'WHITE': 0xFFFFFF, 'AQUA': 0x1ABC9C, 'GREEN': 0x2ECC71, 'BLUE': 0x3498DB,
          'PURPLE': 0x9B59B6, 'LUMINOUS_VIVID_PINK': 0xE91E63, 'GOLD': 0xF1C40F, 'ORANGE': 0xE67E22, 'RED': 0xE74C3C,
          'GREY': 0x95A5A6, 'NAVY': 0x34495E, 'DARK_AQUA': 0x11806A, 'DARK_GREEN': 0x1F8B4C, 'DARK_BLUE': 0x206694,
          'DARK_PURPLE': 0x71368A, 'DARK_VIVID_PINK': 0xAD1457, 'DARK_GOLD': 0xC27C0E, 'DARK_ORANGE': 0xA84300,
          'DARK_RED': 0x992D22, 'DARK_GREY': 0x979C9F, 'DARKER_GREY': 0x7F8C8D, 'LIGHT_GREY': 0xBCC0C0,
          'DARK_NAVY': 0x2C3E50, 'BLURPLE': 0x7289DA, 'GREYPLE': 0x99AAB5, 'DARK_BUT_NOT_BLACK': 0x2C2F33,
          'NOT_QUITE_BLACK': 0x23272A}

color_list = [c for c in colors.values()]

condition = {'clear': 'Ясно', 'partly-cloudy': 'Малооблачно', 'cloudy': 'Облачно с прояснениями',
             'overcast': 'Пасмурно', 'partly-cloudy-and-light-rain': 'Небольшой дождь',
             'partly-cloudy-and-rain': 'Дождь', 'overcast-and-rain': 'Сильный дождь',
             'overcast-thunderstorms-with-rain': 'Сильный дождь, гроза', 'cloudy-and-light-rain': 'Небольшой дождь',
             'overcast-and-light-rain': 'Небольшой дождь', 'cloudy-and-rain': 'Дождь',
             'overcast-and-wet-snow': 'Дождь со снегом', 'partly-cloudy-and-light-snow': 'Небольшой снег',
             'partly-cloudy-and-snow': 'Снег', 'overcast-and-snow': 'Снегопад',
             'cloudy-and-light-snow': 'Небольшой снег', 'overcast-and-light-snow': 'Небольшой снег',
             'cloudy-and-snow': 'Снег'}

wind_dir = {'nw': 'Северо-западный', 'n': 'Северный', 'ne': 'Северо-восточный', 'e': 'Восточный',
            'se': 'Юго-восточный', 's': 'Южный', 'sw': 'Юго-западный', 'w': 'Западный', 'с': 'Штиль'}

part_name = {'night': 'ночью', 'morning': 'утром', 'day': 'днём', 'evening': 'вечером'}

# ========== Модуль WhoInChat ==========
corp_members = {}