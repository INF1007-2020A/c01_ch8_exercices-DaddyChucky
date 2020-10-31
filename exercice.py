#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import csv
import json

# TODO: Définissez vos fonction ici
def sameFiles(file_numba_1, file_numba_2):
    with open(file_numba_1) as f1, open(file_numba_2) as f2:
        lines1 = f1.readlines()
        for line2 in f2.readlines():
            if line2 in lines1:
                return "Files are different."

        return "Files are the same."

def tripleSpace(file_numba_1, file_dump):
    with open(file_numba_1) as f1, open(file_dump, "w") as fd:
        content = f1.read()
        content = content.replace(" ", "   ")
        fd.write(content)
        return file_numba_1 + " spaces got replaced by 3 spaces and content was dumped in " + file_dump

def notesDump(notes, notes_dump):

    with open(notes) as f:
        glob = f.readlines()

    with open(notes_dump, "w") as dump:
        for elem in glob:
            note = int(elem[:2])

            if note > 80:
                note = "B+"
            elif note > 70:
                note = "C+"
            else:
                note = "D"

            dump.write(note + "\n")

def recettes(recettepath):

    choix = input("Souhaitez-vous lire les recettes ou en ajouter ? (lire/ecrire)\n")
    with open(recettepath, "r") as f:
        try:
            data = json.load(f)
        except:
            with open(recettepath, "w") as f:

                reset= {
                "ingredients": [
                        ["sucre, pommes, cannelle, lait, farine"],
                        ["lait, creme"]
                ],
                "recettes": [
                        "Tarte aux pommes",
                        "Tarte au sucre"
                ]
                 }
                json.dump(reset, f)
            data = reset
        if choix == "lire":

            for recette in range(len(data['recettes'])):
                print(f"-=-=-=-=-\nRecette: {data['recettes'][recette]}\nIngrédients: {data['ingredients'][recette]}\n-=-=-=-=-\n")
        else:
            with open(recettepath, "w") as f:
                recettes = data['recettes']
                ingredients = data['ingredients']

                while True:
                    ajouter_recette = input("Écriver une recette à ajouter (exit quand terminé)\n")

                    if ajouter_recette != "exit":
                        recettes.append(ajouter_recette)

                        ajouter_ingredient = None
                        ingr = []
                        while ajouter_ingredient != "exit":
                            ingr.append(ajouter_ingredient)
                            ajouter_ingredient = input("Ajouter des ingredients a cette recette. (tapez exit quand terminé)\n")

                        ingredients.append(ingr)
                    else:
                        break

                json.dump(data, f, indent=4)


def retounerNombre(exemple):
    with open(exemple, "r+") as f:
        data = f.read()
        num_list = []
        cur_num = ""
        for s in data:
            if s.isdigit():
                cur_num += s
            else:
                if cur_num != "":
                    num_list.append(cur_num)
                    cur_num = ""
        f.write("\n\n-=-=-=-\nDump:\n-=-=-=-\n\n")
        for num in num_list:

            f.write(num + "\n")


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    file_numba_1 = "file1.txt"
    file_numba_2 = "file2.txt"
    file_dump = "dump.txt"
    notes = "notes.txt"
    notes_dump = "notesDump.txt"
    recettepath = "recettes.json"
    exemple = "exemple.txt"
    retounerNombre(exemple)