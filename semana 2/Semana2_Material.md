# SEMANA 2 — DECISIONES, CICLOS Y CÓMO CAZAR BUGS

**Curso:** Fundamentos de programación
**Semana:** 2 · del lunes 19 al viernes 23 de octubre de 2026
**Entrega de la Actividad 2:** viernes 23, 23:59 h

> La semana pasada aprendiste a **pensar** un algoritmo. Esta semana le das al programa dos superpoderes: **decidir** (si pasa esto, haz aquello) y **repetir** (hazlo otra vez, y otra, y otra…). Con esas dos ideas se construye casi todo el software que usas a diario.

---

## ÍNDICE

0. Configura tu taller: Python + VS Code + Jupyter en tu computadora
1. Repaso exprés: variables, `input()`, `float()` y f-strings
2. Tema 5: Decisiones (`if`, `elif`, `else`, `and`, `or`, `not`)
3. Tema 6: Ciclo `while` (contadores, acumuladores, `break` y `continue`)
4. Tema 7: Detective de bugs
5. Tema 8: Ciclo `for` y `range()`
6. Chuleta final

---

# 0. CONFIGURA TU TALLER (≈ 20 min)

Hasta ahora usaste Google Colab, que funciona en el navegador. Ahora vas a montar tu propio taller en tu computadora, como un músico que deja de rentar el estudio y arma el suyo en casa. **Colab sigue siendo tu plan B** si algo falla.

Vas a instalar **3 cosas** y configurar **1**:

| # | Qué | Para qué (analogía) |
| :---: | :--- | :--- |
| 1 | **Python** | El motor. Sin él, nada arranca. |
| 2 | **VS Code** | El taller donde escribes y ejecutas. |
| 3 | **Extensiones Python y Jupyter** | Las herramientas del taller. |
| 4 | **Kernel (`ipykernel`)** | El cable que conecta el notebook con el motor. |

> ⚠️ No vamos a usar "entornos virtuales" todavía. Si VS Code te sugiere crear uno (*"Create Environment"* o *"venv"*), **ciérralo o ignóralo**.

### Paso 1 — Instalar Python

