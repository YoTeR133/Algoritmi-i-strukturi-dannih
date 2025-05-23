# Реализация хеш-таблицы с расширением

## Описание задачи
Задача заключается в создании хеш-таблицы для чисел типа `int` с динамическим расширением. 
Требования:  
1. Реализовать хеш-таблицу с методами вставки, поиска, удаления и отображения.  
2. Внедрить механизм увеличения ёмкости таблицы в два раза, когда количество элементов достигает заданного порога (50%).  

## Структура проекта
Проект состоит из трёх файлов:  
- **`client.py`** — точка входа, запрашивает у пользователя начальный размер таблицы и количество элементов для вставки, затем выводит результат.  
- **`interface.py`** — содержит интерфейс хеш-таблицы с абстрактными методами `insert`, `find`, `delete` и `display`.  
- **`UnorderedArray.py`** — реализует хеш-таблицу с использованием линейного пробирования для разрешения коллизий и механизмом расширения.  

### Основные особенности реализации
- **Хеш-функция**: `value % capacity`.  
- **Разрешение коллизий**: линейное пробирование.  
- **Коэффициент загрузки**: 50% (при превышении таблица увеличивается в 2 раза).  
- **Поддержка дубликатов**: дубликаты не добавляются.  
- **Удаление**: используется маркер `<Удалён>` для сохранения целостности цепочек.  

## Вывод
Хеш-таблица успешно реализована с учётом всех требований:  
- Динамическое расширение активируется при достижении 50% заполнения.  
- Поддерживается работа с меньшим количеством элементов без необходимости расширения.  
- Линейное пробирование эффективно решает коллизии.  
- Дубликаты пропускаются, что может привести к меньшему числу элементов, чем запрошено.  
