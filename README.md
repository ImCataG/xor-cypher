# xor-cypher
To encrypt:
```
python encrypt.py <secret> <input file> <binary output file>
```

To decrypt:
```
python encrypt.py <output> <secret> <binary input file>
```

# [![forthebadge](https://forthebadge.com/images/badges/it-works-why.svg)](https://forthebadge.com)

A simple explanation can be found on [Wikipedia](https://en.wikipedia.org/wiki/XOR_cipher).

# Error handling
Errors are self-explanatory. You either input a wrong number of arguments or an invalid password/secret.

# Team VS Team

---

Echipa noastra: HMM <br>
Echipa adversa: yoyoboysss <br>
Parola echipei adverse: S (explicatie la output only)

---

# input + output
```
python inandout/getthatpass.py
```
Se citesc fisierele input.txt si output si se afiseaza xor litera din input cu litera din output. Parola va fi repetata pana la finalul fisierului passwd.txt.


# output only
Echipa yoyoboyss xor-eaza fiecare caracter din input cu TOATE caracterele din parola. Astfel, orice parola cu xorsum egal cu xorsumul parolei originale va decripta textul. Deoarece in input se primesc doar litere mari, litere mici si numere, xorsumul parolei va fi intre 0 si 127. 

```
python allxors/crack.py
```

In folderul 'allxors' am generat 128 de fisiere .txt in care am aplicat xor cu toate numerele de la 0 la 127 pe toate caracterele din outputul de la yoyoboyss. 

```
python allxors/convincingfile.py
[83]
```
Am scris un program care sa verifice care dintre fisiere are cele mai multe caractere care pot aparea intr-un text in limba romana fara diacritice.

file83.txt contine inputul original, deci parola originala are xorsum = 83. Deci parola 'S' poate fi folosita la decriptare.

Nota: Desi sunt 128 de fisiere, inputul original poate fi gasit in maxim 32 de incercari de un om.
