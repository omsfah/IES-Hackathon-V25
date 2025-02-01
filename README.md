# IES-Hackathon-V25
Hackathon i regi av IES, med case fra Mimiro
# Dag 1, innledende tanker
Case 1: Kalver og oppfølging første 90 dager
- Åpenbar BLE kandidat, benytte findmy støtten i nRF5* til å spore kalven i dens omgivelser. Kan detektere om den står, ligger, bevegelse +++, dette kan korreleres mot andre dyr og gi en vibe på trivsel.
- Kan også se på monitorering av forhold i bås, typ temp og ph på dekke er indikativt på forholdene

- Data
	- Posisjonsdata
		- Vinkel
		- Bevegelsesmønster
	- Foring og foringssekvens
		- Hvor ofte spiser kalven
		- Hvor lenge spiser kalven
		- Hvor mye drikker den
	- Flokkatferd
		- Beveger seg fra ved sykdom?
	- Temperatur og andre indikatorer?
		- Puls
			- Stressindikator
		- Vibrasjoner
		- Lyd
			- Støy og stress?
	- Fuktighet
	- Gassdeteksjon (O2 nivå i fjøs?+++)
	- Støv/ PPM3 i omgivelse
	
Hvordan samle data:
	Allerede på microbit: Posisjonsdata, temp sensor, akselerometer, mikrofon

Mangler:
	Puls

Generelt systemoppsett:
	Stasjon per bås, predefinert posisjon, mulig flere for triangulering? Evt andre sensorer, stasjonen vil ha mulighet for ekstern strøm, så evt strømkrevende deteksjon burde tas her
 
 En sensornode per ku, trolig øre eller nese? Evt andre posisjoner?
 
 Korrelere vekstrate mot midjemål (Høyde med akselerometer, mer presist?)
 
 Batterilevetid: 6mnd, dekker hele vekstfasen. Antar kyr har syklisk drektighet, kan som future stretch tenke på avlsprosess og inseminering, evt kan man gjenbruke markører på kyr under svangerskap?

- Støv/ PPM3 i omgivelse

Plan for imorgen:
1: Fordeling av arbeid
	- Git repo
	- Hvordan jobber vi
	- Overordnet plan
	- Pitch? (Pass på å ikke være for spesifikk)
		"7 datapunkter til suksess"
		Binde pitch til tallgrunnlag?
		Ikke begrense oss for mye i pitchen
2: Arbeidsøkt 1
	WIP teste konsepter
	Sette standard rammer (Jeg forventer data slik)
3: Pitchøkt
4: Arbeidsøkt 2
	Polering

Kontaktinfo:
Olaf - --Redacted--
Martin - --Redacted--
Sara - --Redacted--
Sebastian - --Redacted--

Videre tanker: Fertilitetssyklus styres vha lys, prosessen for inseminasjon krever dyrlege + bestilling av oksesæd + riktig timing, 65% suksessrate i norge, 85% i USA (Clean up bull). Kyr er veldig følsomme for tempvariasjon, temperaturstress. Økende kortisol grunnet temp variasjon.
