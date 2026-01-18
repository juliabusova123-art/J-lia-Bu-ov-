# Inteligentné autíčko s využitím Raspberry Pi 4

**Katolícka univerzita v Ružomberku**
Pedagogická fakulta
Katedra pedagogiky a špeciálnej pedagogiky

**Projekt z predmetu:** Internet vecí

**Autor: **Mgr. Júlia Bušová

**Študijný program:** RŠ informatiky

**Miesto a rok: Ružomberok, 2026

---

## 1 Úvod

Projekt sa zameriava na návrh a realizáciu **inteligentného robotického autíčka**, ktoré je schopné samostatného pohybu v priestore a vyhýbania sa prekážkam pomocou senzorov. Autíčko je postavené na platforme Raspberry Pi 4, ktorá slúži ako hlavná riadiaca jednotka systému.

Riadenie autíčka je realizované pomocou programu napísaného v programovacom jazyku Python, ktorý zabezpečuje spracovanie údajov zo senzorov a ovládanie motorov. Projekt bol vytvorený s využitím súčiastok zo školských zdrojov a slúži ako edukačný príklad praktického využitia IoT a programovania.

---

## 2 Účel projektu

Hlavným účelom projektu je:

- návrh a zostrojenie inteligentného robotického autíčka,
- demonštrácia autonómneho pohybu robota,
- praktické využitie Raspberry Pi 4 v oblasti robotiky,
- rozvoj algoritmického myslenia a programovania v jazyku Python.

Systém je navrhnutý tak, aby:

-  sa dokázal voľne pohybovať v priestore bez zásahu používateľa,
-  pomocou senzorov detekoval prekážky,
-  reagoval na zmeny v okolí úpravou smeru jazdy,
-  slúžil ako názorná pomôcka vo vyučovaní.

---

## 3 Použitý hardvér

Projekt využíva nasledovné hardvérové komponenty:

* **Raspberry Pi 4** – hlavná riadiaca jednotka systému, zabezpečuje:

  - spracovanie údajov zo senzorov,
  - riadenie motorov,
  - vykonávanie riadiaceho algoritmu.

- **Ultrazvukový senzor vzdialenosti (HC-SR04)** – slúži na:

  -  meranie vzdialenosti od prekážok,
  -  detekciu objektov pred autíčkom.

- **DC motory s prevodovkou a kolesami** – umožňujú:

  - pohyb autíčka vpred, vzad,
  - zmenu smeru jazdy.

-  **Motorový driver** – zabezpečuje:

  -  ovládanie motorov pomocou signálov z Raspberry Pi.

-  **Podvozok robota** – mechanická konštrukcia autíčka.

-  **Powerbanka** – slúži ako zdroj napájania Raspberry Pi 4 a umožňuje:

- voľný pohyb autíčka bez nutnosti pripojenia na elektrickú sieť.

Všetky použité súčiastky pochádzajú zo školských zdrojov.

---

## 4 Použitý softvér a nástroje

- Raspberry Pi 4 
- Programovací jazyk Python
- Knižnice pre ovládanie GPIO pinov


---

## 5 Princíp fungovania systému

Po zapnutí je Raspberry Pi 4 napájané pomocou powerbanky, čo umožňuje autonómnu prevádzku zariadenia. Riadiaci program v jazyku Python inicializuje vstupy a výstupy a pripraví senzory a motory na činnosť.

Ultrazvukový senzor v pravidelných intervaloch meria vzdialenosť od prekážok. Namerané údaje sú:

- spracované v programe,
- vyhodnotené pomocou jednoduchého riadiaceho algoritmu.

Ak systém zistí prekážku v menšej ako nastavenej bezpečnej vzdialenosti, autíčko automaticky:

- zastaví pohyb,
- zmení smer jazdy,
- pokračuje v jazde novým smerom.

Tento proces prebieha nepretržite, čím je zabezpečený plynulý a inteligentný pohyb autíčka v priestore.

---

## 6 Záver

Projekt inteligentného autíčka demonštruje praktické využitie platformy Raspberry Pi 4 v oblasti IoT a programovania. Výsledné riešenie je funkčné, prehľadné a vhodné ako učebná pomôcka. Projekt poskytuje priestor na ďalší rozvoj, napríklad rozšírenie o bezdrôtové ovládanie, kamerový modul alebo pokročilejšie algoritmy riadenia.
# Iot-inteligentné-autíčko-rasberry pi 4
