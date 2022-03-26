#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Corvophraseur New Generation
	-----------------------------
	copyright 2010, Pierre-Alain Dorange
	
	Adapted from the AppleScript CorvoX (for Adium/Mac) from Aurelien
		http://www.adiumxtras.com/index.php?a=xtras&xtra_id=2646
	Original concept : Luc 'Skywalker' Heinrich
		Corvophraseur 2 (for MacOS 9)

	BSD Licence
"""

__author__="Pierre-Alain Dorange (pdorange@mac.com)"
__date__="6 avril 2010"
__copyright__="Copyright 2010, Pierre-Alain Dorange"
__license__="BSD"
__version__="0.1a"

import random

verbs = ( 	("accéder",2), ("accélérer",2), ("ajuster",2), ("améliorer",2), ("amplifier",2), 
			("analyser",2), ("annuler",2), ("bouffoner",2), ("bouillir",2), ("calcifier",2), 
			("compresser",2), ("créer",2), ("décélérer",2), ("décoder",2), ("décrypter",2), 
			("déstabiliser",2), ("détecter",2), ("diminuer",2), ("dupliquer",2), ("encoder",2), 
			("encrypter",2), ("fracasser",2), ("induire",2), ("inhiber",2), ("inverser",2), 
			("ioniser",2), ("moduler",2), ("neutraliser",2), ("optimiser",2), ("phaser",2), 
			("polariser",2), ("pournifier",2), ("réarranger",2), ("recombiner",2), ("recréer",2), 
			("rediriger",2), ("relayer",2), ("scanner",2), ("signaler",2), ("stabilisr",2), 
			("surcharger",2), ("transformer",2), ("trouer",2), ("zombifier",2))
adjs = (	("à court rayon d'action", "à court rayon d'action", 0), ("à grand rayon d'action", "à grand rayon d'action", 0), 
			("à haute vitesse", "à haute vitesse", 0), ("adaptatif", "adaptative", 2), ("alternatif", "alternative", 2), 
			("alvéolé", "alvéolée", 2), ("artificiel", "artificielle", 2), ("atomique", "atomique", 2), 
			("baleiné", "baleinée", 2), ("ballistique", "ballistique", 2), ("basse vitesse", "basse vitesse", 2), 
			("binaire", "binaire", 2), ("bouffoné", "bouffonée", 2), ("calorifique", "calorifique", 2), 
			("carpien", "carpienne", 2), ("centrique", "centrique", 2), ("compressé", "compressée", 2), 
			("connotatif", "connotative", 2), ("corporel", "corporelle", 2), ("cythérien", "cythérienne", 2), 
			("dimensionnel", "dimensionnelle", 2), ("directionnel", "directionnelle", 2), ("dirigé", "dirigée", 2), 
			("dynamique", "dynamique", 2), ("encrypté", "encryptée", 2), ("génique", "génique", 2), 
			("gildoique", "gildoique", 2), ("gravifique", "gravifique", 2), ("gravitationnel", "gravitationnelle", 2), 
			("holographique", "holographique", 2), ("instable", "instable", 2), ("interstellaire", "interstellaire", 2), 
			("ionisé", "ionisée", 2), ("linéaire", "linéaire", 2), ("localisé", "localisée", 2), ("magnétique", "magnétique", 2), 
			("mécanique", "mécanique", 2), ("microscopique", "microscopique", 2), ("modulaire", "modulaire", 2), 
			("moléculaire", "moléclaire", 2), ("moncturien", "moncturienne", 2), ("navigationnel", "navigationnelle", 2), 
			("oblatif", "oblative", 2), ("ossiphazolé", "ossiphazolée", 2), ("parabolique", "parabolique", 2), 
			("parallele", "parallele", 2), ("phasé", "phasée", 2), ("phasique", "phasique", 2), ("plutonnant", "plutonnante", 2), 
			("plutonné", "plutonnée", 2), ("pourniflant", "pourniflante", 2), ("quantique", "quantique", 2), 
			("refroidi", "refroidie", 2), ("réplicatif", "réplicative", 2), ("résistant", "résistante", 2), 
			("résonnant", "résonnante", 2), ("spatial", "spatiale", 2), ("spinoidal", "spinoidale", 2), ("statique", "statique", 2), 
			("stellaire", "stellaire", 2), ("temporel", "temporelle", 2), ("trigloidal", "trigloidale", 2), ("valvué", "valvuée",2), 
			("véloce","véloce",2), ("vibratile","vibratile",2))
nouns = ( 	("aimant",1,2), ("alignement",1,2), ("amplificateur",1,2), ("anihilateur",1,2), ("capsule",2,2), 
			("assimilateur",1,2), ("balise",2,2), ("bouclier",1,2), ("bouffon",1,2), ("buffer",1,2), 
			("calcifrage",1,2), ("capacité",2,2), ("capilectomie",2,2), ("causalité",2,2), ("chambre",2,2), 
			("champ",1,2), ("champ de force",1,2), ("coeur",1,2), ("conduit",1,2), ("configuration",2,2), 
			("continuum",1,2), ("convertisseur",1,2), ("corridor",1,2), ("crevasse",2,2), ("cristal",1,2), 
			("cybergement",1,2), ("déflecteur",1,2), ("désintégrateur",1,2), ("détonateur",1,2), 
			("diagnostic",1,2), ("disrupteur",1,2), ("distortion",2,2), ("écho",1,2), ("efficience",2,2), 
			("émission",2,2), ("endiguement",1,2), ("énergie",2,2), ("entité",2,2), ("filament",1,2), 
			("filtre",1,2), ("flot",1,2), ("flux",1,2), ("force",2,2), ("formation",2,2), ("fragment",1,2), 
			("fragmenticule",1,2), ("fréquence",2,2), ("gain",1,2), ("générateur",1,2), ("gicleur",1,2), 
			("glomérule",2,2), ("goniotron",1,2), ("graviton",1,2), ("grille",2,2), ("hologramme",1,2), 
			("impulsion",2,2), ("incursion",2,2), ("inducteur",1,2), ("inertie",1,2), ("inhibiteur",1,2), 
			("laplaxmol",1,2), ("matiere",2,2), ("matrice",2,2), ("mécanisme",1,2), ("mine",2,2), 
			("mitochondrie",2,2), ("moteur",1,2), ("moulinotron",1,2), ("multiplexeur",1,2), ("nacelle",2,2), 
			("noyau",1,2), ("nuage",1,2), ("ordinateur",1,2), ("papsouille",2,2), ("parallax",1,2), 
			("particule",2,2), ("plasma",1,2), ("plutonneur",1,2), ("porteuse",2,2), ("poussée",2,2), 
			("radiation",2,2), ("rayon",1,2), ("réhausseur",1,2), ("relai",1,2), ("rémouleur",1,2), 
			("réplicateur",1,2), ("réplication",2,2), ("réseau",1,2), ("résonnateur",1,2), ("ressort",1,2), 
			("rotation",2,2), ("schisme",1,2), ("séquence",2,2), ("signal",1,2), ("signature",2,2), 
			("singularité",2,2), ("sonde",2,2), ("spouniseur",1,2), ("survolteur",1,2), ("sustentation",2,2), 
			("syntagme",1,2), ("tachyon",1,2), ("transistor",1,2), ("translateur",1,2), ("transporteur",1,2), 
			("trigloide",1,2), ("trophoblaste",1,2), ("tropisme",1,2), ("tube",1,2), ("tunnel",1,2), 
			("turbulence",1,2), ("vagissement",1,2), ("vague",2,2), ("vibration",2,2), ("vide",1,2), ("vortex",1,2))
prefix = ( 	"aéro","ana","anti","auto","bi","bulbo","capillo","crypto","extra","hepta","hétéro",
			"homo","méta","micro","morpho","morvo","multi","néo","non","nucléo","octo","penta",
			"poly","proto","pseudo","quadri","rétro","servo","spiro","sub","sur","thermo","theta",
			"trans","tri","turbo" )
gabarits = ("Si nous pouvons [v] [n] [a], nous devrions [v] [n] [a] et [v] [n]", 
			"Capitaine, je ne peux pas [v] [n] parce que [n] [a] est sur le point [d] [n] [a] !",
			"[v] [n] [a] est illogique, puisque [n] [a] va [v] [n] [a].", 
			"Il est possible que [n] [a] puisse [v] [n] [a], mais seulement si nous pouvons [v] [n] [a] et [v] [n] [a] !", 
			"Pas de panique ! [v] [n] [a] ne nous empêche pas [d] [n] [a] ni même [d] [n] [a].", 
			"Voici [n] [a] dont il est temps [d] [n] [a] sans oublier [d] [n] [a].", 
			"Damned, [n] [a] ne peut pas [v] [n] [a] ! Nous allons être obligé [d] [n] [a]...", 
			"Tout va bien a bord. [n] [a] semble [v] correctement. Mais nous devrions [v] [n] [a] pour plus de sécurité.", 
			"Alerte ! [n] [a] semble [v] dangereusement ! Il faut [v] [n] [a] d'urgence !!!", 
			"Veuillez [v] [n] [a] avant [d] sciemment.")

def get_gabarit():
	i=int(len(gabarits)*random.random())
	return gabarits[i]
	
def substitute_verb(prep):
	i=int(len(verbs)*random.random())
	v=verbs[i][0]
	p=verbs[i][1]
	if p==1:
		v="%s-%s" % (substitute_prefix(),v)
	elif p==2:
		if random.random()<0.2:
			v="%s-%s" % (substitute_prefix(),v)
	if prep:
		if check_voyelle(v):
			v="d'%s" % v
		else:
			v="de %s" % v
	return v

def substitute_prefix():
	i=int(len(prefix)*random.random())
	return prefix[i]

def substitute_adj(genre):
	i=int(len(adjs)*random.random())
	return adjs[i][genre]

def substitute_noun(genre):
	i=int(len(nouns)*random.random())
	n=nouns[i][0]	# the nouns
	g=nouns[i][1]	# the genre
	p=nouns[i][2]	# prefix ?
	withAdj=False
	
	if genre>0 and genre<>g :
		substitute_noun(genre)
	else:
		if p==1:
			n="%s-%s" % (substitute_prefix(),n)
		elif p==2:
			if random.random()<0.2:
				n="%s-%s" % (substitute_prefix(),n)
		if withAdj:
			n="%s %s" % (n,substitute_adj(g))
	if check_voyelle(n):
		n="l'%s" % n
	elif g==1:
		n="le %s" % n
	else:
		n="la %s" % n
		
	return n

def check_voyelle(v):
	s="aeiouyéh"
	return (s.find(v[0])>=00)

def main():
	print "Corvophraseur (New Generation)",__version__
	print "---------------------------------------------"

	p0=get_gabarit()
	p1=""
	
	pattern=("[v]","[n]","[a]","[d]","[m]","[f]")
	
	for w in p0.split():
		pat=False
		for p in pattern:
			if w.find(p)>=0:
				s=""
				if p==pattern[0]:
					s=substitute_verb(False)
				if p==pattern[1]:
					s=substitute_noun(0)
				if p==pattern[2]:
					s=substitute_adj(0)
				if p==pattern[3]:
					s=substitute_verb(True)
				if p==pattern[4]:
					s=substitute_noun(1)
				if p==pattern[5]:
					s=substitute_noun(2)
				pat=True
				w=s
		if len(p1)==0:
			p1=w
		else:
			p1=" ".join((p1,w))

	print p1		
	
if __name__=="__main__":
	main()
