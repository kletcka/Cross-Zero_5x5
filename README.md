# FiveCellsGame  

![Крестик](https://avatars.mds.yandex.net/get-pdb/2714303/2e63bedf-ff9d-4a57-ae70-4f06b988e88b/s1200)  
## Как играть
  
Игра:  
- Игроки по очереди ходят  крестиками/ноликами
- Выигрывает игрок, который собрал комбинацию из 3 своих фигурок
- Игра заканчивается, когда выигрывает один игрок или заканчиваются свободные клетки
- Вывод итогов - на экране
- Нажмите на пробел для продолжения
- Играйте
- Наслаждайтесь


## main.py   
WIDTH - int; Ширина экрана        
HEIGHT - int; Высота экрана      
HM - int; сколько квадратов         
ANSWERS - list; все варианты окончания игры     
BACKFILL - tuple; цвет заливки фона        
TEXTFILL - tuple; цвет заливки текста    
NEXTN - str; текст 'введите пробел'   
screen - ?; экран         
clock - ?; таймер     
settings - dict; словарь с настройками   
list_of_f - dict; все поля      
done - boolean; для цикла           
liste  - dict; алгоритмы для счета у окольных квадратов      
which - boolean; какой игрок ходит  
ans - boolean; вывод в игре         
mode - boolean; меню/игра      
  
**Функции:**   
reset() - пересоздает клетки      
  
   
## objects.py    
### Классы:    
#### Field()     
**Атрибуты:**     
image_adress - str?; путь    
my_image - ?; изображение    
x - int; положение по Х   
y - int; положение по Y     
rect - Rect;  для поля    
stage - boolean; текущее состояние  
hi - list; список всех окольных клеток  
  
**Методы:**   
crew(how, vect, ind)  
*how* - boolean; как изменить      
*vect* - str; в каком направлении      
*ind* - int; где конкретно по вектору     
change(how)      
*how* - boolean; как изменить      
check()     
*-Вывод:*  
*is* - boolean; не появилась ли комбинация?   
draw(screen)      
*screen* - ?; экран, где рисовать изображение    
     
## objects.json     
set_numbers_of_cells - сколько клеток  
set_width_of_cells - размеры клеток       
texts - тексты    
--x_wins - текст для победы X   
--o_wins - текст для победы O     
--no_wins - текст для ничьи    
--new - текст для пробела    
colors - цвета      
--back_color - цвет фона     
---r - код красного    
---g - код зеленого       
---b - код голубого  
--text_color - цвет текста    
---r - код красного   
---g - код зеленого  
---b - код голубого  
