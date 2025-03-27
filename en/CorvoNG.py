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
__translator__ = "tkanos"
__date__="6 avril 2010"
__copyright__="Copyright 2010, Pierre-Alain Dorange"
__license__="BSD"
__version__="0.1a"

import random

verbs = ( 	("access",2), ("speed up",2), ("adjust",2), ("upgrade",2), ("amplify",2), 
			("analyse",2), ("cancel",2), ("nullify",2), ("override",2), ("boil",2), ("calcify",2), 
			("compress",2), ("create",2), ("form",2), ("decelerate",2), ("decode",2), ("decipher",2), ("decrypt",2), 
			("destabilize",2), ("detect",2), ("decrease",2), ("replicate",2), ("encode",2), 
			("encrypt",2), ("shatter",2), ("smash",2), ("induce",2), ("inhibit",2), ("disable",2), ("reverse",2),
			("ionize",2), ("module",2), ("neutralize",2), ("optimize",2), ("phase",2), 
			("polarize",2), ("purify",2), ("rearrange",2), ("recombine",2), ("recreate",2), 
			("redirect",2), ("relay",2), ("take over",2), ("scan",2), ("report",2), ("stabilize",2), ("normalize",2), 
			("overload",2), ("transform",2), ("process",2), ("make",2), ("hole",2), ("zombify",2),  ("helm",2), ("engage",2)
		) 
adjs = (	("short range", "short range", 0), ("wide range", "wide range", 0), 
			("high speed", "high speed", 0), ("adaptive", "adaptive", 2), ("alternative", "alternative", 2), 
			("honeycombed", "honeycombed", 2), ("artificial", "artificial", 2), ("atomic", "atomic", 2), ("nuclear", "nuclear", 2), 
			("whaled", "whaled", 2), ("ballistic", "ballistic", 2), ("low speed", "low speed", 2), ("decentralised", "decentralised", 2), 
			("binary", "binary", 2), ("duple", "duple", 2), ("calorific", "calorific", 2), 
			("carpal", "carpal", 2), ("centric", "centric", 2), ("centered", "centered", 2), ("compressed", "compressed", 2), 
			("connotative", "connotative", 2), ("corporeal", "corporeal", 2), ("cytherian", "cytherian", 2), 
			("dimensional", "dimensional", 2), ("directional", "directional", 2), ("directed", "directed", 2), 
			("dynamic", "dynamic", 2), ("encrypted", "encrypted", 2), ("genetic", "genetic", 2), 
			("gildoic", "gildoic", 2), ("gravity", "gravity", 2), ("gravitational", "gravitational", 2), 
			("holographic", "holographic", 2), ("unstable", "unstable", 2), ("interstellar", "interstellar", 2), 
			("ionized", "ionized", 2), ("linear", "linear", 2), ("localized", "localized", 2), ("magnetic", "magnetic", 2), 
			("mechanical", "mechanical", 2), ("microscopic", "microscopic", 2), ("modular", "modular", 2), 
			("molecular", "molecular", 2), ("moncturian", "moncturian", 2), ("navigational", "navigational", 2), 
			("oblative", "oblative", 2), ("ossiphazole", "ossiphazole", 2), ("parabolic", "parabolic", 2), 
			("parallel", "parallel", 2), ("phased", "phased", 2), ("phasic", "phasic", 2), ("plutonizing", "plutonizing", 2), 
			("plutonized", "plutonized", 2), ("pouring", "pouring", 2), ("quantic", "quantic", 2), ("quantum", "quantum", 2), 
			("cooled", "cooled", 2), ("replicative", "replicative", 2), ("resistant", "resistant", 2), 
			("resonant", "resonant", 2), ("spatial", "spatial", 2), ("spinoidal", "spinoidal", 2), ("static", "static", 2), 
			("stellar", "stellar", 2), ("temporal", "temporal", 2), ("trigloidal", "trigloidal", 2), ("valved", "valved",2), 
			("swift","swift",2), ("vibratile","vibratile",2), ("magnifying","magnifying",2)
		)
