from datetime import datetime, timedelta

def process_absences(absences):
    result = []
    absences.sort(key=lambda x: x['date'])
    
    for absence in absences:
        student_id = absence['id']
        student_name = absence['fullName']
        absence_date = datetime.strptime(absence['date'], "%Y-%m-%d").date()
        
        if not result or result[-1]['id'] != student_id or result[-1]['endDate'] + timedelta(days=1) != absence_date:
            result.append({'id': student_id, 'fullName': student_name, 'startDate': absence_date, 'endDate': absence_date})
        else:
            result[-1]['endDate'] = absence_date
    
    # Преобразование дат в строки в формате "гггг-мм-дд"
    for entry in result:
        entry['startDate'] = entry['startDate'].strftime("%Y-%m-%d")
        entry['endDate'] = entry['endDate'].strftime("%Y-%m-%d")
    
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