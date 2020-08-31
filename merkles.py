#Código basado en la implementación de https://medium.com/100-days-of-algorithms/day-75-merkles-puzzles-d9f0e8f9c9d0
from os import urandom
from hashlib import sha1
from random import shuffle,choice
print("El numero de puzzles es 2^n")
puzzle_size=int(input("Por favor ingrese el numero n  (de preferencia 16): "))
puzzle_size = 2 ** 16

def merkles_puzzle():
    secrets = [None] * puzzle_size
    puzzles = [None] * puzzle_size

    for i in range(puzzle_size):
        # generate secret
        secrets[i] = urandom(16)

        # pair := secret|index
        pair = secrets[i] + int.to_bytes(i, 4, 'big')
        # plaintext := pair|sha1(pair)
        plaintext = pair + sha1(pair).digest()

        # cipthertext := ENCRYPT(plaintext, key)
        key = urandom(10)
        noise = sha1(key).digest()
        noise += sha1(noise).digest()
        ciphertext = bytes(i ^ j for i, j in zip(plaintext, noise))

        # puzzle := ciphertext|key
        puzzles[i] = ciphertext + key[2:]

    # randomize order
    shuffle(puzzles)

    # return
    return secrets, puzzles

def solve_puzzle(puzzle):
    ciphertext = puzzle[:40]
    key = puzzle[40:]

    for i in range(puzzle_size):
        # guess key
        noise = sha1(int.to_bytes(i, 2, 'big') + key).digest()
        noise += sha1(noise).digest()

        # plaintext := DECRYPT(ciphertext, key)
        plaintext = bytes(i ^ j for i, j in zip(ciphertext, noise))

        # pair|digest := key|index|sha1(pair)
        pair = plaintext[:20]
        digest = plaintext[20:]

        # on match: time, key, index
        if sha1(pair).digest() == digest:
            return i, pair[:16], int.from_bytes(pair[16:], 'big')

print("Alice genera los puzzles y los secretos")
secretos,puzzles=merkles_puzzle()

print("Bob decodifica algun puzzle random")
tiempoBob,secretoBob,indice=solve_puzzle(choice(puzzles))

print("Bob obtuvo el siguiente secreto:",secretoBob,",con el indice:",indice,", en",tiempoBob,"pasos")
print("Con el indice devuelto por bob, alice obtiene el siguiente secreto:",secretos[indice])


