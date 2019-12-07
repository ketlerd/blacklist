#!/bin/bash
$f1="temp.txt"
$f2="temp2.txt"
$f3="temp3.txt"
$result="result.txt"
eval "sed 's/.*;//' $1 > $f1" 
eval "sed 's/.*://' $f1 > $f2"
eval "sed '/Binary file/d' $f2 > $f3"
eval "sed '/[HASH]/d' $f3 > $result"
