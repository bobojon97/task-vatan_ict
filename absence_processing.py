from datetime import datetime, timedelta

def process_absences(absences):
    sorted_absences = sorted(absences, key=lambda x: (x['id'], x['date']))
    result = []
    current_record = None

    for absence in sorted_absences:
        if current_record is None:
            current_record = {
                'id': absence['id'],
                'fullName': absence['fullName'],
                'startDate': absence['date'],
                'endDate': absence['date']
            }
        else:
            current_date = datetime.strptime(absence['date'], '%Y-%m-%d').date()
            previous_date = datetime.strptime(current_record['endDate'], '%Y-%m-%d').date()

            if current_record['id'] == absence['id'] and (current_date - previous_date).days == 1:
                current_record['endDate'] = absence['date']
            else:
                result.append(current_record)
                current_record = {
                    'id': absence['id'],
                    'fullName': absence['fullName'],
                    'startDate': absence['date'],
                    'endDate': absence['date']
                }

    if current_record is not None:
        result.append(current_record)

    return result


# Пример использования
absences = [
    {"id": 1, "fullName": "Быков Юрий", "date": "2021-09-01"},
    {"id": 56, "fullName": "Мамонтов Панкрат", "date": "2021-09-01"},
    {"id": 12, "fullName": "Ларионов Владимир", "date": "2021-09-01"},
    {"id": 1, "fullName": "Быков Юрий", "date": "2021-09-02"},
    {"id": 56, "fullName": "Мамонтов Панкрат", "date": "2021-09-02"},
    {"id": 1, "fullName": "Быков Юрий", "date": "2021-09-03"},
    {"id": 1, "fullName": "Быков Юрий", "date": "2021-09-04"},
    {"id": 1, "fullName": "Быков Юрий", "date": "2021-09-05"},
    {"id": 1, "fullName": "Быков Юрий", "date": "2021-09-06"},
    {"id": 12, "fullName": "Ларионов Владимир", "date": "2021-09-06"},
    {"id": 12, "fullName": "Ларионов Владимир", "date": "2021-09-08"},
    {"id": 12, "fullName": "Ларионов Владимир", "date": "2021-09-09"},
    {"id": 56, "fullName": "Мамонтов Панкрат", "date": "2021-09-09"},
    {"id": 12, "fullName": "Ларионов Владимир", "date": "2021-09-12"},
    {"id": 12, "fullName": "Ларионов Владимир", "date": "2021-09-13"},
    {"id": 56, "fullName": "Мамонтов Панкрат", "date": "2021-09-18"}
]

result = process_absences(absences)
print(result)