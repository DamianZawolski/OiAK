# OiAK
Projekt z architektury i organizacji komputerów

Streszczenie artykułu:

1.Wprowadzenie:
Idea Systemu Liczb Resztkowych (RNS) sięga starożytnej chińskiej metody konwersji reszt na liczby, a później została formalizowana przez C.F. Gaussa w XIX wieku. Od czasu pojawienia się komputerów cyfrowych, opublikowano wiele artykułów proponujących efektywne algorytmy implementacji RNS na komputerach.

Główną zaletą RNS jest szybkość i niezawodność obliczeń arytmetycznych [1-3]. Pierwsze zastosowanie RNS miało miejsce w poszukiwaniu liczb pierwszych.

Obecnie implementacje RNS można znaleźć w systemach przeciwlotniczych [4], obliczeniach neuronowych [1], przetwarzaniu sygnałów czasu rzeczywistego (rozpoznawanie wzorców) [5] i kryptografii [6]. Arytmetyka modularna (MA) jest skuteczna przy przetwarzaniu dużych strumieni danych (o wielkości kilkuset lub kilku tysięcy bitów) [7]. Dlatego RNS pozwala znacznie zwiększyć wydajność sprzętu oraz poprawić niezawodność i odporność na zakłócenia w przetwarzaniu sygnałów i transferze danych. W 2005 roku odbyła się konferencja w Rosji z okazji 50. rocznicy wprowadzenia RNS w obliczeniach naukowych [22], na której omówiono kluczową rolę RNS w radarach, transferze danych w samolotach kosmicznych i wojskowych (np. Sukhoi) oraz w innych ważnych technologiach.

W niniejszym artykule przedstawiono efektywne sprzętowe obliczenia kombinacyjne mnożenia modularnego oraz funkcji modulo (X(mod P)) dla dowolnego modułu. Przedstawiono również wyniki eksperymentów i porównano je z narzędziami przemysłowymi.

2.Podstawowa wiedza na temat RNS:

Twierdzenie chińskiego twierdzenia o reszcie [23] stwierdza, że istnieje jednoznaczna odpowiedniość między zbiorem reszt X1, X2, ..., Xn a liczbami od 0 do p1 · p2 · ... · pn −1 = P −1. Ponieważ wartość reprezentowanej liczby jest niezmienna przy dowolnej permutacji reszt, RNS jest systemem liczbowym bez pozycji. Te cechy sprawiają, że RNS jest alternatywnym systemem z własnymi zaletami i wadami w porównaniu z innymi systemami reprezentacji. Z jednej strony pozwala na równoległe obliczenia i tym samym przyspiesza je, z drugiej strony nie pozwala na porównanie dwóch liczb reprezentowanych przez ich reszty i ustalenie, która jest większa bez dodatkowych operacji, takich jak konwersja wsteczna do systemu pozycyjnego.

RNS jest formą równoległego przetwarzania danych, w którym arytmetyka komputerowa jest wykonywana przy użyciu reszt z dzielenia przez wcześniej wybraną bazę względnie pierwszych modułów {p1, p2, ..., pm}. Reszty mają mniejszą liczbę cyfr niż oryginalne liczby, a operacje arytmetyczne na resztach mogą być wykonywane oddzielnie dla każdego modulo z bazy, co prowadzi do szybszego przetwarzania (np. szybsze dodawanie i mnożenie) w porównaniu do innych form równoległego przetwarzania danych. Równoległość osiągana jest poprzez obliczenia na resztach. Reszty (A1, B1, A2, B2, ..., An, Bn) są wynikiem podzielenia wejściowych liczb (A i B) przez s wcześniej wybrany zbiór względnie pierwszych (p1, p2, ..., pn) - modułów, gdzie p1 · p2 · ... · pn = P. Obliczenia w RNS nie są ograniczone do operacji arytmetycznych na dwóch operandach i są odpowiednie dla dowolnej liczby operandów.

