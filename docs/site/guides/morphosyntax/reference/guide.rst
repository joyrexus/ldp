************
Morphosyntax
************

* Overview_

* Morphology_

  * `POS Tags`_
  * `POS Notes`_
  * `Prefix Codes`_
  * `Suffix Codes`_

* Syntax_

  * `GR Tags`_
  * `GR Notes`_


Overview
========

A subset of the LDP transcripts have received morphosyntactic coding --
an additional level of annotation that describes the morphosyntactic properties
and relations among the word tokens in an utterance.

These transcripts have a **mor** column (for both parent and child) 
containing morphological coding and a **syn** column containing syntactic 
coding for each utterace.  

The tables below provide a key to the part-of-speech tags and
grammatical-relation labels used in these two columns. 


A Simple Example
----------------

Here's an example of an annotated utterance::

    I         spilled       it       .              # utt
    pro|I     v|spill-PAST  pro|it   .              # mor
    1|2|SUBJ  2|0|ROOT      3|2|OBJ  4|2|PUNCT      # syn

The first line shows the utterance as it would be transcribed
in the **utt** column, the second line shows the morphology annotation that
would be contained in the corresponding **mor** column, and the third line
shows the syntactic annotation that would be contained in the correspoding
**syn** column.

We can represent the above example in a slightly different format, combining
the annotation of the two columns, with one word token per line::

    #  WORD     LEMMA   SUFFIX  POS  DEP  REL
    1  I        I               pro  2    SUBJ
    2  spilled  spill   PAST    v    0    ROOT
    3  it       it              pro  2    OBJ
    4  .        .               .    2    PUNCT

The morphology annotation indicates that the first word ("I") is tagged as 
a pronoun (``pro``) and the second word ("spilled") is tagged as a verb (``v``)
and contains a past-tense suffix (``PAST``).

The syntactic annotation indicates that the first word ("I") is dependent on
the second word ("spilled"), the verb of the utterance, and is playing the
role of grammatical subject in relation to the verb.

Note how it represents the grammatical dependency relations::

                 ┌── PUNCT ──┐
    I      spilled     it    .
    └─ SUBJ ─┘ └─ OBJ ──┘      


.. note::

    For more information about the various steps involved in adding 
    morphosyntactic coding see our `Morphosyntax Annotation Guide`_.

.. _Morphosyntax Annotation Guide: http://joyrexus.spc.uchicago.edu/ldp/docs/guides/morphosyntax/index.html




Morphology
==========

The values in the **mor** column contain a morphological analysis of the word 
tokens in a given utterance: viz., each word's ...

* lemma
* part-of-speech
* prefix
* suffix

For example, consider the utterance transcribed:: 

    let's see, I'm going to make Dad's dinner &xxx .

This would be coded in the mor column as follows::

    aux|let's v|see pro|I~aux|be&1S aux|go-PROG inf|to v|make n:prop|Dad-POSS n|dinner .

Note the following:

- each word token is replaced by its lemma (dictionary form)

- each word is preceded by a part-of-speech code, which consists of 
  lower-case letters and colons

- suffixes may be added at the end of a word, marked by a dash (``-``) or an
  ampersand (``&``) and written using numbers and capital letters

