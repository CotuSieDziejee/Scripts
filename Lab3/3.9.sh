#!/bin/bash
grep -ie "^[a].*[a]$" -e "^[e].*[e]$" -e "^[i].*[i]$" -e "^[u].*[u]$" -e "^[o].*[o]$" -e "^[y].*[y]$" /usr/share/dict/words
