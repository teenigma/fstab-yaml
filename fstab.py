#!/usr/bin/env python3

import sys, yaml

def fstab_generator(argv):
  pass

def main(argv):
  ## Default filename
  input_file = 'fstab.yaml'
  output_file = 'results/fstab.out'

  with open(input_file, "r") as stream:
    try:
      fstab_load = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  if 'fstab' in fstab_load:
    result = fstab_generator(fstab_load['fstab'])
  else:
    print('fstab key is expected.')

if __name__ == "__main__":
  main(sys.argv[1:])
