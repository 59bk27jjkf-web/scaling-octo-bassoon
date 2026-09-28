# Словари для классификации характеристик
positive_words = ['красивый', 'быстро', 'отличный', 'классный', 'удобно', 'отчетливо','спокойно']
negative_words = ['садится', 'разряжается', 'плохой', 'ужасный', 'медленный', 'глючит', 'мах', 'минус']
neutral_words = ['телефон', 'экран', 'батарея', 'дюйма', 'камера', 'корпус']

while True:
    # Ввод отзыва и предложение ввести следующий
    review = input("Введите отзыв о товаре (или 'выход' для завершения): ")
    if review.lower() == 'выход':
        break

    # 1. Предварительная обработка текста
    text = review.lower()
    
    # Обработка знаков препинания
    for punctuation in [',', '.', '!', '?', ';', ':', '-', '(', ')']:
        text = text.replace(punctuation, ' ')
        
    # Разделение текста на отдельные слова
    words = text.split()

    # Списки для найденных характеристик
    positive = []
    negative = []
    neutral = []

    # 2. Цикл обработки слов
    for word in words:
        if word in positive_words:
            positive.append(word)
        elif word in negative_words:
            negative.append(word)
        elif word in neutral_words:
            neutral.append(word)

    # 3. Подсчёт результатов
    pos_count = len(positive)
    neg_count = len(negative)

    # 4. Определение общей оценки
    if pos_count == 0 and neg_count == 0:
        overall = "нейтральный отзыв"
    elif pos_count > neg_count:
        overall = "положительный отзыв"
    elif neg_count > pos_count:
        overall = "отрицательный отзыв"
    else:
        overall = "смешанный отзыв"

    # 5. Вывод результата
    print("\nРезультат обработки текущего отзыва:")
    print(f"Положительные характеристики: {', '.join(positive)}")
    print(f"Отрицательные характеристики: {', '.join(negative)}")
    print(f"Нейтральные характеристики: {', '.join(neutral)}")
    print(f"Общая оценка: {overall}")
    print("-" * 40)