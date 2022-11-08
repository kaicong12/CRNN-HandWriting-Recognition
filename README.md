# CRNN-CTC Model for text recognition
<p align="center">
  <img src="./report/CRNN_Architecture.pbm" alt="model-architecture"/>
</p>

## Download dataset
1. Sign up for an account under the official webpage for handwriting dataset.  
2. Download the IAM Handwriting Dataset for OCR model [here](https://fki.tic.heia-fr.ch/databases/download-the-iam-handwriting-database)  
3. **(Optional)** Download the IAM On-Line Handwriting Dataset [here](https://fki.tic.heia-fr.ch/databases/iam-on-line-handwriting-database) if you wish to experiment with GAN

## Experiment Setup
1. Train a baseline CRNN model on a generic set of handwritings from the IAM Handwriting dataset which consists of handwriting from 674 authors.
2. Compare model performance when only trained on one person's handwriting 

# Generative Adversarial Network (GAN)
In reality, it is costly to collect sufficient real handwriting from a single author in order to assemble a dataset robust enough to represent the author's style. Therefore, we leveraged GAN in order to generate huge amount of synthetic handwriting data 
which resembles the original author's style. However, given the short span of time and the lack of comptational resource, the team did not manage to build a GAN model from scratch. We had instead 
took reference from the [deepwriting model](https://paperswithcode.com/paper/deepwriting-making-digital-ink-editable-via) and recycled the GAN model which the organization had trained. Details and README can be found in the [deepwriting directory](https://github.com/kaicong12/CRNN-HandWriting-Recognition/tree/main/deepwriting)
within this repo.