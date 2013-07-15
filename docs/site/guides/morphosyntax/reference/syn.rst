******
Syntax
******


Introduction
============

We represent grammatical relations (such as subjects, objects, and
adjuncts) between word tokens in an utterance using a convention of 
labeled dependencies.

As in many flavors of dependency-based syntax, each grammatical relation 
represents a relationship between two words in an utterance: a head (or parent) 
and a dependent (or child).  These dependency relations between words are 
labeled, indicating the syntactic relationship holding between the two words.

The **syn** column in our transcripts contains our syntactic annotation 
for each utterance, indicating these grammatical dependency relations holding 
between the word tokens.

For each word token in an utterance (including the punctuation), the **syn** 
column indicates the word token's ...

* number (based on its order in the utterance)
* grammatical dependency (the number of the word token on which it depends)
* grammatical relation (to its dependency)

The meaning of the labels for the grammatical relations are indicated in the
table below.


A Simple Example
----------------

For example, the following simple utterance contains four word tokens::

   you got me !
   1   2   3  4      

It would be annotated as follows::

   you      got        me      !                # utt
   1|2|SUBJ 2|0|ROOT   3|2|OBJ 4|2|PUNCT        # syn
     ^ ----   ^ ----     ^ ---   ^ -----

We can alternatively represent the grammatical-dependency relations 
for this example as follows::

     #  WORD  DEP  REL
     1  you   2    SUBJ
     2  got   0    ROOT
     3  me    2    OBJ
     4  .     2    PUNCT

Observe how this captures the following dependency relations::

               ┌-── PUNCT -──┐
    you      got        me   .
    └─ SUBJ ─┘ └─ OBJ ──┘      

That is, the first word ("you") is dependent on the second word ("got", the 
verb of the sentence, which acts as the head or ``ROOT`` dependency), and 
stands in the relation of a grammatical subject (``SUBJ``) to the verb, etc.


Terminology
===========

When discussing more involved grammatical dependency relations, it's often
helpful to employ a taxonomic/genealogical vocabulary.  Consider the following
taxonomy of food types::

    food
    ├── fruit
    │   ├── banana
    │   └── apple
    │       ├── braeburn 
    │       ├── honeycrisp
    │       └── gala
    └── meat
    

We'll say:

* ``food`` is the **dependency** (or **parent**) of ``fruit`` and ``meat``.
* ``fruit`` and ``meat`` are **dependent** on ``food``.
* ``fruit`` and ``meat`` are **dependants** (or **children**) of ``food``.
* ``banana`` and ``apple`` are **dependants** (or **children**) of ``fruit``.

Note that these terms always indicate *immediate* ancestor/descendant relations 
(e.g., parent/child).

If we want to describe both immediate and non-immediate dependency relations 
we speak of **ancestors** (chain of dependencies) and **descendants** (chain of 
dependants). 

For example, we'll say:

* ``fruit``, ``apple``, and ``gala`` are all **descendants** of ``food``.
* ``food`` is an **ancestor** of ``fruit``, ``apple``, and ``gala``.


Overview
========

Observe that while this annotation scheme captures the grammatical dependency 
relations between words in an utterance, these relations have the structure of a
directed graph with labeled edges.  The words of the utterance serve as nodes
of the graph, the dependency relations (indicated by the indices) serve as
directed edges, and the grammatical relations function as labels on these
edges. The edges should be thought of as directed from a given head word (parent 
node) to its dependents (immediate child nodes).

In other words, the GR tags are labels indicating the syntactic relationship
holding between a head and each of its depedents. Except for the "root" word in
an utterance, note that each word must be dependent on exactly one head word 
(though heads may have several dependents).

Note that head words are typically content words and their dependents are
typically function words.  For example, nouns are the heads of determiners 
(forming a GR of type DET with the noun as the head and the determiner as the 
dependent), and verbs are chosen as the heads of auxiliaries (forming a GR of 
type AUX with the verb as the head and the auxiliary as the dependent). An 
exception to this rule is coordination, where coordinated items are dependents 
of the coordinator (for example, in "boys and girls" each noun is a dependent 
of "and", forming two GRs of type COORD). 

When both words in a GR are members of lexical (content) categories, the 
direction of the relation follows common practice, where complements, 
adjuncts and modifiers are dependents of the words they complement or modify.
For example, adjectives are typically dependents of nouns, and adverbs are 
typically dependent of verbs, adjectives or other adverbs.  

By convention, vocatives and communicators are dependents of the main verb of 
their sentences.  


