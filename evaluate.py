import matplotlib.pyplot as plt


def visualize_prediction(self, weight_path, start_idx, end_idx):
    """
    Plot prediction of images from start_idx: end_idx
    """
    # load the saved best model weights
    valid_model = self.model.build_valid_model(weight_path)

    # predict outputs on validation images
    prediction = valid_model.predict(self.valid_images[start_idx: end_idx])

    # use CTC decoder
    decoded = K.ctc_decode(prediction,
                           input_length=np.ones(prediction.shape[0]) * prediction.shape[1],
                           greedy=True)[0][0]

    out = K.get_value(decoded)

    # see the results
    for i, x in enumerate(out):
        print("original_text = ", self.valid_original_text[start_idx + i])
        print("predicted text = ", end='')
        for p in x:
            if int(p) != -1:
                print(self.dataset_obj.char_list[int(p)], end='')
        plt.imshow(self.valid_images[start_idx + i].reshape(32, 128), cmap=plt.cm.gray)
        plt.show()
        print('\n')