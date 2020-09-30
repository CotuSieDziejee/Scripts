#!/bin/bash

awk '$1=="for"    {++ilosc} END { print "for: "   ilosc }' plik.cpp
awk '$1=="while"  {++ilosc} END { print "while: " ilosc }' plik.cpp
awk '$1=="until"  {++ilosc} END { print "until: " ilosc }' plik.cpp
