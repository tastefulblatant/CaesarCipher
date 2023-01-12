import os

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(message, shift_number):
    shifted_text = ""
    for one_letter in message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index + shift_number
            shifted_text += alphabet[new_index]
        else:
            shifted_text += one_letter
    print(f"Tvoje sifrovana zprava je: {shifted_text}")

def decode(encrypted_message, shift_number):
    decrypted_text = ""
    for one_letter in encrypted_message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index - shift_number
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += one_letter
    print(f"Tvoje desifrovana zprava je: {decrypted_text}")
while True:
    choice = input("Napiste 'zakodovat' pro zakodovani zpravy.\nNapiste 'odkodovat' pro odkodovani zpravy\n")
    
    text = input("Napiste svou zpravu: \n").lower()
    shift = int(input("Napiste cislo posunu. "))
    if choice == "zakodovat":
        encode(text, shift)
    elif choice == "odkodovat":
        decode(text, shift)
    continue_w = input("Chcete pokracovat?\n")
    if continue_w in("no","ne"):
        break
    elif continue_w in("ano","jo","yes"):
        continue
        