Przetwarzanie danych w RNS obejmuje następujące kroki. Najpierw, wejściowe operandy A1, A2, ..., An są konwertowane z reprezentacji pozycyjnej na modularne poprzez obliczenie reszt (lub reszt) względem modułów {p1, p2, ..., pm} (patrz lewy blok na rys. 1); następnie wykonywane są operacje arytmetyczne na resztach operandy dla każdego modulo pi, gdzie i = 1, ..., n (środkowy blok na rys. 1); wreszcie wyniki S1, S2, ..., Sm dla każdego modulo są konwertowane z powrotem z reprezentacji modularnej na pozycyjną S (patrz prawy blok na rys. 1). Konwersja na reprezentację modularną (konwersja bezpośrednia) jest realizowana przez funkcję X(mod P), której wynik jest przekazywany do drugiego kroku operacji. Drugi krok obliczeń w RNS wymaga wykonania modularnej sumy, mnożenia i innych funkcji arytmetycznych takich jak A · B + C. Trzeci krok w RNS oblicza postać wielomianu S1 · C1 + S2 · C2 + ... + Sm · Cm − P · r, gdzie S1, S2, ... są wynikami poprzedniego kroku, C1, C2, ... są wcześniej obliczonymi stałymi, r to stała, która jest uzyskiwana podczas obliczania wielomianu, a P = p1 · p2 · ... · pm. Innymi słowy, trzeci krok w RNS oblicza (S1 · C1 + S2 · C2 + ... + Sm · Cm)(mod P). Dlatego główne operacje arytmetyczne potrzebne do obliczeń w RNS to funkcja modulo X(mod P), modularna suma i modularne mnożenie.

Na przykład, A = 37, B = 19, a P = p1 · p2 · p3 = 3 · 5 · 7 = 105. W tym przypadku A1 = 1, B1 = 1, A2 = 2, B2 = 4, A3 = 2, B3 = 5, czyli A = (1, 2, 2) i B = (1, 4, 6). W tym przypadku dodawanie jest realizowane poprzez sumowanie reszt o odpowiednim indeksie, czyli A+B = ((A1 + B1) mod p1, (A2 + B2) mod p2, (A3 + B3) mod p3) = (2, 1, 0) = S.

Istnieje kilka sposobów konwersji liczby S na liczbę pozycyjną. Najczęstszy z nich opiera się na następującej formule:
Z = (X1 · Y1 + X2 · Y2 + ... + Xn · Yn) mod P = X1 · Y1 + X2 · Y2 + ... + Xn · Yn − k · P,

(1)

gdzie k jest liczbą naturalną, a Yi = P/pi · q, gdzie q powinno spełniać warunek q · P/pi (mod pi) = 1, i = 1, 2, ..., n, a q = 1, 2, ..., pi − 1.
Zgodnie z tą formułą S = 2 · 70 + 1 · 21 + 0 · 15 = 161 − 1 · 105 = 56, gdzie: Y1 = 105/3 · 2, ponieważ 2·105/3 (mod3) = 1; Y2 = 105/5 · 1, ponieważ 1·105/5 (mod5) = 1; Y3 = 105/7 · 1, ponieważ 1·105/7 (mod7) = 1.

Istnieją jednak pewne istotne ograniczenia implementacji RNS dla szerokiego zakresu obliczeń, a mianowicie konwersja ze systemu pozycyjnego na RNS i wstecz. Faktycznie żadne narzędzie do automatyzacji projektowania elektroniki (EDA) (poza Synopsys) nie może generować obwodu do obliczenia funkcji modulo. Wyjątkiem jest sytuacja, gdy modulo P = 2^δ, gdzie δ jest liczbą naturalną, ponieważ dowolna liczba z modulo 2^δ równa się δ najmniej znaczącym bitom tej liczby. W przeciwnym przypadku problem jest obliczeniowo trudny. Konwersja wsteczna jest nieco łatwiejsza, ponieważ polega na mnożnikach i sumatorach (jak pokazano w formule (1)). Jednak w końcu trzeba obliczyć funkcję modulo z modulo P lub wykonać porównanie z wartością k · P wiele razy, aby znaleźć k, lub zastosować konwencjonalne podejście mieszanej podstawy [10], w każdym przypadku znacznie zmniejszając wydajność konwersji. W praktyce oba problemy są rozwiązywane przez wybór z małego zbioru specjalnych modułów, co ogranicza zastosowanie RNS.

3. Opisany tekst dotyczy obliczania funkcji modulo (X(mod P)) w kontekście kryptografii i systemu liczbowego pozostałości (RNS). W obu przypadkach konieczne jest operowanie na ogromnych liczbach X o setkach i tysiącach bitów. Istnieje jednak znaczna różnica między tymi obszarami pod względem wymagań dotyczących obliczania X(mod P).

W kryptografii wartość P jest liczbą pierwszą lub liczbą, która może być rozłożona na 2 lub rzadziej 3 czynniki, tj. P = p1 · p2 · p3, gdzie p1, p2, p3 to liczby pierwsze. W RNS wartość P może być rozłożona na n czynników, gdzie n może wynosić kilkadziesiąt, np. P = p1 ·p2 ·...·pn. Mimo tej różnicy, implementacja sprzętowa funkcji modulo stanowi wąskie gardło zarówno dla kryptografii, jak i dla RNS.

