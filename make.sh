#!/bin/sh

if [ "$#" -lt 1 ]; then
	echo "Usage: ./make.sh <day> [run]"
	exit 0
fi

if [ ! -e "$1/solution.c" ]; then
	echo "No solution for $1"
	exit 0
fi

CC=gcc
CFLAGS=-Wall
LDFLAGS=`cat $1/LDFLAGS.txt 2> /dev/null`

$CC $CFLAGS $LDFLAGS -o solution_$1 run.c $1/solution.c

if [ "$2" = "run" ]; then
	./solution_$1
fi
