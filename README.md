# Cross-Zero_5x5

<картинка>

## Как играть
  
Игра:  
- Игроки по очереди ходят  крестиками/ноликами
- Выигрывает игрок, который собрал комбинацию из 3 своих фигурок
- Игра заканчивается, когда выигрывает один игрок или заканчиваются свободные клетки
- Вывод итогов - в консоль
- Играйте
- Наслаждайтесь


## main.py
WIDTH - int; Ширина экрана     
HEIGHT - int; Высота экрана 
screen - ?; экран   
clock - ?; таймер    
done - boolean; для цикла     
hm - int; сколько квадратов    
list_of_f - dict; все поля        
alli - list; все окольные квадраты   
liste  - dict; алгоритмы для счета у окольных квадратов    
which - boolean; какой игрок ходит  
answers - list; все варианты окончания игры  
ans - boolean; вывод в игре    
  
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
  