nouns = ( 	("magnet",1,2), ("alignment",1,2), ("amplifier",1,2), ("anihilator",1,2), ("capsule",2,2), 
			("assimilator",1,2), ("beacon",2,2), ("tag",2,2), ("shield",1,2), 
			("calcificator",1,2), ("capacity",2,2), ("capilectomy",2,2), ("causality",2,2), ("room",2,2), 
			("field",1,2), ("force field",1,2), ("heart",1,2), ("pipe",1,2), ("configuration",2,2), 
			("continuum",1,2), ("converter",1,2), ("corridor",1,2), ("rift",2,2), ("cristal",1,2), 
			("cyberment",1,2), ("deflector",1,2), ("disintegrator",1,2), ("detonator",1,2), ("trigger",1,2), 
			("diagnostic",1,2), ("disruptor",1,2), ("distortion",2,2), ("echo",1,2), ("efficiency",2,2), 
			("emission",2,2), ("transmission",2,2), ("containment",1,2), ("energy",2,2), ("entity",2,2), ("filament",1,2), 
			("filter",1,2), ("flow",1,2), ("flood",1,2), ("stream",1,2), ("flux",1,2), ("force",2,2), ("forming",2,2), ("fragment",1,2), ("chip",1,2), 
			("motherboard",1,2),  ("fragmenticle",1,2), ("frequency",2,2), ("gain",1,2), ("generator",1,2), ("jet",1,2),  ("spray",1,2), 
			("glomerulus",2,2), ("goniotron",1,2), ("graviton",1,2), ("grid",2,2), ("hologram",1,2), 
			("impulsion",2,2), ("incursion",2,2), ("inductor",1,2), ("inertia",1,2), ("inhibitor",1,2), 
			("plaxmol",1,2), ("matter",2,2), ("matrix",2,2), ("mecanism",1,2), ("bomb",2,2), 
			("mitochondria",2,2), ("engine",1,2), ("motor",1,2), ("moulinotron",1,2), ("reelmill",1,2), ("multiplexer",1,2), ("muxer",1,2), ("pod",2,2), 
			("core",1,2), ("nucleur",1,2), ("cloud",1,2), ("computer",1,2), ("parallax",1,2), 
			("particle",2,2), ("plasma",1,2), ("plutonator",1,2), ("bearer",2,2), ("impulse",2,2), 
			("radiation",2,2), ("beam",1,2), ("booster",1,2), ("relay",1,2), ("grinder",1,2), 
			("replicator",1,2), ("replicatant",1,2),("replication",2,2), ("network",1,2), ("resonator",1,2), ("spring",1,2), 
			("rotation",2,2), ("schism",1,2), ("sequence",2,2), ("signal",1,2), ("signature",2,2), 
			("singularity",2,2), ("probe",2,2), ("sensor",2,2), ("sponsor",1,2), ("sustenance",2,2), 
			("syntagm",1,2), ("tachyon",1,2), ("transistor",1,2), ("translator",1,2), ("transporter",1,2), 
			("trigloid",1,2), ("trophoblast",1,2), ("tropism",1,2), ("tube",1,2), ("conduit",1,2), ("tunnel",1,2), 
			("turbulence",1,2), ("wave",2,2), ("vibration",2,2), ("vacuum",1,2), ("void",1,2), ("vortex",1,2)
		)
prefix = ( 	"aero","ana","anti","auto","bi","bulbo","capillo","crypto","cyber", "extra","hepta","hetero",
			"homo","meta","micro","morpho","morvo","multi","neo","non","nucleo","octo","penta",
			"poly","proto","pseudo","quadri","rétro","servo","spiro","sub","sur","thermo","theta",
			"trans","tri","turbo" )
gabarits = ("If we can [v] the [a] [n] , we could [v] the [a] [n] and [v] the [n]", 
			"Captain, I can't [v] the [n] because the [a] [n] is about [d] the [a] [n]  !",
			"Captain, we have to [v] the [a] [n] into the [a] to avoid a [a] [n]!",
			"[v] the [a] [n] is illogical, because the [a] [n] is going to [v] the [a] [n].", 
			"It's possible that the [a] [n] could [v] the [a] [n], but only if we could [v] the [a] [n] and [v] the [a] [n] !", 
			"Don't panic ! [v] the [a] [n] so we could avoid [d] the [a] [n] without [d] the [a] [n].", 
			"Here is the [a] [n] and it's time [d] the [a] [n] without [d] the [a] [n].", 
			"Damn, the [a] [n] could not [v] the [a] [n] ! we will be obliged [d] the [a] [n]...", 
			"All is well on board. The [a] [n] seems to [v] properly. But we should [v] the [a] [n] for more safety.", 
			"Warning ! The [a] [n] seems [v] dangerously ! We have to [v] the [a] [n] urgently !!!", 
			"Please [v] the [a] [n] before [d] deliberately.")

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
			v="to %s" % v
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
	
	if genre>0 and genre!=g :
		substitute_noun(genre)
	else:
		if p==1:
			n="%s-%s" % (substitute_prefix(),n)
		elif p==2:
			if random.random()<0.2:
				n="%s-%s" % (substitute_prefix(),n)
		if withAdj:
			n="%s %s" % (n,substitute_adj(g))
		
	return n

def main():
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

	print(p1)		
	
if __name__=="__main__":
	main()
