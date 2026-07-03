# -*- coding: utf-8 -*-
import html, json

# weekday keys: mon tue wed thu fri sat sun
# Each entry: num, name, mun (kommun), region, typ, days{}, season(note for the weekly days), special(text), addr
M = []
def add(num,name,mun,region,typ,days=None,season="",special="",addr=""):
    M.append(dict(num=num,name=name,mun=mun,region=region,typ=typ,
                  days=days or {},season=season,special=special,addr=addr))

R1="Skåne & Blekinge"; R2="Småland"; R3="Halland"

# ---------------- SKÅNE & BLEKINGE ----------------
add(1,"Båstadportens loppis","Båstad",R1,"L",{"sat":"10–16"},addr="Tomtaholmsvägen 8, Östra Karup")
add(2,"Båstad GIF Loppis","Båstad",R1,"L",{"sat":"10–13"},addr="Örebäcksvallen, Båstad")
add(3,"Märits","Båstad",R1,"A",special="Öppettider ej angivna i guiden")
add(4,"Klenoden i Rammsjö","Båstad",R1,"A",{"thu":"14–18","fri":"14–18","sat":"10–14"},season="18/6–8/8",addr="Rammsjövägen 184, Båstad")
add(5,"Västra Karups IF:s Loppis","Båstad",R1,"L",{"tue":"14–17","sat":"11–14"},addr="Glimmingevägen 1, Västra Karup")
add(6,"Grevie GIK:s Loppisbutik","Båstad",R1,"L",{"mon":"10–13","wed":"10–13","thu":"15–18","sat":"11–14"},addr="Stålhögavägen 12, Grevie")
add(7,"Rutigt & Randigt Second hand","Båstad",R1,"A",{"thu":"13–18","fri":"13–18","sat":"11–15"},season="Högsäsong: mån–sön 13–18, lör 11–16. Vinter nov–mar varierande tider",addr="Grusåsvägen 1, Grevie")
add(8,"Förslövs IF Loppislada","Båstad",R1,"L",{"tue":"10–12","wed":"10–12","thu":"15–17","sat":"10–12"},season="Reservation för ändringar vinter/midsommar",addr="Idrottsvägen 4, Förslöv")
add(9,"Viarpform 1900","Båstad",R1,"A",{"sun":"11–16","mon":"11–16","tue":"11–16","wed":"11–16","thu":"11–16"},season="Storhelger & sommar 26/6–14/8 (sön–tors). Annars öppet på förfrågan",addr="Bjäredalsvägen 392, Förslöv")
add(10,"Vejby Loppis","Ängelholm",R1,"L",{"wed":"10–13","thu":"17–19","fri":"10–13","sat":"10–13","sun":"13–15"},addr="Haragårdsvägen 45, Vejbystrand")
add(11,"Johannas Finloppis","Ängelholm",R1,"L",special="Öppettider annonseras på Instagram/Facebook (@johannasfinloppis)")
add(12,"Antikkulan Antikt & Retro","Ängelholm",R1,"A",{"sun":"11–16"},season="Sön fr.o.m 22/3. Sommar 21/6–16/8 varje dag 11–16. Kristi himmelsfärd 14–17/5 11–16. Stängt jan, feb & halva mars",addr="Valhallsbyaväg 118, Ängelholm")
add(13,"Smedjans Second Hand","Ängelholm",R1,"L",{"wed":"12–15","sat":"12–15"},season="Sommarloppis: juli (ons & lör). Även 14–17/5 kl 11–16",addr="Valnötsvägen 5, Ängelholm")
add(14,"Hjärnarp GIF:s Loppis","Ängelholm",R1,"L",{"wed":"10–14","thu":"16:30–18:30","sat":"10–14","sun":"12–15"},season="Sommarloppis på IP 27/6 kl 14",addr="Hjärnarpsvägen 3, Hjärnarp")
add(15,"PMU Second Hand","Ängelholm",R1,"L",special="Transportgatan 5. Se pmu.se/hitta-butik för öppettider",addr="Transportgatan 5, Ängelholm")
add(16,"Fyndhuset","Ängelholm",R1,"A/L",special="Öppettider ej tydligt angivna i guiden")
add(17,"Electric Mud Records","Ängelholm",R1,"L",{"tue":"12–18","wed":"12–18","thu":"12–18","fri":"12–18","sat":"10–14","sun":"12–15"},addr="Järnvägsgatan 8, Ängelholm")
add(18,"Villa Rönne loppis","Ängelholm",R1,"L",special="Öppettider uppdateras på Instagram (@villaronneloppis)",addr="Västra Kyrkogatan 1, Ängelholm")
add(19,"Skattkammaren Loppis","Ängelholm",R1,"L",{"tue":"13–18","wed":"13–18","thu":"13–18","sat":"10–15","sun":"10–15"},addr="Sandvångsgatan 12, Ängelholm")
add(20,"Varuförmedlingen","Ängelholm",R1,"L",{"tue":"14–18","thu":"14–18","sat":"10–15","sun":"11–15"},season="Sommar juni–sept: även ons 14–18",addr="Industrigatan 6 (runt hörnan), Ängelholm")
add(21,"Fyndet Antik & Kuriosa","Ängelholm",R1,"A",{"tue":"15–18","thu":"15–18","sat":"10–15","sun":"11–15"},season="Sommar juli–aug: tis/ons/tor 14–18, lör 10–15, sön 11–15",addr="Industrigatan 6, Ängelholm")
add(22,"Madam De'vill","Ängelholm",R1,"A",{"wed":"12–18","thu":"12–18","fri":"12–18","sat":"10–14"},addr="Storgatan 58, Ängelholm")
add(23,"Starby vintage och loppis","Ängelholm",R1,"A",special="Öppettider & info på Instagram (starbyvintageochloppis)",addr="Starby landsväg 344, Ängelholm")
add(24,"Delsinger Antik","Ängelholm",R1,"A",{"sat":"11–16","sun":"11–16"},addr="Framtidsgatan, avfart Ängelholm N")
add(25,"Össjö Lanthandel","Ängelholm",R1,"A",{"sat":"10–15","sun":"10–15"},season="Hela påskhelgen 10–16",addr="Össjö-Boarpsvägen 181, Boarp")
add(26,"Logan","Ängelholm",R1,"A/L",special="Öppettider ej angivna i guiden")
add(27,"Össjö Loppis","Ängelholm",R1,"L",special="Sista lördagen i augusti, ca kl 13 (Ekebo)",addr="Ekebo, Össjö")
add(28,"Höganäs BK Loppis","Höganäs",R1,"L",{"thu":"13–16","sat":"10–14"},season="Inlämning tis 13–16",addr="Verkstadsgatan 11, Höganäs")
add(29,"EK Antik & Kuriosa","Höganäs",R1,"A",{"sun":"11–15"},addr="Brännerigatan 38, Höganäs")
add(30,"Röda Korset Höganäs","Höganäs",R1,"L",{"tue":"13–17","wed":"13–17","thu":"13–17","sat":"10–14"},season="Kontrollera aktuella tider på redcross.se/hoganas",addr="Storgatan 21, Höganäs")
add(31,"Retro Höganäs","Höganäs",R1,"A",special="Se Instagram (retro_hoganas)",addr="Bruksgatan 26, Höganäs")
add(32,"Loppan Höganäs","Höganäs",R1,"L",{"mon":"10–18","tue":"10–18","wed":"10–18","thu":"10–18","fri":"10–18","sat":"10–14"},addr="Storgatan 63, Höganäs")
add(33,"Loppans Möbleria","Höganäs",R1,"L",{"thu":"13–17"},addr="Verkstadsgatan 8, Höganäs")
add(34,"Alledals antik & kuriosa","Höganäs",R1,"A",{"sat":"12–16"},season="Öppnar i samband med Antikturen (Kristi himmelsfärd). Övr. tider se sociala medier",addr="Brandstorpsvägen 159, Ingelsträde/Viken")
add(35,"Living by Clementz","Höganäs",R1,"L",special="Öppettider ej angivna i guiden")
add(36,"Ryssamöllagården Inredning & Trädgård","Helsingborg",R1,"A",{"fri":"11–15","sat":"11–15","sun":"11–15"},addr="Mjöhultsvägen 202, Allerum")
add(37,"Leksaksmässan Helsingborg","Helsingborg",R1,"A",special="Leksaks- och Nostalgimarknad varje vår & höst. Teknikhallen, Filbornavägen 9")
add(38,"Hoarder Shop Ödåkra","Helsingborg",R1,"A",{"fri":"11–18","sat":"11–16","sun":"11–16"},season="Tiderna kan variera – följ sociala medier",addr="Fabriksgatan 2, Ödåkra")
add(39,"Nr11 Second Hand och Antikt","Helsingborg",R1,"L",{"mon":"12–18","tue":"12–18","wed":"12–18","thu":"12–18","fri":"12–18","sat":"11–15","sun":"11–15"},addr="Rosenbergsgatan 11, Helsingborg")
add(40,"Mats Antik & Loppis","Helsingborg",R1,"A",{"mon":"10–18","tue":"10–18","wed":"10–18","thu":"10–18","fri":"10–18","sat":"10–14"},addr="Mogatan 6, Helsingborg")
add(41,"Röda Korset Helsingborg","Helsingborg",R1,"L",special="Se facebook.com/rodakorsetsecondhandhbg",addr="Örnsköldsviksgatan 15, Helsingborg")
add(42,"Framtid","Helsingborg",R1,"L",{"mon":"10–16","thu":"10–16"},season="Sista söndagen i månaden 11–14",addr="Landskronavägen 14, Helsingborg")
add(43,"Harlyckans kuriosa & retro","Helsingborg",R1,"A",special="Öppettider ej tydligt angivna i guiden")
add(44,"Busfrö Nytt & Bytt","Helsingborg",R1,"L",special="Kullagatan 23. Se busfro.se",addr="Kullagatan 23, Helsingborg")
add(45,"Agges Loppis","Landskrona",R1,"L",{"sun":"9–16"},addr="Ringvägen 48, Landskrona")
add(46,"Kassaskrinet secondhand","Landskrona",R1,"L",{"thu":"11–18","sun":"11–15"},addr="Industrigatan 68, Landskrona")
add(47,"Bjuvs Loppis","Bjuv",R1,"L",{"sat":"09–13"},addr="Ågatan 8 (Bjuvs Gruvmuseum)")
add(48,"Åstorps FF loppis","Åstorp",R1,"L",{"tue":"12–15","thu":"12–15","sat":"10–15"},addr="Trädgårdsgatan 36, Åstorp")
add(49,"Ställets Antik & Kuriosa","Åstorp",R1,"A",{"mon":"11–16","tue":"11–16","wed":"11–16","thu":"11–16","fri":"11–16","sat":"11–16","sun":"11–16"},season="Stängt tis, ons & tors sept–maj",addr="Parallellvägen 50, Åstorp")
add(50,"Boutique Nytt o Nött","Klippan",R1,"L",season="Mest söndagar 11–15",special="Datum 2026: 26/4; 3 & 31/5 (+ Antikturen 14–17/5); 7 & 28/6; 5 & 26/7; 2, 9 & 30/8; 6 & 27/9; 4 & 25/10; 7 & 28/11; 6/12 (julmys). Kl 11–15",addr="Öja 4646, Klippan")
add(51,"Klippans antikt, retro & loppis","Klippan",R1,"A",{"sat":"11–15","sun":"11–15"},season="Apr–sept ojämna veckor lör & sön. Okt–mar ojämna veckor endast lördag",addr="Ängelholmsgatan 35, Klippan")
add(52,"Perstorp Bälinge IK loppis","Perstorp",R1,"L",special="Ring 0726-024888 för öppethållande",addr="Badvägen 7, Perstorp")
add(53,"Nytt liv second hand","Örkelljunga",R1,"L",special="Öppettider ej angivna i guiden")
add(54,"Starkeld.com Eket","Örkelljunga",R1,"A",special="Öppet efter överenskommelse. Tider på Facebook/Instagram",addr="Kungsleden 9, Eket")
add(55,"Citykyrkan Second Hand","Örkelljunga",R1,"L",{"tue":"10–18","wed":"10–18","thu":"10–18","sat":"10–16"},addr="Hallandsv. 24, Örkelljunga")
add(56,"Göinge Bohagstjänst Tyringe","Hässleholm",R1,"A",{"thu":"13–17:30","sat":"11–16","sun":"11–16"},season="Fre 13–17:30 juni–augusti",addr="Hörjavägen 4, Tyringe")
add(57,"Fredrik Johansson Loppis i Finja","Hässleholm",R1,"L",{"tue":"10–16","thu":"10–16","sat":"10–16","sun":"10–16"},season="Bakluckeloppis 1 gång/mån (slutet av månaden) fr.o.m april",addr="Saxbäcksvägen 1, Finja")
add(58,"Hässleholms IF Loppis","Hässleholm",R1,"L",{"tue":"13–18","thu":"16–20","sun":"13–17"},season="Österås (Hövdingegatan 25): tis 13–18, tor 16–20, sön 13–17. Centrum (3:e avenyn 9): tis 13–18, tor 13–18, lör 10–14",addr="Hövdingegatan 25 / 3:e avenyn 9, Hässleholm")
add(59,"PMU Secondhand Hässleholm","Hässleholm",R1,"L",{"tue":"12–18","wed":"12–18","thu":"12–18","sat":"10–15"},addr="Industrigatan 8, Hässleholm")
add(60,"Röda korset Hässleholm","Hässleholm",R1,"L/C",{"tue":"11–18","thu":"11–18","sat":"11–14"},addr="Östergatan 17, Hässleholm")
add(61,"Freeflow secondhand","Hässleholm",R1,"L",{"tue":"14–18","sat":"10–15","sun":"13–15"},addr="Enhörningsvägen 2, Hässleholm")
add(62,"Retro Living Vittsjö","Hässleholm",R1,"A",special="Öppettider se Facebook/Instagram (retro_living_i_vittsjo)",addr="Lehultsvägen 17, Vittsjö")
add(63,"Emmaljunga Folkets Hus Loppis","Hässleholm",R1,"L",{"mon":"11–16","tue":"11–16","wed":"11–16","thu":"11–16","fri":"11–16","sat":"11–16","sun":"11–16"},season="Öppet 21/6–9/8",addr="Kronobergsvägen 5, Emmaljunga")
add(64,"Snapphane Auktioner","Hässleholm",R1,"Au",special="Auktionsfirma. PL 5297 Röinge",addr="Röinge, Hässleholm")
add(65,"Modighus","Hässleholm",R1,"A",special="Öppettider ej angivna i guiden")
add(66,"Diana & Du","Hässleholm",R1,"A/L/C",{"thu":"12–17","fri":"12–17","sat":"11–16","sun":"11–16"},addr="Södra Vägen 2, Bjärnum")
add(67,"Vinslövs IF Loppis","Hässleholm",R1,"L",{"mon":"15–18"},season="Helgfria måndagar 15–18 + 2:a & 4:e lördagen i månaden 10–13",addr="Godsmagasinet, N. Järnvägsgatan, Vinslöv")
add(68,"Butiken Vackra Ting","Hörby",R1,"A",special="Öppettider ej angivna i guiden")
add(69,"Myllan Yllefabriken Marieholm","Eslöv",R1,"L",{"sat":"10–16","sun":"10–16"},addr="Yllegatan 4, Marieholm")
add(70,"Frid & Fröjd Stockamöllan","Eslöv",R1,"A",special="Öppettider ej angivna i guiden")
add(71,"Larssons Lager","Kävlinge",R1,"L",{"sun":"9–16"},season="50-talscafé öppet söndagar",addr="Floravägen 54, Kävlinge")
add(72,"Raststället second hand Furulund","Kävlinge",R1,"L",{"mon":"9:30–13:30","tue":"13:30–17:30","wed":"9:30–13:30","thu":"13:30–17:30"},season="Första lördagen i månaden 10–13:30. Sommar/vinter kan tiderna variera",addr="Grönegatan 2, Furulund")
add(73,"Hall Items","Lund",R1,"A",special="Aktuella öppettider på Instagram (hallitems)",addr="Risavägen 2A, Genarp")
add(74,"Vombs kaffestuga","Lund",R1,"C",{"sat":"12–17","sun":"12–17"},season="Öppnar midsommar 22/6. Kvällsöppet juli: onsdagar 17–21",addr="Vomb")
add(75,"Vintage Vinyl Records","Lund",R1,"L",special="Se visitlund.se / sociala medier",addr="Lilla Fiskaregatan 4, Lund")
add(76,"Relove & More","Malmö",R1,"A",special="Öppettider ej angivna i guiden",addr="Södergatan 12, Malmö")
add(77,"Claeshallen konst & antikviteter","Malmö",R1,"A",{"tue":"11–18","thu":"11–18","fri":"11–17","sat":"10–15"},season="Mån, ons & sön stängt",addr="Cypressv. 6, Malmö")
add(78,"Busfrö Nytt & Bytt","Malmö",R1,"L",special="Södra Förstadsg. 14. Se busfro.se",addr="Södra Förstadsgatan 14, Malmö")
add(79,"Lions loppis Höllviken","Vellinge",R1,"L",{"sat":"10–13"},season="Varje lördag i udda veckor",addr="Skegrievägen 75, Höllviken")
add(80,"Äspö Retrotorp","Trelleborg",R1,"A",special="Öppettider ej angivna i guiden")
add(81,"PMU Second Hand Trelleborg","Trelleborg",R1,"L",special="Tommarpsvägen 85. Se pmu.se",addr="Tommarpsvägen 85, Trelleborg")
add(82,"Blå gåsen vintage shop Skivarp","Skurup",R1,"A",special="Öppettider ej angivna i guiden",addr="Skivarp")
add(83,"Återbrukets hus","Svedala",R1,"L/A",{"wed":"14–18","thu":"12–17","fri":"12–17","sat":"11–15"},addr="Storgatan 42, Svedala")
add(84,"Spiken i Kistan","Sjöbo",R1,"A",{"wed":"12–18","thu":"12–18","fri":"12–18","sat":"12–16","sun":"12–16"},season="Ring ALLTID innan – ej alltid bemannat",addr="Storgatan 34, Lövestad")
add(85,"Kostallet i Heinge","Sjöbo",R1,"A",{"sun":"11–15"},addr="Östra Klasarödsvägen 246, Lövestad")
add(86,"Allt i Allo Prylmarknad Hammenhög","Simrishamn",R1,"L",{"sat":"10–16"},season="Varje lördag med vissa undantag",addr="Herrestadsv. 3, Hammenhög")
add(87,"Industrigatan 12","Simrishamn",R1,"A",special="Se Instagram (industrigatan_12)",addr="Industrigatan 12, Simrishamn")
add(88,"Karossgården Antik i Gladsax","Simrishamn",R1,"A",special="Öppettider ej angivna i guiden",addr="Gladsax")
add(89,"Borg Design","Tomelilla",R1,"A",special="Öppettider se borgdesign.se",addr="Tryde 5801, Tomelilla")
add(90,"Norrvalla","Tomelilla",R1,"A",special="Öppettider se norrvalla.se / sociala medier",addr="Storgatan 39, Smedstorp")
add(91,"Antikt & Kuriosa Degeberga","Kristianstad",R1,"A",{"tue":"14–17","wed":"14–17","thu":"14–17","sat":"11–17","sun":"11–17"},season="1/9–31/5 (se intill). Sommar 1/6–31/8: alla dagar 11–17",addr="Tingsvägen 23, Degeberga")
add(92,"Degeberga GoIF Loppis","Kristianstad",R1,"L",{"thu":"18–20"},season="Helgfria torsdagar, säsong 5/3–26/11",addr="Forsakarsvägen 35, Degeberga")
add(93,"Stallet Second Hand","Kristianstad",R1,"A",{"sat":"11–16","sun":"12–16"},season="Vinter 16/8–14/6: lör 11–16, sön 12–16. Sommar 15/6–15/8: tis–fre 14–17, lör 11–17, sön 12–17",addr="Lyngbyvägen 244, Gärds Köpinge")
add(94,"Magasinet Tollarp","Kristianstad",R1,"A",special="Öppettider på Instagram (aterbruk_i_magasinet)",addr="Anne-Marie Åbergsväg 23, Sätaröd")
add(95,"Lilla Loppan Tollarp","Kristianstad",R1,"A",{"tue":"12–16","wed":"12–16","thu":"12–16","sat":"10–13"},addr="Feglers gata 30, Tollarp")
add(96,"Retro en trappa upp Östra Vram","Kristianstad",R1,"A",{"tue":"12–17","wed":"12–17","thu":"12–19","sun":"12–15"},season="Ev. semester någon vecka – ring vid lång resa",addr="Östra Vramsvägen 29, Tollarp")
add(97,"Vittskövle byloppis","Kristianstad",R1,"L",{"sat":"10–12"},season="Helgfria lördagar. Extra sommaröppet juni–augusti 10–13",addr="Bakom kyrkan, Vittskövle")
add(98,"Torget 11 Vintage & Secondhand","Kristianstad",R1,"A",{"sat":"11–15"},season="Helgfria lördagar. Extraöppet påsk, sommar & jul",addr="Torget 11, Åhus")
add(99,"Lion Loppis Åhus","Kristianstad",R1,"L",{"sat":"09–13"},season="Helgfria lördagar",addr="Fyrvaktaregatan 1, Åhus")
add(100,"Röda Korset Secondhand Kristianstad","Kristianstad",R1,"L",{"mon":"10–17","tue":"10–16","wed":"10–16","thu":"10–17","fri":"10–16","sat":"10–15"},addr="Östra Vallgatan 19, Kristianstad")
add(101,"Peters retro & kuriosa","Kristianstad",R1,"A",{"tue":"12–17","wed":"12–17","thu":"12–17","sat":"10–15"},addr="JH Dahlsgatan 19, Kristianstad")
add(102,"PMU Pingstkyrkan Secondhand","Kristianstad",R1,"L",special="Näsbychaussen 119. Se pmu.se",addr="Näsbychaussen 119, Kristianstad")
add(103,"Majas Stöd Mot Barncancer Secondhand","Kristianstad",R1,"L",{"tue":"10–18","wed":"10–18","thu":"10–18","fri":"10–18","sat":"10–15"},addr="Nässelvägen 5, Kristianstad")
add(104,"Retro & Antikt i Rinkaby","Kristianstad",R1,"A",{"thu":"13–16","sat":"11–16"},season="Övriga tider se Instagram (lennartsdesignoretro)",addr="Gälltoftavägen 1, Rinkaby")
add(105,"Furuboden Second Hand","Kristianstad",R1,"L",{"tue":"10–14","thu":"10–18"},addr="Blekingevägen 6F, Kristianstad")
add(106,"Returen","Kristianstad",R1,"L",{"mon":"13–17:30","wed":"09–17:30","fri":"09–14:30","sat":"09–14:30","sun":"09–14:30"},addr="Optovägen 2, Kristianstad")
add(107,"Möbelmagasinet","Östra Göinge",R1,"L",{"mon":"10–17","tue":"10–17","wed":"10–17","thu":"10–17","fri":"10–17","sat":"10–13:30"},season="Semesterstängt v. 28–30",addr="Fabriksgatan 6, Hanaskog")
add(108,"Treby IF loppis Killeberg","Osby",R1,"L",{"sat":"10–12:30"},season="Första lördagen varje månad",addr="Killeberg")
add(109,"Östbergs Antikt & Kuriosa","Olofström",R1,"A",{"sat":"10–16","sun":"10–16"},season="Året om",addr="V. Storgatan 4, Olofström")
add(110,"Beckas antik & kuriosa","Sölvesborg",R1,"A",{"sun":"10–15"},season="Alla söndagar",addr="Lörbyvägen 358, Sölvesborg")
add(111,"Pryttlar & Pinaler","Karlshamn",R1,"A",{"tue":"13–17","sat":"10–15"},season="Stängt endast midsommardagen",addr="Strömmavägen 28 (under Kreativum), Karlshamn")
add(112,"Kallinge second hand","Ronneby",R1,"A",{"thu":"13–18","fri":"13–18","sat":"10–14"},season="Med vissa avvikande tider",addr="Flisevägen 1, Kallinge")
add(113,"Stenladan Fågelmara","Karlskrona",R1,"A",special="Öppettider uppdateras på Facebook",addr="Riksvägen 56, Fågelmara")
add(114,"Röda Korset Lyckeby","Karlskrona",R1,"L",{"tue":"12–17","thu":"12–17","sat":"11–15"},addr="Lallerstedts gata 4, Lyckeby")

