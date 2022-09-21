# Legacy crypto algorithms

List of my realisations of some legacy crypto algorithms created on Python.

## Table of Contents

-   [General info](#general-info)
-   [Technologies](#technologies)
-   [Project Setup](#project-setup)
-   [Example of work](#example-of-work)
    -   [Caesar cipher](#caesar-cipher)
    -   [Gronsfeld cihper](#gronsfeld-cihper)
    -   [Playfair cipher](#playfair-cipher)
    -   [Polybius Square cipher](#polybius-square-cipher)
    -   [Transposition cipher](#transposition-cipher)
    -   [Vernam cipher](#vernam-cipher)
    -   [Visioner cipher](#visioner-cipher)

## General info

The repository contains such algorithms as:

-   [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
-   [Gronsfeld cihper](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Gronsfeld_cipher)
-   [Playfair cipher](https://en.wikipedia.org/wiki/Playfair_cipher)
-   [Polybius Square cipher (vertical and horizontal)](https://en.wikipedia.org/wiki/Polybius_square)
-   [Transposition cipher (vertical and horizontal)](https://en.wikipedia.org/wiki/Transposition_cipher)
-   [Vernam cipher](https://en.wikipedia.org/wiki/Gilbert_Vernam#The_Vernam_cipher)
-   [Visioner cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

Algorithms that need a default alphabet support two languages - Russian and English.

## Technologies

### Core

-   Python version: 3.9.6

### Libraries

-   numpy version: 1.23.3

## Project Setup

To run some script apply following command, for example running of Playfair cipher:

```bash
python playfair.py
```

## Example of work

The examples of work of the algorithms are represented below.

### Caesar cipher

**Usage**

```python
caesar_en = Caesar('en', 5)
caesar_ru = Caesar('ru', 5)

print('Encoded en:', caesar_en.encode('HELLO WORLD'))
print('Decoded en:', caesar_en.decode('MJQQT BTWQI'))

print('Encoded ru:', caesar_ru.encode('ПРИВЕТ МИР'))
print('Decoded ru:', caesar_ru.decode('ФХНЗКЧ СНХ'))
```

**Result**

```bash
Encoded en: MJQQT BTWQI
Decoded en: HELLO WORLD
Encoded ru: ФХНЗКЧ СНХ
Decoded ru: ПРИВЕТ МИР
```

### Gronsfeld cihper

**Usage**

```python
gronsfeld_en = Gronsfeld('en')
gronsfeld_ru = Gronsfeld('ru')

print('Encoded en:', gronsfeld_en.encode('HELLO WORLD', 1234))
print('Decoded en:', gronsfeld_en.decode('IGOPP ZSSNG', 1234))

print('Encoded ru:', gronsfeld_ru.encode('ПРИВЕТ МИР', 1234))
print('Decoded ru:', gronsfeld_ru.decode('РТЛЖЖФ РЙТ', 1234))
```

**Result**

```bash
Encoded en: IGOPP ZSSNG
Decoded en: HELLO WORLD
Encoded ru: РТЛЖЖФ РЙТ
Decoded ru: ПРИВЕТ МИР
```

### Playfair cipher

**Usage**

```python
playfair_en = Playfair('en')
playfair_ru = Playfair('ru')

print('Encoded en:', playfair_en.encode('IDIOCYOFTENLOOKSLIKEINTELLIGENCE', 'WHEATSON'))
print('Decoded en:', playfair_en.decode('KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE', 'WHEATSON'))

print('Encoded ru:', playfair_ru.encode('ПРИВЕТМИР', 'КЛАД'))
print('Decoded ru:', playfair_ru.decode('РСМБМОГМПЦ', 'КЛАД'))
```

**Result**

```bash
Encoded en: KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE
Decoded en: IDIOCYOFTENLOXOKSLIKEINTELLIGENCEX
Encoded ru: РСМБМОГМПЦ
Decoded ru: ПРИВЕТМИРХ
```

### Polybius Square cipher

**Usage**

```python
polybius_en_vertical = PolybiusSquare('en')
polybius_en_horizontal = PolybiusSquare('en', horizontal=True)

polybius_ru_vertical = PolybiusSquare('ru')
polybius_ru_horizontal = PolybiusSquare('ru', horizontal=True)

print('Encoded vertically en:',polybius_en_vertical.encode('HELLO WORLD'))
print('Decoded vertically en:',polybius_en_vertical.decode('NKQQT BTWQI'))

print('Encoded horizontally en:',polybius_en_horizontal.encode('HELLO WORLD'))
print('Decoded horizontally en:',polybius_en_horizontal.decode('IAMMP XPSME'))

print('Encoded vertically ru:',polybius_ru_vertical.encode('ПРИВЕТ МИР'))
print('Decoded vertically ru:',polybius_ru_vertical.decode('ХЦПИМШ ТПЦ'))

print('Encoded horizontally ru:',polybius_ru_horizontal.encode('ПРИВЕТ МИР'))
print('Decoded horizontally ru:',polybius_ru_horizontal.decode('РСКГАН ЖКС'))
```

**Result**

```bash
Encoded vertically en: NKQQT BTWQI
Decoded vertically en: HELLO WORLD
Encoded horizontally en: IAMMP XPSME
Decoded horizontally en: HELLO WORLD
Encoded vertically ru: ХЦПИМШ ТПЦ
Decoded vertically ru: ПРИВЕТ МИР
Encoded horizontally ru: РСКГАН ЖКС
Decoded horizontally ru: ПРИВЕТ МИР
```

### Transposition cipher

**Usage**

```python
transposition_horizontal = TranspositionCipher()
print('Encoded horizontally:', end=' ')
print(repr(transposition_horizontal.encode('WHAT THE BUATIFUL WORLD AROUND US', 'SUN')))
print('Decoded horizontally:', end=' ')
print(repr(transposition_horizontal.decode('DWA HTAAIRTFO UUTLNH DEW  OUBRSUL', 'SUN')))

transposition_vertical = TranspositionCipher(vertical=True)
print('Encoded vertically:', end=' ')
print(repr(transposition_vertical.encode('WHAT THE BUATIFUL WORLD AROUND US', 'SUN')))
print('Decoded vertically:', end=' ')
print(repr(transposition_vertical.decode('AT AF R ODSWTHBTUWLAU H EUILODRNU', 'SUN')))
```

**Result**

```bash
Encoded horizontally: 'DWA HTAAIRTFO UUTLNH DEW  OUBRSUL'
Decoded horizontally: 'WHAT THE BUATIFUL WORLD AROUND US'
Encoded vertically: 'AT AF R ODSWTHBTUWLAU H EUILODRNU'
Decoded vertically: 'WHAT THE BUATIFUL WORLD AROUND US'
```

### Vernam cipher

**Usage**

```python
print('Encoded:', Vernam.encode('Hello world', 'sun'))
print('Decoded:', Vernam.decode('3b10021f1a4e041a1c1f11', 'sun'))
```

**Result**

```bash
Encoded: 3b10021f1a4e041a1c1f11
Decoded: Hello world
```

### Visioner cipher

**Usage**

```python
visioner_en = Visioner('en')
print('Encoded en:', end=' ')
print(visioner_en.encode('WHAT THE BUATIFUL WORLD AROUND US', 'SUN'))
print('Decoded en:', end=' ')
print(visioner_en.decode('OBNL GZY TONLCSMF OIEDX SLBMHQ OF', 'SUN'))

visioner_ru = Visioner('ru')
print('Encoded ru:', end=' ')
print(visioner_ru.encode('ЧТО ЗА ЗАМЕЧАТЕЛЬНЫЙ МИР ВОКРУГ НАС', 'СОЛНЦЕ'))
print('Decoded ru:', end=' ')
print(visioner_ru.decode('ИБЪ ЮЕ ЦЛЪЫЬСБРЩТТМШ ЪЯХ РЪШЖШФ ЩНЗ', 'СОЛНЦЕ'))
```

**Result**

```bash
Encoded en: OBNL GZY TONLCSMF OIEDX SLBMHQ OF
Decoded en: WHAT THE BUATIFUL WORLD AROUND US
Encoded ru: ИБЪ ЮЕ ЦЛЪЫЬСБРЩТТМШ ЪЯХ РЪШЖШФ ЩНЗ
Decoded ru: ЧТО ЗА ЗАМЕЧАТЕЛЬНЫЙ МИР ВОКРУГ НАС
```
