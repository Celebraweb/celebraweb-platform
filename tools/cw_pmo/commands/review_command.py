"""
CW PMO
Review Command
"""

from pathlib import Path


class ReviewCommand:

    def run(self):

        print()
        print("=" * 60)
        print("           CW PMO - REVIEW")
        print("=" * 60)
        print()

        documents = [

            "docs/00-Governance/PROJECT.yaml",

            "docs/00-Governance/DECISION-LOG.md",

            "docs/00-Governance/CW-140-Product-Backlog.md",

            "docs/00-Governance/CW-141-Sprint-Review.md",

            "docs/00-Governance/CW-142-Sprint-Retrospective.md",

            "docs/00-Governance/CW-143-Open-Issues.md",

            "docs/00-Governance/CW-144-Technical-Debt.md",

        ]

        print("Reconstruyendo contexto del proyecto")
        print()

        missing = False

        for document in documents:

            if Path(document).exists():

                print(f"OK  {document}")

            else:

                print(f"ERROR  {document}")

                missing = True

        print()

        if missing:

            print("REVIEW FALLÓ")
            print()

            return

        print("Project Memory ........ OK")
        print("Executive Brief ....... READY")

        print()
        print("=" * 60)
        print("REVIEW FINALIZADO")
        print("=" * 60)
        print()