"""
utils_solved.py - Soluciones de referencia del proyecto.

Este archivo contiene las implementaciones completas de todas las funciones.
Úsalo como referencia si no alcanzaste a terminar algún ejercicio durante
la sesión, o para verificar que tu solución es equivalente a esta.

Recuerda que hay varias formas correctas de resolver un problema: si tu
código produce los mismos resultados que estos ejemplos, tu solución es válida.
"""


# ---------------------------------------------------------------------------
# Datos de práctica
# ---------------------------------------------------------------------------

DECLARACIONES = [
    {
        "nit": "900123456",
        "nombre": "Empresa ABC S.A.S.",
        "municipio": "Bogota",
        "periodo": "202401",
        "valor": 1_500_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "800234567",
        "nombre": "Comercial XYZ Ltda.",
        "municipio": "Medellin",
        "periodo": "202401",
        "valor": 850_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "700345678",
        "nombre": "Servicios LMN S.A.S.",
        "municipio": "Cali",
        "periodo": "202401",
        "valor": 0,
        "estado": "INACTIVO",
    },
    {
        "nit": "600456789",
        "nombre": "Industrias PQR S.A.",
        "municipio": "Barranquilla",
        "periodo": "202401",
        "valor": 2_300_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "500567890",
        "nombre": "Distribuidora STU Ltda.",
        "municipio": "Bogota",
        "periodo": "202402",
        "valor": 950_000,
        "estado": "PENDIENTE",
    },
    {
        "nit": "400678901",
        "nombre": "Inversiones VWX S.A.S.",
        "municipio": "Medellin",
        "periodo": "202402",
        "valor": 3_200_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "300789012",
        "nombre": "Transportes YZA Ltda.",
        "municipio": "Cali",
        "periodo": "202402",
        "valor": 450_000,
        "estado": "SUSPENDIDO",
    },
    {
        "nit": "200890123",
        "nombre": "Construcciones BCD S.A.",
        "municipio": "Barranquilla",
        "periodo": "202402",
        "valor": 1_100_000,
        "estado": "ACTIVO",
    },
]


# ---------------------------------------------------------------------------
# FUNCIONES Y PROCEDIMIENTOS
# ---------------------------------------------------------------------------

def calcular_iva(valor_base, tasa=0.19):
    """
    Calcula el IVA sobre un valor base.

    Args:
        valor_base (float): Monto antes de impuestos.
        tasa (float): Tasa de IVA. Por defecto 0.19 (19 %).

    Returns:
        float: Valor del IVA.

    Ejemplos:
        calcular_iva(1_000_000)        -> 190000.0
        calcular_iva(1_000_000, 0.05)  -> 50000.0
        calcular_iva(0)                -> 0.0
    """
    iva = valor_base * tasa
    return iva


def formatear_reporte_valor(nit, nombre, valor, estado):
    """
    Genera una línea de reporte con los campos principales de una declaración.

    Args:
        nit (str): NIT del contribuyente.
        nombre (str): Nombre o razón social.
        valor (float): Valor declarado.
        estado (str): Estado del registro.

    Returns:
        str: Cadena con formato "NIT XXXXXXXXX | Nombre | $valor | ESTADO".

    Ejemplo:
        formatear_reporte_valor("900123456", "Empresa ABC S.A.S.", 1_500_000, "ACTIVO")
        -> "NIT 900123456 | Empresa ABC S.A.S. | $1,500,000 | ACTIVO"
    """
    linea = f"NIT {nit} | {nombre} | ${valor:,} | {estado}"
    return linea


def mostrar_resultado(etiqueta, valor):
    """
    Procedimiento: imprime un resultado con formato de moneda.

    Args:
        etiqueta (str): Descripción del resultado.
        valor (float): Valor numérico a mostrar.
    """
    print(f"  {etiqueta}: ${valor:,.0f}")


def generar_ficha_contribuyente(nit, nombre, municipio, periodo, valor, estado):
    """
    Genera una ficha formal de contribuyente como texto multilínea.

    Args:
        nit (str): NIT del contribuyente.
        nombre (str): Nombre o razón social.
        municipio (str): Municipio de registro.
        periodo (str): Período en formato YYYYMM.
        valor (float): Valor declarado.
        estado (str): Estado del registro.

    Returns:
        str: Texto con la ficha en recuadro.
    """
    nombre_mayusculas = nombre.upper()
    municipio_mayusculas = municipio.upper()
    valor_formateado = f"${valor:,}"
    ficha = (
        f"╔══════════════════════════════════════╗\n"
        f"║  FICHA DE CONTRIBUYENTE              ║\n"
        f"╠══════════════════════════════════════╣\n"
        f"  NIT        : {nit}\n"
        f"  Nombre     : {nombre_mayusculas}\n"
        f"  Municipio  : {municipio_mayusculas}\n"
        f"  Periodo    : {periodo}\n"
        f"  Valor      : {valor_formateado}\n"
        f"  Estado     : {estado}\n"
        f"╚══════════════════════════════════════╝"
    )
    return ficha


