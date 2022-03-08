#coding=utf-8
#!/usr/bin/env python3

#python train_CNN.py h5/axion1_40-250GeV_100k_mass0p5GeV.h5

import sys
import os
#import random
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import random
import time
import importlib
import logging
from tqdm import tqdm

import ROOT 

random.seed(10)

from h5py import File as HDF5File

import tensorflow as tf
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Model, Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten , Convolution2D, MaxPooling2D , Lambda, Conv2D, Activation,Concatenate, Input, BatchNormalization
from tensorflow.keras.optimizers import Adam , SGD , Adagrad, RMSprop
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler, EarlyStopping, CSVLogger, ReduceLROnPlateau
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras import regularizers , initializers
import tensorflow.keras.backend as K
from joblib import dump, load

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

from keras.layers import Lambda, Input
from keras.layers import Dropout, Flatten, Dense 
import keras.backend as K
from keras.models import Sequential, Model 
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate


import enum
print(enum.__file__)  

def usage():
	print ('test usage')
	sys.stdout.write('''
			SYNOPSIS
			./train_CNN.py process 
			\n''')


# for particle, datafile in s.iteritems():
def _load_data(label, datafile):

    import h5py
    print("load_data from datafile", datafile)
    d = h5py.File(datafile, 'r')
    first = np.expand_dims(d['layer_0'][:], -1)
    second = np.expand_dims(d['layer_1'][:], -1)
    third = np.expand_dims(d['layer_2'][:], -1)
    four = np.expand_dims(d['layer_3'][:], -1)
    energy = d['energy'][:].reshape(-1, 1) * 1000  # convert to MeV
    sizes = [first.shape[1], first.shape[2], second.shape[
        1], second.shape[2], third.shape[1], third.shape[2], four.shape[1], four.shape[2]]
    y = [label] * first.shape[0]

    return first, second, third, four, y, energy, sizes




def main():

    args = sys.argv[1:]
    #if len(args) < 1:
    #    return usage()

    #particle
    tag0 = args[0]
    #mass
    tag1 = args[1]
    tag = tag0 + "_" + tag1; 
    path = "./results/"+tag+"/";
    
    sigLabel = "";
    bg0Label = "$\gamma$"
    bg1Label = "$\pi^{0}$"
    if "axion1" in tag:
        sigLabel = "$a \\rightarrow \gamma\gamma$"
    elif "axion2" in tag:
        sigLabel = "$a \\rightarrow 3\pi^{0}$"
    elif "scalar1" in tag:
        sigLabel = "$s \\rightarrow \pi^{0}\pi^{0}$"


    print ('part1')   

    s = ["h5/" + tag + "_40-250GeV_100k.h5",  "h5/gamma_" + tag1 + "_40-250GeV_100k.h5", "h5/pi0_" + tag1 + "_40-250GeV_100k.h5"];
    labels_ = {"h5/" + tag + "_40-250GeV_100k.h5":0, "h5/gamma_" + tag1 + "_40-250GeV_100k.h5":1, "h5/pi0_" + tag1 + "_40-250GeV_100k.h5":2}
    test_split=0.3
    n_classes=3

    #<HDF5 dataset "energy": shape (100000, 1), type "<f8">
    #<HDF5 dataset "layer_0": shape (100000, 4, 16), type "<f8">
    #<HDF5 dataset "layer_1": shape (100000, 4, 128), type "<f8">
    #<HDF5 dataset "layer_2": shape (100000, 16, 16), type "<f8">
    #<HDF5 dataset "layer_3": shape (100000, 16, 8), type "<f8">
    first_all_, second_all_, third_all_, four_all_, y_all_, energy_all_, sizes_all_ = [
        np.concatenate(t) for t in [
            #This assumes different inputs have the same size
           a for a in zip(*[_load_data(labels_[file], file) for file in s])
        ]
    ]
  
    shuffler = np.random.permutation(len(first_all_))
    first_all = first_all_[shuffler]
    second_all = second_all_[shuffler]
    third_all = third_all_[shuffler]
    four_all = four_all_[shuffler]
    y_all = y_all_[shuffler]
    energy_all = energy_all_[shuffler]
    print("Before shuffel: y_all[0, 100000, 299999]'", y_all_[0], " ", y_all_[100000], "", y_all_[299999])
    print("After shuffel: y_all[0, 100000, 299999]'", y_all[0], " ", y_all[100000], "", y_all[299999])

    nall=first_all.shape[0] 
    #nall=10000 
    ntrain=int(nall*(1-test_split)) 

    #Print sizes
    #print("sizes_sig = ", sizes_sig)
    #print("sizes_bkg0 = ", sizes_bkg0)
    #print("sizes_bkg1 = ", sizes_bkg1)

    # Use GeV for energy
