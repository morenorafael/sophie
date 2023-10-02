# Qtile

### repositorio

```sh
git clone git@github.com:morenorafael/sophie.git
```

## Dependencias

```sh
sudo pacman -Syyu
```

```sh
sudo pacman -S pulseaudio-bluetooth bat exa docker docker-compose flameshot bluez bluez-utils nodejs npm neovim python-neovim ttf-ubuntu-mono-nerd ttf-font-awesome zip unzip neofetch zsh git firefox
```

## zsh

```sh
sudo pacman -Syyu
```

```sh
sudo pacman -S zsh
```

### Oh My ZSH

```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### zsh-autosuggestions

```sh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

### ZSH-Syntax-Highlighting

```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

## Docker

```sh
sudo pacman -Syyu
```

```sh
sudo pacman -S docker docker-compose
```

```sh
sudo systemctl start docker.service
```

```sh
sudo systemctl enable docker.service
```

```sh
sudo usermod -aG docker $USER
```

## Bluetooth

```sh
sudo pacman -S bluez bluez-utils pulseaudio-bluetooth
```

```sh
pulseaudio --kill
```

```sh
pulseaudio --start
```

```sh
sudo usermod -aG lp,audio $USER
```