# ---------------------------------------------------------------------------
# ENCADENAMIENTO DE FUNCIONES
# ---------------------------------------------------------------------------

def limpiar_nit(nit):
    """
    Elimina guiones y puntos de un NIT.

    Args:
        nit (str): NIT posiblemente con guiones o puntos.

    Returns:
        str: NIT sin guiones ni puntos.

    Ejemplos:
        limpiar_nit("900-123-456")  -> "900123456"
        limpiar_nit("900.123.456")  -> "900123456"
        limpiar_nit("900123456")    -> "900123456"
    """
    sin_guiones = nit.replace("-", "")
    sin_puntos = sin_guiones.replace(".", "")
    return sin_puntos


def validar_nit(nit):
    """
    Valida que un NIT tenga el formato correcto.

    Args:
        nit (str): NIT a validar (puede tener guiones o puntos).

    Returns:
        bool: True si es válido, False si no.

    Ejemplos:
        validar_nit("900123456")    -> True
        validar_nit("900-123-456")  -> True
        validar_nit("ABC123")       -> False
        validar_nit("123")          -> False
    """
    nit_limpio = limpiar_nit(nit)
    solo_digitos = nit_limpio.isdigit()
    longitud_valida = len(nit_limpio) >= 9 and len(nit_limpio) <= 10
    return solo_digitos and longitud_valida


def normalizar_texto(texto):
    """
    Limpia y normaliza una cadena de texto.

    Args:
        texto (str): Texto a normalizar.

    Returns:
        str: Texto normalizado en mayúsculas y sin espacios extra.

    Ejemplos:
        normalizar_texto("  bogotá d.c.  ")  -> "BOGOTÁ D.C."
        normalizar_texto("  empresa  abc  ") -> "EMPRESA ABC"
    """
    return texto.strip().upper().replace("  ", " ")


def procesar_nit(nit):
    """
    Limpia y valida un NIT. Retorna un mensaje con el resultado.

    Args:
        nit (str): NIT a procesar.

    Returns:
        str: Mensaje indicando si el NIT es válido o no.

    Ejemplos:
        procesar_nit("900-123-456")  -> "NIT 900123456: válido"
        procesar_nit("ABC-123")      -> "NIT ABC-123: INVÁLIDO"
    """
    nit_limpio = limpiar_nit(nit)
    es_valido = validar_nit(nit_limpio)
    if es_valido:
        mensaje = f"NIT {nit_limpio}: válido"
    else:
        mensaje = f"NIT {nit}: INVÁLIDO"
    return mensaje


def pipeline_nit(nit):
    """
    Aplica un pipeline de tres operaciones sobre un NIT.

    Args:
        nit (str): NIT de entrada.

    Returns:
        str: Informe del resultado del pipeline.

    Ejemplos:
        pipeline_nit("900-123-456")  -> "NIT 900123456 — apto para procesamiento"
        pipeline_nit("ABC-123")      -> "NIT ABC-123 — rechazado: formato inválido"
    """
    nit_limpio = limpiar_nit(nit)
    es_valido = validar_nit(nit_limpio)
    if es_valido:
        informe = f"NIT {nit_limpio} — apto para procesamiento"
    else:
        informe = f"NIT {nit} — rechazado: formato inválido"
    return informe


# ---------------------------------------------------------------------------
# CONDICIONALES SIMPLES
# ---------------------------------------------------------------------------

def esta_al_dia(dias_mora):
    """
    Determina si un contribuyente está al día en sus pagos.

    Args:
        dias_mora (int): Días de mora.

    Returns:
        bool: True si dias_mora es 0, False en cualquier otro caso.

    Ejemplos:
        esta_al_dia(0)   -> True
        esta_al_dia(30)  -> False
    """
    if dias_mora == 0:
        return True
    else:
        return False


