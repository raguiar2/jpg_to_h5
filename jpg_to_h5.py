import os
import h5py
import argparse
import numpy as np


def convert_file(input_dir, filename, output_dir):
    filepath = input_dir + '/' + filename
    fin = open(filepath, 'rb')
    binary_data = fin.read()
    new_filepath = output_dir + '/' + filename[:-4] + '.hdf5'
    f = h5py.File(new_filepath)
    dt = h5py.special_dtype(vlen=np.dtype('uint8'))
    dset = f.create_dataset('binary_data', (100, ), dtype=dt)
    dset[0] = np.fromstring(binary_data, dtype='uint8')


def main(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename[-4:] == '.jpg':
            convert_file(input_dir, filename, output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_dir', dest='input_dir', type=str,
                    help='Input directory containing .jpg images')
    parser.add_argument('--output_dir', dest='output_dir', type=str,
                    help='Output directory containing .h5 images')
    args = parser.parse_args()
    if args.input_dir is None or args.output_dir is None:
        raise Exception('Please specify an input and output directory')
    main(args.input_dir, args.output_dir)