#!/bin/bash
h="650" #allow for pallete opening without need to resize 
t=`yad --title="Title Color" --color --palette --init-color="#757575" --height=$h | tr -d "#"`
s=`yad --title="Section Color" --color --palette --init-color="#397249" --height=$h | tr -d "#"`
r=`yad --title="Rule Color" --color --palette --init-color="#9cb770" --height=$h | tr -d "#"`
styleIn="style_chmduquesne.m.tex"
styleOut="withcolors.tex"

sed -e "s/%%titleC%%/${t}/g" -e "s/%%sectionC%%/${s}/g" -e "s/%%ruleC%%/${r}/g" $styleIn > $styleOut

