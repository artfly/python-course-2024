# Задание 6

### 1. Flashcards (6 баллов)

Напишите программу, которая будет помогать изучать новую информацию с помощью методики [flashcards](https://en.wikipedia.org/wiki/Flashcard)

Пример работы программы:
```
Доступные комманды:
- /load filename - загрузить карточки из файла
- /save filename - сохранить карточки в заданный файл
- /study - проверить знание карточек
- /add - добавить новую карточку
- /help - показать дотупные команды
- /exit - завершить программу

Введите комманду:
/load programming_cards.txt
Загружено 5 карточек из категории "programming"
Введите комманду:
/study
Сколько карточек будем повторять?
3
Нажмите 'Enter' после вопроса, чтобы показать ответ

Инструкция, которая завершает цикл досрочно?

break

В чем разница между классом и объектом?

Класс - это заготовка объекта, чертеж, как объект будет выглядеть после
Объект - это уже созданная сущность, в ней инициалзированы атрибуты
Приммер: Dog - класс, конкретная собака - объект

Что такое параметр?

То, что на вход принимает функция, штука в скобочках в объявлении функции
Пример: в def foo(a) а - параметр

Введите комманду:
/add

Вопрос в карточке:
Как выглядит конструктор класса?

Ответ:
def __init__(self, параметры)

Сохранить эту карточку в категории "programming"(y/n)?
y

В категории "programming" теперь 6 карточек

/save programming_cards.txt

Карточки сохранены

/exit
```

#### 1.1 load_cards

Напишите функцию `load_cards(filename)`, которая принимает на вход название файла и загружает из него коллекцию карточек.  
Функция должна возвращать коллекцию карточек (коллекция и карточка - это классы в программе)

Формат файла:
- 1 строка - название коллекции
- далее в файле лежат вопросы и ответы

Формат вопросов и ответов:
- 1 строка - сколько строк занимает вопрос / ответ
- содержимое вопроса или ответа

Пример файла:
```
programming
1
В чем разница между классом и объектом?
3
Класс - это заготовка объекта, чертеж, как объект будет выглядеть после
Объект - это уже созданная сущность, в ней инициалзированы атрибуты
Приммер: Dog - класс, конкретная собака - объект
1
Что такое параметр?
2
То, что на вход принимает функция, штука в скобочках в объявлении функции
Пример: в def foo(a) а - параметр
```

#### 1.2 save_cards

Напишите функцию `save_cards(filename, collection)`, которая на вход принимает коллекцию карточек и имя файла.  
Функция должна записать в полученный файл коллекцию карточек в формате, описанном в 1.1.  
Если такой файл уже существует на диске, то нужно его перезаписать.

#### 1.3 study

Напишите функцию `study(collection)`, которая на вход принимает коллекцию карточек.  
Эта функция: 
- спрашивает у пользователя, сколько будем тренировать карточек в этот раз. если в коллекции нет столько карточек, то сообщает сколько карточек всего и переспрашвает снова
- выбирает случайную карточку из всех (без повторов)
- показывает вопрос и ждет ввода пользователя. когда он нажал enter - показывает к карточке ответ
- выбирает следующую случайную карточку до тех пор, пока не показали столько карточек, сколько сказал пользователь

Для выбора случайной карточки можно воспользоваться функцией `random.randint` (использовалась в предыдущем задании `hangman`)

#### 1.4 add_card

Напишите функцию `add_card(collection)`, которая на вход принимает коллекцию карточек. 
Эта функция добавляет новую карточку в коллекцию на основе того, что введет пользователь:
- выводит на экран строку "Вопрос в карточке:", ждет ввода пользователя
- запоминает вопрос, выводит на экран "Ответ:"
- запоминает ответ для карточки, создает карточку как объект класса
- добавляет карточку в коллекцию

#### 1.5 help

Напишите функцию `help()`, которая ничего не принимает и возвращает строку с описанием доступных в программе команд

#### 1.6 main

Напишите функцию `main()`, которая:

- показывает пользователю информацию о доступных командах
- в бесконечном цикле ждет очередную команду
- когда пользователь ввел команду:
  - если пришла команда `/exit`, то выходит из бесконечного цикла
  - если пришла неизвестная команда, то сообщает об этом и печатает список доступных команд снова
  - иначе вызывает одну из доступных функций (ввод пользователя нужно проверить на корректность перед вызовом)

Вызовите `main` в своем файле.