# ---------------- SMÅLAND ----------------
add(115,"Markaryds IF","Markaryd",R2,"A",special="Öppettider ej angivna i guiden")
add(116,"PMU Lagadalskyrkans Second Hand","Markaryd",R2,"L",{"tue":"15–18","sat":"10–14"},season="Möbelförsäljning (Järnvägsgatan 53): tis 13–18",addr="Lagastigsgatan 22, Strömsnäsbruk")
add(117,"Hird-Bay Antiques","Markaryd",R2,"A",{"sat":"–","sun":"–"},season="Oftast öppet lör & sön. Aktuella tider på hemsida/sociala medier",addr="Bergshult 4291, Markaryd")
add(118,"Tovhults Retro Traryd","Markaryd",R2,"A",{"sat":"10–14"},season="De flesta lördagar. Alla tider på Facebook",addr="Skolgatan 1, Traryd")
add(119,"Annas Kuriosa","Ljungby",R2,"A",special="Öppet? Ring! 073-5748994",addr="Bäckaryd 1, Hamneda")
add(120,"Lillstugan Loppis & Kuriosa","Ljungby",R2,"L",{"sun":"10–17"},season="Öppnar skärtorsdagen, därefter de flesta söndagar t.o.m september",addr="Romborna, Norragården 1, Annerstad")
add(121,"Västre Gård Loppis & Kuriosa","Ljungby",R2,"L",{"sun":"11–17"},season="Apr–jun sön 11–17. Juli–aug tor–sön 11–17. Sep–nov sön 11–15",addr="Berghem, Västregård 5, Ljungby")
add(122,"Jonas second hand","Ljungby",R2,"L",{"tue":"12–17","sat":"10–14"},season="Extra öppettider på Facebook",addr="Gängesvägen 9, Ljungby")
add(123,"Bolmsö loppis","Ljungby",R2,"A",{"sun":"11–16"},season="5/4–26/9 sön 11–16. 14/6–15/8 även mån/tis/ons 11–16",addr="Bolmsö")
add(124,"Hela människan second hand","Gislaved",R2,"L",{"tue":"14–18","wed":"14–17","thu":"11–18","sat":"10–13"},addr="Köpmansgatan 5C, Gislaved")
add(125,"Gnosjö Hjälpers Secondhandbutik","Gnosjö",R2,"L",{"thu":"14–18","sat":"10–14"},season="Hela året. Undantag vissa helger",addr="Smedjegatan, Gnosjö")
add(126,"Hellmans Antik","Gnosjö",R2,"A",special="Öppettider se Facebook/Instagram",addr="Hellmansgatan 18, Gnosjö")
add(127,"Nalles Loppis","Vaggeryd",R2,"L",{"tue":"13–18","wed":"13–18","thu":"13–18","fri":"13–18"},season="1/5–30/9 även lör & sön (ring 079-3499522)",addr="Storgatan 4, Vaggeryd")
add(128,"Busfrö Nytt & Bytt","Jönköping",R2,"L",special="Smedjegatan 23C. Se busfro.se",addr="Smedjegatan 23C, Jönköping")
add(129,"PMU Second Hand","Jönköping",R2,"L",special="Smedjegatan 27. Se pmu.se",addr="Smedjegatan 27, Jönköping")
add(130,"Patina Antikviteter & Byggnadsvård","Nässjö",R2,"A",special="Se patina.nu / Instagram",addr="Larstorps Gård, Nässjö")
add(131,"Antikstoppet i Ör","Växjö",R2,"A",{"sun":"11–17"},season="April–oktober. Övrig tid enl. ö.k.",addr="Ör Svartensgård 5, Ör")
add(132,"Loppis på Loen","Växjö",R2,"L",special="Öppet enl. ö.k. juni–september. Se Loppispaloen",addr="Fägerstad Norregård 1, Furuby")
add(133,"Boalindas Antikt & Loppis","Växjö",R2,"A",{"sun":"11–17"},season="Maj–september",addr="Boda 3, Lammhult")
add(134,"Busfrö Nytt & Bytt","Växjö",R2,"L",special="Storgatan 29. Se busfro.se",addr="Storgatan 29, Växjö")
add(135,"Lekaryds Antikt & Loppis","Alvesta",R2,"A",{"sun":"11–16"},season="Alla söndagar april–november",addr="Lekaryd, Alvesta")
add(136,"Östregård antikt och loppmarknad","Alvesta",R2,"A",{"sun":"12–18"},season="Alla söndagar april–sept. Kaffeservering & korvvagn",addr="Moheda")
add(137,"Olofs Handelsbod","Alvesta",R2,"A",{"sun":"10–17"},season="Söndagar maj–september",addr="Ådalsvägen 20, Moheda")
add(138,"La boutique retro (Retro Källan)","Alvesta",R2,"A",{"sat":"10–15"},addr="Värendsgatan 4, Alvesta")
add(139,"Maris Bonnaloppis","Alvesta",R2,"L",{"sun":"13–17"},season="Maj–september",addr="Forssa, Norregården 1, Hjortsberga")
add(140,"Smedjans Antik","Alvesta",R2,"A",{"sun":"11–15"},season="Alla söndagar. Övr. tider se smedjanantik.se",addr="Gröna gatan 7, Vislanda")
add(141,"Ragnarssons Antik & Café","Älmhult",R2,"A/C",special="Virdavägen 12, Liatorp. Se sociala medier",addr="Virdavägen 12, Liatorp")
add(142,"Prästbackens Antik","Älmhult",R2,"A",{"mon":"12–18","tue":"12–18","wed":"12–18","thu":"12–18","fri":"12–18","sat":"10–16","sun":"12–16"},addr="S. Esplanaden 26, Älmhult")
add(143,"Live!","Älmhult",R2,"A",special="Live! loppmarknad, Handelsvägen 6. Se almhult.se/guide26",addr="Handelsvägen 6, Älmhult")
add(144,"Antikaffären i Tingsryd","Tingsryd",R2,"A",{"wed":"10–18","thu":"10–18","fri":"10–18","sat":"10–14"},season="Sommartid (ovan). Övrig tid enl. ö.k.",addr="Storgatan 60, Tingsryd")
add(145,"Vrångeboda Loppis","Tingsryd",R2,"L",season="Datum 2026: 9, 16 & 23/5; 13 & 27/6; 4, 11, 18 & 19/7; 8 & 15/8; 5/9. Kl 10–15",special="Specifika lördagar/söndagar 10–15",addr="Vrångeboda 1, Ryd")
add(146,"Hatterians Pinaler","Lessebo",R2,"A",{"tue":"14–19","thu":"14–19","sun":"11–18"},season="V. 27–34 även mån & fre 14–19",addr="Kongagatan 6, Lessebo")
add(147,"Leroy","Lessebo",R2,"L",{"tue":"14–19","thu":"14–19","sun":"11–18"},season="V. 27–34 även mån & fre 14–19",addr="Åkerhultsvägen 2, Lessebo")
add(148,"Loppis i Skruv","Lessebo",R2,"L",special="Öppettider ej angivna i guiden",addr="Skruv")
add(149,"Gamla mejeriet i Karstorp","Vetlanda",R2,"A",special="Se mejerietikarlstorp.se",addr="Karstorp, Vetlanda")
add(150,"Sommarloppis i Kokos musiklada","Vetlanda",R2,"L",{"sun":"11–16"},season="Söndagar maj–september",addr="Södra Skog 8, Ramkvilla")
add(151,"Röda Korset Second Hand Eksjö & Mariannelund","Eksjö",R2,"L",{"wed":"12–16","sat":"10–14"},season="Eksjö (Österlånggatan 33): ons 12–16, lör 10–14. Mariannelund (Centralgatan 3): tis & tor 15–18, lör 10–13",addr="Österlånggatan 33, Eksjö / Centralgatan 3, Mariannelund")
add(152,"Antikt & Gjutjärn","Eksjö",R2,"A",special="Nybrogatan 7A. Se sociala medier / ring 070-847 50 14",addr="Nybrogatan 7A, Eksjö")
add(153,"Busfrö Nytt & Bytt","Västervik",R2,"L",special="Storgatan 25. Se busfro.se",addr="Storgatan 25, Västervik")
add(154,"Busfrö Nytt & Bytt","Oskarshamn",R2,"L",special="Flanaden 2. Se busfro.se",addr="Flanaden 2, Oskarshamn")
add(155,"Allt det gamla goda","Nybro",R2,"A",{"fri":"11–16","sat":"11–16","sun":"11–16"},season="Sommar fre–sön 11–16. Övriga året endast sön 11–16",addr="Björstorp 321, Örsjö (Eskilsryd)")
add(156,"Busfrö Nytt & Bytt","Kalmar",R2,"L",special="Kaggensgatan 25A. Se busfro.se",addr="Kaggensgatan 25A, Kalmar")
add(157,"Antikrundan i Limmared","Tranemo",R2,"A/L",{"tue":"13–17","sat":"10–14"},season="Året om. Antikveckan v.30: mån–fre 11–17, lör 10–14",addr="Limmared")

