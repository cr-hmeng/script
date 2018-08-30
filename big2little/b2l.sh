#!/bin/bash

echo "Usage: ./b2l.sh [DATAFILE]"

DATAFILE=$1

BASE="/fixed_big"
DATA="/data.bin"
CONV="/conv.bin"
PRAM="/conv_param_mpf.bin"
BN_A="/conv_A.bin"
BN_B="/conv_B.bin"
BN0="/bn0.bin"
BIAS="/conv_param_1.bin"
RELU="/relu0.bin"
POOL="/pool0.bin"
SCPA0="/sc_param_0.bin"
SCPA1="/sc_param_1.bin"
SC0="/sc0.bin"
SC1="/sc1.bin"

if [ -e $DATAFILE$BASE$DATA ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$DATA $DATAFILE$DATA
    echo " "
else
   echo " not found data.bin"
fi

if [ -e $DATAFILE$BASE$CONV ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$CONV $DATAFILE$CONV
    echo " "
else
   echo " not found conv.bin"
fi

if [ -e $DATAFILE$BASE$PRAM ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$PRAM $DATAFILE$PRAM
    echo " "
else
   echo " not found conv_param_mpf.bin"
fi

if [ -e $DATAFILE$BASE$BIAS ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$BIAS $DATAFILE$BIAS
    echo " "
else
   echo " not found conv_param_1.bin"
fi

if [ -e $DATAFILE$BASE$RELU ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$RELU $DATAFILE$RELU
    echo " "
else
   echo " not found relu0.bin"
fi

if [ -e $DATAFILE$BASE$POOL ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$POOL $DATAFILE$POOL
    echo " "
else
   echo " not found pool0.bin"
fi

if [ -e $DATAFILE$BASE$SCPA0 ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$SCPA0 $DATAFILE$SCPA0
    echo " "
else
   echo " not found sc_param_0.bin"
fi

if [ -e $DATAFILE$BASE$SCPA1 ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$SCPA1 $DATAFILE$SCPA1
    echo " "
else
   echo " not found sc_param_1.bin"
fi

if [ -e $DATAFILE$BASE$SC0 ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$SC0 $DATAFILE$SC0
    echo " "
else
   echo " not found sc0.bin"
fi

if [ -e $DATAFILE$BASE$SC1 ]; #if has ./report
then
   python b2l.py $DATAFILE$BASE$SC1 $DATAFILE$SC1
    echo " "
else
   echo " not found sc1.bin"
fi


