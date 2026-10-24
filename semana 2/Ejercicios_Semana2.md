# 23 EJERCICIOS DE PRÁCTICA — SEMANA 2

**Curso:** Fundamentos de programación
**Alcance:** repaso exprés, decisiones, ciclo `while`, detective de bugs y ciclo `for`.

Resuélvelos en un notebook (`semana2/practica.ipynb`) conforme avanzamos. **No son evaluables**, pero son el entrenamiento para la Actividad 2: quien los hace, la resuelve sin sufrir.

**Nivel:** 🟢 calentamiento · 🟡 en forma · 🔴 modo experto

> ✍️ **Antes de programar cualquier ejercicio** 🟡 o 🔴, escribe en tu libreta la tabla Entrada-Proceso-Salida o la tabla de decisión. Dos minutos de papel ahorran veinte de errores.

---

## BLOQUE R · REPASO EXPRÉS (lunes)

### R1 🟢 Años en el escenario
Pide el nombre de una banda y el año en que se formó. Muestra cuántos años lleva en el escenario (año actual: 2026).
**Entrada:** `Metallica`, `1981`
**Salida:** `Metallica lleva 45 años en el escenario`

### R2 🟢 Puesto de merch
Una playera cuesta $350 y una calcomanía $25. Pide cuántas de cada una compras y muestra el total.
**Entrada:** `2` playeras, `3` calcomanías
**Salida:** `Total de tu merch: $775.00`

---

## BLOQUE D · DECISIONES (lunes y martes)

### D1 🟢 El cadenero
Pide la edad. Si tiene 18 años o más, muestra `¡Adelante, disfruta el show!`; si no, `Lo siento, no pasas`.
**Entrada:** `17`
**Salida:** `Lo siento, no pasas`

### D2 🟢 ¿Me alcanza la gasolina?
Pide los litros en el tanque, el rendimiento (km por litro) y los km de la rodada. La autonomía es `litros × rendimiento`. Indica si llegas y con cuántos km de sobra, o cuántos km te faltan.
**Entrada:** `12`, `25`, `280` → **Salida:** `Llegas con 20.0 km de sobra`
**Entrada:** `12`, `25`, `350` → **Salida:** `Carga gasolina: te faltan 50.0 km`

### D3 🟡 Reseña de calificaciones
Pide una calificación de 0 a 10 y muestra su reseña con `elif`: menos de 6 → `Reprobado`; de 6 a menos de 8 → `Suficiente`; de 8 a menos de 10 → `Bien`; 10 → `Excelente`.
**Entrada:** `8.5`
**Salida:** `Bien`

### D4 🟡 Acceso al área VIP
Pide la edad, si trae pulsera VIP (`si`/`no`) y si está en la lista de invitados (`si`/`no`). Entra al VIP quien sea mayor de edad **y** además traiga pulsera **o** esté en la lista.
**Entrada:** `20`, `no`, `si` → **Salida:** `Acceso VIP permitido`
**Entrada:** `16`, `si`, `si` → **Salida:** `Acceso denegado`
💡 Pista: usa paréntesis para agrupar el `or`.

### D5 🟡 ¿Salgo a rodar?
Pide la temperatura (°C) y si llueve (`si`/`no`). Si llueve **o** hace menos de 5 °C → `Mejor en carro`; si hace menos de 15 °C → `Rodada con chamarra gruesa`; en otro caso → `¡Perfecto para rodar!`
**Entrada:** `12`, `no`
**Salida:** `Rodada con chamarra gruesa`
✍️ Antes de programar, haz la tabla de decisión con todos los casos.

### D6 🔴 Estacionamiento del estadio
Las primeras 2 horas cuestan $20 en total; cada hora adicional, $10. El cobro máximo es $100. Pide las horas (entero) y muestra el total.
**Entrada:** `1` → `Total a pagar: $20.00`
**Entrada:** `5` → `Total a pagar: $50.00`
**Entrada:** `12` → `Total a pagar: $100.00`

---

## BLOQUE W · CICLO `while` (miércoles)

### W1 🟢 Cuenta regresiva del show
Con `while`, imprime del 10 al 1 y al final `¡Que empiece el show!`
**Entrada:** ninguna
**Salida:** `10`, `9`, …, `1`, `¡Que empiece el show!`

### W2 🟡 El afinador
Una cuerda está afinada si su frecuencia está entre 438 y 442 Hz (incluidos). Pide la frecuencia hasta que esté afinada. Si está por debajo, muestra `Muy baja: aprieta la clavija`; si está por arriba, `Muy alta: afloja la clavija`. Al final, cuántos intentos fueron.
**Entrada:** `432`, `445`, `440`
**Salida:**
```
Muy baja: aprieta la clavija
Muy alta: afloja la clavija
¡Afinada! Lo lograste en 3 intentos
```
🎸 Es el algoritmo del Versus 3 de la semana pasada, ahora convertido en código.

### W3 🟡 Alcancía para el festival
El boleto del festival cuesta $1,500. Pide depósitos hasta alcanzar la meta y muestra en cuántos depósitos lo lograste y cuánto ahorraste.
**Entrada:** `500`, `300`, `800`
**Salida:** `¡Meta alcanzada en 3 depósitos! Ahorraste $1600.00`