Relative Clauses
----------------

Nouns are dependents of verbs when the noun is a complement (such as subject 
or object), but verbs can also be dependents of nouns, as in the case of 
relative clauses (where a clause modifies a noun, and the verb is the root of 
the dependency subtree representing the clause).  In the case of 
prepositional phrases, the preposition is chosen as the head of the
prepositional object (in a POBJ relation).  


Clausal Dependencies
--------------------

In cases where a clause has a relation to another clause, the verb of the lower
(subordinate) clause is used as a dependent. For example, consider the relative 
clause of the sentence "The boy I saw drew a picture"::

    #  WORD     DEP  REL
    1  The      2    DET
    2  boy      5    SUBJ
    3  I        4    SUBJ
    4  saw      2    CMOD
    5  drew     0    ROOT
    6  a        7    DET
    7  picture  8    OBJ
    8  .        5    PUNCT

    ┌─DET─┐ ┌─SUBJ─┐    ┌-─--PUNCT--──┐
    The boy I    saw drew a  picture  .
          ├--CMOD-─┘ |    |     ├-OBJ-┘ 
          └---SUBJ--─┘    └-DET─┘      


The verb "saw" of the relative clause is treated as dependent in a CMOD 
(clausal modifier of a nominal) relation with the noun "boy".  The other 
relations in this sentence are as expected: "The" and "a" are dependents 
in DET relations with "boy" and "picture", "boy" is the dependent in a SUBJ 
relation with "saw", and "picture" is in a OBJ relation with "drew".  Finally, 
"drew" is the root of the dependency tree for this sentence.


Required vs. Optional
---------------------

Our tagging system itself makes two broad distinctions, which are useful to understand before looking at specific grammatical relationship tags.

First, it distinguishes between required and optional elements.  A required element is demanded by a transitive or ditransitive verb, or by a preposition.  Removing this element changes the basic meaning of the sentence.  Optional elements give more information about the head of their clause, but they can be easily removed without destroying meaning.  

The following are examples of required elements:

        I saw *him*.
        I saw *what you did*.
        I gave *the book to her*.

This broad category covers things like objects (OBJ), objects of prepositions (POBJ), and complements (COMP, XCOMP).

These, on the other hand, are optional:

        I saw *already*.
        I saw *after you did*.

This category covers things like adjuncts (JCT), modifiers (MOD), and clausal adjuncts and modifiers (CJCT, XJCT, CMOD, XMOD). 


Finite vs. Non-Finite
---------------------

The tagging system also draws a distinction between finite and non-finite verbal clauses.  The difference here is that the form of a finite element is dependent on other information in the sentence, but the form of a non-finite element will never change.  Non-finite elements are generally infinitives or particles.  

The following are finite verbs:

        I know they went to the park.
        I know he goes to the park.

While these are non-finite:

        I know how to go to the park.
        It's hard to run.

These categories are easily distinguished in our system by looking at the tag itself.  Finite clauses generally begin with a C (CMOD, CSUBJ, COMP, CPRED, etc.) while non-finite clauses generally begin with an X (XMOD, XCOMP, XPRED, XSUBJ, etc.).


GR Tags
=======

The grammatical relationship codes have the following interpretations:

===========  ======================================= 
Tag          Grammatical Relation
===========  ======================================= 
``AUX``      Auxiliary
``CJCT``     Finite clausal adjunct
``CMOD``     Finite clausal modifier
``COM``      Communicator
``COMP``     Finite complement
``COORD``    Coordinated word
``CPRED``    Finite clausal predicate
``CPZR``     Complementizer
``CSUBJ``    Finite clausal subject
``DET``      Determiner
``ENUM``     Enumerated word
``ESUBJ``    Existential subject
``INF``      Infinitive
``IOBJ``     Preposition introducing indirect object 
``JCT``      Non-clausal adjunct
``LOC``      Obligatory locative identifier
``MOD``      Non-clausal modifier of a nominal
``NEG``      Negation
``OBJ``      Object
``OBJ2``     Indirect object without preposition
``POBJ``     Prepositional object
``PRED``     Predicate
``PTL``      Particle
``PUNCT``    Punctuation
``QUANT``    Quantifier
``ROOT``     Head of sentence (verbal)
``ROOT-NV``  Head of sentence (non-verbal)
``SRL``      Serial verb
``SUBJ``     Subject
``TAG``      Verb used as tag
``TOP``      Topicalizer
``VOC``      Vocative
``XCOMP``    Non-finite complement
``XJCT``     Non-finite clausal adjunct
``XMOD``     Non-finite clausal modifier
``XPRED``    Non-finite clausal predicate
``XSUBJ``    Non-finite clausal subject
===========  ======================================= 


