from infrastructure.manifest_loader import ManifestLoader

loader = ManifestLoader()

manifest = loader.load()

print(manifest)