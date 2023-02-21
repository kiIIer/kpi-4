# Теорія ймовірності та математична статистика

Теорія ймовірності є математичною наукою, що вивчає закономірності у випадкових явищах.

Предметом теорії ймовірностей є вивчення ймовірнісних закономірностей масових однорідних випадкових подій.

Експерименти, які в незмінних умовах можна повторити будь-яку кількість разів, але результати яких непередбачувані, у теорії ймовірностей називають випробуваннями

В результаті випробувань відбуваються події

Якщо ми підкидаємо кубик це експеримент а приклад елементарної події це випадіння одинички

Є і більш складні події, такою є випадіння непарного числа(1, 3, 5)

Події бувають достовірні випадкові та неможливі.

Достовірна - 100 проц відбудеться і ніяка інша

Неможлива - яка ніколи не може відбутись(викинути 7 на кубику д6)

Випадкова - може відбутись а може і ні

Коли описують ці події якоюсь математичною мовою, їх позначають великими літерами.

## Простір подій

Якщо ми проводимо якийсь експеримент, то в резульатті відбуваються якісь події

Пря цьому результатом можуть бути кілька елементрних подій(аверс або реверс при монетці)

Якщо підкидаємо гральну кістку - 1-6 на кубитку

Якщо запишемо всі ці елементарні події - отримаємо простір елементарних події Позначається $\Omega$

Часто треба визначити які подіх можуть відбутись та записати їх

Також може бути подія з множини елементарних(випадіння парного - 3 елементарні)

## Масові події

Коли ми розглядали предмет, там розглядаються масові події. Кожна випадкова подія є наслідком кількох невідомих причин які призводядь по певних подій.

Ми не можемо точно сказати чи випаде 1 чи ні на гральній кістці. Але якщо ми будемо проводити випробування багато разів, розглядати певну подію в однакових умовах, можна знайти імовірність з якою вона буде зв'являтись.

## Випадкові події

Ми вже знаємо що є елементарні події та більш складні які з них складаються.

Окрім цього випадкові пдії можна розділити на деякі різновиди.

Перші подіх називаютсья несумісними, якщо поява однієї з них виключає інші, викинути парне та непарне одночасне.

Якщо поява однієї подіх не виключає можливості появи іншої то вони сумісні. Вони не завжди відбуваються одночасно, але можуть разом. Викинути парне та менше 5. Можуть бути одночасно але не завжди.

По суті якщо ми розпишемо всі складні події на елементарні. Випадіння парного - 2,4,6. Випадіння числа менше 5 - 1234. Якщо перетин є то події є сумісними.

Події називають рівноможливими якщо немає причин стверджувати, що будь-яка з них можливіша за інші. Випадіння аверсу та реверсу мають однакову можливість

Дві несумісні події, які утворюють повну групу події називають протилежними. Якщо повна група подіх складається з двох подій та вони є несумісними, то вони є протилежними. Позгачаєтсья як НЕ з дискретки.

## Ймовірність

Для описання випадкової події недостатньо "можлива певна подія" потрібне певне число яке буде описувати степінь можливості події

Ось таке число і є ймовірністю події зазвичай позначають p (мала літера P)

Ймовірність є чиво? я єто не напішу

Численна міра степеню об'єктивної можливості цієї події.

Ймовірність події A позначається P(A)

Щоб оперувати ймовірністю, треба її якось знаходити. треба знаходити елементарні події які сприяють появі A поділити на загальну.

Якщо візьмемо монетку, то число можливих елементарних подій: випаде реверс або аверс, тобто елементарних подій дві, n = 2 в такому випробуванні. Наприклад подія А - випадіння аверсу. Число подій які сприяють випадінню А - 1, випадіння аверсу, тобто m = 1. Тоді ймовірність випадінню аверсу це 1/2; m не більше ніж n, тобто P не більше одиниці(або до 100 відсотків)

Якщо взяти випробування підкидання кістки і подія А - випадіння парного, то подія А - складна та число подій що сприяють - випадіння 246 та в нас буде m = 3. А число всіх можливих елементарних подій - 6, бо в нас 6 елементарних подій. Ймовірність випадінню A - 3/6 або знову 1/2.

На практичних ми будемо вирішувати більш складні задачі, де не так просто порахувати події які сприяють випадінню події А та треба буде згадати комбінаторику.

## Відносна частота

Якщо ми проводимо експерименти, ми можемо порахувати відносну частоту події А. Ми проводимо якусь кількість випробувань, де подія А з'явилась m разів. Відносна частота події А - те скільки з'явилсь поділити на загальну кількість випробувань.

Якщо беремо монетку та підкидаємо, та кожного разу дивимось що в нас вийшло та запам'ятовуємо, в нас вийде приблизто те що треба.

## Статистична ймовірність

Якщо кількість випробувань прямує до нескінченності, то частота буде прямувати до самої випадковості. За такими експериментами можемо отримати статистичну ймовірність такого.

Це можна теоретично розрахувати ймовірність, приканути елементарні події, поділене на загальну кількість. Або встановити статистично, але проводити багато разів

## Властивості ймовірності

Подія може бути достовірною, очевидно що p(A)=1. Як приклад достовірної події є випадіння на кістці числа не більше 6, тобто 6 за, 6 всього та в нас виходить 1

