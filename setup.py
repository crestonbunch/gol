from cx_Freeze import setup, Executable
import pygame._view
import os
import re

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('run.py')
]

setup(name='GoL',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)


