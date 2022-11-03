import argparse
import os


def train(args):
    print(args.model_save_dir)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', '--model_save_dir', type=str, default='./ocr_runs/', help='Path to main model save directory')
    parser.add_argument('-I', '--input_image_file', type=str, required=True, help='Path to input training file')
    parser.add_argument('-L', '--input_label_file', type=str, required=True, help='Path to input training file')
    args = parser.parse_args()

    # directory to store model checkpoint
    if not os.path.isdir(args.model_save_dir):
        os.mkdir(args.model_save_dir)

    train(args)
