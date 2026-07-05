"""
CelebraWeb Platform Bootstrap

Inicializa una instalación nueva de la plataforma.

Sprint 10 - CW-202
"""

from pathlib import Path


def run():

    print("=" * 60)
    print(" CelebraWeb Platform Bootstrap")
    print("=" * 60)

    print("Bootstrap iniciado...")

    print(f"Proyecto : {Path.cwd()}")

    print("Bootstrap finalizado correctamente.")


if __name__ == "__main__":

    run()