# ACTIVIDAD EVALUABLE 1 — MI RUTINA DIGITAL: DEL PROBLEMA AL PRIMER PROGRAMA

**Curso:** Fundamentos de programación
**Semana:** 1 · Temas 1 al 4
**Ponderación:** 6% de la calificación total del curso
**Modalidad:** Individual
**Fecha límite:** Viernes 16 de octubre de 2026, 23:59 h
**Evidencia de entrega:** Liga pública de tu repositorio de GitHub

---

## 1. El reto

¿Cuánto de tu día se va en pantallas? Probablemente más de lo que crees.

Antes de escribir una sola línea de código, un profesional **entiende el problema, lo descompone y diseña la solución**. Pasa lo mismo con un arquitecto: primero dibuja los planos y después se construye. En esta actividad vas a recorrer ese camino completo:

1. **Pensar** el problema y escribir su solución paso a paso (algoritmo).
2. **Dibujar** esa solución (diagrama de flujo).
3. **Preparar** tu espacio de trabajo profesional (Git y GitHub).
4. **Ver** cómo tu diseño se convierte en un programa real (Python).
5. **Parte E (sanción):** investigar y describir como algoritmo un procedimiento matemático (ver Parte E).

> No necesitas saber programar todavía. Necesitas **pensar con orden**.

**El problema a resolver:** diseñar una calculadora que pida el nombre de una persona y las horas diarias que dedica a **5 plataformas digitales** (por ejemplo, redes sociales, mensajería, streaming, videojuegos y música). Debe calcular el **tiempo total** y el **porcentaje del día (24 h)** que representa, y mostrar un resumen.

---

## 2. Partes de la actividad

### Parte A — Diseño del algoritmo (30 pts)

**A1. Planteamiento del problema.** Explica con tus palabras, en 3 a 5 líneas, qué problema resuelve la calculadora y para qué le serviría a alguien.

**A2. Tabla Entrada-Proceso-Salida (EPS).** Completa la tabla:

| Fase | ¿Qué es? | En mi problema |
| :--- | :--- | :--- |
| **Entrada** | Datos que necesito recibir | *(nombre y horas de las 5 plataformas que elegiste)* |
| **Proceso** | Cálculos que hago con esos datos | *(suma total y porcentaje)* |
| **Salida** | Resultados que muestro | *(¿qué ve el usuario al final?)* |

Fórmula del porcentaje: `porcentaje = (tiempo_total / 24) * 100`

**A3. Algoritmo en lenguaje natural.** Escribe los pasos numerados. Deben empezar con **Inicio** y terminar con **Fin**, y cada paso debe contener **una sola acción**. El algoritmo debe cumplir las tres características: **preciso, definido y finito**.

| ❌ Paso ambiguo | ✅ Paso preciso |
| :--- | :--- |
| Pregunta las horas. | Pedir al usuario las horas que dedica al día a redes sociales y guardarlas como `horas_redes`. |
| Haz las cuentas. | Sumar las horas de las 5 plataformas y guardar el resultado como `tiempo_total`. |

**A4. Prueba de escritorio con tus datos reales.** "Ejecuta" tu algoritmo a mano con tus propias horas de uso. Puedes usar la calculadora del celular, pero **debes escribir la operación completa**.

| Plataforma | Horas al día |
| :--- | :---: |
| *Ej. Redes sociales* | *2.5* |
| ... | ... |
| **Tiempo total** | **(suma escrita)** |
| **Porcentaje del día** | **(operación escrita)** |

> 💡 Tip: revisa la pantalla de "Bienestar digital" o "Tiempo en pantalla" de tu celular para usar datos reales.

---

### Parte B — Diagrama de flujo (10 pts)