# ---------------- HALLAND ----------------
add(158,"Silverhjelms spis & kamin","Laholm",R3,"A",special="Flyttar våren 2026. Ring 0700-900091 för info")
add(159,"Röda Korset Laholm / Hyltebruk","Laholm",R3,"L",special="Öppettider på redcross.se. Laholm: Östertullsgatan 24. Hyltebruk: Storgatan 18",addr="Östertullsgatan 24, Laholm / Storgatan 18, Hyltebruk")
add(160,"Kattens Loppis","Laholm",R3,"L",{"tue":"13–17","sat":"13–17","sun":"13–17"},season="April–oktober (ovan). Sommar midsommar–15/8: mån–ons 10–17, tor–sön 13–17",addr="Kristianstadsvägen 6, Våxtorp")
add(161,"BK Walldia Loppis","Laholm",R3,"L",{"sun":"13–15","tue":"17–19"},season="Mars–maj & okt–6/12: söndagar ojämn vecka 13–15. Juni–15/9: varje tisdag 17–19",addr="Brohuset 2, Vallberga")
add(162,"Farfars & Farmors Antikviteter","Laholm",R3,"A",{"sun":"12–15"},season="Övriga tider se Facebook",addr="Fridhemsvägen 47, Lilla Tjärby, Laholm")
add(163,"Det Konstiga Stallet","Laholm",R3,"A",{"sun":"12–15"},season="De flesta söndagar. Övrig tid enl. ö.k.",addr="Norra Skogaby 231, Laholm")
add(164,"Skogaby BK Loppis","Laholm",R3,"L",{"sun":"10–13"},season="Vissa söndagar. Se skogabybk.se",addr="Skogaby (skyltat från väg 15)")
add(165,"BTK Serve Loppis","Laholm",R3,"L",season="Datum 2026: lör 21/3 kl 11; lör 9/5 kl 11; ons 24/6 kl 18; ons 12/8 kl 18; lör 10/10 kl 11; lör 21/11 kl 11",special="Loppisar vissa dagar (restloppis dagen efter kl 10)",addr="Tjärbyvägen 18 A, Laholm")
add(166,"Busfrö Nytt & Bytt","Halmstad",R3,"L",special="Brogatan 3. Se busfro.se",addr="Brogatan 3, Halmstad")
add(167,"PMU Second Hand","Halmstad",R3,"L",special="Stormgatan 10. Se pmu.se",addr="Stormgatan 10, Halmstad")
add(168,"BK Astrio loppis o Café","Halmstad",R3,"L/C",{"wed":"10–18","thu":"10–18","fri":"10–18","sat":"11–15","sun":"11–15"},season="800 kvm möbler & kuriosa",addr="Kundvägen 2, Flygstaden, Halmstad")
add(169,"Patriks prylar","Halmstad",R3,"A",special="Caféet genomgår ägarbyte – se patriksprylar.se för aktuella tider")
add(170,"IS Halmia Loppis","Halmstad",R3,"L",special="Öppettider ej angivna i guiden")
add(171,"Cityknallens loppis","Halmstad",R3,"L",{"tue":"11–17","wed":"11–17","sat":"11–17","sun":"11–17"},addr="Skepparegatan 70, Halmstad")
add(172,"Fyra vänners Loppis Slättåkra","Halmstad",R3,"L",special="Öppettider ej angivna i guiden",addr="Slättåkra")
add(173,"Antikstället i Slöinge","Falkenberg",R3,"A",{"wed":"10–18","thu":"10–18","fri":"10–18","sat":"10–15"},season="Mån & tis – ring. V. 27–31: mån–fre 10–18, lör 10–15",addr="Stationsgatan 4, Slöinge")
add(174,"Loppis i Årstad","Falkenberg",R3,"L",{"sat":"11–14","sun":"11–14"},season="30/5–30/8 lör–sön (stängt 11–12/7). Juli: ons–sön 11–14",addr="Hebergsvägen 4, Årstad")
add(175,"Agape Foundation","Falkenberg",R3,"L",special="Se agapefoundation.se / Facebook",addr="Stenbrottsvägen 1, Falkenberg")
add(176,"Farmors Lada B&B","Falkenberg",R3,"A",{"mon":"10–16","tue":"10–16","wed":"10–16","thu":"10–16","fri":"10–16","sat":"10–16","sun":"10–16"},season="Öppet varje dag juni, juli & augusti",addr="Lynga 128, Glommen")
add(177,"Fridens vintage","Falkenberg",R3,"A/L",{"sun":"11–15"},season="Sommartid utökat – se Facebook/Instagram",addr="Sjönevad 308, Vessigebro")
add(178,"Väby Loppis Vessigebro","Falkenberg",R3,"L",{"sun":"11–15"},season="19/3–17/12",addr="Väby 401, Vessigebro")
add(179,"Hilles Loppis","Falkenberg",R3,"L",{"sat":"11–15","sun":"11–15"},season="1/3–22/12. Kan variera vid större helger",addr="Köinge 131, Ullared")
add(180,"Gammalt & Nytt i Bockalt","Hylte",R3,"A",{"sun":"14–18"},season="Juli & augusti även lördagar 11–15",addr="Ryabergsvägen 104, Fröslida")
add(181,"Dugatorp Antikt & Loppis","Kungsbacka",R3,"A/L",{"sun":"12–16"},addr="Förlandavägen 98, Fjärås")
add(182,"Godsmagasinet","Kungsbacka",R3,"A",special="Antik inredningsbutik med loppisavdelning. Se antikbutik.se",addr="Tjolöholmsvägen 5, Fjärås")