def aplicar_descuento(valor, pago_voluntario):
    """
    Aplica un descuento del 10 % si el pago es voluntario.

    Args:
        valor (float): Valor original del pago.
        pago_voluntario (bool): True si el pago es voluntario.

    Returns:
        float: Valor con descuento, o el valor original si no aplica.

    Ejemplos:
        aplicar_descuento(1_000_000, True)   -> 900000.0
        aplicar_descuento(1_000_000, False)  -> 1000000
    """
    if pago_voluntario:
        descuento = valor * 0.10
        valor_con_descuento = valor - descuento
        return valor_con_descuento
    else:
        return valor


def asignar_prioridad(valor, tiene_historial_incumplimiento):
    """
    Asigna una prioridad de atención según valor e historial.

    Args:
        valor (float): Valor declarado.
        tiene_historial_incumplimiento (bool): True si hay historial.

    Returns:
        str: "ALTA", "MEDIA" o "BAJA".
    """
    valor_alto = valor > 1_000_000
    tiene_historial = tiene_historial_incumplimiento
    if valor_alto and tiene_historial:
        return "ALTA"
    elif valor_alto or tiene_historial:
        return "MEDIA"
    else:
        return "BAJA"


# ---------------------------------------------------------------------------
# CONDICIONALES ANIDADOS
# ---------------------------------------------------------------------------

def clasificar_mora(dias_mora, valor):
    """
    Clasifica la situación de mora de un contribuyente.

    Args:
        dias_mora (int): Días de mora.
        valor (float): Valor declarado.

    Returns:
        str: "Mora alta", "Mora baja" o "Sin mora".
    """
    if dias_mora > 0:
        if valor > 500_000:
            return "Mora alta"
        else:
            return "Mora baja"
    else:
        return "Sin mora"


def determinar_tipo_seguimiento(estado, valor, municipio):
    """
    Determina el tipo de seguimiento que requiere un registro.

    Args:
        estado (str): Estado del registro.
        valor (float): Valor declarado.
        municipio (str): Municipio del contribuyente.

    Returns:
        str: Tipo de seguimiento asignado.
    """
    if estado == "ACTIVO":
        municipio_prioritario = municipio == "Bogota" or municipio == "Medellin"
        valor_alto = valor > 2_000_000
        if municipio_prioritario and valor_alto:
            return "Seguimiento prioritario"
        else:
            return "Seguimiento estándar"
    elif estado == "PENDIENTE":
        return "Seguimiento urgente"
    else:
        return "Sin seguimiento"


def evaluar_cumplimiento(estado, valor, dias_mora, historial):
    """
    Evalúa el nivel de cumplimiento de un contribuyente.

    Args:
        estado (str): Estado del registro.
        valor (float): Valor declarado.
        dias_mora (int): Días de mora.
        historial (bool): True si tiene historial de incumplimiento.

    Returns:
        str: Nivel de cumplimiento.
    """
    if estado == "ACTIVO" and dias_mora == 0:
        return "Cumplimiento total"

    if estado == "ACTIVO" and dias_mora > 0:
        if dias_mora <= 30 and not historial:
            return "Incumplimiento leve"
        else:
            return "Incumplimiento grave"

    if estado == "PENDIENTE" or estado == "SUSPENDIDO":
        if historial and valor > 1_000_000:
            return "Caso crítico"
        else:
            return "Incumplimiento grave"

    return "Incumplimiento leve"


# ---------------------------------------------------------------------------
# CONDICIONALES ENCADENADOS
# ---------------------------------------------------------------------------

def clasificar_contribuyente(valor):
    """
    Clasifica al contribuyente según su valor declarado.

    Args:
        valor (float): Valor declarado.

    Returns:
        str: Categoría del contribuyente.
    """
    if valor > 5_000_000:
        return "GRANDE"
    elif valor > 1_000_000:
        return "MEDIANO"
    elif valor > 100_000:
        return "PEQUEÑO"
    elif valor > 0:
        return "MÍNIMO"
    else:
        return "SIN VALOR"


def describir_periodo(periodo):
    """
    Retorna el trimestre al que pertenece un período.

    Args:
        periodo (str): Período en formato YYYYMM.

    Returns:
        str: Nombre del trimestre, o "Período no reconocido".

    Ejemplos:
        describir_periodo("202401")  -> "Primer trimestre"
        describir_periodo("202407")  -> "Tercer trimestre"
    """
    if len(periodo) != 6 or not periodo.isdigit():
        return "Período no reconocido"
    mes = int(periodo[4:])
    if mes >= 1 and mes <= 3:
        return "Primer trimestre"
    elif mes >= 4 and mes <= 6:
        return "Segundo trimestre"
    elif mes >= 7 and mes <= 9:
        return "Tercer trimestre"
    elif mes >= 10 and mes <= 12:
        return "Cuarto trimestre"
    return "Período no reconocido"


