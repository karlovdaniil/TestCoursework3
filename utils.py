import json


def load_json(path: str) -> list[dict] | str:
    with open(path, "r", encoding="utf-8") as read_files:
        data = json.load(read_files)
        return data


def sorted_json_by_date(data: list[dict]) -> list[dict]:
    data = [trans for trans in data if trans]
    sorted_data = sorted(data, key=lambda x: x.get('date'), reverse=True)
    return sorted_data


def get_data_from_operation(trans: dict, type_: str) -> tuple[str, str]:
    if type_ in trans:
        acc_or_card_name = ' '.join(trans[type_].split()[:-1])
        acc_card = trans[type_].split(' ')[-1]
        number = ''
        if 'Счет' in acc_or_card_name:
            number = '**' + acc_card[-4:]
        else:
            for i in range(len(acc_card)):
                if 6 <= i < 12:
                    number += '*'
                else:
                    number += acc_card[i]
                if (i + 1) % 4 == 0 and i != 15:
                    number += ' '
    elif 'Открытие' in trans['description']:
        return 'Пополнение', ''
    else:
        acc_or_card_name, number = '', ''
    return acc_or_card_name, number
