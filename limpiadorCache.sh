#!/bin/bash

#Archivo plantilla para ejecuciones de comandos y direcciones largas para servidores o con terminales sin acceso de corte y pega desde el terminal.
#Generalmente se ejecutara con sudo para permiso de usuiario.
#En Debian11 se tenda que ejecutar sin el comando sudo y ejecuarlo con super usuario su.

echo "----------------------------------------------------"
echo "Se limpiara la cache"
    sudo du -sh  /var/cache/apt

echo "----------------------------------------------------"
echo "Se limpiara la thumbnails"
    sudo du -sh ~/.cache/thumbnails
    rm -rf  ~/.cache/thumbnails/*
#espera 1 segundo
echo "  Despues:"
        sleep 2s
    sudo du -sh ~/.cache/thumbnails

echo "----------------------------------------------------"
echo "Se limpiara el sistema "
echo "----------------------------------------------------"
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove

# mié 01 feb 2023 13:46:22 CST