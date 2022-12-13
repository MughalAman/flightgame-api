import json

all_jobs = {
        "job_name": [
        "Haravoi", "Tee töitä mäkkärissä,", "Pese autoja", "Siivoa kauppakeskusta", "Aja nurmikkoa",
        "Myy keksimääsi virvoitusjuomaa", "Kudo sukkia ja myy niitä", "Leikkaa hiuksia", "Kiillota kenkiä",
        "Myy leivoksia", "Siivoa vessoja", "Myy kiviä", "Myy omenoita", "Myy päärynöitä",
        "Anna hierontoja", "Kerää banaanaeja ja myy niitä", "Voita shakkiturnaus", "Myy tekemiäsi housuja",
        "Myy fidget spinnereitä", "Leikkaa partoja", "Väärennä isoäitisi testamentti", "Varasta rahaa mummoilta",
        "Myy aseita", "Myy itseäsi", "Salamurhaa joku", "Varasta ja myy wolt-tilauksia",
        "Myy elimiä", "Ryöstä pankki", "Myy sarvikuonon sarvia", "Varasta punaiselta ristiltä"
        ],

        "is_bad": [
        "False", "False", "False", "False", "False", "False", "False", "False", "False", "False",
        "False", "False", "False", "False", "False", "False", "False", "False", "False", "False",
        "True", "True", "True", "True", "True", "True", "True", "True", "True", "True"
        ],

        "reward": [
        150,250,350,450,500,120,220,320,420,520,130,230,330,430,530,140,240,340,440,540,
        1000,1200,2000,1750,1450,1100,2100,2050,2100,1550
        ],

        "penalty_message" : [
        "Onnistuit rikkomaan haravan ja joudut ostamaan uuden.",
        "Tarjoilit asiakkaalle pilaantunutta ruokaa ja sait potkut",
        "Naarmutit asiakkaan autoa ja juoksit tapahtumapaikalta karkuun",
        "Ajoit siivouskoneella seinään ja pakenit",
        "Rikoit asiakkaasi ruoholeikkurin ja piilotit sen puskaan",
        "Virvoitusjuomasi aiheutti sairaskohtauksia asiakkailla",
        "Kaaduit kutomapuikon pälle ja se puhkaisi rintakehäsi. Joudut sairaalaan",
        "Leikkasit asiakkaalta kaikki hiukset ja sait potkut.",
        "Käytit syövyttävää ainetta ja pilasit asiakkaan kengät",
        "Käytit pilaantuneita aineita ja leivoksesi eivät myyyneet",
        "Sait infektion ja jouduit sairaalaan",
        "Asiakas suuttui huonosta palvelusta ja heitti kiven naamaasi.",
        "Omenat olivat pilaantuneita.",
        "Päärynöissä oli saasteita.",
        "Käyttäydyit epäasiallisesti ja menetit asiakkaasi",
        "Karannut apina vei tuotteesi.",
        "Huijasit ja sinut diskattiin",
        "Ompelit huonosti housut ja jokainen hajosi.",
        "Asiakas huijasi kaikki tuotteet sinulta.",
        "Viilsit asiakkaan korvan irti ja karkasit.",
        "Testamentissa oli kirjoitusvirhe ja sinua syytetään väärennysrikoksesta.",
        "Mummo osasi Brasilialaista jiu-jitsua ja mursi niskasi",
        "Laatikossa ollut käsikranaatti räjäytti myyntihetkellä sinut ja asiakkaasi",
        "Sinut kidnapattiin ja vietiin Pohjois-Koreaan työleirille.",
        "Olit huolimaton ja liukastuit verilammikkoon. Kaaduit suoraan veitsesi päälle.",
        "Poliisit näkivät varkauden ja pidättivät sinut.",
        "Lupasit ostajille liikaa ja he ottivat maksuksi molemmat silmäsi",
        "Vartijat taklasivat sinut ennen kun ehdit vetää aseesi esiin.",
        "Asiakkaasi oli salapoliisi joka ilmiantoi sinut",
        "Punainen risti sai sinut kiinni ja vei kaiken veresi."
        ]


    }

print(json.dumps(all_jobs))