import urllib.parse
# ---------------- links ----------------
def ig(h): return "https://instagram.com/"+h
def wb(u): return u if u.startswith("http") else "https://"+u
def fbp(h): return "https://facebook.com/"+h
def fbs(q): return "https://www.facebook.com/search/top?q="+urllib.parse.quote(q)
PMU=wb("pmu.se"); BUS=wb("busfro.se")
LINKS={
2:{"fb":fbp("bastadgif.loppis")},
7:{"fb":fbs("Rutigt & Randigt Grevie")},
8:{"web":wb("fif.se")},
9:{"web":wb("viarpform1900.se"),"insta":ig("viarpform1900")},
11:{"insta":ig("johannasfinloppis")},
12:{"web":wb("antikkulan.se")},
14:{"fb":fbs("Hjärnarps GIF loppis")},
15:{"web":PMU},
17:{"fb":fbp("electricmudrecords")},
18:{"insta":ig("villaronneloppis")},
20:{"web":wb("fyndetangelholm.com")},
21:{"web":wb("fyndetangelholm.com"),"insta":ig("fyndetangelholm")},
23:{"insta":ig("starbyvintageochloppis")},
24:{"insta":ig("delsingerantikinredning")},
27:{"web":wb("ossjoskf.com")},
30:{"web":wb("redcross.se/hoganas")},
31:{"insta":ig("retro_hoganas")},
36:{"insta":ig("ryssamollagarden_inredning")},
37:{"web":wb("leksaksmarknaden.se")},
38:{"insta":ig("hoardershop_samlarbutik")},
39:{"web":wb("nr11.se"),"fb":fbp("kuriosan")},
41:{"fb":fbp("rodakorsetsecondhandhbg")},
42:{"web":wb("framtid-hbg.se")},
44:{"web":BUS},
50:{"insta":ig("boutiquenyttonott") if False else ""},
51:{"fb":fbs("Klippans Antikt Retro Loppis")},
54:{"web":wb("starkeld.com"),"insta":ig("starkeld.com")},
55:{"fb":fbs("Citykyrkan Second Hand Örkelljunga")},
57:{"fb":fbs("Fredrik Johansson Loppis i Finja")},
58:{"web":wb("inlamna.se")},
60:{"web":wb("rodakorset.se/hassleholm")},
61:{"fb":fbs("Hässleholm Freeflow Secondhand")},
62:{"insta":ig("retro_living_i_vittsjo")},
67:{"web":wb("vinslovsif.se")},
71:{"web":wb("larssonslager.net")},
72:{"web":wb("svenskakyrkan.se/lackalanga/raststallet")},
73:{"insta":ig("hallitems")},
74:{"insta":ig("vombskaffestuga")},
77:{"web":wb("claeshallen.se"),"insta":ig("claeshallen_malmo")},
78:{"web":BUS},
81:{"web":PMU},
84:{"web":wb("spikenikistan.com")},
85:{"fb":fbs("Kostallet i Heinge")},
86:{"web":wb("osterlenkonsult.se")},
87:{"insta":ig("industrigatan_12")},
89:{"web":wb("borgdesign.se")},
90:{"web":wb("norrvalla.se")},
91:{"web":wb("antiktokuriosa.com")},
92:{"web":wb("degebergagoif.se")},
93:{"web":wb("stalletsecondhand.se")},
94:{"insta":ig("aterbruk_i_magasinet")},
95:{"insta":ig("lillalopppansloppis")},
96:{"insta":ig("retroentrappaupp")},
98:{"fb":fbs("Torget 11 Vintage Secondhand Åhus")},
101:{"insta":ig("petersretrokuriosa")},
102:{"web":PMU},
103:{"insta":ig("majassecondhand.se")},
104:{"insta":ig("lennartsdesignoretro")},
106:{"insta":ig("returen_kristianstad")},
107:{"web":wb("svensflytt.se")},
110:{"fb":fbp("beckasantiktochkuriosa")},
114:{"fb":fbs("Röda Korset Secondhand Karlskrona")},
116:{"web":PMU},
117:{"web":wb("hird-bay-antiques.se")},
118:{"fb":fbs("Tovhults Retro")},
119:{"web":wb("annaskuriosa.se")},
120:{"insta":ig("birgitta_lillstugan")},
122:{"fb":fbs("Jonas second hand Ljungby")},
123:{"web":wb("bolmsoloppis.se"),"insta":ig("bolmsoloppis")},
124:{"insta":ig("helamanniskan_gislaved")},
125:{"web":wb("gnosjohjalper.se")},
126:{"fb":fbs("Hellmans Antik Gnosjö")},
128:{"web":BUS},
129:{"web":PMU},
130:{"web":wb("patina.nu"),"insta":ig("patinaantikviteter")},
132:{"fb":fbs("Loppis på Loen")},
134:{"web":BUS},
135:{"insta":ig("lekarydsantikt")},
136:{"web":wb("ostregard.se"),"insta":ig("ostregard")},
137:{"web":wb("olofshandelsbod.com")},
139:{"fb":fbs("Maris Bonnaloppis Hjortsberga")},
140:{"web":wb("smedjanantik.se")},
143:{"web":wb("almhult.se/guide26")},
144:{"web":wb("antikaffarenitingsryd.se")},
145:{"web":wb("plockprylar.com")},
146:{"web":wb("hatterianspinaler.se")},
149:{"web":wb("mejerietikarlstorp.se")},
151:{"insta":ig("roda_korset_eksjo_kupan")},
152:{"insta":ig("antikt_och_gjutjarn_eksjo")},
153:{"web":BUS},
154:{"web":BUS},
155:{"insta":ig("alltdetgamlagoda")},
156:{"web":BUS},
157:{"web":wb("ilimmared.se")},
159:{"web":wb("rodakorset.se")},
160:{"insta":ig("kattens.loppis"),"fb":fbs("Kattens Loppis och Kuriosa Våxtorp")},
162:{"fb":fbs("Farfars Farmors Antikviteter Laholm")},
163:{"web":wb("konstigastallet.se")},
164:{"web":wb("skogabybk.se")},
165:{"web":wb("laholmsbtkserve.se")},
166:{"web":BUS},
167:{"web":PMU},
169:{"web":wb("patriksprylar.se")},
171:{"insta":ig("cityknallensloppis")},
173:{"insta":ig("antikstället4")},
175:{"web":wb("agapefoundation.se")},
176:{"web":wb("farmorslada.se"),"insta":ig("farmorslada")},
177:{"insta":ig("fridensvintage")},
178:{"fb":fbs("Väby Loppis Vessigebro")},
179:{"fb":fbs("Hilles loppis Ullared")},
180:{"web":wb("missionshusetifroslida.se"),"insta":ig("missionshuset_froslida")},
181:{"fb":fbs("Dugatorp Antikt Loppis Fjärås")},
182:{"web":wb("antikbutik.se")},
}
for m in M:
    lk={k:v for k,v in LINKS.get(m["num"],{}).items() if v}
    m["links"]=lk

