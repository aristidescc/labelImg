from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["os"], 'excludes': [], "include_files": ["data", "tesseract"]}

base = 'Console'

executables = [
    Executable('labelImg.py', base=base, target_name = 'LabelImg')
]

setup(name='LabelImg',
      version = '1.0',
      description = 'Aplicación para etiquetado de imágenes, especialmente preparado para etiquetado de documentos.',
      options = {'build_exe': build_options},
      executables = executables)
