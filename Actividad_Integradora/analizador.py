import matplotlib.pyplot as plt


def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return None


def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.
    Parametros:
        texto (str): el texto a analizar
    Retorna:
        dict: pares {palabra: frecuencia}
    """
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def graficar(frecuencias, top_n=10):
    """
    Genera y guarda un grafico de barras horizontales con las
    top_n palabras mas frecuentes.
    Parametros:
        frecuencias (dict): pares {palabra: frecuencia}
        top_n (int): cantidad de palabras a graficar
    """
    top = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]
    palabras = [p for p, f in top]
    valores = [f for p, f in top]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()


def main():
    texto = leer_archivo("texto_integradora.txt")
    if texto is None:
        return
    frecuencias = contar_frecuencias(texto)
    print(f"Palabras totales: {sum(frecuencias.values())}")
    print(f"Palabras distintas: {len(frecuencias)}")
    graficar(frecuencias)


if __name__ == "__main__":
    main()
