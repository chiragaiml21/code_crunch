import subprocess

try:
  subprocess.run(['nvidia-smi'])
  print("Nvidia GPU detected!")
except subprocess.CalledProcessError:
  print("No Nvidia GPU in system!")
