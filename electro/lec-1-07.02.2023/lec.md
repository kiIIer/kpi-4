# Електроніка та мікропроцессорна техніка

## Про курс

Кинули електронний підручник в телеграмі. Там є силабус: що треба вивчати та які лаби. В цьому семестрі курсова робота. Там є варіанти для виконання, ті самі що в минулому семестрі. Є методичка до курсової роботи. В наступну середу буде консультація до курсової о 19. Є модульна: методичка до модульної. Є посібник в якому є які лабораторні роботи, в якому порядку та короткі методички до них. 3 лаби по avers студія, виконувати коменти. Потім поставити протеус(8.6) на консультації нам покажуть ці проекти.

## Характеристика мікропроцессорних систем

Мікропроцессор не мав пам'яті але мав аривметичинй пристрій, робив арви операції та керувава зв'язком з шиною.

Спраава в тому що електроніка розвивалася дуже швидко та потужно. Спочатку на лампах, потім на транзисторах, мікросхемах(малий ступінь інтеграції) потім прийшли середньої степені інтеграції. Далі були виликі та надвеликі. Вони реалізовували жорстку логіку. Де була другована плала, робилися отвори. Робили рисунок та потім запаювали певні елементи. З'яднання з отворами були окремі та після запайки змінувалася функція. Але якщо треба змінити функцію, то це габела. Це треба було робити технічно користувачеві та це не зручно. А ось з'явлення мікропроцессора якого можна було програмувати, можна було змінити програму а не технічний варіант пристрою. Коли Новацький вивчав це сам, там він читав мікропроцессорну техніку сам. ведеться вивчення під двома кутами. Soft та Hard.  hard - технічна реалізація, soft - програмування. Ці частини пов'язані, тому ми будемо вивчати і софт на прикладі команд та потім самі модулі пам'яті, переривання, введення, виведеня.

Тармін мікроавм з'явиввся пізніше мікроппроцессорм - це універасальний блок для обробки. Вона включала озп, мікропроцессоп, постійний запам'ятовуваний пристрій, пристрій введення та виведення.

Потім була однокристальна авм, реалізована на базі мікросхемі кристалів.

Потім була заміна на мікроконтроллер, містить пам'ять, пам'ять програм, порти введення виведення, процессор, таймери, ацп, цап.

Ми спочатку на мікропроцессорах а потім на мікроконтроллери перейдемо.

### Основні характеристики

Довжина слова , кількість комірок, швидкодія

Наприклад 8-бітний МП i8080 має 16 пдресний ліній, що може були 2^16 комірок пам'яті. Об'єм пам'яті тоді буде 64Кбайт.

Мікроконтроллер 8 бітний АТ89С51 має 16 адресний ліній та може бути 64Кбайта пам'яті

Швидкодія визначається часом виконання певних програм або команд. МОже бути максимаьлне значення тактової частоти. Знаючи максимальну частоту знаємо тривалість одного такту.

Можна оцінювати швидкодію часом пересилання з пересилання з регістру до регістру.

Потужний мікуропроцессор має велику довжину слова данних, багато комірок та швидко працює.

### Система числення

Це символічне представлення данних певними символами.  
Часто використовують 2, 10 та 16-у  
Окрім систем числення викорисовуютсья коди та мають назви систем числення. КОли в 2-ій відображаємо інформацію - маємо код.  
Найпростіша десяткова система числення. Викостовується 10 цифр від 0 до 9, оскільки це позиційна система, кожне число має розряди, розряди йдуть від 0 до 9(10-1) там понятно короче как работает.  
Найбільша цифра на 1 менша основи. Для визначення кожної, цифра множиться на вагу позиції на якій стоїть.

### Функціональна система мікропроцессорної системи

Згідно зі стандартами є різні типи схем. Сьогодні буде струкрутна, де всі складові зображені прямокутниками є тільки стрілками та напрямок передачі

Фнукціональна більш розгорнута, де є зв'язки та лінії. Вона є гіпотетичною, бо в нас обстрактинй об'єкт керування.