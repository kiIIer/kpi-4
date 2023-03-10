# Кількість інформації

До кількості інформації висувається кілька вимог:

1. Невідємність величини
2. Адитивність
3. Прямувати до нули при недостовірності повідомлення

Обчислюється за формулою Шенона. Чим більша імовірність появи слова тим менше інфомрації воно в себе несе.

Зі збільшенням ступеня очікуваності повідомлення тим менше корисного воно несе.

## Одиниця виміру

Існує джерело повідомлень та спостережник який може описувати джерело за допомогою алфавіта.  Наприклад двійковий алфавіт. Потужність такого алфавіту - 2, нам також треба множина появи кожного слова. Умова максимуму ентропії, коли імовірності однакові. Ентропія - середня кількість інформації яка припадає на повідомлення.

Фомрула для обчислення кільксті інфомації = $I=\log_b{p}$. Якщо 0 та 1 мають імовірнісь 50%, то в одному інформація - 1 біт.

Розглянемо десятковий алфавіт, в кожного 1/10. Кількість інформації буде 1 dit = decimal digit.

Рознлянемо натуральний алфавіт А. A={0; 1; 2.71}. q=e=2.71.  Множина імовірностей 1/e Сумма імовірностей перевищує одиницю.  Кількість інформації в такому повідомленні буде 1 nit = natural digit.

Найбільш близький до натурального - трійковий алфавіт. Він є найефективнішим. Працює в усіх сферах. Але вони є ненадійними, тому не широко вживатися. Позначимо символи з множини 0, 1, 2.  Варіант фізичної реалізації алфавіту рівнями напруги: A = {-3V, 0V, +3V}.  Одна з таких обчислювальних машин - Сетунь.

Ентропія джерела - середня кількість інформації що міститься в одному повідомленні джерела.

Один біт це не 0 і не 1 це не символи, 1 біт це кількість інфомрації, яка міститься у одному із двох рівноімовірних симловів, що генеруютсья гіпотетечним двійковим джерелом повідомлень

## Джерело повідомлень

Фізичний об'єкт та спостерігач який може описувати фізичний об'єкт у певний момент часу.

## Ентропія джерела повідомлень

Це загальна характеристика джерела повідомлень вцілому. В повідомлення тільки кілкість інфомації. ДЖерело може мати середню кількість інфомації та середню кількість повідомлень

## Безумовна ентропія джерела

Безумовна ентропія є характеристикою джерела А у тмоу випадку, коли А розглядається як статистично ізольований від інших джерел об'єкт, символи якого не мають статичтичного вплаву і вз'язку між ними

## Стиснення даних

Оптимальне неріввномірне кодування

Для встановлення мінімального значення кількості повідомлень, треба максимізувати ентропію джерела
