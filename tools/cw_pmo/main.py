"""
CW PMO
Main
"""

import sys

from services.project_service import ProjectService

from commands.generate_command import GenerateCommand
from commands.review_command import ReviewCommand
from commands.sync_command import SyncCommand
from commands.sprint_close import SprintCloseCommand
from commands.start_command import StartCommand
from commands.validate_command import ValidateCommand


def context():

    c = ProjectService().get_context()

    print()
    print("=" * 50)
    print("          CELEBRAWEB PMO")
    print("=" * 50)
    print()

    print(f"Proyecto : {c.project}")
    print(f"Versión  : {c.version}")
    print(f"Sprint   : {c.sprint}")
    print(f"Estado   : {c.sprint_status}")
    print(f"Fase     : {c.phase}")
    print(f"Release  : {c.release}")

    print()
    print("=" * 50)


def main():

    if len(sys.argv) == 1:
        context()
        return

    command = sys.argv[1].lower()

    if command == "review":
        ReviewCommand().run()
        return


    if command == "start":
        StartCommand().run()
        return

    if command == "generate":
        GenerateCommand().run()
        return

    if command == "sync":
        SyncCommand().run()
        return

    if command == "validate":
        ValidateCommand().run()
        return

    if command == "close":
        SprintCloseCommand().execute()
        return

    print()
    print("Comando no reconocido.")
    print()
    print("Comandos disponibles:")
    print("  start")
    print("  review")
    print("  generate")
    print("  sync")
    print("  validate")
    print("  close")
    print()


if __name__ == "__main__":
    main()