#!/usr/bin/env python3

import sys, yaml

def fstab_generator(argv):
  output_lines = ''
  fs_dump_list = ['xfs', 'ext2', 'ext3', 'ext4']

  for mount_source in argv:
    mount_details = argv[mount_source]
    mount = {}

    # Mount source
    mount['source'] = mount_source
    if mount_details['type'] == 'nfs':
      mount['source'] += ':' + mount_details['export']

    # Mount point
    mount['point'] = mount_details['mount']

    # Mount filesystem
    mount['fs_type'] = mount_details['type']

    # Mount options
    mount['options'] = 'defaults'
    if 'options' in mount_details:
      for option in mount_details['options']:
        mount['options'] += ',' + option

    # Mount dump
    if mount_details['type'] in fs_dump_list:
      mount['dump'] = '1'
    else:
      mount['dump'] = '0'

    # Mount pass
    if mount_details['mount'] == '/':
      mount['pass'] = '1'
    else:
      mount['pass'] = '2'

    output_lines += mount['source'] + '\t' + mount['point'] + '\t' + mount['fs_type'] + '\t' + mount['options'] + '\t' + mount['dump'] + ' ' + mount['pass'] + '\n'

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
    with open(output_file, "w") as file:
      try:
        file.write(result)
      except IOError as exc:
        print(exc)
  else:
    print('fstab key is expected.')

if __name__ == "__main__":
  main(sys.argv[1:])
