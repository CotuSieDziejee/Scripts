#!/bin/bash
grep -e "\(.o\)\{4,\}" -e "\(o.\)\{4,\}" -e "\(.o.\)\{4,\}" /usr/share/dict/words