Якщо подія неможлива то ймовірністьдорівнює нулеві. Як приклад розглядали випадіння числа більше 6. Тобто ніколи такого не буде. Якщо подія випадкова то там буде від 0 до 1

Якщо події А та Б несумісні і вони не можуть відбутися одночасно та ми знаємо їх ймовірності, то ймовірність цих подій це сумма їх ймовірностей.

*я устал*

## Теорема додавання несумісних подій

... а загальна ймовірність випадіння події це 6, тообто ймовірність випадіння 1 це одна шоста, а якщо потрібна ймовірність випадіння не 1, то це протилежна подія. Це 1 - ймовірність події А.

Відповідна сумма ймовірностей подій, що утворюють повну группу подій - одиниця

*почему в первий день первая пара в 730(((*

## Додавання сумісний подій

Ми бачили що буде з несумісними, там сумма ймовірностей. Якщо події сумісні, то ймовірність настання однієї це сумма ймовірностей цих подій без сумми імовірностей їх настання одночасно.

Якщо ми візьмемо якісь сумісні події, типу випадіння парног числа та випадіння числа не менше 5, події сумісні, бо 6 відноситься до обох. Ймовірність випадіння парного - 1/2(3 варіанти а всього 6). Ймовірність подіх Б, тобто не менше 5, це 5 або 6, тобто 2/6 або 1/3. Відповідно щоб порахувати ймовірність сумми цих подій, ми додаємо ймовірність події А, ймовірність події Б та відняти ймовірність спільного настання, тобто вірогідність цифри 6. Оскільки це 1/6, то в нас буде 1/2 + 1/3 - 1/6.

## Залежні події

Окрім сумісних та несумісних які можуть просто відбуватись або не вібдуватись при випробуваннях, є залежні та незалежні події. Випадкоі події залежні, якщо ймовірність появи однієї з них, залежить або не залижить від появи іншої. Відповідно, якщо є події А та Б та подія А відбулась, то ймовірність події Б буде від цього залежати. Ми отримаємо умовну ймовірність події Б, ймовірність події Б при умові що подія А відбулась, та позначають P(B|A) = P(AB)/P(A)

Ймовірність одночасного відбуття подій, це незалежна помножити на залежну з умовою що є незалежна. Можна оперувати більш ніж двома подіями.

*спать хочу*

## Добуток незалежних подій

Якщо поява однієї не впливає на появі іншої, там більш проста формула, добудок подій це шанс обох.

Ці події залежні або незалежні відбуваютсья в наслідок якогось випробування й імовірність однієї залежить відбулась чи не відбулась інша подія

Є подія підкидання кубику та подія випадіння непарного числа. Розглянемо іншу подію, випадіння числа більше 3. Так і так випадкова подія. Якщо ми підкидаємо та знаємо що в нас вібдулась подія А, випадіння немарного. То чи впливає на ймовірність події Б в цьому експерименті. Впливає, якщо в нас випало 1 3 або 5, а в події Б входять числа 456, якщо в нас випало число 5 то відбулась і подія Б, а ні то ні. Якщо в результаті підкидання кубика то ймовірність того що настала подія Б це буде 1/3, варіант коли в нас випаде 5. Це приклад залежних подій

*может чайок заваріть?*

## Настання принаймні однієї подійї

Одиниця відняти всіх ймовірностей ненастання подій.

Тобто...

Єм...
Наприклад...
Якщо взяту ту саму гральну кісту та її викоритсати як приклад в цьому та наприклад ймовірність настання прийнаймні однієї з подій наприклад ми маємо якусь групу подій, випадає число 1 чи 3 чи 5, ймовірні настання кожної = 1/6 ймовірність ненастання кожної 5/6 та ймовірність настання прийнаміні 1 це 1 - q^n. Цю вормулу можна використовувати для перевірки настання одніїє з подій

Це один приклад

Нехай є якась база ДНК, в нас є зразок взятий в якоїсь людини, якщо ми здійсьнюємо випробування, тобто порівнюємо це з кожним екземпляром бази - 1/10_000 всього в базі дкн є 20_000 екземплярів, яка ймовірність того що зразок співпаде з хоча б одним. Короче я думав там мало а там 86% нічо так

Навіть якщо якась подія має малу ймовірність, при значній кількості випробувань, ймовірність що вона відбудеться хоча б 1 раз це доволі висока ймовірність

## Формула повної ймовірності

Якщо є випадкова подія А і може відбуватись з однією з подій h1, h2. Та вони незалежні тоді ймовірність подіх А є формулою повної ймовірності

## Формула Баєса

Коли ми проводимо випробування та якщо знаємо гіпотези до проводення випробування, це ми все знаємо до того як проводимо випробування та в результаті відбуваєтсья подія А, тоді можемо обчислити ймовірності гіпотез з врахуванням того, що подія А - відбулась

Приклад

Нехай є завод який виробляє материньські плати. 1% з них з дефектом. Інженери розробити процедуру тестування та ми застотосуємо її до нормальної то теаст скаже що вона якісна з шансом 99,9%. Якщо тестувати дефектну то видасть дефектра у 99,99%. Застосовуємо тест до випадкової плати, результат - дефектна. Яка ймовірність того, що плата якісна?

Застосувавши формулу Баєса з лекції, по суті треба знайти ймовірність якісної плати, коли тест видав "дефектна". Тоді ймовірінсть h1 - 0,99. h2 - 0,01;