import argparse
import time
import winsound


def formatear_tiempo(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:02d}"


def sonar_alerta():
    for _ in range(3):
        winsound.Beep(880, 250)
        time.sleep(0.15)


def ejecutar_ciclo(nombre, duracion_minutos):
    duracion = max(1, int(duracion_minutos * 60))
    print(f"\n=== {nombre.upper()} ===")
    print(f"Duración: {duracion_minutos} minutos")

    for segundos_restantes in range(duracion, 0, -1):
        tiempo_restante = formatear_tiempo(segundos_restantes)
        print(f"\rTiempo restante: {tiempo_restante}   ", end="", flush=True)
        time.sleep(1)

    print("\n")
    print(f"¡{nombre.upper()} terminado! Es hora de parar y descansar.")
    sonar_alerta()


def main():
    parser = argparse.ArgumentParser(description="Temporizador tipo Pomodoro")
    parser.add_argument("--trabajo", type=float, default=25, help="Minutos de trabajo (por defecto: 25)")
    parser.add_argument("--descanso", type=float, default=5, help="Minutos de descanso (por defecto: 5)")
    parser.add_argument("--ciclos", type=int, default=4, help="Número de ciclos de trabajo (por defecto: 4)")
    args = parser.parse_args()

    print("Pomodoro iniciado")
    print("Presiona Ctrl+C para detenerlo manualmente.\n")

    try:
        for ciclo in range(1, args.ciclos + 1):
            print(f"Ciclo {ciclo}/{args.ciclos}")
            ejecutar_ciclo("trabajo", args.trabajo)

            if ciclo < args.ciclos:
                ejecutar_ciclo("descanso", args.descanso)

        print("\n✅ Todos los ciclos terminaron. Puedes descansar o empezar otro.")
    except KeyboardInterrupt:
        print("\n\nTemporizador detenido por el usuario.")


if __name__ == "__main__":
    main()