- prefixes may be added before the part-of-speech code, separated from the main
  lexeme by a pound sign (``#``)

- compound words have normal part-of-speech codes and word types, joined
  together by plus signs (``+``), and preceded by the part-of-speech code of the
  compound as a whole (e.g., ``n|+adj|black+n|bird``)

- cliticized words are written with a tilde (``~``) connecting it to the 
  previous word.


POS Tags
--------

The **mor** column indicates the part-of-speech of each word token in an
utterance.  The following table provides short descriptions of the meaning
of each part-of-speech tag.


================  =============================
Tag               Part of Speech
================  =============================
``adj``           adjective
``adj:n``         adjective derived from noun
``adj:v``         adjective derived from verb
``adv``           adverb
``adv:adj``       adverb derived from adjective
``adv:int``       intensifying adverb
``adv:loc``       locational adverb
``adv:tem``       temporal adverb
``adv:wh``        WH adverb
``aux``           auxiliary verb
``co``            communicator
``co:voc``        vocative communicator
``conj:coo``      coordinating conjunction
``conj:subor``    subordinating conjunction
``det``           determiner
``det:num``       numeric determiner
``det:wh``        WH determiner
``fil``           filler
``inf``           infinitive
``int``           interjection
``n``             noun
``n:adj``         noun derived from adjective
``n:gerund``      nominal gerund
``n:pt``          plurale tantum noun
``n:v``           noun derived from verb
``neg``           negation
``on``            onomatopoeia
``part``          participle
``post``          postposition
``prep``          preposition
``pro``           pronoun
``pro:dem``       demonstrative pronoun
``pro:exist``     existential pronoun
``pro:indef``     indefinite pronoun
``pro:poss``      possessive pronoun
``pro:poss:det``  determiner possessive pronoun
``pro:refl``      reflexive pronoun
``pro:wh``        WH pronoun
``ptl``           particle
``qn``            quantifier
``rel``           relativizer
``v``             verb
``v:n``           verb derived from noun
================  =============================


POS Notes
+++++++++

Below is a quick overview of the main part-of-speech classes.

**Adjectives** modify nouns, either prenominally, or predicatively. Unitary compound modifiers such as *good-looking* should be labeled as adjectives.

**Adverbs** cover a heterogenous class of words including: manner adverbs, which generally end in *-ly*; locative adverbs, which include expressions of time and place; intensifiers that modify adjectives; and post-head modifiers, such as *indeed* and *enough*.

**Communicators** are used for interactive and communicative forms which fulfill a variety of functions in speech and conversation. Many of these are formulaic expressions such as *hello, good-morning, good-bye, please, thank-you*. Also included in this category are words used to express emotion, as well as imitative and onomatopeic forms, such as *ah, aw, boom, boom-boom, icky, wow, yuck, yummy*.

**Conjunctions** conjoin two or more words, phrases, or sentences. Coordinating conjunc- tions include: *and, but, or, yet*. Subordinating conjunctions include: *although, because, if, unless, until*.

**Determiners** include articles, and definite and indefinite determiners. Possessive determiners such as *my* and *your* are tagged ``det:poss``.

The **infinitive** marker is the word *to* which is tagged ``inf|to``. 

**Nouns** are tagged with ``n`` for common nouns, and ``n:prop`` for proper nouns 
(names of people, places, fictional characters, brand-name products).

The word *not* serves as a **negation** marker and is tagged ``neg|not``.

**Numbers** are tagged ``num`` for cardinal numbers. The ordinal numbers are adjectives. 

**Particles** are words that are often also prepositions, but serve as verbal particles.

**Prepositions** are tagged as ``prep``. Only words that are part of a prepositional phrase should be coded as prepositions.  

**Quantifiers** include *each, every, all, some*, and similar items.


Prefix Codes
------------

==========  ===========================
Prefix      Function
==========  ===========================
``CO``      verb prefix (*co-*)
``DE``      verb prefix (*de-*)
``MEGA``    verb prefix (*mega-*)
``MINI``    verb prefix (*mini-*)
``MULTI``   verb prefix (*multi-*)
``NON``     verb prefix (*non-*)
``SEMI``    verb prefix (*semi-*)
``SUPER``   verb prefix (*super-*)
``UNDER``   verb prefix (*under-*)
``UP``      verb prefix (*up-*)
``ANTI``    verb prefix (*anti-*)
``DIS``     verb prefix (*dis-*)
``MIS``     verb prefix (*mis-*)
``OUT``     verb prefix (*out-*)
``OVER``    verb prefix (*over-*)
``PRE``     verb prefix (*pre-*) 
``PRO``     verb prefix (*pro-*)
``RE``      verb prefix (*re-*)
``UN``      verb prefix (*un-*)
==========  ===========================


Suffix Codes
------------

===========  =================================================
Suffix       Meaning
===========  =================================================
``13S``      first- and third-person singular
``1S``       first-person singular
``3S``       third-person singular
``ABLE``     *-able* verb to adj derivational suffix
``AGT``      agentive suffix
``AL``       *-al* noun to adj derivational suffix
``COND``     conditional verb suffix
``CP``       comparative adj and adverb suffix
``DIM``      diminutive suffix
``ER``       *-er* nominalizer
``FULL``     *-full/ful* nominal suffix (*spoonful*)
``GERUND``   gerund suffix
``ISH``      *-ish* adjective or noun to adj suffix
``LESS``     *-less* noun to adj suffix
``LIKE``     *-like* noun to adj suffix (*fishlike*)
``LOOKING``  *-looking* adjective suffix (*funnylooking*)
``LY``       *-ly* adj to adverb suffix
``NESS``     *-ness* adj to noun suffix
``PAST``     past tense marker
``PERF``     perfect participle marker
``PL``       plural marker
``POSS``     possessive suffix
``PRES``     present tense marker
``PROG``     progressive participle marker
``SP``       superlative adj and adverb marker
``Y``        *-y* verb or noun to adj suffix (*burny*)
``ZERO``     null suffix for verbs with no explicit past tense
===========  =================================================


Syntax
======

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

                 ┌── PUNCT ──┐
    you      got        me   .
    └─ SUBJ ─┘ └─ OBJ ──┘      

That is, the first word ("you") is dependent on the second word ("got", the 
verb of the sentence, which acts as the head or ``ROOT`` dependency), and 
stands in the relation of a grammatical subject (``SUBJ``) to the verb, etc.


Terminology
-----------

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


GR Tags
-------

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


GR Notes
--------

SUBJ
++++

Used to identify the subject of clause, when the subject itself is not
a clause. Typically, the head is a verb (the main verb of the subject’s
clause), and the dependent is a noun (or another nominal, such as a pronoun, or
any head of a noun phrase). Clauses that act as subjects are denoted by CSUBJ
or XSUBJ, depending on whether the clausal subject is finite or non-finite (see
below). Note that throughout the labeling scheme, in general, CGR denotes a
finite clausal version of the relation GR, and XGR denotes a non-finite clausal
version of the relation GR, where the relation GR may be a subject, adjunct,
predicate nominal, etc.

Example::

    Mary saw a movie. 
    SUBJ(Mary-1, saw-2)

CSUBJ 
+++++

Used to identify the finite clausal subject of another clause. The head is 
typically the main verb of the matrix clause, and the dependent is the main 
verb of the clausal subject.

Example::

    That Mary screamed scared John.
    CSUBJ(screamed-3, scared-4)


XSUBJ
+++++

used to identify the non-finite clausal non-finite subject of another clause. The head is typically the main verb of the matrix clause, and the dependent is the main verb of the clausal subject.

Example::

    Eating vegetables is important. 
    XSUBJ(eating-1, is-3)


OBJ
+++

Used to identify the first object of a verb. Typically, the head is a verb, and the dependent is a noun (or other nominal). The dependent must be the head of a required non- clausal and non-prepositional complement of the verb (head of OBJ). A clausal complement relation should be denoted by COMP or XCOMP (depending on whether the clausal complement is finite or non-finite, see below), not OBJ or OBJ2.

Example::

    Mary saw a movie. 
    OBJ(movie-4, saw-2)


OBJ2
++++

Used to identify the second object of a ditransitive verb, when not introduced by a preposition. Typically, the head is a ditransitive verb, and the dependent is a noun (or other nominal). The dependent must be the head of a required non-clausal and non-prepositional complement of a verb (head of OBJ2) that is also the head of an OBJ relation. A second complement that has a preposition as its head should be denoted by IOBJ, not OBJ2.

Example::

    Mary gave John a book. 
    OBJ2(book-5, gave-2)


IOBJ
++++

Used to identify an object (required complement) introduced by a preposition. When a prepositional phrase appears as the required complement of a verb, it is the dependent in an IOBJ relation, not a JCT (adjunct) relation. The head is typically a verb, and the dependent is a preposition (not the complement of the preposition, see POBJ below).

Example::

    Mary gave a book to John.
    IOBJ(to-5, gave-2)


COMP
++++

Used to identify a finite clausal complement of a verb. The head is typically the main verb of the matrix clause, and the dependent is the main verb of the clausal complement.

Example::

    I think that Mary saw a movie.
    COMP(saw-5, think-2)


XCOMP
+++++

Used to identify a non-finite clausal complement of a verb. The head is typically the main verb of the matrix clause, and the dependent is the main verb of the clausal complement. The XCOMP relation is only used for non-finite clausal complements, not predicate nominals or predicate adjectives (see PRED below).

Examples::

    Mary likes watching movies.
    XCOMP(watching-3, likes-2)

    Mary wants me to watch a movie.
    XCOMP(watch-5, wants-2)


PRED
++++

Used to identify a predicate nominal or predicate adjective of the subject of verbs such as be and become. The head of PRED is the verb, not its subject. The predicate may be nominal, in which case the dependent is a noun (or other nominal), or adjectival, in which case the dependent is an adjective. PRED should not be confused with XCOMP, which identifies a non-finite complement of a verb (some syntactic formalisms group PRED and XCOMP in a single category).

Examples::

    Mary is a student.
    PRED(student-4, is-2)

    Mary got angry.
    PRED(angry-3, got-2)


CPRED
+++++

Used to identify a finite clausal predicate of the subject of verbs such as be and become. The head of CPRED is the main verb (of the matrix clause), not its subject.

Example::

    The problem is that Mary sees too many movies. 
    CPRED(sees-6, is-3)


XPRED
+++++

Used to identify a non-finite clausal predicate of the subject of verbs such as be and become. The head of CPRED is the main verb (of the matrix clause), not its subject.

Example::

    My goal is to win the competition.
    XPRED(win-5, is-3)


JCT
+++

used to identify an adjunct (an optional modifier) of a verb, adjective, or adverb. The head of JCT is a verb, adjective or adverb. The dependent is typically an adverb, a
preposition (in the case of phrasal adjuncts headed by a preposition, such as a prepositional phrase). Intransitive prepositions may be treated as adverbs, in which case the JCT relation applies, or particles, in which case the PTL relation (see below) applies. Adjuncts are optional, and carry meaning on their own (and do not change the basic meaning of their JCT heads).

Examples::

    Mary spoke very clearly.
    JCT(clearly-4, spoke-2) JCT(very-3, clearly-4)

    Mary spoke at the meeting.
    JCT(at-3, spoke-2)

    Mary is very tired.
    JCT(very-3, tired-2)


CJCT
++++

Used to identify a finite clause that acts like an adjunct of a verb, adjective, or adverb. The head of CJCT is a verb, adjective, or adverb. The dependent is typically the main verb of a subordinate clause.

Example::

    Mary left after she heard the news.
    CJCT(heard-5, left-2)


XJCT
++++

Used to identify a non-finite clause that acts like an adjunct of a verb, adjective, or adverb. The head of CJCT is a verb, adjective, or adverb. The dependent is typically the main verb of a non-finite subordinate clause.

Example::

    Mary left after hearing the news.
    CJCT(hearing-4, left-2)


MOD
+++

Used to identify a non-clausal nominal modifier or complement. The head is a noun, and the dependent is typically an adjective, noun or preposition.

Examples::

    Mary saw a red car.
    MOD(red-4, car-5)

    Mary saw the boy with the dog.
    MOD(with-5, boy-4)

    The Physics professor spoke clearly.
    MOD(Physics-2, professor-3)


CMOD
++++

Used to identify a finite clause that is a nominal modifier (such as a relative clause) or complement. The head is a noun, and the dependent is typically a finite verb.

Example::

    The student who visited me was smart.
    CMOD(visited-4, student-2)


XMOD
++++

Used to identify a non-finite clause that is a nominal modifier (such as a relative clause) or complement. The head is a noun, and the dependent is typically a non-finite verb.

Example::

    The student standing by the door is smart.
    XMOD(standing-3, student-2)


AUX
+++

Used to identify an auxiliary of a verb, or a modal. The head is a verb, and the dependent is an auxiliary (such as be or have) or a modal (such as can or should).

Examples::

    Mary has seen many movies.
    AUX(has-2, seen-3)

    Are you eating cake?
    AUX(are-1, eating-3)

    You can eat cake.
    AUX(can-2, eat-3)


NEG
+++

Used to identify verbal negation. When the word not (contracted or not) follows an auxiliary or modal (or sometimes a verb), it is the dependent of a NEG relation (not JCT), where the auxiliary, modal or verb (in the absence of an auxiliary or modal) is the head.

Examples::

    I am not eating cake. NEG(not-3, am-2)
    Speak not of that subject. NEG(not-2, speak-1)


DET
+++

Used to identify a determiner of a noun. Determiners include the, a, as well as possessives (my, your, etc) and demonstratives (this, those, etc), but not quantifiers (all, some, any, etc; see QUANT below). Typically, the head is a noun and the dependent is a determiner. In cases where a word that is usually a determiner does not have a head, there is no DET relation.

Example::

    The students ate that cake. 
    DET(the-1, students-2) DET(that-4, cake-5)


QUANT
+++++

Used to identify a nominal quantifier, such as three, many, and some. Typically, the head is a noun, and the dependent is a quantifier. In cases where a quantifier has no head, there is no QUANT relation.

Example::

    Many students saw three movies yesterday. 
    QUANT(many-1, students-2) QUANT(three-4, movies-5)


POBJ
++++

Used to identify the object of a preposition. The head is a preposition, and the dependent is typically a noun.

Example::

    Mary saw the book on her desk.
    POBJ(desk-7, on-5)


PTL
+++

Used to identify the verb particle (usually a preposition) of a phrasal verb. Intransitive prepositions that change the meaning of a verb should be in a PTL relation, not JCT (see above). The head is a verb, and the dependent is a preposition.

Example::

    Mary decided to put off the meeting until Thursday. 
    PTL(off-5, put-4)


CPZR
++++

Used to identify a complementizer (usually a subordinate conjunction). The head is a verb, and the dependent is a complementizer. It is the verb (head of a CPZR relation) of an embedded clause that acts as the dependent in a relation involving the embedded clause and its matrix clause, not the complementizer (the verb is higher in the dependency tree than the complementizer).

Examples::

    I think that Mary left. 
    CPZR(that-3, left-5)

    She ate the cake because she was hungry. 
    CPZR(because-5, was-7)


COM
+++

Used to identify a communicator (such as hey, okay, etc). Because communicators are typically global in a given sentence, the head of COM is typically the root of the sentence’s dependency tree (the dependent of the ROOT relation, see below). The dependent is a communicator.

Example::

    Okay, you can read the book.
    COM(okay-1, read-4)


INF
+++

Used to identify an infinitival particle (to). The head is a verb, and the dependent is always to.

Example::

    Mary wants to read a book.
    INF(to-3, read-4)


VOC
+++

Used to identify a vocative. As with COM, the head is the root of the sentence. The dependent is a vocative.

Example::

    Mary, you may not eat the cake.
    VOC(Mary-1, eat-5)


TAG
+++

Used to identify tag questions, where the tag is headed by a verb, auxiliary or modal. Tags of the type found in “this is red, right?” and “Let me do it, okay?” are identified as dependents in a COM relation, not TAG. The head of a TAG relation is typically a verb, and the dependent is the verb, auxiliary or modal in the tag question.

Example::

    This is good, isn’t it? 
    TAG(is-4, is-2)
    NEG(n’t-5, is-4)
    SUBJ(it-6, is-4)


COORD
+++++

Used to identify coordination. The head is a coordinator (usually and), and several types of dependents are possible. The head coordinator may have two or more dependents, including the coordinated items. Once the COORD relations are formed between the head coordinator and each coordinated item (as dependents), the coordinated phrase can be thought of as a unit represented by the head coordinator. For example, consider two coordinated verb phrases with a single subject (as in “I walk and run”), where two verbs are dependents in COORD relations to a head coordinator. The head of COORD is then also the head of a SUBJ relation where the subject is the dependent. This indicates that both verbs have that same subject. In the case of a coordinated string with multiple coordinators, the COORD relation applies compositionally from left to right. In coordinated lists with more than two items, but only one coordinator, the head coordinator takes each of the coordinated items as dependents. In the absence of an overt coordinator, the right-most coordinated item acts as the coordinator (the head of the COORD relation).

Examples::

    Mary likes cats and dogs. 
    COORD(cats-3, and-4)
    COORD(dogs-5, and-4)
    OBJ(and-5, likes-2)

    Mary likes birds and cats and dogs. 
    COORD(birds-3, and-4) 
    COORD(cats-5, and-4) 
    COORD(and-4, and-6) 
    COORD(dogs-7, and-6)
    OBJ(and-6, likes-2)


ROOT
++++

This is the relation between the topmost word in a sentence (the root of the dependency tree). The topmost word in a sentence is the word that is the head of one or more relations, but is not the dependent in any relation with other words. This word is the dependent in the ROOT relation.

Example::

    Mary saw many movies last week. 
    ROOT(saw-2, LeftWall-0)

