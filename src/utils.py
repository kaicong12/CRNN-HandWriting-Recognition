import numpy as np
import cv2
import os
import os.path as osp
import xml.etree.cElementTree as et


def extract_words_from_directories(self):
    words = []
    xml_files = os.listdir(self.xml_dir)

    for xml_filename in xml_files:
        tree = et.parse(osp.join(self.xml_dir, xml_filename))
        root = tree.getroot()

        for word in root.iter('word'):
            text_id = word.attrib['id']

            splits = text_id.split("-")
            split_0 = splits[0]
            split_1 = "-".join(splits[:2])

            filepath = osp.join(self.png_dir, split_0, split_1, f"{text_id}.png")
            if not osp.isfile(filepath):
                raise Exception(f"{filepath} not found.")

            words.append({
                'id': text_id,
                'image_filepath': filepath,
                'text': word.attrib['text']
            })

    return words


def encode_to_labels(txt, char_list):
    """
    Args:
        txt:
        char_list:

    Returns:

    """
    # encoding each output word into digits
    dig_lst = []
    for index, chara in enumerate(txt):
        dig_lst.append(char_list.index(chara))

    return dig_lst


def process_image(img):
    """
    Converts image to shape (32, 128, 1) & normalize
    """
    w, h = img.shape

    # image thresholding
    #     _, img = cv2.threshold(img,
    #                            128,
    #                            255,
    #                            cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Aspect Ratio Calculation
    new_w = 32
    new_h = int(h * (new_w / w))
    img = cv2.resize(img, (new_h, new_w))
    w, h = img.shape

    img = img.astype('float32')

    # Converts each to (32, 128, 1)
    if w < 32:
        add_zeros = np.full((32 - w, h), 255)
        img = np.concatenate((img, add_zeros))
        w, h = img.shape

    if h < 128:
        add_zeros = np.full((w, 128 - h), 255)
        img = np.concatenate((img, add_zeros), axis=1)
        w, h = img.shape

    if h > 128 or w > 32:
        dim = (128, 32)
        img = cv2.resize(img, dim)

    img = cv2.subtract(255, img)

    img = np.expand_dims(img, axis=2)

    # Normalize
    img = img / 255

    return img