def calcular_sancion_basica(dias_mora, valor_base):
    """
    Calcula la sanción por mora según los días de atraso.

    Args:
        dias_mora (int): Días de mora.
        valor_base (float): Valor sobre el que se aplica la sanción.

    Returns:
        float: Valor de la sanción.

    Ejemplos:
        calcular_sancion_basica(0, 1_000_000)    -> 0.0
        calcular_sancion_basica(15, 1_000_000)   -> 10000.0
        calcular_sancion_basica(100, 1_000_000)  -> 100000.0
    """
    if dias_mora == 0:
        tasa = 0.0
    elif dias_mora <= 30:
        tasa = 0.01
    elif dias_mora <= 60:
        tasa = 0.03
    elif dias_mora <= 90:
        tasa = 0.05
    else:
        tasa = 0.10
    sancion = valor_base * tasa
    return sancion


def priorizar_cobro(valor, dias_mora, tipo_contribuyente):
    """
    Asigna una prioridad de cobro de P1 (más urgente) a P5 (menos urgente).

    Args:
        valor (float): Valor declarado.
        dias_mora (int): Días de mora.
        tipo_contribuyente (str): "GRANDE", "MEDIANO" o "PEQUEÑO".

    Returns:
        str: Prioridad de cobro.
    """
    mora_alta = dias_mora > 60
    mora_media = dias_mora > 30 and dias_mora <= 60
    valor_alto = valor > 1_000_000
    if tipo_contribuyente == "GRANDE" and mora_alta:
        return "P1"
    elif tipo_contribuyente == "GRANDE" and mora_media:
        return "P2"
    elif tipo_contribuyente == "MEDIANO" and mora_alta:
        return "P2"
    elif valor_alto and mora_media:
        return "P3"
    elif mora_alta:
        return "P3"
    elif mora_media:
        return "P4"
    else:
        return "P5"


# ---------------------------------------------------------------------------
# CICLOS FOR
# ---------------------------------------------------------------------------

def imprimir_nits_validos(nits):
    """
    Imprime solo los NITs válidos de una lista, numerados desde 1.

    Args:
        nits (list): Lista de NITs como cadenas de texto.
    """
    print("NITs válidos:")
    contador = 1
    for nit in nits:
        if validar_nit(nit):
            print(f"  {contador}. {nit}")
            contador = contador + 1


def calcular_totales(valores):
    """
    Calcula el total, el promedio y el valor máximo de una lista.

    Args:
        valores (list): Lista de valores numéricos.

    Returns:
        tuple: (total, promedio, maximo)

    Ejemplo:
        total, promedio, maximo = calcular_totales([100, 200, 300])
        # total=600, promedio=200.0, maximo=300
    """
    total = 0
    maximo = valores[0]
    for valor in valores:
        total = total + valor
        if valor > maximo:
            maximo = valor
    promedio = total / len(valores)
    return total, promedio, maximo


def generar_periodos_multiple(anio_inicio, anio_fin, meses_por_anio=12):
    """
    Genera los códigos de período para un rango de años.

    Args:
        anio_inicio (int): Primer año a incluir.
        anio_fin (int): Último año a incluir.
        meses_por_anio (int): Cuántos meses generar por año.

    Returns:
        list: Lista de cadenas en formato YYYYMM.

    Ejemplo:
        generar_periodos_multiple(2024, 2025, 3)
        -> ['202401', '202402', '202403', '202501', '202502', '202503']
    """
    periodos = []
    for anio in range(anio_inicio, anio_fin + 1):
        for mes in range(1, meses_por_anio + 1):
            codigo = f"{anio}{mes:02d}"
            periodos.append(codigo)
    return periodos


# ---------------------------------------------------------------------------
# CICLOS WHILE
# ---------------------------------------------------------------------------

def buscar_primer_valido(nits):
    """
    Busca el primer NIT válido en una lista usando while.

    Args:
        nits (list): Lista de NITs como cadenas de texto.

    Returns:
        str | None: El primer NIT válido, o None si no hay ninguno.
    """
    indice = 0
    while indice < len(nits):
        nit = nits[indice]
        if validar_nit(nit):
            return nit
        indice = indice + 1
    return None