Głównym ograniczeniem przy przetwarzaniu dużych liczb w RNS jest złożoność realizacji sprzętowej konwerterów. Wynika to z faktu, że do obliczenia funkcji modulo i odzyskania reprezentacji pozycyjnej należy przeprowadzić operacje dzielenia, modularnego mnożenia i porównywania. Istnieje różne podejścia do rozwiązania tego problemu, ale zazwyczaj są one ograniczone przez wartości modularne (np. mod 2^k - 1, mod 2^k, mod 2^k + 1) oraz liczbę operandów.

Kryptografia wymaga, aby czynniki P były jak najtrudniejsze. Oznacza to znaczne zwiększenie złożoności realizacji sprzętowej, ponieważ nieznane jest efektywne sprzętowe wykonanie X(mod P) dla dowolnego P. W RNS wszystkie czynniki P są znane. Ponadto p1, p2, ..., pn są wybierane jako specjalne liczby, dla których znana jest efektywna realizacja sprzętowa. Problemem jest jednak to, że zbiór specjalnych liczb, dla których znane są efektywne algorytmy, jest bardzo ograniczony. Jest to główny czynnik, który ogranicza szerokie zastosowanie RNS.

Istnieją podejścia do projektowania sprzętu dla X(mod P), ale są one sekwencyjne i/lub charakteryzują się wysokimi kosztami sprzętowymi i niską wydajnością w porównaniu z podejściami dla zestawów specjalnych liczb.

Obliczanie funkcji modulo może być zaprojektowane z użyciem elementów sekwencyjnych, ale wymagają one większych obszarów i są wolniejsze w porównaniu z podejściami kombinacyjnymi. Z drugiej strony, dostępność pamięci umożliwia obliczanie niektórych wartości modulo przy użyciu zapisanych uprzednio wartości.

Inne podejścia obejmują wykorzystanie własności okresowych dla liczb potęgowych dwójki, metody modularnego potęgowania oraz techniki oparte na własnościach rezyduów potęg dwójki.

Podsumowując, obliczanie funkcji modulo dla dużych liczb wiąże się z wyzwaniami w zakresie implementacji sprzętowej, zarówno w kryptografii, jak i w RNS. Istnieje kilka różnych podejść, które oferują różne sposoby efektywnego obliczania funkcji modulo dla dużych liczb, jednak nadal istnieją ograniczenia związane z liczbą operandów, specjalnymi wartościami i wydajnością sprzętu.

4.Nasz zaproponowany sposób obliczania funkcji modulo charakteryzuje się następującymi cechami:

Jest on stosowany dla dowolnego modulo oraz zakresu bitów wejściowych.
Może być zastosowany do mnożenia modulo, dodawania modulo oraz funkcji modulo.
Opiera się na logice kombinacyjnej.
W proponowanych procedurach istnieją pewne wspólne zadania:

Wejścia (czynniki wejściowe A · B w mnożeniu lub X w X(mod P)) są podzielone na podwektory.
Wszystkie podwektory są łączone, aby zdefiniować wielomian.
Ten proces jest powtarzany tak długo, jak wynik > 2 · P.
4.1 Obliczanie funkcji modulo
Proponujemy następującą procedurę dwuetapową do obliczania X(mod P):

X jest podzielone na k podwektorów o ≤ δ bitach w każdym podwektorze, gdzie δ = dlog2P − 1e.
Uzyskane podwektory są łączone zgodnie z równaniem 3:
X(mod P) = Xk
i=1
Xi ·
2
δ·(i−1)(mod P)

. (3)

To równanie można zastosować rekurencyjnie, generując zredukowane wyniki pośrednie w każdym kroku. Współczynnik 2δ·(i−1)(mod P) jest stały i nie przekracza P − 1. W pierwszym kroku Xi = 2δ −1, ponieważ równanie 3 osiąga maksymalną wartość. Następnie równanie 3 jest wywoływane rekurencyjnie, dopóki wynik nie będzie ≤ 2 · P. Na końcu wynik jest porównywany z P i jeśli trzeba, od niego odejmowana jest wartość P. Cały proces (przypominający obliczenia Fouriera) jest przedstawiony w algorytmie 1.

Dla celów ilustracji, rozważmy następujący przykład. Załóżmy, że X to wejście 18-bitowe, a P = 47. Wtedy modulo P jest liczbą 6-bitową, a wejście X jest podzielone na trzy 6-bitowe krotki X = (X3, X2, X1), gdzie X1 = (x6, x5, . . . , x1), X2 = (x12, x11, . . . , x7), a X3 = (x18, x17, . . . , x13). Następnie 2^6 (mod 47) = 17 (mod 47) i 2^12 (mod 47) = 7 (mod 47). W związku z tym w pierwszej iteracji równanie 3 przyjmuje następującą postać:

