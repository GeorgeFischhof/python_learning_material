
from modules import exporter
from modules.exporter import EXPORT_CONSTANT

print("I am the importer 04")

print(EXPORT_CONSTANT)

print(exporter.EXPORT_CONSTANT)

exporter.export_function()

# export_function()
# does not work...