def sumar_hasta_limite(valores, limite):
    """
    Acumula valores de la lista mientras el total no supere el límite.

    Args:
        valores (list): Lista de valores numéricos.
        limite (float): Tope máximo de acumulación.

    Returns:
        tuple: (cantidad_procesada, total_acumulado)

    Ejemplo:
        sumar_hasta_limite([1_500_000, 850_000, 2_300_000], 3_000_000)
        -> (2, 2350000)
    """
    total = 0
    cantidad = 0
    indice = 0
    while indice < len(valores):
        valor_actual = valores[indice]
        if total + valor_actual > limite:
            break
        total = total + valor_actual
        cantidad = cantidad + 1
        indice = indice + 1
    return cantidad, total


def encontrar_primer_sobre_umbral(valores, umbral):
    """
    Busca el primer valor de la lista que supere el umbral.

    Args:
        valores (list): Lista de valores numéricos.
        umbral (float): Valor que debe superarse.

    Returns:
        float | None: El primer valor que supera el umbral, o None.

    Ejemplos:
        encontrar_primer_sobre_umbral([850_000, 950_000, 2_300_000], 2_000_000)
        -> 2300000
        encontrar_primer_sobre_umbral([100, 200, 300], 5_000_000)
        -> None
    """
    indice = 0
    while indice < len(valores):
        valor_actual = valores[indice]
        if valor_actual > umbral:
            return valor_actual
        indice = indice + 1
    return None


def validar_secuencia_periodos(periodos):
    """
    Verifica que una lista de períodos esté en orden consecutivo.

    Args:
        periodos (list): Lista de códigos en formato YYYYMM.

    Returns:
        tuple: (es_valida, indice_salto)

    Ejemplos:
        validar_secuencia_periodos(["202401", "202402", "202403"])
        -> (True, None)
        validar_secuencia_periodos(["202401", "202403"])
        -> (False, 1)
    """
    if len(periodos) <= 1:
        return True, None
    indice = 0
    while indice < len(periodos) - 1:
        anio_actual = int(periodos[indice][:4])
        mes_actual = int(periodos[indice][4:])
        anio_siguiente = int(periodos[indice + 1][:4])
        mes_siguiente = int(periodos[indice + 1][4:])
        if mes_actual == 12:
            anio_esperado = anio_actual + 1
            mes_esperado = 1
        else:
            anio_esperado = anio_actual
            mes_esperado = mes_actual + 1
        if anio_siguiente != anio_esperado or mes_siguiente != mes_esperado:
            return False, indice + 1
        indice = indice + 1
    return True, None


# ---------------------------------------------------------------------------
# LISTAS
# ---------------------------------------------------------------------------

def agregar_unico(lista, elemento):
    """
    Agrega un elemento a la lista solo si no está ya presente.

    Args:
        lista (list): Lista de elementos.
        elemento: Elemento a agregar.

    Returns:
        list: Lista actualizada.

    Ejemplos:
        agregar_unico(["ACTIVO", "INACTIVO"], "PENDIENTE")
        -> ["ACTIVO", "INACTIVO", "PENDIENTE"]
        agregar_unico(["ACTIVO", "INACTIVO"], "ACTIVO")
        -> ["ACTIVO", "INACTIVO"]
    """
    if elemento not in lista:
        lista.append(elemento)
    return lista


def filtrar_valores_en_rango(valores, minimo, maximo):
    """
    Retorna una nueva lista con los valores dentro del rango dado.

    Args:
        valores (list): Lista de valores numéricos.
        minimo (float): Límite inferior (inclusive).
        maximo (float): Límite superior (inclusive).

    Returns:
        list: Lista filtrada.

    Ejemplo:
        filtrar_valores_en_rango([100, 500, 1000, 1500], 400, 1100)
        -> [500, 1000]
    """
    resultado = []
    for valor in valores:
        esta_en_rango = valor >= minimo and valor <= maximo
        if esta_en_rango:
            resultado.append(valor)
    return resultado


def ordenar_valores(valores, descendente=True):
    """
    Retorna una nueva lista ordenada usando el algoritmo de burbuja.

    Args:
        valores (list): Lista de valores numéricos.
        descendente (bool): True para orden descendente.

    Returns:
        list: Lista ordenada. La original no se modifica.

    Ejemplo:
        ordenar_valores([1_500_000, 850_000, 2_300_000, 450_000])
        -> [2300000, 1500000, 850000, 450000]
    """
    resultado = list(valores)
    n = len(resultado)
    for i in range(n):
        for j in range(0, n - i - 1):
            if descendente:
                deben_intercambiarse = resultado[j] < resultado[j + 1]
            else:
                deben_intercambiarse = resultado[j] > resultado[j + 1]
            if deben_intercambiarse:
                temporal = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = temporal
    return resultado


