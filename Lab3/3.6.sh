#!/bin/bash
grep -iE "^[aeiouy]?([qwrtpsdfghjklzxcvbnm][aeiouy])+[qwrtpsdfghjklzxcvbnm]?$" /usr/share/dict/words