**Windows**
1. Entra a [python.org/downloads](https://www.python.org/downloads/) y descarga la versión estable más reciente (botón amarillo).
2. Ejecuta el instalador. **ANTES de darle "Install Now", marca la casilla `Add python.exe to PATH`** (abajo de la ventana). Es el paso más importante. Si lo olvidas, desinstala y vuelve a instalar.
3. Desactiva el "falso Python" de la Microsoft Store: *Configuración → Aplicaciones → Configuración avanzada de aplicaciones → Alias de ejecución de aplicaciones* → **apaga** `python.exe` y `python3.exe`.
4. Comprueba: abre una terminal nueva (PowerShell o Git Bash) y escribe:
   ```bash
   python --version
   ```
   Debe responder algo como `Python 3.x.x`.

**macOS**
1. Descarga el instalador para macOS desde [python.org/downloads](https://www.python.org/downloads/) e instálalo con las opciones por defecto.
2. Comprueba en la Terminal. **En Mac siempre se escribe `python3`**:
   ```bash
   python3 --version
   ```

### Paso 2 — Instalar VS Code
Descárgalo de [code.visualstudio.com](https://code.visualstudio.com/) e instálalo con las opciones por defecto. En Windows, marca también *"Agregar a PATH"* y *"Abrir con Code"* si aparecen.

### Paso 3 — Instalar las extensiones
En VS Code, abre el panel de **Extensiones** (icono de cuatro cuadritos a la izquierda, o `Ctrl+Shift+X` / `Cmd+Shift+X`) e instala estas dos, ambas publicadas por **Microsoft**:

| Extensión | Qué trae |
| :--- | :--- |
| **Python** | Soporte para Python (instala sola *Pylance* y *Python Debugger*). |
| **Jupyter** | Soporte para notebooks `.ipynb` (instala sola sus complementos). |

Opcional: **Spanish Language Pack for Visual Studio Code**, si prefieres el menú en español.

### Paso 4 — Instalar el kernel
El kernel es lo que permite que el notebook "hable" con Python. Abre la terminal **dentro de VS Code** (*Terminal → New Terminal*) y escribe:

| Sistema | Comando |
| :--- | :--- |
| Windows | `python -m pip install ipykernel` |
| macOS | `python3 -m pip install ipykernel` |

> 💡 Si te saltas este paso, no pasa nada grave: la primera vez que ejecutes una celda, VS Code te dirá *"requires the ipykernel package"* y te ofrecerá **Install**. Acepta.

### Paso 5 — Abrir tu repositorio y crear un notebook
1. *File → Open Folder…* y elige la carpeta de **tu repositorio del curso**, el mismo de la semana 1.
2. Crea la carpeta `semana2` (icono de carpeta con "+" en el explorador).
3. Dentro de `semana2`, crea un archivo llamado `practica.ipynb`.

### Paso 6 — Elegir el kernel
1. Arriba a la derecha del notebook verás **Select Kernel**. Haz clic.
2. Elige **Python Environments** y luego la versión de Python que instalaste (por ejemplo `Python 3.x.x`).
3. Si aparece una opción que dice *Microsoft Store* o *venv*, **no la elijas**.

### Paso 7 — Prueba de sonido 🎸
Escribe en una celda y presiona `Shift + Enter`:
```python
nombre = input("¿Cómo te llamas? ")
print(f"¡{nombre}, tu taller está listo!")
```
> 👀 En VS Code, la caja para escribir de `input()` aparece **arriba, al centro de la ventana**, no debajo de la celda. Escribe ahí y presiona `Enter`.

### Si algo falla

| Síntoma | Solución |
| :--- | :--- |
| `python` no se reconoce (Windows) | No marcaste *Add to PATH*. Reinstala Python marcándola y **cierra y reabre** VS Code. |
| Al escribir `python` se abre la Microsoft Store | Te faltó apagar los alias (Paso 1.3). |
| `python` no existe (Mac) | En Mac se usa `python3`. |
| No aparece mi Python en *Select Kernel* | Cierra y reabre VS Code. Si persiste, `Ctrl+Shift+P` → *Python: Select Interpreter*. |
| La celda se queda "pensando" con un `[*]` | Hay un `input()` esperando respuesta arriba de la ventana. |
| Nada funciona y ya pasaron 10 min | Sigue en **Google Colab** y lo arreglamos después. |

---

# 1. REPASO EXPRÉS: LO QUE YA SABES (SIN SABER QUE LO SABES)

En la Actividad 1 ejecutaste una calculadora. Ahora vas a escribir código tú. Antes, las 4 piezas de siempre:

| Pieza | Qué hace | Ejemplo |
| :--- | :--- | :--- |
| Variable | Una caja con etiqueta que guarda un dato | `banda = "Metallica"` |
| `input()` | Pregunta y espera respuesta. **Siempre llega como texto.** | `edad = input("Edad: ")` |
| `int()` / `float()` | Convierte texto en número entero o decimal | `edad = int(input("Edad: "))` |
| `print(f"...")` | Muestra un mensaje; lo que va en `{ }` se reemplaza por su valor | `print(f"Tienes {edad} años")` |

**Tipos de dato que vas a usar esta semana:**

| Tipo | Qué es | Ejemplo |
| :--- | :--- | :--- |
| `int` | Número entero | `25` |
| `float` | Número con decimales | `39.6` |
| `str` | Texto, siempre entre comillas | `"fin"` |
| `bool` | Verdadero o falso | `True`, `False` |

> 🔑 **El error número 1 de la semana:** `"5" + 3` truena porque no puedes sumar texto con número. Si vas a hacer cuentas con lo que te dan con `input()`, conviértelo primero con `int()` o `float()`.

---

# 2. TEMA 5: DECISIONES

### 2.1 La idea: el cadenero del concierto
En la entrada de un concierto hay un cadenero. No deja pasar a todos: **revisa una condición** y, según el resultado, decide.

```
          ¿Tiene 18 años o más?
            /              \
          Sí                No
          ↓                  ↓
   "Adelante, disfruta"   "Lo siento, no pasas"
```

Eso es un `if`: el programa deja de ir en línea recta y **elige un camino**.

### 2.2 Las preguntas que la computadora sabe hacer (comparadores)
Toda decisión empieza con una pregunta de **Sí o No**. Su respuesta es `True` o `False`.

| Operador | Pregunta | Ejemplo | Resultado si `edad = 18` |
| :---: | :--- | :--- | :---: |
| `==` | ¿Es igual a? | `edad == 18` | `True` |
| `!=` | ¿Es diferente de? | `edad != 18` | `False` |
| `>` | ¿Es mayor que? | `edad > 18` | `False` |
| `>=` | ¿Es mayor o igual que? | `edad >= 18` | `True` |
| `<` | ¿Es menor que? | `edad < 18` | `False` |
| `<=` | ¿Es menor o igual que? | `edad <= 18` | `True` |

> ⚠️ **`=` no es lo mismo que `==`.** Un `=` **guarda** un valor en una caja (`edad = 18`). Dos `==` **preguntan** si son iguales (`edad == 18`). Confundirlos es un clásico.

### 2.3 `if` y `else`: dos caminos
```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("¡Adelante, disfruta el show!")
else:
    print("Lo siento, no pasas")

print("Siguiente en la fila...")
```

**Las 3 reglas de escritura de Python** (si fallas una, Python se queja):
1. La pregunta termina en **dos puntos** `:`.
2. Lo que pertenece a esa decisión va **con sangría** (4 espacios o un `Tab`). La sangría es como estar **dentro del escenario**: lo que está sangrado ocurre solo si se cumple la condición.
3. Lo que vuelve al margen izquierdo (`print("Siguiente en la fila...")`) ocurre **siempre**, pase lo que pase.

### 2.4 `elif`: la taquilla con varias tarifas
Cuando hay **más de dos caminos**, usas `elif` ("si no, pero si…"). Python revisa de arriba hacia abajo y **se queda con el primero que se cumpla**. Los demás ni los lee.

```python
edad = int(input("Edad: "))

if edad < 12:
    print("Boleto infantil: $50")
elif edad < 60:
    print("Boleto general: $120")
else:
    print("Boleto de adulto mayor: $60")
```

> 💡 **El orden importa.** Si pones primero `edad < 60`, un niño de 8 años entraría ahí (8 es menor que 60) y pagaría tarifa general. Ordena las condiciones de la **más específica a la más general**.

### 2.5 `and`, `or`, `not`: reglas de acceso combinadas
El cadenero del área VIP es más exigente: revisa **dos cosas a la vez**.

| Operador | Significado | Analogía |
| :---: | :--- | :--- |
| `and` | **Las dos** deben cumplirse | Para el VIP necesitas ser mayor de edad **y** traer pulsera VIP. |
| `or` | **Al menos una** debe cumplirse | Entras si traes boleto **o** si estás en la lista de invitados. |
| `not` | **Invierte** la respuesta | Pasas si **no** traes objetos prohibidos. |

```python
edad = int(input("Edad: "))
pulsera = input("¿Traes pulsera VIP? (si/no): ")

if edad >= 18 and pulsera == "si":
    print("Bienvenido al área VIP 🤘")
else:
    print("Esta zona es solo VIP")
```

### 2.6 Antes de programar: la tabla de decisión ✍️
Antes de escribir los `if`, haz en tu libreta una **tabla con todos los casos posibles** y qué debe pasar en cada uno. Si la tabla está bien, el código casi se escribe solo.

| ¿Edad ≥ 18? | ¿Pulsera VIP? | Resultado |
| :---: | :---: | :--- |
| Sí | Sí | Pasa al VIP |
| Sí | No | Zona general |
| No | Sí | No pasa (es menor) |
| No | No | No pasa |

> 🎯 Esta tabla es la base de la **Parte A de la Actividad 2**.

### 2.7 Decisiones dentro de decisiones (anidamiento)
Puedes meter un `if` dentro de otro. Solo tienes que **sangrar un nivel más**:
```python
edad = int(input("Edad: "))
if edad >= 18:
    pulsera = input("¿Traes pulsera VIP? (si/no): ")
    if pulsera == "si":
        print("Área VIP")
    else:
        print("Zona general")
else:
    print("No pasas")
```
Fíjate que **solo a los mayores de edad se les pregunta por la pulsera**. A un menor ni se le pregunta.

---

# 3. TEMA 6: CICLO `while`

### 3.1 La idea: "mientras haya gasolina, sigue rodando"
Un `while` repite un bloque **mientras una condición sea verdadera**. No sabes de antemano cuántas vueltas serán: solo sabes **cuándo parar**.

```
   ┌──────────────────────────┐
   ↓                          │
¿Hay gasolina? ──Sí──> Rodar un tramo
   │
   No
   ↓
 Detenerse
```

```python
gasolina = 3
while gasolina > 0:
    print(f"Rodando... me quedan {gasolina} litros")
    gasolina = gasolina - 1
print("Sin gasolina, a empujar la moto 😅")
```

> ⚠️ **El ciclo infinito.** Si dentro del ciclo **nunca cambias** la variable de la condición (aquí, `gasolina`), la condición nunca se vuelve falsa y el programa se repite para siempre. En VS Code se detiene con el botón ⏹ (*Interrupt*) de la celda.

### 3.2 Contador y acumulador: el odómetro y la cuenta del bar

| Concepto | Qué hace | Analogía | Código típico |
| :--- | :--- | :--- | :--- |
| **Contador** | Suma **siempre lo mismo** (de 1 en 1) | El contador de vueltas al circuito | `vueltas = vueltas + 1` |
| **Acumulador** | Suma **valores que cambian** | La cuenta del bar: cada ronda cuesta distinto | `cuenta = cuenta + precio` |

Los dos **empiezan en 0 antes del ciclo**. Si los pones dentro, se reinician en cada vuelta.

```python
cuenta = 0
rondas = 0
while rondas < 3:
    precio = float(input("Precio de la ronda: "))
    cuenta = cuenta + precio      # acumulador
    rondas = rondas + 1           # contador
print(f"Fueron {rondas} rondas. Total: ${cuenta:.2f}")
```

### 3.3 `break`: la salida de emergencia
`break` **termina el ciclo de inmediato**, sin importar la condición. Su uso más común es `while True` (repetir sin fin), y el `break` es la puerta de salida.

```python
total = 0
while True:
    dato = input("Precio (o 'fin' para cerrar la cuenta): ")
    if dato == "fin":
        break                     # salimos del ciclo
    total = total + float(dato)
print(f"Total: ${total:.2f}")
```
> 💡 Fíjate en el orden: **primero** se revisa si escribió `"fin"` y **después** se convierte a número. Si conviertes primero, `float("fin")` truena.

### 3.4 `continue`: saltar la canción
`continue` **salta el resto de esta vuelta** y pasa a la siguiente, como darle "siguiente" a una canción que no te gusta: el playlist sigue, solo que esa no suena.

```python
i = 0
while i < 4:
    i = i + 1
    cancion = input(f"Canción {i}: ")
    if cancion == "reguetón":
        print("Saltada ⏭")
        continue
    print(f"Sonando: {cancion} 🤘")
```

> ⚠️ **Trampa clásica:** si el contador (`i = i + 1`) va **después** del `continue`, la vuelta saltada nunca lo incrementa y puedes quedar en un ciclo infinito. Incrementa el contador **antes** del `continue`.

---

# 4. TEMA 7: DETECTIVE DE BUGS 🔍

Un **bug** ("bicho") es un error en el programa. El término ya se usaba en ingeniería, pero se volvió famoso en 1947, cuando el equipo de Grace Hopper encontró una polilla real atorada en la computadora Mark II de Harvard y la pegó en su bitácora. Hoy todos los programadores pasan más tiempo **encontrando** bugs que escribiendo código nuevo. Encontrarlos es una habilidad, no una vergüenza.

### 4.1 Los 3 tipos de bug

| Tipo | Qué pasa | Analogía | Ejemplo |
| :--- | :--- | :--- | :--- |
| **De sintaxis** | Python **ni siquiera arranca**: no entiende lo que escribiste. | Una partitura con notas que no existen: nadie puede tocarla. | `print("Hola` (falta la comilla) |
| **De ejecución** | Arranca, pero **truena a la mitad** con un mensaje rojo. | La moto arranca y se apaga en el semáforo. | `int("veinte")`, `10 / 0` |
| **De lógica** | Funciona **sin errores**, pero el resultado **está mal**. Es el más peligroso. | Llegas perfecto… a la ciudad equivocada. | `promedio = a + b + c / 3` |

### 4.2 Cómo leer el mensaje de error
El mensaje rojo no es un regaño: es una **multa de tránsito** que te dice exactamente qué hiciste, dónde y por qué. **Léelo de abajo hacia arriba:**

```
Traceback (most recent call last):
  File "...", line 2, in <module>
    total = boletos * 45.5
            ~~~~~~~~^~~~~~
TypeError: can't multiply sequence by non-int of type 'float'
```

| Pregunta | Dónde se ve | Respuesta |
| :--- | :--- | :--- |
| ¿**Qué** tipo de error? | Última línea, antes de los dos puntos | `TypeError`: operaste con tipos que no combinan |
| ¿**Por qué**? | Última línea, después de los dos puntos | No se puede multiplicar un texto por un decimal |
| ¿**Dónde**? | `line 2` y la línea señalada con `^` | `total = boletos * 45.5` |

En este caso, `boletos` llegó de `input()` como texto y nunca se convirtió con `int()`.

**Los errores que más vas a ver esta semana:**

| Error | Significa | Causa típica |
| :--- | :--- | :--- |
| `SyntaxError` | Algo está mal escrito | Faltan `:`, comillas o paréntesis |
| `IndentationError` | La sangría está mal | Mezclaste espacios o te faltó sangrar |
| `NameError` | Esa variable no existe | Error de dedo: `totla` en vez de `total` |
| `TypeError` | Operaste con tipos incompatibles | Sumaste texto con número |
| `ValueError` | El valor no se puede convertir | `int("fin")`, `float("1,5")` |
| `ZeroDivisionError` | Dividiste entre cero | Un contador que se quedó en 0 |

### 4.3 Técnica del detective: rastrear con `print()`
Para los bugs de **lógica** no hay mensaje rojo. La técnica es **espiar las variables**: agrega `print()` temporales para ver qué valor tienen en cada vuelta, como una **prueba de escritorio automática**.

```python
total = 0
for i in range(1, 4):
    precio = float(input("Precio: "))
    total = total + precio
    print(f"🔍 vuelta {i}: precio={precio}, total={total}")   # espía temporal
```
Cuando encuentres el bug, **borra los espías**.

**Protocolo del detective:**
1. **Reproduce** el error: ¿con qué datos falla?
2. **Lee** el mensaje (si lo hay), de abajo hacia arriba.
3. **Predice** a mano qué valor debería tener cada variable.
4. **Espía** con `print()` y compara contra tu predicción.
5. **Corrige un solo cambio a la vez** y vuelve a probar.

---

# 5. TEMA 8: CICLO `for` Y `range()`

### 5.1 La idea: el setlist
Un `while` es "rueda hasta que se acabe la gasolina": no sabes cuántas vueltas. Un `for` es un **setlist**: antes de empezar el concierto ya sabes que son, por ejemplo, 5 canciones, y el ciclo va de la primera a la última.

```python
for cancion in range(1, 6):
    print(f"Tocando la canción {cancion} de 5")
print("¡Gracias, buenas noches! 🤘")
```
El `for` se encarga solo del contador. **No tienes que escribir `i = i + 1`** y por eso no hay riesgo de ciclo infinito.

### 5.2 `range()`: el contador automático

| Escribes | Genera | Ojo |
| :--- | :--- | :--- |
| `range(5)` | 0, 1, 2, 3, 4 | Empieza en 0 y **no incluye** el 5 |
| `range(1, 6)` | 1, 2, 3, 4, 5 | El segundo número **nunca se incluye** |
| `range(0, 21, 5)` | 0, 5, 10, 15, 20 | El tercer número es el **salto** |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 | Salto negativo: cuenta regresiva |

> 🎯 Truco: si quieres del 1 al N, escribe `range(1, N + 1)`.

### 5.3 `for` con acumulador
```python
n = int(input("¿Cuántos artículos de merch compraste? "))
total = 0
for i in range(1, n + 1):
    precio = float(input(f"Precio del artículo {i}: "))
    total = total + precio
print(f"Gastaste ${total:.2f} en merch")
```

### 5.4 ¿`for` o `while`?

| Pregunta | Usa |
| :--- | :--- |
| ¿Sé **cuántas veces** se repite antes de empezar? (5 vueltas, N alumnos, 7 días) | `for` |
| ¿Se repite **hasta que pase algo**? (hasta escribir "fin", hasta afinar, hasta llenar el tanque) | `while` |

`break` y `continue` funcionan igual dentro de un `for`.

### 5.5 Bonus visual: dibujar con texto
En Python puedes "multiplicar" un texto: `"█" * 4` produce `████`. Con un `for` haces gráficas en la consola:
```python
for dia in range(1, 4):
    horas = int(input(f"Horas de práctica el día {dia}: "))
    print(f"Día {dia} | " + "█" * horas)
```

---

# 6. CHULETA FINAL

```python
# DECIDIR
if condicion:            # ¿se cumple?
    ...
elif otra_condicion:     # ¿si no, se cumple esta?
    ...
else:                    # si ninguna se cumplió
    ...

# REPETIR MIENTRAS (no sé cuántas veces)
while condicion:
    ...                  # ¡cambia algo para que algún día termine!

# REPETIR N VECES (sí sé cuántas veces)
for i in range(1, n + 1):
    ...

# CONTROL DEL CICLO
break      # salir del ciclo ya
continue   # saltar a la siguiente vuelta

# PATRONES
contador = contador + 1        # contar
acumulador = acumulador + x    # sumar valores
```
