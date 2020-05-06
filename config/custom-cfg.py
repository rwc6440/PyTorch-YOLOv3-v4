import os
import argparse



if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_classes", '-n', type=int, default=1, help="number of classes")
    opt = parser.parse_args()

    n_class = opt.n_classes
    custom_num = 3*(n_class+5)
    f = open(f'./yolov4-custom.txt', 'r')
    tar = open(f'./yolov4-custom.cfg', 'w')

    a=f.read()
    a = a.replace('custom_num', str(custom_num))
    a = a.replace('$NUM_CLASSES', str(n_class))
    tar.write(a)