X(mod 47) = X1 + X2 · 2
6
(mod 47) + X3 · 2
12(mod 47) =
= X1 + X2 · 17 + X3 · 7(mod 47).

Ten proces jest kontynuowany, aż do osiągnięcia wyniku ≤ 94 (2 · P). Na końcu wynik jest porównywany z P, a jeśli jest większy, od niego odejmowana jest wartość P.

4.2 Obliczanie modularnego iloczynu (A · B mod P)
Proponujemy następującą procedurę dwuetapową do obliczania (A · B mod P):

A i B są podzielone na k podwektorów o ≤ δ bitach w każdym podwektorze, gdzie δ = ⌈log2 P⌉.
Pary odpowiadających sobie podwektorów są mnożone i sumowane zgodnie z równaniem 4:
(A · B mod P) = Ak
i=1
Ai · Bi ·
2
δ·(i−1)(mod P)

. (4)

Podobnie jak w przypadku funkcji modulo, równanie 4 może być zastosowane rekurencyjnie. Na końcu wynik jest porównywany z P, a jeśli jest większy, od niego odejmowana jest wartość P.

5. Minimalizacja funkcji boolowskich w operacjach modularnych
Wynik dowolnego obliczenia arytmetycznego można przedstawić jako sumę iloczynów (SOP).
Jednak pierwotne reprezentacje w postaci tabel prawdy mogą być trudne do zarządzania dla narzędzi syntezy, na przykład tabela prawdy dla iloczynu dwóch operandów wejściowych o długości 16 bitów wymaga 64 kolumn (16 kolumn dla każdego operandu i 32 kolumn dla wyniku) oraz ponad czterech miliardów wierszy.
Dla pary krotek o długości δ bitów, rozważamy wyrażenie 2^i (mod P) · Xi · 2^(δ·(i−1))(mod P), gdzie i = 1, 2, ..., k, to odpowiednie czynniki mnożenia. Wartość 2^i (mod P) jest stałą, której bity są zbędne przy minimalizacji, ponieważ wszystkie wiersze tabeli prawdy odpowiadające tej stałej mają taką samą wartość 2^i (mod P).

Początkowa tabela prawdy dla X (mod P) składa się z P wierszy i 2 · δ kolumn, gdzie lewe δ kolumny odpowiadają wszystkim liczbom całkowitym od 0 do P-1, a prawe kolumny odpowiadają X · 2^i (mod P).
Przykład: Rozważmy 28 (mod 13) = 9 (mod 13) = 1001₂. W tym przypadku subtabela 1 reprezentuje tabelę prawdy dla X · 9 (mod 13) przed minimalizacją, a subtabela 2 reprezentuje SOP po minimalizacji (można ją uzyskać za pomocą narzędzi takich jak [12] lub ELS [13]). Czyli pierwsze cztery bity w ostatnim wierszu tabeli prawdy w subtabeli 1 reprezentują 12₁₀, a prawe cztery bity reprezentują 12 · 9 (mod 13) = 4₁₀. Dla wejścia X o długości 18 bitów i P = 47, wszystkie pary odpowiednich czynników są reprezentowane jako SOP: z 12 kolumnami (6 wejść i 6 wyjść) X2 · 17 (mod 47) i X3 · 7 (mod 47); z 11 kolumnami (5 wejść i 6 wyjść) X1 · 2 · 17 (mod 47); z 9 kolumnami (3 wejścia i 6 wyjść) X2 · 2 · 17 (mod 47); z 8 kolumnami (2 wejścia i 6 wyjść) X3 · 2 · 17 (mod 47).

W powyższym przykładzie z ostatniego fragmentu w Listingu 1.2, modularne mnożenie dwóch liczb o długości 6 bitów modulo 47 obejmuje sześć bloków. Każdy blok realizuje funkcje boolowskie zminimalizowane za pomocą narzędzi takich jak Espresso lub ELS:

blok mult 3x3 realizuje mnożenie 3 na 3 bity, z 6 wejściami i 6 wyjściami;
blok mult 3x3 8 realizuje wieloargumentowe mnożenie modulo 47: ([3:1] · [3:1] · 8)(mod 47), z 6 wejściami i 6 wyjściami;
blok mult 3x3 17 realizuje wieloargumentowe mnożenie modulo 47: ([3:1] · [3:1] · 17)(mod 47), z 6 wejściami i 6 wyjściami;
blok mult 3 8 realizuje wieloargumentowe mnożenie modulo 47: ([3:1] · 8)(mod 47), z 3 wejściami i 6 wyjściami, przy czym trzy najmniej znaczące bity są równe zero;
blok mult 2 17 realizuje wieloargumentowe mnożenie modulo 47: ([2:1] · 17)(mod 47), z 2 wejściami i 6 wyjściami, przy czym czwarty bit jest równy zero.

