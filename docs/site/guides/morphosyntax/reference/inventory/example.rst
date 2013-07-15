Noun Phrases
============

Bare Noun
---------

We are defining bare noun phrases as phrases that contain unmodified nouns
(that do not themselves act as modifiers). A modifier is something that adds 
to or restricts the sense of the head noun. For example, in the phrase "a good 
family house" all three word tokens preceding the noun *house* modify its
sense. 

Now that we've stated the general criteria, we currently make a number of
exceptions in our heuristics for identifying bare noun phrases in our corpus:

1. We do not exclude plural nouns or compound nouns from consideration.  
   English plural nouns are of course marked and this marker affects the 
   sense of the noun, but we nevertheless consider it as an unmodified noun.

2. We exlcude pronouns, proper nouns, and letters (tagged with an ``@l``
   marker) from consideration.

3. We also exclude from consideration any nouns that are themselves dependent
   on a modifier. (E.g., the word *water* in the noun phrase "a bucket
   of water" is dependent on the preposition *of* which is modifiying *bucket*.


======  ==================================  ===================================
Status  Example                             Note
======  ==================================  ===================================
``+``   *Cookies*!                          Plural forms OK
``-``   A *cookie*!                         Modified by "a"
``+``   I want *cookies*.           
``-``   I want some *cookies*.              Modified by "some"
``+``   *Train* goes here.
``-``   The *train* goes here.              Modified by "the"
``+``   *Four*, *five*, and *six*.
``-``   a@l, b@l, and c@l.                  We exclude letter forms
``+``   The ducks swim in *water*.          
``-``   The ducks in *water* swim.          Part of larger NP
``+``   Paper *plane* in the air!           Part of compound noun
``-``   Fast *plane* in the air!
``-``   *I* like you.                       We exclude pronouns
``+``   *People* like you.
``-``   *John* likes you.                   We exclude proper nouns
======  ==================================  ===================================

