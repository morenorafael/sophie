#!/bin/bash

# Instalar zsh
sudo pacman -S --noconfirm git
sudo pacman -S --noconfirm zsh

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

rm ~/.zshrc
ln -s ~/sophie/.zshrc ~/.zshrc

echo "Se instalo zsh"


# Instalar dunst
sudo pacman -S --noconfirm dunst

ln -s ~/sophie/.config/dunst ~/.config/dunst

echo "Se instalo dunst"


# Instalar picom
sudo pacman -S --noconfirm picom

ln -s ~/sophie/.config/picom ~/.config/picom
picom -b --config ~/.config/picom/picom.conf

echo "Se instalo picom"