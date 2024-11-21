# Знакомство с языком Python (семинары). Урок 10

## Задание

### Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

#### ([перейти к скрипту](https://github.com/shualyyyyy/gblinux/blob/main/delfiletodir.sh))

```

var = ['разработка', 'сокет', 'декоратор']

for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))

#те же строки полученные из онлайн конвертера

var = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
       b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
       b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))
```

### Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

#### ([перейти к скрипту](https://github.com/shualyyyyy/gblinux/blob/main/delfiletodir.sh))
```
var = [b'class', b'function', b'method']

for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))
```

### Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе

#### ([перейти к скрипту](https://github.com/shualyyyyy/gblinux/blob/main/delfiletodir.sh))

```
var2 = b'attribute'
var3 = b'класс'
var4 = b'функция'
var5 = b'type'   
```
На строки записанные на кириллице вылетает исключение
 ```
 File "/Users/alexander/pyServer01/pe_server01.py", line 46
    var3 = b'класс'
          ^
SyntaxError: bytes can only contain ASCII literal characters.'''
```
### Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).'

#### ([перейти к скрипту](https://github.com/shualyyyyy/gblinux/blob/main/delfiletodir.sh))

```
var6 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in var6:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print('#'*15)

```
### Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице'''

#### ([перейти к скрипту](https://github.com/shualyyyyy/gblinux/blob/main/delfiletodir.sh))

```
import subprocess


ping_resurs = [['ping', 'yandex.ru'],['ping', 'youtube.com']]

for ping_now in ping_resurs:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i<10:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            break
```

### Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое

#### ([перейти к скрипту](https://github.com/shualyyyyy/gblinux/blob/main/delfiletodir.sh))

```
import locale

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

#Создаем файл
with open('resurs.txt', 'w+') as f_n:
    for i in resurs_string:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n) # печатаем объект файла, что бы узнать его кодировку

file_coding = locale.getpreferredencoding()

# Читаем из файла
with open('resurs.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)
```