``COORD`` may be combined with any relationship type that is being 
coordinated (e.g. ``COORD-ROOT``, ``COORD-POBJ``).

Additionally, the following grammatical-relation combinations are recognized:
   
===================  ======================================= 
Code                 Meaning
===================  ======================================= 
``DET-SUBJ``         Determiner ...
``DET-OBJ``          
``DET-POBJ``
``DET-PRED``
``INF-COMP``         Infinitive ...
``INF-XCOMP``
``INF-CJCT``
``INF-XJCT``
``INF-CSUBJ``
``INF-XSUBJ``
``INF-CMOD``
``INF-XMOD``
``INF-CPRED``
``INF-XPRED``
``INF-ROOT`` 
``AUX-COMP``         Auxiliary ...
``AUX-XCOMP``
``AUX-CJCT``
``AUX-XJCT``
``AUX-CSUBJ``
``AUX-XSUBJ``
``AUX-CMOD``
``AUX-XMOD``
``AUX-CPRED``
``AUX-XPRED``
``AUX-ROOT`` 
===================  ======================================= 


Notes on specific tags
----------------------


The following is a comprehensive list of the grammatical relations in the GRASP annotation scheme. Example GRs as well as other relevant GR to that particular GR are provided. In this annotation scheme, C refers to clausal and X refers to non-finite clausal. This list is divided into relations with the predicate as head and relations with the argument as head. In the examples, the dependent is marked in italics.

Predicate-head relations 
========================

First, we list the relations in which the dependent attaches to a head that serves as the predicate. In many of these relations, the head is the verb. The combination of a verb with all of its arguments, including the SUBJ argument, constitutes a verb phrase.


SUBJ
----

SUBJect identifies the subject of clause, when the subject itself is not a clause. Typically, the head is the main verb and the dependent is a nominal. 

	*You* eat vegetables. 


CSUBJ
-----

ClausalSUBJect identifies the finite clausal subject of another clause.  The head is the main verb, and the dependent is the main verb of the clausal subject. An alternative analysis of these structures would treat the subordinator “that” as the head of the CSUBJ. 

	*That you ate your vegetables* is important. 

XSUBJ
-----

XSUBJect identifies the non-finite clausal subject of another clause. The head is the main verb, and the dependent is the main verb of the clausal subject. 

	*Eating vegetables* is important.


OBJ
---

OBJect identifies the first object of a verb. The head is the main verb, and the dependent is a nominal or a noun that is the head of a nominal phrase. A clausal complement relation should be denoted by COMP or XCOMP (depending on whether the clausal complement is finite or non-finite, see below), not OBJ or OBJ2. 

	You read *the book*.


OBJ2
----

OBJect2 identifies the second object of a ditransitive verb, when not introduced by a preposition. The head is a ditransitive verb, and the dependent is a noun (or other nominal). The dependent must be the head of a required non- clausal and nonprepositional complement of a verb (head of OBJ2) that is also the head of an OBJ relation. A second complement that has a preposition as its head should be denoted by IOBJ, not OBJ2. 

	He gave *you* the book.


IOBJ
----

IndirectOBJect identifies an (required) object complement introduced by a preposition. When a prepositional phrase appears as the required complement of a verb, it is the dependent in an IOBJ relation, not a JCT (adjunct) relation. The head is the main verb, and the dependent is a preposition (not the complement of the preposition, see POBJ below). 

	Mary gave a book *to* John.


LOC
---

LOCative identifies the relation between a verb and a required location. Locations are required for verbs such as put or live. LOC takes the place of JCT in such cases when the PP is required by the verb. This is especially relevant for here, there, and back, which would otherwise be labeled JCT for other verbs. 

	Put the toys *there*.


COMP
----

COMPlement identifies a finite clausal complement of a verb. The head is the main verb of the matrix clause, and the dependent is the main verb of the clausal complement. 

	I think *that was Fraser*.


XCOMP
-----

XCOMPlement identifies a non-finite clausal complement of a verb. The head is the main verb of the matrix clause, and the dependent is the main verb of the clausal complement. The XCOMP relation is only used for non-finite clausal complements, not predicate nominals or predicate adjectives (see PRED). 

	I told you *to go*. 
	I hate *leaving*.


PRED
----