Dibuja el diagrama de flujo de **tu** algoritmo de la Parte A3. Puedes hacerlo **a mano en tu libreta** (fotografía nítida y legible) o en [draw.io](https://app.diagrams.net). Cada bloque del diagrama debe corresponder a un paso de tu algoritmo.

| Símbolo | Forma | Se usa para |
| :--- | :--- | :--- |
| Terminal | Óvalo | Inicio y Fin |
| Entrada / Salida | Paralelogramo | Pedir datos o mostrar resultados |
| Proceso | Rectángulo | Cálculos y asignaciones |
| Flecha | → | Indica el orden en que se ejecutan los pasos |

**Opcional (+5 pts extra, sin exceder 100):** realizar el pseudocódigo en PSeInt y exportar su diagrama de flujo.

---

### Parte C — Repositorio en GitHub (25 pts)

**C1. Repositorio y estructura.** Usa un repositorio **público** para el curso (si ya creaste `curso-python-semana1` en clase, úsalo) con esta estructura:

```
tu-repositorio/
├── README.md
└── semana1/
    ├── Actividad1_MiRutinaDigital.pdf
    ├── diagrama_flujo.jpg            (o .png)
    ├── calculadora_tiempo_digital.ipynb
    └── ParteE_DivisionSintetica.pdf  (escaneo de tus hojas a mano)
```

**C2. README.md.** Debe incluir tu nombre, el nombre del curso y una descripción de 2 a 3 líneas de lo que contiene el repositorio. **No incluyas** correo, teléfono ni datos personales sensibles: es un repositorio público.

**C3. Historial de commits.** Debes tener un mínimo de **3 commits**, hechos conforme avanzas y no todos al final, con mensajes que describan el cambio. Ejemplos:

```
docs: agregar README del curso
docs: agregar algoritmo y diagrama de flujo de la actividad 1
feat: completar calculadora de tiempo digital en notebook
```

**C4. Evidencia de instalación.** Incluye en tu PDF una captura de la terminal con la salida de `git --version` y `git config user.name`.

> ⚠️ No subas capturas de `git config --list`: muestran tu correo en un repositorio público.

---

### Parte D — Primer contacto con Python (15 pts)

Descarga el notebook plantilla **`calculadora_tiempo_digital.ipynb`** que te compartirá el profesor y sigue sus instrucciones. Ahí vas a:

1. Ejecutar la calculadora con tus datos.
2. Ampliarla de 3 a 5 plataformas.
3. Señalar qué líneas de código son la Entrada, el Proceso y la Salida.
4. Comparar el resultado del programa con tu prueba de escritorio (A4).

Puedes trabajarlo en Jupyter (en tu computadora) o en **Google Colab**. Si usas Colab, descárgalo como `.ipynb` (*Archivo → Descargar → Descargar .ipynb*) y súbelo a tu repositorio.

---

### Parte E — SANCIÓN ACADÉMICA: Algoritmo de la división sintética (20 pts)

> ⚠️ **Esta parte es una sanción académica aplicada a todo el grupo** por las conductas irrespetuosas y el lenguaje inapropiado presentados en clase, contrarios al reglamento del curso. Desde el primer día se estableció que esta materia puede ser sencilla o muy demandante según el compromiso y el comportamiento del grupo. Las conductas indebidas futuras tendrán consecuencias académicas similares.
>
> **Es obligatoria y forma parte de la calificación de esta actividad.**

#### El reto

En preparatoria aprendiste a **bajar el grado de un polinomio** con la **división sintética** (también llamada **regla de Ruffini**). Probablemente ya no lo recuerdas. Tu tarea es **investigarlo**, aplicarlo y, sobre todo, **convertirlo en un algoritmo**: un procedimiento tan preciso que otra persona que nunca lo ha visto pudiera seguirlo sin preguntarte nada.

**Todo se entrega hecho a mano** en hojas o en libreta, con letra legible, escaneado en un solo PDF. **No se aceptan entregas impresas ni escritas en computadora.**

#### Material de referencia

- Video (español): [División sintética de polinomios](https://www.youtube.com/watch?v=cbQfP1Er1WU)
- Lectura (español): [División sintética de polinomios — LibreTexts](https://espanol.libretexts.org/Bookshelves/Educacion_Basica/Analisis/02%3A_Funciones_polinomiales_y_racionales/2.06%3A_Encontrar_ceros_de_polinomios/2.6.02%3A_Divisi%C3%B3n_Sint%C3%A9tica_de_Polinomios)
- Puedes consultar otras fuentes. Cítalas al final de tu entrega.

#### Ejemplo de referencia (solo entradas y salidas)

Este ejemplo te sirve para **comprobar** que tu procedimiento es correcto. El **cómo** se llega del inicio al final es lo que tú debes investigar y describir.

| | Entrada | Salida |
| :--- | :--- | :--- |
| **Problema** | P(x) = x⁴ + x³ − 7x² − x + 6, con raíces conocidas **r₁ = 1** y **r₂ = 2** | Polinomio de grado 2 |
| **1ª división** | P(x) entre (x − 1) | Q₁(x) = x³ + 2x² − 5x − 6 · residuo **0** |
| **2ª división** | Q₁(x) entre (x − 2) | Q₂(x) = x² + 4x + 3 · residuo **0** |

**Resultado:** el polinomio bajó de **grado 4 a grado 2**: P(x) = (x − 1)(x − 2)(x² + 4x + 3)

#### Tu polinomio asignado

Usa el polinomio que corresponde al **último dígito de tu matrícula**. Resolver un polinomio distinto al asignado vale **0** en esta parte.

| Último dígito | Polinomio P(x) | Raíz r₁ | Raíz r₂ |
| :---: | :--- | :---: | :---: |
| **0 o 1** | x⁴ − 10x³ + 35x² − 50x + 24 | 1 | 2 |
| **2 o 3** | x⁴ − 5x³ + 5x² + 5x − 6 | 2 | −1 |
| **4 o 5** | x⁴ + x³ − 11x² − 9x + 18 | 3 | −2 |
| **6 o 7** | x⁴ − 5x² + 4 | 1 | −1 |
| **8 o 9** | x⁴ + 2x³ − 13x² − 14x + 24 | −2 | 3 |

#### Lo que debes entregar (a mano)

**E1. Algoritmo general en lenguaje natural.** Describe el procedimiento de la división sintética para **cualquier** polinomio, no solo el tuyo:
- Debe iniciar con **Inicio** y terminar con **Fin**, con pasos numerados y una sola acción por paso.
- Identifica las **entradas** (¿qué datos necesito?), el **proceso** y las **salidas** (¿qué obtengo?).
- Debe ser preciso. "Haz las operaciones" no es un paso; tienes que decir **qué** operación, **con qué números** y **dónde** escribes el resultado.
- Debe indicar qué hacer si el polinomio **no tiene algún término** (por ejemplo, si falta el término x³).
- Debe indicar cómo se **interpreta el resultado**: cuál es el nuevo polinomio, de qué grado queda y qué significa el residuo.
- Debe indicar cómo **repetir** el procedimiento para bajar un grado más.

**E2. Prueba de escritorio con tu polinomio asignado.** Aplica tu algoritmo paso a paso:
- Primera división con r₁: muestra la tabla de la división sintética completa y escribe Q₁(x) y el residuo.
- Segunda división con r₂ aplicada a Q₁(x): tabla completa, Q₂(x) y residuo.
- Escribe la expresión final: P(x) = (x − r₁)(x − r₂) · Q₂(x)

**E3. Comprobación.** Multiplica (x − r₁)(x − r₂) · Q₂(x) y demuestra que obtienes de nuevo tu P(x) original.

**E4. Fuentes consultadas.** Lista los videos, páginas o libros que usaste.

> 🔎 El profesor puede pedirte que resuelvas en el pizarrón la división de un polinomio distinto usando **tu** algoritmo. Si no puedes, la Parte E no se considera tuya.

---

## 3. Entregables

| Entregable | Archivo | Ubicación |
| :--- | :--- | :--- |
| Documento de la actividad (portada con nombre, matrícula y grupo; partes A, B y C4) | `Actividad1_MiRutinaDigital.pdf` (Word exportado a PDF) | `semana1/` |
| Diagrama de flujo | `diagrama_flujo.jpg` / `.png` | `semana1/` (y también insertado en el PDF) |
| Notebook resuelto | `calculadora_tiempo_digital.ipynb` | `semana1/` |
| Parte E (sanción), hecha a mano y escaneada | `ParteE_DivisionSintetica.pdf` | `semana1/` |
| **Evidencia final** | **Liga pública del repositorio** | Plataforma del curso |

**Reglas de entrega:**
- La fecha límite **no se pospone**. Si Git, GitHub o Python te dan problemas, documenta el error con una captura dentro de tu PDF y entrega lo que tengas a tiempo.
- La prueba de escritorio debe usar **tus datos reales**. Las entregas idénticas o sustancialmente iguales entre alumnos se califican con 0.
- El profesor puede pedirte que expliques tu algoritmo en clase. Si no puedes explicarlo, la Parte A no se considera tuya.

---

## 4. Rúbrica de evaluación (100 pts)

| Parte | Criterio | Pts | Excelente (100%) | Bueno (75%) | Regular (50%) | Insuficiente (0%) |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| A | **Tabla EPS** | 8 | Entrada, Proceso y Salida correctos y completos para las 5 plataformas. | Un elemento mal clasificado o faltante. | Dos o más elementos mal clasificados. | No la incluye. |
| A | **Algoritmo en lenguaje natural** | 14 | Inicio/Fin, pasos numerados, una acción por paso; preciso, definido y finito; cubre las 5 plataformas, suma, porcentaje y salida. | Completo, con 1 o 2 pasos ambiguos. | Incompleto, desordenado o con varios pasos ambiguos. | No lo incluye. |
| A | **Prueba de escritorio** | 8 | Datos propios, operaciones escritas y resultados correctos. | Resultados correctos sin todas las operaciones escritas. | Errores de cálculo o datos incompletos. | No la incluye. |
| B | **Diagrama de flujo** | 10 | Símbolos correctos, flujo completo y coherente con el algoritmo, legible. | Coherente con 1 o 2 símbolos mal usados. | Incompleto o no coincide con el algoritmo. | No lo incluye o es ilegible. |
| C | **Repositorio, estructura y README** | 12 | Público, estructura `semana1/` correcta, README completo y archivos en su lugar. | Público con fallas menores de estructura o README incompleto. | Archivos sueltos sin estructura o sin README. | No entrega liga o el repositorio es privado. |
| C | **Historial de commits** | 8 | 3 o más commits progresivos con mensajes descriptivos. | 3 commits con mensajes poco descriptivos. | 1 o 2 commits. | Sin commits propios. |
| C | **Evidencia de instalación** | 5 | Captura con `git --version` y `git config user.name`. | Captura incompleta. | — | No la incluye. |
| D | **Notebook ejecutado y ampliado** | 8 | Celdas ejecutadas con datos propios y calculadora funcionando con 5 plataformas. | Ejecutado con 5 plataformas, pero con un error menor (ej. una plataforma no se suma). | Solo ejecuta la versión de 3 plataformas. | No entrega notebook o no está ejecutado. |
| D | **Análisis EPS y comparación** | 7 | Identifica correctamente las líneas de E/P/S, compara contra A4 y responde la reflexión. | Identificación correcta con comparación o reflexión incompleta. | Identificación con errores. | No lo responde. |
| E | **Algoritmo de división sintética (sanción)** | 10 | Inicio/Fin, pasos numerados y precisos, EPS identificado; cubre términos faltantes, interpretación del resultado y repetición para bajar otro grado. Hecho a mano. | Completo, con 1 o 2 pasos ambiguos o sin cubrir los términos faltantes. | Incompleto o tan vago que no podría seguirse sin ayuda. | No lo incluye, no está hecho a mano o es copia. |
| E | **Prueba de escritorio: 2 divisiones (sanción)** | 7 | Polinomio asignado correcto; ambas tablas completas y correctas, residuos 0 y Q₂(x) correcto. | Una división correcta y la otra con errores menores de cálculo. | Solo una división, o ambas con errores. | No la incluye o usa otro polinomio. |
| E | **Comprobación y fuentes (sanción)** | 3 | La multiplicación reconstruye P(x) y cita sus fuentes. | Comprobación con error menor o sin fuentes. | Comprobación incompleta. | No la incluye. |
| — | **Extra: PSeInt** | +5 | Pseudocódigo funcional y diagrama exportado desde PSeInt. | | | |
| | **TOTAL** | **100** | | | | |

---

## 5. Checklist antes de entregar

- [ ] Mi PDF tiene portada, A1–A4, el diagrama insertado y la captura de C4.
- [ ] Mi prueba de escritorio usa mis horas reales y muestra las operaciones.
- [ ] Mi diagrama coincide paso a paso con mi algoritmo.
- [ ] Mi notebook está ejecutado (se ven las salidas) y funciona con 5 plataformas.
- [ ] Mi repositorio es público y tiene la carpeta `semana1/` con los 4 archivos.
- [ ] Tengo al menos 3 commits con mensajes claros.
- [ ] Mi Parte E está hecha a mano, usa el polinomio de mi matrícula, tiene las 2 divisiones y la comprobación, y está escaneada en un solo PDF.
- [ ] Abrí la liga de mi repositorio en una ventana de incógnito y se ve todo.
