#!/usr/bin/env python3

import sys, yaml

def fstab_generator(argv):
  output_lines = ''

  for mount_source in argv:
    mount_details = argv[mount_source]
    mount = {}

    # Mount source
    mount['source'] = mount_source
    if mount_details['type'] == 'nfs':
      mount['source'] += ':' + mount_details['export']

    output_lines += mount['source'] + '\n'

  return(output_lines)

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
    print(result)
  else:
    print('fstab key is expected.')

if __name__ == "__main__":
  main(sys.argv[1:])