# ---------------- generate HTML ----------------
WD=[("mon","Måndag"),("tue","Tisdag"),("wed","Onsdag"),("thu","Torsdag"),("fri","Fredag"),("sat","Lördag"),("sun","Söndag")]
TYPE_LABEL={"A":"Antikt/Design/Retro/Vintage","L":"Loppis/Second hand","Au":"Auktionsfirma","C":"Café","BB":"Bed & Breakfast"}

data_json=json.dumps(M,ensure_ascii=False)

# stats
with_days=sum(1 for m in M if m["days"])
variable=len(M)-with_days

html_out="""<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Loppiskalender 2026 – Skåne, Blekinge, Småland & Halland</title>
<style>
:root{--bg:#0a1a2f;--card:#12273f;--ink:#e8f0fb;--muted:#8ba6c9;--accent:#4f9be8;--accent2:#1c3f63;--line:#26456a;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.5;font-size:16px}
header{background:linear-gradient(135deg,#0e2f56,#071426);color:#fff;padding:26px 20px;border-bottom:1px solid var(--line)}
header h1{font-size:24px;letter-spacing:.2px}
header h1{margin:0 0 6px;font-size:24px}
header p{margin:0;opacity:.92;font-size:15px}
.wrap{max-width:1280px;margin:0 auto;padding:18px 16px 60px}
.controls{position:sticky;top:0;z-index:600;background:rgba(10,26,47,.97);backdrop-filter:blur(6px);padding:12px 0;border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.controls input,.controls select{padding:8px 10px;border:1px solid var(--line);border-radius:8px;font-size:14px;background:var(--card);color:var(--ink)}
.controls input::placeholder{color:var(--muted)}
#q{flex:1;min-width:180px}
.btn{padding:8px 12px;border:1px solid var(--accent);border-radius:8px;font-size:14px;background:var(--accent);color:#04121f;font-weight:600;cursor:pointer}
.btn.ghost{background:transparent;color:var(--accent)}
#locstatus{font-size:12px;color:var(--muted);flex-basis:100%}
.tabs{display:flex;gap:6px;margin:16px 0;flex-wrap:wrap}
.tab{padding:8px 14px;border:1px solid var(--line);border-radius:20px;background:var(--card);color:var(--ink);cursor:pointer;font-size:14px}
.tab.active{background:var(--accent);color:#04121f;border-color:var(--accent);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;align-items:start}
@media(max-width:1000px){.grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:820px){.grid{grid-template-columns:repeat(2,1fr)}}
.daycol{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.daycol h3{margin:0;padding:11px 12px;background:var(--accent2);color:#fff;font-size:15px;line-height:1.35}
.daycol .body{padding:6px 8px}
.item{padding:7px 6px;border-bottom:1px dashed var(--line);font-size:13px}
.item:last-child{border-bottom:none}
.item .nm{font-weight:600}
.item .hr{color:var(--accent);font-weight:600;font-size:12px}
.item .mu{color:var(--muted);font-size:11.5px}
.badge{display:inline-block;font-size:10px;padding:1px 5px;border-radius:4px;background:#1d3c5e;color:#9fc6f2;margin-left:4px;vertical-align:middle}
.lk{margin-left:6px;white-space:nowrap}
.lk a{text-decoration:none;font-size:15px;margin-left:5px}
.todayhead{margin:8px 0 14px}
.todayhead .th-day{font-size:22px;font-weight:700;text-transform:capitalize}
.todayhead .th-sub{color:var(--muted);font-size:14px;margin-top:2px}
.todaygrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
@media(max-width:760px){.todaygrid{grid-template-columns:1fr}}
.card .cbadge{display:inline-block;font-size:10px;padding:1px 6px;border-radius:4px;background:#1d3c5e;color:#9fc6f2;margin-left:6px;vertical-align:middle}
.card .chrs .big{font-size:16px;font-weight:700;color:var(--accent)}
.taglist{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;margin-top:8px}
.tagcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.tagcard .tc-name{font-weight:700;font-size:15px}
.tagcard .tc-meta{color:var(--muted);font-size:13px;margin:2px 0 3px}
.tagcard .tc-info{font-size:14px}
.tagcard .tc-links{margin-top:6px}
@media(max-width:760px){.taglist{grid-template-columns:1fr}}
.count{color:var(--muted);font-size:11px;font-weight:400}
table{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden}
th,td{text-align:left;padding:9px 11px;border-bottom:1px solid var(--line);font-size:13px;vertical-align:top}
th{background:#173350;color:var(--ink)}
tr:hover td{background:#163254}
.reg{display:inline-block;font-size:11px;padding:2px 8px;border-radius:6px;background:#163254;color:#9fc6f2;margin:14px 0 6px}
.note{color:var(--muted);font-size:12px}
.section-title{font-size:18px;font-weight:700;margin:26px 0 8px;padding-left:10px;border-left:4px solid var(--accent)}
.hide{display:none}
.legend{font-size:12px;color:var(--muted);margin:10px 0}
.legend b{color:var(--ink)}
a{color:var(--accent)}
/* day picker (week view on phones) */
.daypicker{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.daychip{flex:1 1 auto;min-width:44px;min-height:46px;padding:6px 8px;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);font-size:15px;cursor:pointer;text-align:center;line-height:1.15}
.daychip .dc{display:block;font-size:11px;color:var(--muted);font-weight:600}
.daychip.active{background:var(--accent);color:#04121f;border-color:var(--accent);font-weight:700}
.daychip.active .dc{color:#04121f}
.daypanel{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.daypanel h3{margin:0;padding:12px 14px;background:var(--accent2);color:#fff;font-size:16px}
.daypanel .body{padding:6px 12px}
/* cards (list view on phones) */
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:10px}
.card .cn{font-weight:700;font-size:15px}
.card .cmeta{color:var(--muted);font-size:12.5px;margin:2px 0 5px}
.card .chrs{font-size:13.5px}
.card .chrs b{color:var(--accent)}
.card .caddr{color:var(--muted);font-size:12px;margin-top:5px}
@media(max-width:760px){
  body{font-size:15px}
  #grid{display:block}
  .controls{gap:8px;padding:10px 0}
  #q,.controls select{flex:1 1 100%;width:100%;font-size:16px;min-height:46px}
  .tab{flex:1 1 auto;text-align:center;min-height:46px;font-size:15px}
  .item{padding:9px 6px;font-size:14px}
  .item .hr{font-size:13px}
  .item .mu{font-size:12px}
  .section-title{font-size:17px}
}
</style>
</head>
<body>
<header>
<h1>🛋️ Loppiskalender 2026</h1>
<p>När är antik- och loppisbutikerna öppna? Skåne, Blekinge, Småland &amp; Halland.</p>
</header>
<div class="wrap">
<div class="controls">
  <input id="q" placeholder="Sök butik, kommun eller adress…">
  <select id="region"><option value="">Alla regioner</option><option>Skåne &amp; Blekinge</option><option>Småland</option><option>Halland</option></select>
  <select id="typ">
    <option value="">Alla typer</option>
    <option value="A">Antikt/Retro/Vintage</option>
    <option value="L">Loppis/Second hand</option>
    <option value="C">Café</option>
    <option value="Au">Auktion</option>
  </select>
</div>
<div class="tabs">
  <div class="tab active" data-view="today">☀️ Öppna idag</div>
  <div class="tab" data-view="week">📅 Veckokalender</div>
  <div class="tab" data-view="list">📋 Lista</div>
</div>
<div class="legend">
  <b>Öppna idag</b> visar butiker som är öppna just idag. <b>Veckokalender</b> visar en vald veckodag och <b>Lista</b> alla butiker med adress och länkar. Sök och filtrera högst upp. <span class="badge">säsong</span> betyder att tiderna varierar under året – se Lista för detaljer. &nbsp;🌐 webbplats · 📘 Facebook · 📷 Instagram
</div>

<div id="todayview"></div>

<div id="weekview" class="hide">
  <div class="grid" id="grid"></div>
  <h2 class="section-title">Öppet vissa datum eller enligt info på nätet <span class="count" id="spcount"></span></h2>
  <div id="specials"></div>
  <h2 class="section-title">Öppettider saknas i guiden <span class="count" id="nacount"></span></h2>
  <div id="naEl"></div>
</div>

<div id="listview" class="hide"></div>

</div>
<script>
const DATA = """+data_json+""";
const WD = """+json.dumps(WD,ensure_ascii=False)+""";
const TYPE_LABEL = """+json.dumps(TYPE_LABEL,ensure_ascii=False)+""";

const q=document.getElementById('q'), regionSel=document.getElementById('region'), typSel=document.getElementById('typ');
const grid=document.getElementById('grid'), specialsEl=document.getElementById('specials'), listview=document.getElementById('listview');
const naEl=document.getElementById('naEl'), spcount=document.getElementById('spcount'), nacount=document.getElementById('nacount');
const weekview=document.getElementById('weekview'), todayview=document.getElementById('todayview');

function esc(s){return (s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function matchType(m,t){if(!t)return true;return (m.typ||'').split('/').includes(t);}
function isNA(m){ return !Object.keys(m.days||{}).length && !m.season && (!m.special || /ej\s+(tydligt\s+)?angivna/i.test(m.special)); }
function linksHtml(m){
  const L=m.links||{}; let s='';
  if(L.web)   s+='<a href="'+L.web+'" target="_blank" rel="noopener" title="Webbplats">🌐</a>';
  if(L.fb)    s+='<a href="'+L.fb+'" target="_blank" rel="noopener" title="Facebook">📘</a>';
  if(L.insta) s+='<a href="'+L.insta+'" target="_blank" rel="noopener" title="Instagram">📷</a>';
  return s? '<span class="lk">'+s+'</span>' : '';
}

function filtered(){
  const term=q.value.trim().toLowerCase(), reg=regionSel.value, t=typSel.value;
  return DATA.filter(m=>{
    if(reg && m.region!==reg) return false;
    if(!matchType(m,t)) return false;
    if(term){const hay=(m.name+' '+m.mun+' '+(m.addr||'')+' '+m.region).toLowerCase(); if(!hay.includes(term))return false;}
    return true;
  });
}
function sortMs(ms){ return ms.slice().sort((a,b)=>a.mun.localeCompare(b.mun,'sv')||a.num-b.num); }
function isMobile(){ return window.matchMedia('(max-width:760px)').matches; }

// weekday of "today" -> our key order (JS getDay: 0=Sun..6=Sat)
const DAYMAP=['sun','mon','tue','wed','thu','fri','sat'];
let selectedDay=DAYMAP[new Date().getDay()];

function openItemHtml(m,key){
  return '<div class="item"><div class="nm">'+esc(m.name)+(m.season?' <span class="badge">säsong</span>':'')+'</div>'+
         '<div class="hr">'+esc(m.days[key])+'</div>'+
         '<div class="mu">'+esc(m.mun)+' · '+esc(m.region)+linksHtml(m)+'</div></div>';
}
function fullHours(m){
  let hrs=''; const dk=Object.keys(m.days||{});
  if(dk.length){
    hrs = WD.filter(([k])=>m.days[k]).map(([k,l])=>'<b>'+l.slice(0,3)+'</b> '+esc(m.days[k])).join(' · ');
    if(m.season) hrs+='<div class="note">'+esc(m.season)+'</div>';
  } else if(m.season){ hrs='<div class="note">'+esc(m.season)+'</div>'; }
  if(m.special) hrs+='<div class="note">'+esc(m.special)+'</div>';
  if(!hrs) hrs='<span class="note">–</span>';
  return hrs;
}
function renderTagList(el, arr, builder){
  el.innerHTML = arr.length ? '<div class="taglist">'+arr.map(m=>'<div class="tagcard">'+builder(m)+'</div>').join('')+'</div>'
                            : '<p class="note">Inga i nuvarande filter.</p>';
}

// --- parse Swedish season text and test whether today's date falls in a listed period ---
const SVMON={januari:1,jan:1,februari:2,feb:2,mars:3,mar:3,april:4,apr:4,maj:5,juni:6,jun:6,juli:7,jul:7,augusti:8,aug:8,september:9,sept:9,sep:9,oktober:10,okt:10,november:11,nov:11,december:12,dec:12};
const MLAST=[0,31,29,31,30,31,30,31,31,30,31,30,31];
const MONWORD=Object.keys(SVMON).sort((a,b)=>b.length-a.length).join('|');
function mval(mm,dd){ return mm*100+dd; }
function parsePoint(str,isEnd){
  str=str.trim().toLowerCase().replace(/[.]/g,''); let m;
  if(m=str.match(new RegExp('^([0-9]{1,2}) *[/] *([0-9]{1,2})$'))) return {m:+m[2],d:+m[1]};
  if(m=str.match(new RegExp('^([0-9]{1,2}) +('+MONWORD+')$'))) return {m:SVMON[m[2]],d:+m[1]};
  if(m=str.match(new RegExp('^('+MONWORD+')$'))) { const mo=SVMON[m[1]]; return {m:mo,d:isEnd?MLAST[mo]:1}; }
  return null;
}
function rangeCovers(a,b,tv){ const s=mval(a.m,a.d),e=mval(b.m,b.d); return s<=e ? (tv>=s&&tv<=e) : (tv>=s||tv<=e); }
function seasonCoversToday(txt){
  if(!txt) return false;
  const now=new Date(), tv=mval(now.getMonth()+1, now.getDate());
  const PT='([0-9]{1,2} *[/] *[0-9]{1,2}|[0-9]{1,2} +(?:'+MONWORD+')|(?:'+MONWORD+'))';
  const re=new RegExp(PT+' *[-–—] *'+PT,'gi');
  let m, any=false;
  while(m=re.exec(txt)){
    any=true;
    const a=parsePoint(m[1],false), b=parsePoint(m[2],true);
    if(a&&b&&a.m&&b.m&&rangeCovers(a,b,tv)) return true;
  }
  if(!any){ // no explicit range: try a month list like "juni, juli & augusti"
    const toks=txt.toLowerCase().split(/[^a-zåäö]+/).map(w=>SVMON[w]).filter(Boolean);
    if(toks.length>=2 && toks.includes(now.getMonth()+1)) return true;
  }
  return false;
}

function renderWeek(){
  const ms=sortMs(filtered());
  if(isMobile()) renderWeekMobile(ms); else renderWeekGrid(ms);
  // rolling/announced + N/A sections (shared by both layouts)
  const sp=sortMs(ms.filter(m=>!Object.keys(m.days||{}).length && !isNA(m) && (m.special||m.season)));
  renderTagList(specialsEl, sp, m=>'<div class="tc-name">'+esc(m.name)+'</div>'+
    '<div class="tc-meta">'+esc(m.mun)+' · '+esc(m.typ||'')+'</div>'+
    '<div class="tc-info">'+esc(m.special||m.season)+'</div>'+
    (linksHtml(m)?'<div class="tc-links">'+linksHtml(m)+'</div>':''));
  spcount.textContent='('+sp.length+')';
  const na=sortMs(ms.filter(isNA));
  renderTagList(naEl, na, m=>'<div class="tc-name">'+esc(m.name)+'</div>'+
    '<div class="tc-meta">'+esc(m.mun)+' · '+esc(m.typ||'')+'</div>'+
    (linksHtml(m)?'<div class="tc-links">'+linksHtml(m)+'</div>':''));
  nacount.textContent='('+na.length+')';
}
function renderWeekGrid(ms){
  grid.innerHTML='';
  WD.forEach(([key,label])=>{
    const open=ms.filter(m=>m.days && m.days[key]);
    const col=document.createElement('div'); col.className='daycol';
    let inner='<h3>'+label+' <span class="count">('+open.length+')</span></h3><div class="body">';
    if(!open.length) inner+='<div class="item note">–</div>';
    open.forEach(m=>inner+=openItemHtml(m,key));
    inner+='</div>'; col.innerHTML=inner; grid.appendChild(col);
  });
}
function renderWeekMobile(ms){
  const counts={}; WD.forEach(([k])=>counts[k]=ms.filter(m=>m.days&&m.days[k]).length);
  if(!WD.some(([k])=>k===selectedDay)) selectedDay=DAYMAP[new Date().getDay()];
  let chips='<div class="daypicker">'+WD.map(([k,l])=>
      '<button class="daychip'+(k===selectedDay?' active':'')+'" data-day="'+k+'"><span class="dc">'+l.slice(0,3)+'</span>'+counts[k]+'</button>').join('')+'</div>';
  const label=WD.find(([k])=>k===selectedDay)[1];
  const open=ms.filter(m=>m.days&&m.days[selectedDay]);
  let panel='<div class="daypanel"><h3>'+label+' <span class="count">('+open.length+' öppna)</span></h3><div class="body">';
  panel += open.length? open.map(m=>openItemHtml(m,selectedDay)).join('') : '<div class="item note">Inga butiker med fasta tider denna dag.</div>';
  panel+='</div></div>';
  grid.innerHTML=chips+panel;
  grid.querySelectorAll('.daychip').forEach(b=>b.onclick=()=>{ selectedDay=b.dataset.day; renderWeek(); });
}

function renderList(){
  const ms=filtered();
  const regions=['Skåne & Blekinge','Småland','Halland'];
  if(isMobile()) renderListMobile(ms,regions); else renderListDesktop(ms,regions);
}
function renderListDesktop(ms,regions){
  let html='';
  regions.forEach(r=>{
    const rows=sortMs(ms.filter(m=>m.region===r));
    if(!rows.length) return;
    html+='<h2 class="section-title">'+r+' <span class="count">('+rows.length+')</span></h2>';
    html+='<table><thead><tr><th>#</th><th>Butik</th><th>Kommun</th><th>Typ</th><th>Öppettider</th><th>Adress / länkar</th></tr></thead><tbody>';
    rows.forEach(m=>{
      html+='<tr><td>'+m.num+'</td><td><b>'+esc(m.name)+'</b></td><td>'+esc(m.mun)+'</td>'+
            '<td>'+esc(m.typ||'')+'</td><td>'+fullHours(m)+'</td>'+
            '<td class="note">'+esc(m.addr||'')+' '+linksHtml(m)+'</td></tr>';
    });
    html+='</tbody></table>';
  });
  listview.innerHTML=html||'<p class="note">Inga träffar.</p>';
}
function renderListMobile(ms,regions){
  let html='';
  regions.forEach(r=>{
    const rows=sortMs(ms.filter(m=>m.region===r));
    if(!rows.length) return;
    html+='<h2 class="section-title">'+r+' <span class="count">('+rows.length+')</span></h2>';
    rows.forEach(m=>{
      html+='<div class="card"><div class="cn">'+esc(m.name)+'</div>'+
            '<div class="cmeta">'+esc(m.mun)+' · '+esc(m.typ||'')+'</div>'+
            '<div class="chrs">'+fullHours(m)+'</div>'+
            (m.addr?'<div class="caddr">'+esc(m.addr)+'</div>':'')+
            (linksHtml(m)?'<div style="margin-top:6px">'+linksHtml(m)+'</div>':'')+'</div>';
    });
  });
  listview.innerHTML=html||'<p class="note">Inga träffar.</p>';
}

function renderToday(){
  const key=DAYMAP[new Date().getDay()];
  const label=(WD.find(([k])=>k===key)||['','']) [1];
  const dateStr=new Date().toLocaleDateString('sv-SE',{day:'numeric',month:'long',year:'numeric'});
  const open=sortMs(filtered().filter(m=>m.days&&m.days[key]));
  let html='<div class="todayhead"><div class="th-day">'+esc(label)+'</div>'+
           '<div class="th-sub">'+esc(dateStr)+' · '+open.length+' butiker öppna med fasta tider</div></div>';
  if(open.length){
    html+='<div class="todaygrid">'+open.map(m=>
      '<div class="card"><div class="cn">'+esc(m.name)+(m.season?'<span class="cbadge">säsong</span>':'')+'</div>'+
      '<div class="cmeta">'+esc(m.mun)+' · '+esc(m.region)+' · '+esc(m.typ||'')+'</div>'+
      '<div class="chrs"><span class="big">'+esc(m.days[key])+'</span></div>'+
      (m.addr?'<div class="caddr">'+esc(m.addr)+'</div>':'')+
      (linksHtml(m)?'<div style="margin-top:6px">'+linksHtml(m)+'</div>':'')+'</div>').join('')+'</div>';
  } else {
    html+='<p class="note">Inga butiker med fasta öppettider idag.</p>';
  }
  // "possibly open": seasonal shops whose period covers today but that aren't in the confirmed list
  const possibly=sortMs(filtered().filter(m=> !(m.days&&m.days[key]) && seasonCoversToday(m.season)));
  html+='<h2 class="section-title">Kanske öppet idag – säsong <span class="count">('+possibly.length+')</span></h2>'+
        '<p class="note">Butiker vars säsong täcker dagens datum. Öppettiderna varierar (t.ex. bara helger) – läs texten och kontrollera gärna innan besök.</p>';
  if(possibly.length){
    html+='<div class="taglist">'+possibly.map(m=>'<div class="tagcard">'+
      '<div class="tc-name">'+esc(m.name)+'</div>'+
      '<div class="tc-meta">'+esc(m.mun)+' · '+esc(m.region)+' · '+esc(m.typ||'')+'</div>'+
      '<div class="tc-info">'+esc(m.season)+'</div>'+
      (linksHtml(m)?'<div class="tc-links">'+linksHtml(m)+'</div>':'')+'</div>').join('')+'</div>';
  } else {
    html+='<p class="note">Inga säsongsbutiker med period som täcker idag.</p>';
  }
  html+='<p class="note" style="margin-top:16px">Butiker med rörliga/aviserade tider (t.ex. "se Facebook") kan också vara öppna – se <b>Lista</b>.</p>';
  todayview.innerHTML=html;
}

let view='today';
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{
  document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
  t.classList.add('active'); view=t.dataset.view;
  todayview.classList.toggle('hide',view!=='today');
  weekview.classList.toggle('hide',view!=='week');
  listview.classList.toggle('hide',view!=='list');
  render();
});
function render(){ if(view==='today') renderToday(); else if(view==='week') renderWeek(); else renderList(); }
[q,regionSel,typSel].forEach(el=>el.addEventListener('input',render));
let rz; window.addEventListener('resize',()=>{ clearTimeout(rz); rz=setTimeout(render,150); });
render();
</script>
</body>
</html>
"""
import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"index.html")
open(OUT,"w",encoding="utf-8").write(html_out)
print("Wrote",OUT)
print("Total:",len(M),"| with weekly hours:",with_days,"| variable/announced:",variable)