# ---------------------------------------------------------------------------
# DICCIONARIOS
# A partir de aquí los ejercicios usan DECLARACIONES.
# ---------------------------------------------------------------------------

def indexar_por_nit(declaraciones):
    """
    Construye un diccionario donde la clave es el NIT y el valor
    es el registro completo de esa declaración.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Diccionario indexado por NIT.

    Ejemplo:
        indice = indexar_por_nit(DECLARACIONES)
        indice["600456789"]["nombre"]  -> "Industrias PQR S.A."
    """
    indice = {}
    for declaracion in declaraciones:
        nit = declaracion["nit"]
        indice[nit] = declaracion
    return indice


def construir_resumen_por_estado(declaraciones):
    """
    Agrupa las declaraciones por estado y acumula conteo y total.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Diccionario con conteo y total por estado.
    """
    resumen = {}
    for declaracion in declaraciones:
        estado = declaracion["estado"]
        valor = declaracion["valor"]
        if estado not in resumen:
            resumen[estado] = {"conteo": 0, "total_valor": 0}
        resumen[estado]["conteo"] = resumen[estado]["conteo"] + 1
        resumen[estado]["total_valor"] = resumen[estado]["total_valor"] + valor
    return resumen


def agrupar_por_municipio(declaraciones):
    """
    Agrupa los registros por municipio.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Diccionario con listas de registros por municipio.
    """
    grupos = {}
    for declaracion in declaraciones:
        municipio = declaracion["municipio"]
        if municipio not in grupos:
            grupos[municipio] = []
        grupos[municipio].append(declaracion)
    return grupos


def imprimir_agrupacion(agrupacion):
    """
    Procedimiento: imprime un resumen formateado por municipio.

    Args:
        agrupacion (dict): Resultado de agrupar_por_municipio().
    """
    print("Resumen por municipio:")
    print(f"  {'Municipio':<15} {'Declaraciones':>14} {'Total':>14}")
    print("  " + "-" * 45)
    for municipio in agrupacion:
        registros = agrupacion[municipio]
        cantidad = len(registros)
        total = 0
        for registro in registros:
            total = total + registro["valor"]
        print(f"  {municipio:<15} {cantidad:>14} ${total:>13,}")


def calcular_estadisticas(declaraciones):
    """
    Calcula estadísticas generales del conjunto de declaraciones.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Estadísticas del conjunto.
    """
    total_registros = len(declaraciones)
    total_activos = 0
    suma_valores = 0
    suma_valores_activos = 0
    valor_maximo = 0
    for declaracion in declaraciones:
        valor = declaracion["valor"]
        suma_valores = suma_valores + valor
        if valor > valor_maximo:
            valor_maximo = valor
        if declaracion["estado"] == "ACTIVO":
            total_activos = total_activos + 1
            suma_valores_activos = suma_valores_activos + valor
    if total_activos > 0:
        promedio_activos = suma_valores_activos / total_activos
    else:
        promedio_activos = 0
    return {
        "total_registros": total_registros,
        "total_activos": total_activos,
        "suma_valores": suma_valores,
        "promedio_valor_activos": promedio_activos,
        "valor_maximo": valor_maximo,
    }


def filtrar_por_estado(declaraciones, estado):
    """
    Retorna una nueva lista con solo los registros del estado indicado.

    Args:
        declaraciones (list): Lista de registros de declaraciones.
        estado (str): Estado a filtrar.

    Returns:
        list: Registros que coinciden con el estado.
    """
    resultado = []
    for declaracion in declaraciones:
        if declaracion["estado"] == estado:
            resultado.append(declaracion)
    return resultado


def buscar_por_nit(declaraciones, nit_buscado):
    """
    Busca la primera declaración con el NIT indicado usando while.

    Args:
        declaraciones (list): Lista de registros de declaraciones.
        nit_buscado (str): NIT a buscar.

    Returns:
        dict | None: El primer registro con ese NIT, o None si no existe.

    Ejemplo:
        resultado = buscar_por_nit(DECLARACIONES, "600456789")
        resultado["nombre"]  -> "Industrias PQR S.A."
    """
    indice = 0
    while indice < len(declaraciones):
        declaracion = declaraciones[indice]
        if declaracion["nit"] == nit_buscado:
            return declaracion
        indice = indice + 1
    return None
