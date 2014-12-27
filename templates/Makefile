# Rappels sur les Makefile
#   $@ : Le nom de la cible
#   $< : Le nom de la première dépendance
#   $^ : La liste des dépendances
#   $? : La liste des dépendances plus récentes que la cible
#   $* : Le nom du fichier sans suffixe
#
# Syntaxe :
#   cible: dépendance1, dépendance2, ..., dépendanceN
#   [tab]commande1
#   [tab]commande2
#   [tab]@commande3
#
# .PHONY : Les dépendances seront systématiquement reconstruites
#

CC = gcc
CFLAGS = -W -Wall -ansi -pedantic
EXEC = hello

all: $(EXEC)

hello: hello.cpp hello.hpp
	$(CC) $< -o $@ $(CFLAGS)

clean:
	rm *.o

mrproper: clean
	rm $(EXEC)

.PHONY: clean mrproper