### W4 🟡 Playlist sin relleno (`continue`)
Pide la duración (en minutos) de 5 canciones. Las que duren **más de 6 minutos** se saltan con `continue` (muestra `Muy larga, la saltamos`). Al final, cuántas canciones quedaron y su duración total.
**Entrada:** `4.5`, `8`, `3`, `7.2`, `5`
**Salida:**
```
Muy larga, la saltamos
Muy larga, la saltamos
Canciones en tu playlist: 3
Duración total: 12.5 min
```
⚠️ Cuidado con dónde incrementas el contador de canciones pedidas (Tema 6, sección 3.4).

### W5 🔴 Rodada con tanque limitado (`break`)
La moto tiene 15 L y rinde 20 km/L (autonomía de 300 km). Pide los km de cada tramo hasta que el usuario escriba `fin`. Si un tramo haría que el recorrido supere la autonomía, detén el ciclo con `break` y avisa en qué tramo te quedaste sin gasolina.
**Entrada:** `120`, `90`, `110` → **Salida:** `¡Sin gasolina en el tramo 3! Llevabas 210 km`
**Entrada:** `120`, `90`, `fin` → **Salida:** `¡Llegaste! Recorriste 210 km y te sobran 90 km de autonomía`

---

## BLOQUE B · DETECTIVE DE BUGS (jueves y viernes)

### B1 🟢 Clasifica el bug
Para cada línea, indica si el error es de **sintaxis**, de **ejecución** o de **lógica**, y cómo se corrige.
```python
a) print("Bienvenidos al show)
b) edad = int("veinte")
c) promedio = (8 + 9 + 10) / 2        # se quiere el promedio de 3 calificaciones
d) total = 10 / 0
e) if edad > 18:                     # se quiere dejar pasar a los de 18 o más
f) if edad >= 18                     # (la línea completa es así)
```

### B2 🟡 Lee la multa
Un compañero ejecutó esto, escribió `3` y obtuvo el mensaje de abajo. Responde: ¿qué tipo de error es?, ¿en qué línea?, ¿por qué ocurrió? y ¿cómo se corrige?
```python
boletos = input("¿Cuántos boletos? ")
total = boletos * 45.5
```
```
TypeError: can't multiply sequence by non-int of type 'float'
```

### B3 🟡 El show que nunca empieza
Este código debería hacer una cuenta regresiva, pero se queda trabado para siempre. ¿Qué tipo de bug es y cómo se corrige?
```python
n = 10
while n > 0:
    print(n)
print("¡Que empiece el show!")
```

### B4 🔴 El cajero tramposo
Este código debería pedir el precio de **4** productos y mostrar el total. Tiene **3 bugs**. Encuéntralos con la técnica del detective (espías con `print()`), clasifícalos y escribe la versión corregida.
```python
for i in range(1, 4):
    total = 0
    precio = input(f"Precio del producto {i}: ")
    total = total + precio
print(f"Total: {total}")
```
**Entrada esperada:** `100`, `50`, `25`, `25`
**Salida correcta:** `Total: 200.0`

---

## BLOQUE F · CICLO `for` (jueves)

### F1 🟢 Vueltas al circuito
Con `for` y `range()`, imprime `Vuelta 1 completada` hasta `Vuelta 5 completada` y al final `¡Bandera a cuadros! 🏁`

### F2 🟡 Gastos de la semana
Pide el gasto de cada uno de los 7 días de la semana y muestra el total y el promedio diario.
**Entrada:** `50`, `0`, `120`, `35`, `80`, `200`, `15`
**Salida:**
```
Gasto de la semana: $500.00
Promedio diario: $71.43
```

### F3 🟡 Votación: ¿qué banda abre el festival?
Pide cuántos votos habrá y luego cada voto (`1`, `2` o `3`). Cuenta los votos de cada banda y anuncia la ganadora (o `Hay empate`).
**Entrada:** `6` votos: `1`, `2`, `1`, `3`, `1`, `2`
**Salida:**
```
Banda 1: 3 | Banda 2: 2 | Banda 3: 1
Gana la banda 1
```

### F4 🟡 Calendario de ensayos
La banda ensaya cada 3 días, empezando el día 3, en un mes de 30 días. Usa `range()` con salto para mostrar los días de ensayo y cuántos ensayos hay en total.
**Salida:** `Ensayo el día 3`, `Ensayo el día 6`, …, `Ensayo el día 30`, `Total de ensayos en el mes: 10`

### F5 🔴 Mismo problema, dos ciclos
Un puesto de merch quiere sumar sus ventas del día.
- **Versión A (`for`):** primero pregunta cuántas ventas hubo y luego pide cada una.
- **Versión B (`while`):** pide ventas hasta que el usuario escriba `fin`.

Prueba ambas con las ventas `350`, `120` y `80` (total `$550.00`). En una celda Markdown explica en 2–3 líneas **cuándo conviene cada versión**.

---

## BONUS · DIBUJAR CON TEXTO (opcional)

### P1 🟢 Ecualizador
Pide el nivel (de 1 a 10) de 5 bandas de un ecualizador y dibuja cada barra con `"█" * nivel`.
**Entrada:** `3`, `5`, `2`, `7`, `4`
**Salida:**
```
Banda 1 | ███
Banda 2 | █████
Banda 3 | ██
Banda 4 | ███████
Banda 5 | ████
```
