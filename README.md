Domácí úkoly
------------
Domácí úkol 1 (6 bodů) | měkký deadline: 12. 4. 2020
Domácí úkol 2 (6 bodů) | měkký deadline: 26. 4. 2020
Domácí úkol 3 (6 bodů) | měkký deadline: 10. 5. 2020
Domácí úkol 4 (6 bodů) | měkký deadline: 17. 5. 2020

tvrdý deadline: 24. 5. 2020

Pokyny pro vypracování
----------------------
+ Utvořte skupiny po nejvýše třech (pokud vám to situace dovolí). 
+ Ze své skupiny vyberte reprezentanta.
+ Úlohu odevzdejte ve formě zprávy ve formátu PDF emailem cvičícímu, ke kterému přísluší reprezentant.
+ Zpráva nechť obsahuje řešení zadaných úkolů spolu s vysvětlením vašeho postupu, grafy, diskusí výsledků a klíčovými částmi kódu.
+ Není potřeba vytvářet funkční softwareový prototyp. Dbejte na to, aby zpráva obsahovala postup i výsledky, ne jen funkci, jejímž spouštěním výsledek dostaneme.
+ Pokud chcete, můžete se rozhodnout některé z úkolů nevypracovat a získat za ně nula bodů. Tuto skutečnost indikujte.
+ Tvrdý dead-line pro vypracování všech úkolů je 24. 5. 2020.
+ Každý úkol má svůj měkký deadline, pokud odevzdáte před tímto dead-linenem, bude váš úkol opraven přednostně a dostanete možnost odevzdat opravený úkol na základě připomínek cvičícího

Parametry úlohy spočtěte následovně:
------------------------------------
K = den narození reprezentanta skupiny (1-31),
L = počet písmen v příjmení reprezentanta,
X = ((K*L*23) mod (20)) + 1,
Y = ((X + ((K*5 + L*7) mod (19))) mod (20)) + 1.
Z archivu hw1-source.zip vezměte datový soubor č. 1 s názvem xxx.txt a datový soubor č. 2 s názvem yyy.txt, kde

xxx je X doplněné zepředu symbolem 0 na trojciferné číslo. Tj. pro X = 5 je xxx = 005.
yyy je Y doplněné zepředu symbolem 0 na trojciferné číslo.
Každý z datových souborů reprezentuje prvních cca 1000 slov nějaké anglické knihy. V prvním řádku se vždy nachází informace o knize a autorovi. Ve druhém řádku je potom samotný text, který je již předzpracován do tvaru přímo použitelného pro požadovanou analýzu.

Poznámky
--------
Úlohy můžete řešit v libovolném softwaru umožnujícím provádět potřebné výpočty. Testové statistiky můžete počítat ručně nebo s využitím statistických balíčků a funkcí.
Vždy je potřeba vysvětlit postup a výsledek řádně interpretovat.

Software
--------
Vhodný je např. Python[1] (+scipy stats), R, Mathematica, Matlab, Excel atd.


Úkol 1
======
(1b) Z obou datových souborů načtěte texty k analýze. Pro každý text zvlášť odhadněte pravděpodobnosti znaků (symbolů včetně mezery), které se v textech vyskytují. Výsledné pravděpodobnosti graficky znázorněte.
(1b) Pro každý text zvlášť spočtěte entropii odhadnutého rozdělení znaků.
(2b) Nalezněte optimální instantní kód CC pro kódování znaků jednoho z textů.
(2b) Pro každý text zvlášť spočtěte střední délku kódu CC a porovnejte ji s entropií rozdělení znaků.

Úkol 2
======
(1b) Z obou datových souborů načtěte texty k analýze. Pro každý text zvlášť odhadněte základní charakteristiky délek slov, tj. střední hodnotu a rozptyl. Graficky znázorněte rozdělení délek slov.
(1b) Pro každý text zvlášť odhadněte pravděpodobnosti písmen (symbolů mimo mezery), které se v textech vyskytují. Výsledné pravděpodobnosti graficky znázorněte.
(1.5b) Na hladině významnosti 5% otestujte hypotézu, že rozdělení délek slov nezávisí na tom, o který jde text. Určete také p-hodnotu testu.
(1.5b) Na hladině významnosti 5% otestujte hypotézu, že se střední délky slov v obou textech rovnají. Určete také p-hodnotu testu.
(1b) Na hladině významnosti 5% otestujte hypotézu, že rozdělení písmen nezávisí na tom, o který jde text. Určete také p-hodnotu testu.
Nápověda k bodům 3 a 5: Proveďte test nezávislosti v kontingenční tabulce.

Úkol 3
======
(1b) Z jednoho datového souboru načtěte text k analýze. Odhadněte pravděpodobnosti písmen (včetně mezer), které se v textu vyskytují. Takto získané empirické rozdělení graficky znázorněte. Pro další body předpokládejme, že je text vygenerován z homogenního markovského řetězce s diskrétním časem.
(1.5b) Za tohoto předpokladu odhadněte matici přechodu. Pro odhad matice přechodu vizte přednášku 17.
(2b) Na základě matice z předchozího bodu najděte stacionární rozdělení tohoto řetězce.
(1.5b) Porovnejte stacionární rozdělení se získaným empirickým rozdělením. Tj. na hladině 5% otestujte hypotézu, že se empirické rozdělení z bodu 1 rovná stacionárnímu rozdělení.

Úkol 4
======
M∣G∣∞, \lambda = 10~\mathrm{s}^{-1}λ=10 s −1 S\sim\mathrm{Unif}(0,1)S∼Unif(0,1), N_0 = 0N 0=0
(2b)simulace a zobrazení trajektorie \{N_t \mid t\in(0,10~\mathrm{s})\}{N t∣t∈(0,10 s)}
(2b)simulace $N = 1000$ nezávislých trajektorií pro t\in(0,1000)t∈(0,1000), odhad rozdělení N_1000N 1 000
(2b)grafické(nebo i statistické?) porovnání výsledku s asymptotickým odhadem