#    first_sig, second_sig, third_sig, four_sig, energy_sig = [
#        (X.astype(np.float32) / 1000)[:100000]
#        for X in [first_sig, second_sig, third_sig, four_sig, energy_sig]
#    ]
 
    #tuple object
    #inputs = [(first_all, second_all, third_all, four_all)] # Input Simulation
    X_train = [(first_all[:ntrain], second_all[:ntrain], third_all[:ntrain], four_all[:ntrain])] # Input Simulation
    X_test = [(first_all[ntrain:nall], second_all[ntrain:nall], third_all[ntrain:nall], four_all[ntrain:nall])] # Input Simulation
    
    y_train = y_all[:ntrain] 
    y_test = y_all[ntrain:nall] 
    energy_test = energy_all[ntrain:nall] 

    print("train size", X_train[0][0].shape)
    print("test size", X_test[0][0].shape)
    
    y_train = to_categorical(y_train, n_classes, dtype ="int32") 
    y_test = to_categorical(y_test, n_classes, dtype ="int32") 
    print(y_test.shape)
    print(energy_test.shape)

    ## Taken from https://tutorials.one/how-to-use-the-keras-functional-api-for-deep-learning/
    ## The first required Conv2D parameter is the number of filters that the convolutional layer will learn. 
    # first input model
    visible1 = Input(shape=(4,16,1), name="visible1")
    conv11 = Conv2D(32, kernel_size=3, activation='relu', padding = "same", name="conv11")(visible1)
    pool11 = MaxPooling2D(pool_size=(2, 2), name="pool11")(conv11)
    conv12 = Conv2D(64, kernel_size=3, activation='relu', padding = "same", name="conv12")(pool11)
    pool12 = MaxPooling2D(pool_size=(2, 2), name="pool12")(conv12)
    logging.info("cov11.shape {}".format( conv11.shape))
    logging.info("pool1.shape {}".format( pool11.shape))
    logging.info("cov12.shape {}".format( conv12.shape))
    logging.info("pool2.shape {}".format( pool12.shape))
    flat1 = Flatten(name="flat1")(pool12)
    
    
    # second input model
    visible2 = Input(shape=(4,128,1),name="visible2")
    conv21 = Conv2D(32, kernel_size=3, activation='relu', padding = "same",name="conv21")(visible2)
    pool21 = MaxPooling2D(pool_size=(2, 2),name="pool21")(conv21)
    conv22 = Conv2D(64, kernel_size=3, activation='relu', padding = "same",name="conv22")(pool21)
    pool22 = MaxPooling2D(pool_size=(2, 2),name="pool22")(conv22)
    flat2 = Flatten(name="flat2")(pool22)
    logging.info("cov21.shape {}".format( conv21.shape))
    logging.info("poo21.shape {}".format( pool21.shape)) 
    logging.info("cov22.shape {}".format( conv22.shape)) 
    logging.info("poo22.shape {}".format( pool22.shape)) 
   

    # third input model
    visible3 = Input(shape=(16,16,1),name="visible3")
    conv31 = Conv2D(32, kernel_size=3, activation='relu', padding = "same",name="conv31")(visible3)
    pool31 = MaxPooling2D(pool_size=(2, 2),name="pool31")(conv31)
    conv32 = Conv2D(64, kernel_size=3, activation='relu', padding = "same",name="conv32")(pool31)
    pool32 = MaxPooling2D(pool_size=(2, 2),name="pool32")(conv32)
    flat3 = Flatten(name="flat3")(pool32)
    logging.info("cov31.shape {}".format( conv31.shape))
    logging.info("poo31.shape {}".format( pool31.shape))
    logging.info("cov32.shape {}".format( conv32.shape))
    logging.info("poo32.shape {}".format( pool32.shape))

    # forth input model
    visible4 = Input(shape=(16,8,1),name="visible4")
    conv41 = Conv2D(32, kernel_size=3, activation='relu', padding = "same",name="conv41")(visible4)
    pool41 = MaxPooling2D(pool_size=(2, 2),name="pool41")(conv41)
    conv42 = Conv2D(64, kernel_size=3, activation='relu', padding = "same",name="conv42")(pool41)
    pool42 = MaxPooling2D(pool_size=(2, 2),name="pool42")(conv42)
    flat4 = Flatten(name="flat4")(pool42)
    logging.info("cov41.shape {}".format( conv41.shape))
    logging.info("poo41.shape {}".format( pool41.shape))
    logging.info("cov42.shape {}".format( conv42.shape))
    logging.info("poo42.shape {}".format( pool42.shape))


    # merge input models
    merge = Concatenate(name="concatenate")([flat1, flat2, flat3, flat4])
    
    
    # interpretation model
    # adding fully connected layers
    hidden1 = Dense(32, activation='relu',name="hidden1")(merge)
    hidden2 = Dense(32, activation='relu',name="hidden2")(hidden1)
    # output layer -> n_classes Neurons for n_classes different classes 
    output = Dense(n_classes, activation='softmax',name="output")(hidden2)
    cnn = Model(inputs= [visible1, visible2, visible3, visible4], outputs=output)

    cnn.compile(loss="categorical_crossentropy", optimizer='adam', metrics=['acc'])
    #cnn.compile(loss="categorical_crossentropy", optimizer=RMSprop(lr=1e-4), metrics=['acc'])
    # summarize layers
    print(cnn.summary())
    # plot graph
    #plot_model(cnn, to_file='cnn_multiple_inputs.png')
  
    print("start fit\n")
    #epoch = 5
    #history = cnn.fit(X_train, y_train,  epochs=5, batch_size=100, validation_split =test_split)
    history = cnn.fit(X_train, y_train,  epochs=5, batch_size=100, validation_data =(X_test, y_test))
    y_pred = cnn.predict(X_test, batch_size=100)
    y_pred = np.argmax(y_pred, axis=1)
    y_test = np.argmax(y_test, axis=1)
    print("y_pred", y_pred.shape) 
    print("y_test", y_test.shape) 
    print("y_test[0], energy_test[0]", y_test[0], energy_test[0]) 
    print("y_test[1], energy_test[1]", y_test[1], energy_test[1]) 
    print("y_test[2], energy_test[2]", y_test[2], energy_test[2]) 
    #log_confusion_matrix(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred, normalize = 'true')
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                          #display_labels=["Signal", "bg0", "bg1"])
                          display_labels=["{}".format(sigLabel), "{}".format(bg0Label), "{}".format(bg1Label)])
    disp.plot(cmap="Blues", values_format='.4f')
    plt.yticks(rotation=90)
    plt.tight_layout()
    #plt.title('Confusion matrix ')
    print("Generating {}ConfusionMatrix.pdf".format(path))
    plt.savefig(path+"ConfusionMatrix.pdf")


    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(acc))
    fig=plt.figure(figsize=(8,6))
    fig.patch.set_color('white')
    plt.plot(epochs, acc, 'r', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend()
    print("Generating {}cnn_acc.pdf".format(path))
    plt.savefig(path + "cnn_acc.pdf")
    
    fig=plt.figure(figsize=(8,6))
    fig.patch.set_color('white')
    plt.plot(epochs, loss, 'r', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend()
    print("Generating {}cnn_loss.pdf".format(path))
    plt.savefig(path + "cnn_loss.pdf")


    #plot efficiency
    sigEff = ROOT.TEfficiency("Signal efficiency", "", 10, 40, 250)
    bkg0Eff = ROOT.TEfficiency("Bkg0 efficiency", "", 10, 40, 250)
    bkg1Eff = ROOT.TEfficiency("Bkg1 efficiency", "", 10, 40, 250)

    #sigEff.SetTitle("%s;E_{a} [GeV];Efficiency"%("Unbinned training"));
    if "axion" in tag:
        sigEff.SetTitle(";E_{a} [GeV];Efficiency");
        bkg0Eff.SetTitle(";E_{a} [GeV];");
    elif "scalar" in tag:
        sigEff.SetTitle(";E_{s} [GeV];Efficiency");
        bkg0Eff.SetTitle(";E_{s} [GeV];");


    for j in range(len(energy_test)):
        if y_test[j] ==0 :
            if y_pred[j] == 0:
                sigEff.Fill(True, energy_test[j]/1000.)
            else:
                sigEff.Fill(False, energy_test[j]/1000.)
        if y_test[j] ==1 :
            if y_pred[j] == 0:
                bkg0Eff.Fill(True, energy_test[j]/1000.)
            else:
                bkg0Eff.Fill(False, energy_test[j]/1000.)
        if y_test[j] ==2 :
            if y_pred[j] == 0:
                bkg1Eff.Fill(True, energy_test[j]/1000.)
            else:
                bkg1Eff.Fill(False, energy_test[j]/1000.)

    plot_eff(tag, sigEff, bkg0Eff, bkg1Eff, path, "eff")
    save_eff(sigEff, bkg0Eff, bkg1Eff, path+ "eff_" +  "sig.txt", path+ "eff_" + "gamma.txt", path+ "eff_" + "pi0.txt")
    
    return



def plot_eff(output, sigEff, bkg0Eff, bkg1Eff, savepath, filename, twopanels=True):
    if twopanels:
        ROOT.gStyle.SetTitleSize(0.08, "xy");
        ROOT.gStyle.SetLabelSize(0.08, "xy");
        ROOT.gStyle.SetTitleOffset(1.1,"x");
        ROOT.gStyle.SetTitleOffset(0.8, "y");
        ROOT.gStyle.SetPadLeftMargin(0.2);

    sigEff.SetFillStyle(3004);
    sigEff.SetFillColor(ROOT.kRed);
    sigEff.SetMarkerColor(ROOT.kRed);
    sigEff.SetLineColor(ROOT.kRed);
    sigEff.SetMarkerStyle(20);

    bkg0Eff.SetFillStyle(3005);
    bkg0Eff.SetFillColor(ROOT.kBlue);
    bkg0Eff.SetMarkerColor(ROOT.kBlue);
    bkg0Eff.SetLineColor(ROOT.kBlue);
    bkg0Eff.SetMarkerStyle(20);

    bkg1Eff.SetFillStyle(3005);
    bkg1Eff.SetFillColor(ROOT.kGreen);
    bkg1Eff.SetMarkerColor(ROOT.kGreen);
    bkg1Eff.SetLineColor(ROOT.kGreen);
    bkg1Eff.SetMarkerStyle(20);


    canvas = ROOT.TCanvas(filename, "", 700, 600)
    tpad = ROOT.TPad(filename+"tpad", "", 0, 0.5, 1, 1.0)
    bpad = ROOT.TPad(filename+"bpad", "", 0, 0.05, 1, 0.5)
    tpad.SetTopMargin(0.1);
    tpad.SetBottomMargin(0.00);
    bpad.SetTopMargin(0.0);
    bpad.SetBottomMargin(0.2);

    canvas.SetFillStyle(1001);
    canvas.cd()
    tpad.Draw()
    bpad.Draw()
    
    tpad.cd()
    sigEff.Draw("")
    ROOT.gPad.Update();
    graph = sigEff.GetPaintedGraph();
    graph.SetMinimum(0.89);
    graph.SetMaximum(1.15);

    x0=0.7
    x1=0.95
    y0=0.75
    y1=0.9
    if twopanels:
        x0=0.5
        x1=0.85
        y0=0.55
        y1=0.9
    leg = ROOT.TLegend(x0, y0, x1, y1)

    if "axion1" in output:
        leg.AddEntry(sigEff, "a#rightarrow #gamma #gamma","APL");
    elif "axion2" in output:
        #leg.AddEntry(sigEff, "a#rightarrow 3#pi^{0} #rightarrow 6#gamma","APL");
        leg.AddEntry(sigEff, "a#rightarrow 3#pi^{0}","APL");
    elif "scalar1" in output:
        #leg.AddEntry(sigEff, "s#rightarrow #pi^{0}#pi^{0} #rightarrow 4#gamma","APL");
        leg.AddEntry(sigEff, "s#rightarrow #pi^{0}#pi^{0}","APL");
    leg.AddEntry(bkg0Eff, "#gamma","APL");
    leg.AddEntry(bkg1Eff, "#pi^{0}","APL");
    leg.SetLineStyle(0);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);
    leg.Draw();

    bpad.cd()
    bkg0Eff.Draw("")
    bkg1Eff.Draw("same")
    ROOT.gPad.Update();
    graph = bkg0Eff.GetPaintedGraph();
    graph.SetMinimum(0);
    graph.SetMaximum(0.0599); #1.3
    bpad.Update();
    #ROOT.gPad.SetLogy();

    canvas.Update()
    canvas.Show()

    canvas.SaveAs("{}{}.pdf".format(savepath,filename))


def save_eff(sigEff, bkg0Eff, bkg1Eff, sigEff_file, bkg0Eff_file, bkg1Eff_file, nbins  = 10, lowEdge = 40, binwidth=21):
    print("The efficiency has ", nbins, " bins")

    fsig = open(sigEff_file, 'w')
    fbkg0 = open(bkg0Eff_file, 'w')
    fbkg1 = open(bkg1Eff_file, 'w')
    fsig.write('EnergyRangeLow, EnergyRangeUp, Eff, EffErrLow, EffErrUp\n')
    fbkg0.write('EnergyRangeLow, EnergyRangeUp, Eff, EffErrLow, EffErrUp\n')
    fbkg1.write('EnergyRangeLow, EnergyRangeUp, Eff, EffErrLow, EffErrUp\n')
    for i in range(nbins):
        eneLow = lowEdge + i*binwidth
        eneUp = eneLow + binwidth
        sigEffNom = sigEff.GetEfficiency(i+1)
        sigEffErrLow = sigEff.GetEfficiencyErrorLow(i+1)
        sigEffErrUp = sigEff.GetEfficiencyErrorUp(i+1)

        bkg0EffNom = bkg0Eff.GetEfficiency(i+1)
        bkg0EffErrLow = bkg0Eff.GetEfficiencyErrorLow(i+1)
        bkg0EffErrUp = bkg0Eff.GetEfficiencyErrorUp(i+1)

        bkg1EffNom = bkg1Eff.GetEfficiency(i+1)
        bkg1EffErrLow = bkg1Eff.GetEfficiencyErrorLow(i+1)
        bkg1EffErrUp = bkg1Eff.GetEfficiencyErrorUp(i+1)

        fsig.write("{:.1f}, {:.1f}, {:.3f}, {:.3f}, {:.3f}\n".format(eneLow, eneUp, sigEffNom, sigEffErrLow, sigEffErrUp))
        fbkg0.write("{:.1f}, {:.1f}, {:.3f}, {:.3f}, {:.3f}\n".format(eneLow, eneUp, bkg0EffNom, bkg0EffErrLow, bkg0EffErrUp))
        fbkg1.write("{:.1f}, {:.1f}, {:.3f}, {:.3f}, {:.3f}\n".format(eneLow, eneUp, bkg1EffNom, bkg1EffErrLow, bkg1EffErrUp))





def plot_confusion_matrix(cm, class_names):
    """
    Returns a matplotlib figure containing the plotted confusion matrix.

    Args:
       cm (array, shape = [n, n]): a confusion matrix of integer classes
       class_names (array, shape = [n]): String names of the integer classes
    """

    figure = plt.figure(figsize=(8, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    #plt.title("Confusion matrix")
    plt.colorbar()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=45)
    plt.yticks(tick_marks, class_names)

    # Normalize the confusion matrix.
    cm = np.around(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], decimals=2)

    # Use white text if squares are dark; otherwise black.
    threshold = cm.max() / 2.

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        color = "white" if cm[i, j] > threshold else "black"
        plt.text(j, i, cm[i, j], horizontalalignment="center", color=color)

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return figure

def log_confusion_matrix(y_test, y_pred):

    # Use the model to predict the values from the test_images.

    # Calculate the confusion matrix using sklearn.metrics
    cm = confusion_matrix(y_test, y_pred)

    figure = plot_confusion_matrix(cm, class_names = ["Signal", "Bg0", "Bg1"])
    cm_image = plot_to_image(figure)

    # Log the confusion matrix as an image summary.
    tf.summary.image("Confusion Matrix", cm_image, step=epoch)


if __name__ == '__main__':
	print('start')
	main()
