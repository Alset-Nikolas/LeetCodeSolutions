<h1 align="center">Свойство делителей числа n</h1>
<p>Пусть n целое число</p>
<p>

if n == 1: 
    return [1] 
Делители = [1] 

for x in range(2, int(n**0.5)+1):  
    if n % x == 0: 
        Делители.append(x)
        Делители.append(n//x)

</p>