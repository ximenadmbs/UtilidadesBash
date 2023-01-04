#!/bin/bash

#neofetch

echo "Cargando la barra desde Python"

#Cargando la barra desde Python
    #python3 $HOME/Documentos/UtilidadesBash/PythonUtilidades/barraProgreso1.py

#barra de progreso aplicando a un archivo para comprimir en zip:
    pv December.tar.xz | zip > $HOME/Vídeos/December.zip

    #pv December.tar.xz | tar -Jxvf December.tar.xz -C $HOME/Vídeos/
echo "OK"
