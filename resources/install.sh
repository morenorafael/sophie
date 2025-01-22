#!/bin/bash

sudo pacman -S --noconfirm xcb-util-cursor

echo "Instalando el cursor...\n"
tar -xf Breeze.tar.tar
sudo mv Breeze /usr/share/icons

echo "Instalando el tema...\n"
tar -xf Nordic.tar.xz
sudo mv Nordic /usr/share/themes

echo "Instalando los iconos...\n"
tar -xf Zafiro-Nord-Dark-Black.tar.xz
sudo mv Zafiro-Nord-Dark-Black /usr/share/icons