6. Wyniki eksperymentalne
Porównaliśmy naszą procedurę z trzema narzędziami EDA: Synopsys, Mentor Graphics (dla standardowych komórek) i Xilinx (dla FPGA). Ponieważ Mentor Graphics i Xilinx nie syntezują ogólnych operacji modularnych, porównaliśmy je w przypadku specjalnych modułów, takich jak 2^s - 1, 2^s + 1. Nasze podejście wykazuje zyski sięgające do 10%.
Synopsys jest jedynym narzędziem EDA, które generuje obwody X(mod P). Przedstawiamy wyniki syntezy z wykorzystaniem narzędzia Synopsys 2014 na technologii ASIC Standard Cell o rozmiarze 28 nm, dostarczonej przez United Microelectronics Corporation.

Pierwsze pięć wykresów porównuje czas opóźnienia obwodów X(mod P) (w MHz) dla wejść X o długościach 100, 200, 300, 400 i 500 bitów, odpowiednio dla modułów P o długościach 19 (5 bitów), 53 (6 bitów), 113 (7 bitów), 241 (8 bitów), 461 (9 bitów), 997 (10 bitów), 2011 (11 bitów) i 4051 (12 bitów). Wyniki wydajności są grupowane w trzy kategorie:

Zaproponowane podejście jest szybsze o kilkanaście razy (aż do 30 razy) dla modułów 11- i 12-bitowych we wszystkich zakresach wejść (dwie prawe części wykresów).
Zaproponowane podejście jest średnio szybsze o 15% (aż do 300%) dla prawie wszystkich modułów o długościach od 5 do 10 bitów we wszystkich zakresach wejść (środkowe i lewe części wykresów).
Zaproponowane podejście jest wolniejsze, z istotną różnicą tylko dla trzech przypadków (dla modułów 5-bitowych i wejść o długościach 100 i 200 bitów oraz dla modułów 9-bitowych i wejścia o długości 10 bitów - odpowiednio 75%, 66% i 67%), a także niewielką przewagą (średnio do 5%) dla modułów 6- i 7-bitowych dla wejścia o długości 100 bitów oraz dla modułów 6- i 9-bitowych dla wejścia o długości 200 bitów.
Należy zauważyć, że eksperymenty przeprowadzono dla 40 różnych wartości.
Kolejne pięć wykresów porównuje powierzchnię obwodów X(mod P) (liczbę komórek z biblioteki komórek) dla wejść X o długościach 100, 200, 300, 400 i 500 bitów, odpowiednio dla tych samych modułów jak w eksperymentach dotyczących wydajności. Wyniki dotyczące powierzchni pokazują przewagę zaproponowanego podejścia, które poprawia się nawet o 30 razy dla wszystkich modułów i wartości wejściowych.

7. Wnioski i dalsze badania
Wydajność arytmetyki komputerowej stanowi jedną z głównych zalet RNS w porównaniu do tradycyjnych podejść. Zaproponowaliśmy technikę, która znacznie poprawia obszar i wydajność RNS w porównaniu do syntezy przy użyciu standardowych narzędzi EDA.
Eksperymenty pokazują znaczące korzyści naszego podejścia w porównaniu do Synopsys. Zysk wydajności wynosi nawet 30 razy, a obszar nawet 15 razy. Ponadto, Synopsys nie był w stanie syntezować obwodów dla wejść X większych niż 500 bitów: synteza przez Synopsys funkcji modulo dla wejścia o długości 600 bitów nie powiodła się po dziewięciu dniach, podczas gdy z naszym podejściem zajęło to zaledwie 20 minut.
Nasze podejście nie jest ograniczone do modularnego mnożenia i funkcji modulo, ale może być rozszerzone na dowolne operacje arytmetyczne. Dziesiątki obwodów zostało zaprojektowanych przy wykorzystaniu prezentowanej tutaj techniki, a następnie zintegrowanych w jednostki arytmetyczne przez fabrykę hi-tech Integral (Mińsk, Białoruś).
Tematy dalszych badań obejmują:

Porównanie różnych form reprezentacji (SOP, rozwinięcia Reed-Muller, diagramy decyzyjne binarne) w realizacji częściowych iloczynów;

Projektowanie układów FPGA przy użyciu architektur Xilinx i Altera.