PREDicate identifies a predicate nominal, predicate adjective, or a prepositional complement of verbs such as be and become. The head is the verb. PRED should not be confused with XCOMP, which identifies a non-finite complement of a verb (some syntactic formalisms group PRED and XCOMP in a single category). 

	I’m not *sure*. 
	He is a *doctor*. 
	He is *in* Chicago.


CPRED
-----

ClausalPREDicate identifies a finite clausal predicate that identifies the status of the subject of verbs such as be and become. The head is the main verb of the matrix clause, not its subject. The dependent is the verb of the predicate clause.

	This is *how we do it*.


XPRED
-----

XPREDicate identifies a non-finite clausal predicate of the subject of verbs such as be and become. The head is the main verb (of the matrix clause), not its subject. 

	My goal is *to win*. 


POBJ
----

PrepositionalOBJect is the relation between a preposition and its object. The head is a preposition, and the dependent is typically a noun. The traditional treatment of the prepositional phrase views the object of the preposition as the head of the prepositional phrase. However, we are here treating the preposition as the head, since the prepositional phrase then participates in a further JCT relation to a head verb or a NJCT relation to a head noun. 

	You want to sit on the *stool*?


Argument-head relations
=======================

Relations in which the arguments (rather than the predicates) serve as the heads include relations of adjunction and modification. 


JCT
---

adJunCT identifies an adjunct that modifies a verb, adjective, or adverb.  This grammatical relation covers a wide variety of structures whose exact form is best understood by noting the specific parts of speech that are involved. In all of these, the adjunct is the predicate, since it opens up a valency slot for something to attach to. The head of JCT is the verb, adjective or adverb to which the JCT attaches as a dependent. The dependent is typically an adverb, a preposition (in the case of phrasal adjuncts headed by a preposition, such as a prepositional phrase). Intransitive prepositions may be treated as adverbs, in which case the JCT relation applies. Adjuncts are optional, and carry meaning on their own (and do not change the basic meaning of their JCT heads). Verbs requiring a complement describing location may be treated as prepositional objects, in which case the IOBJ relation applies (see above). 

	That’s *much* better. 
	He ran *with* a limp.


CJCT
----

ClausaladJunCT identifies a finite clause that adjoins to a verb, adjective, or adverb head. The dependent is typically the main verb of a subordinate clause and this clause attaches to the root verb of the main clause. 

	We can’t find it, *because it is gone*.


TAG
---

TAG is the relation between the finite verb of a tag question and the root verb of the main clause. 

	You know how to count, *don’t* you?


XJCT
----

XadJunCT identifies a non-finite clause that adjoins to a verb, adjective, or adverb. The dependent is typically the main verb of a non-finite subordinate clause. 

	She’s outside *sleeping*.
 

MOD
---

MODifier identifies a non-clausal nominal modifier or complement. The head is a noun, and the dependent is typically an adjective, noun or preposition. 

	I like *grape* juice.
	I like the juice *of grapes*.


CMOD
----

ClausalMODifier identifies a finite clause that is a nominal modifier (such as a relative clause) or complement. The head is a noun, and the dependent is typically a finite verb. 

	Here are the grapes *I like*.


XMOD
----

XMODifier identifies a non-finite clause that is a nominal modifier (such as a relative clause) or complement. The head is a noun, and the dependent is typically a non-finite verb. 

	It’s time *to take a nap*. 

DET
---

DETerminer identifies a determiner of a noun. Determiners include the, a, as well as (adjectival) possessives pronouns (my, your, etc) and demonstratives (this, those, etc), but not quantifiers (all, some, any, etc; see QUANT below). Typically, the head is a noun and the dependent/governor is a determiner. In cases where a word that is usually a determiner does not have a head, there is no DET relation. 

	I want *that* cookie.


QUANT
-----

QUANTifier identifies a nominal quantifier, such as three, many, and some. Typically, the head is a noun, and the dependent is a quantifier. In cases where a quantifier has no head, there is no QUANT relation. In English, the MOD, DET, and QUANT relations have largely the same syntax. However, within the noun phrase, we occasionally see that they are ordered as QUANT+DET+MOD+N. 

	I’ll take *three* bananas.


AUX
---

AUXiliary identifies an auxiliary of a verb, or a modal. The head is a verb, and the dependent is an auxiliary (such as be or have) or a modal (such as can or should). 

	*Can* you do it?


NEG
---

