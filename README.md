# kursadarbs1

Romans Drozdovs 221REB069
Aleksandrs Šenkarenko 221RDB370

# Bot:

Tika izmantotas bibliotēkas telegram, asyncio, datetime, time

telegram:
Projektā tika izmantota asinhrona telegram bibliotēka, lai ērti saņemtu šodienas lekciju grafiku, pateicoties kura ar komandu /today var iegūt grafiku tieši no telefona ērtajā ziņojumu lietotnē.
Ar šo bibliotēku tika izveidots "bezgalīgs cikls", kas reāllaikā izseko notikumiem, kas ienāk no api telegram, apstrādā tos un sūta atpakaļ informāciju. Mūsu gadījumā bots saņem komandu un atbild uz to, sūtot pilnu šodienas priekšmetu grafiku.

Lai palaistu botu, jāaizstāj 'token' lauka vērtība 23. rindā ar jūsu bota tokena vērtību.

asyncio:
Paša bibliotēka asyncio tika izmantota botā "bezgalīgajam ciklam", lai notikumus iegūtu un apstrādātu asinhroni. Taču tā kā funkcija get_data() darbojas sinhroni un bloķē kopējo botu ciklu, nācās ietīt šo funkciju asinhronā korutīnā, izmantojot run_in_executor(). To izsaucam ar saņemto "bezgalīgo ciklu", izmantojot funkciju asyncio.get_event_loop(), lai bots neslēgtu darbu un turpinātu reaģēt uz notikumiem, kas uz to ienāk.

time:
Šī bibliotēka tiek izmantota, lai aizkavētu selenium darbu ar time.sleep() funkciju. To izmanto sinhronā funkcijā get_data(), un tā darbojas sinhroni. Šīs bibliotēkas izmantošana ir saistīta ar to, ka paša funkcija ir sinhrona, un asyncio.sleep() metode netika piemērots.

datetime:
Šī bibliotēka tiek izmantota, lai iegūtu informāciju par pašreizējo dienu, mēnesi un gadu, izmantojot datetime.datetime.utcnow() funkciju.

# Parser:
Tika izmantotas silenium biblioteka, lai stradatu ar vietnes datiem un nonemtu informāciju par studenta kursa, grupas un lekcijas informaciju

programmura atver vietni, kurā atlasa vēlamo kursu un grupu, pēc tam, pamatojoties uz datumu, nolasa informāciju par lekcijām, kas notiek konkrētajā dienā un atgriež rezultātu botam, kas pēc tam parāda informāciju par lekcijām, kuras būs.  ja lekciju nav , tad programma pēc informācijas pārbaudes parāda, ka tajā dienā lekciju nav.
