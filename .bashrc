[[ $- != *i* ]] && return
PS1="\[\e[0;32m\]\u@\h \W\[\e[0m\] \$ "

alias clean="sudo pacman -Sc && sudo pacman -R $(pacman -Qtdq)"
alias config='/usr/bin/git --git-dir=~/.dotfiles/ --work-tree=~/'
alias ls="ls -a --color=auto"

export PATH=/usr/local/bin:$PATH
#export PATH=/usr/local/i386elfgcc/bin:$PATH
. "$HOME/.cargo/env"