NEGation identifies verbal negation. When the word not (contracted or not) follows an auxiliary or modal (or sometimes a verb), it is the dependent in a NEG relation (not JCT), where the auxiliary, modal or verb (in the absence of an auxiliary or modal) is the head. 

	Mommy will *not* read it.


INF
---

INFinitive identifies an infinitival particle (to). The head is a verb, and the dependent is always to. 

	He’s going *to* drink the coffee.


SRL
---

SeRiaL identifies serial verbs such as go play and come see. In English, such verb sequences start with either come or go. The initial verb is the dependent, and the verb next to the inital verb, e.g., play and see in the previous example, is the head (the adjacent verb is typically the root of the sentence). 

	*Come* see if we can find it. 
	*Go* play with your toys over there.


CPZR
----

ComPlementiZeR identifies the relation between a complementizer (that, which) or a subordinate conjunction and the verb to which it attaches. After this attachment, the verbal head acts as the dependent in a CJCT relation involving the embedded clause and its matrix clause (the verb is higher in the dependency tree than the complementizer). 

	Wait *until* the noodles are cool.


Root linkage
============

There is also a set of relations in which the dependent is a sentential modifier. These could be viewed as depending on either the root or the left wall. Somewhat arbitrarily, we code them as linking to the root.

COM
---

COMmunicator identifies a communicator (such as hey, okay, etc). Because communicators are typically global in a given sentence, the head of COM is typically the root. The dependent is a communicator. COM items often appear either at the very beginning or very end of a clause or sentence. 

	*Yes*, you got a fly. 
	You need more paper, *right*? 


VOC
---

VOCative identifies a vocative. As with COM, the head is the root of the sentence. The dependent is a vocative. 

	Some more cookies, *Eve*?


TOP
---

TOPicalization identifies an object or a predicate nominal that has been topicalized. The head is the ROOT of the sentence, and the dependent is the topicalized item. 

	*Tapioca*, there is no tapioca.



Cosmetic relations
==================

There are several relations that are just used during transcription to assist in the accurate training of the GRASP tagger:

PUNCT
-----

PUNCTuation is the relation between the final punctuation mark and the root. 


ROOT
----

ROOT is the relation between the topmost word in a sentence (the root of the dependency tree) and the LeftWall. The topmost word in a sentence is the word that is the head of one or more relations, but is not the dependent in any relation with other words (except for the LeftWall).


Series relations
================

Some additional relations involve processes of listing, coordination, and classification. In these, the final element is the head and the initial elements all depend on the final head. In English, this extends the idea that the last element in a compound is the head.


ENUM
----

ENUMeration involves a relation between elements in a series without any coordination based on a conjunction (and, but, or). The series can contain letters, numbers, and nominals. The head is the last item in the series, and all the other items in the enumeration depend on this last word. 

	One, two, three, four.


COORD
-----

COORD is the relationship of phrases that have been conjoined with a coordinating conjunction, which then serves as the head of the entire conjoined phrase.

	I like *walking* and *jumping*.


Bivalency
=========

The above GRs describe dependencies in terms of the direction of the major valency relations. However, many of these relations have a secondary bivalent nature. For example, in the relations of thematic roles with the verb, it is also true that nominals are “looking for” roles in predications. Within the noun phrase, common nouns are looking for completion with either articles or plurality. Also, the attachment of auxiliaries to non-finite verbs serves to complete their finite marking. We can think of these additional valency relations as secondary relations. In all of these cases, valency works within the overall framework of dependency. Because GRASP relations are unidirectional, bivalency cannot be represented in GRASP.


Ellision Relations
==================

In addition to the basic GRs, there is this additional set of GRs used for marking elided elements.


AUX-
----

AUX-, when added onto the beginning of a verbal GR, identifies an auxiliary verb serving as the head of a clause where the main verb has been elided.  The relations you will see beginning with AUX are AUX-CJCT, AUX-CMOD, AUX-COMP, and AUX-ROOT.
	
	Yes, I *can* xxx.

INF-
----

INF-, when added onto the beginning of a verbal GR, identifies an infinitive particle serving as the head of a clause where the main verb has been elided.  The relations you will see beginning with INF are INF-CJCT, INF-COMP, INF-XCOMP, and INF-ROOT.

	I want *to*.


DET-
----
 
DET-, when added onto the beginning of a nominal GR, identifies a determiner serving as the head of a noun phrase where the noun has been elided, usually through interrupted speech.  The relations you will see beginning with DET are DET-OBJ, DET-POBJ, DET-PRED, and DET-SUBJ.

	I saw *the* +...


