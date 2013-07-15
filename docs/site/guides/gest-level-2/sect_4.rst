.. _g2sect_4:


****************************************
Timing, Reference, Semantics, and Syntax
****************************************

Timing
======

Goal: To record exactly where a gesture occurs within the *word order* of a spoken utterance.

* Timing is coded for all gestures, including Functional Acts.
* The gestures take place during the highlighted words.  If a gesture extends past the beginning or the end of an utterance it will be noted with the ``[`` or ``]`` symbols.

+-----------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------+
| Code                                                                  | Definition                                                                         | Example Utterance                                   | Example Code         |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------+
| Word numbers separated by commas (no spaces).                         | Timing is coded as the range of word numbers that are spoken during the gesture.   | "He went **over to the store**"                     | 3,4,5,6              |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------+
|                                                                       |                                                                                    | "**It was big**!"                                   | 1,2,3                |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------+
|                                                                       |                                                                                    | "**[The big round ball]**!"                         | 0.5, 1, 2, 3, 4, 4.5 |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------+
|                                                                       |                                                                                    | "I want it **now**!"                                | 4                    |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------+


Timing can begin before an utterance and continue after an utterance. For gestures beginning before an utterance, timing begins at 0.5. For gestures continuing after an utterance, timing ends at N.5. 

* Beats are used to emphasize a specific word or words in speech. Each instance of emphasis should be coded individually. Thus, an utterance with multiple beats will have multiple codes. 


Relational Timing
=================

Goal: To record, in general terms, where gestures fall in relation to *whole utterances*.

* Relational timing is also coded for all gestures

+--------+-------------+-----------------------------------------------------------------------------------------+-------------------------------------+
| Code   | Category    | Definition                                                                              | Example Utterance                   |
+--------+-------------+-----------------------------------------------------------------------------------------+-------------------------------------+
| B      | Beginning   | Gesture overlaps with the beginning of the utterance but does not last until the end.   | "**He** did it"                     |
|        |             |                                                                                         |                                     |
+--------+-------------+-----------------------------------------------------------------------------------------+-------------------------------------+
| M      | Middle      | Gesture is performed entirely within the utterance.                                     | "I saw **cars** at school"          |
|        |             |                                                                                         |                                     |
+--------+-------------+-----------------------------------------------------------------------------------------+-------------------------------------+
| E      | End         | Gesture overlaps with the beginning of the utterance but does not last until the end.   | "A mouse went **there**"            |
|        |             |                                                                                         |                                     |
+--------+-------------+-----------------------------------------------------------------------------------------+-------------------------------------+
| W      | Whole       | Gesture overlaps with the whole utterance.                                              | "**It was big**!"                   |
|        |             |                                                                                         |                                     |
+--------+-------------+-----------------------------------------------------------------------------------------+-------------------------------------+

As of session 11H, we are leaving this column blank. The information gained from this column can be obtained from the numeric timing column. Relational timing was coded for 09H and 10H for both P2 and P3 subjects. 


CHAT deletions
--------------

If the word or words that the gesture occurs during has/have been deleted during the removal of disfluent speech for CHAT processing, code timing as NA.

Semantic Correlate (word and word number)
=========================================

Goal: To record the word that is reinforced or disambiguated by a gesture performed during the utterance. 

When to code
------------
Semantic Correlate is coded for:
1. Deictics
2. Iconics and Metaphorics
3. Emphatics
4. Nods and Shakes (when RF)


 * Not coded for Conventionals other than nods and shakes (and only for nods and shakes when a variant of yes (e.g. yeah, uh-huh, mm+hm, sure, good, right, etc.) or no (e.g. nope, nah, not, neither, didn't, isn't, etc.) is used in speech.
 * Not coded when there is no speech (Semantic Correlate is not the same as GLOSS)
 * ADDs do not have semantic correlates!

Explanation
-----------

The semantic correlate of a gesture should be whatever word or phase is reinforced or disambiguated by the gesture. Coders should aim to reduce this correlate to its smallest possible unit of meaning for aid in analysis. Thus, in the utterance "I want the blue car" + POINT (to blue car), the semantic correlate should be "CAR" not "BLUE CAR." Single nouns or verbs should be used whenever possible, adjectives and adverbs should be ignored. In situations where both the object and the location could be chosen as the correlate, the object takes precedence over location.

Examples
--------

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Utterance + GESTURE**                           | **Semantic Correlate:** List the word that is reinforced or disambiguated by the gesture as it appears in the utterance.  | **Semantic Correlate Number:** The number of the semantic correlate as it appears in the word order of the utterance.  |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "This one is pink" + POINT                        | PINK                                                                                                                      | 4                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "This cow is pink" + POINT                        | COW                                                                                                                       | 2                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Pink" + POINT                                    | PINK                                                                                                                      | 1                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Do you like big ones?" + ICONIC (for big)        | BIG ONES                                                                                                                  | 4,5                                                                                                                    |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Do you like big ones?" + POINT                   | BIG ONES                                                                                                                  | 5,6                                                                                                                    |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "You do it!" + POINT (to other)                   | YOU                                                                                                                       | 1                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "The CD is on the table" + POINT TO CD ON TABLE   | CD                                                                                                                        | 3                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| " It is on the table" + POINT TO CD ON TABLE      | TABLE                                                                                                                     | 5                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "It is there" + POINT TO BOTTLE                   | IT                                                                                                                        | 1                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "These are mine" + POINT TO SELF                  | MINE                                                                                                                      | 3                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "It's my hat" + POINT TO SELF                     | MY                                                                                                                        | 3                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "It's my hat" + POINT TO HAT                      | HAT                                                                                                                       | 4                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I don't know" + FLIP                             | X                                                                                                                         | X                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| POINT (to door)                                   | X                                                                                                                         | X                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Can you help?" + POINT (to closed box)           | X                                                                                                                         | X                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I want all of them" + POINT                      | THEM                                                                                                                      | 5                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "These three" + CONT POINT                        | THESE THREE                                                                                                               | 1,2                                                                                                                    |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "These three bears" + CONT POINT                  | THREE BEARS                                                                                                               | 2,3                                                                                                                    |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Over here" + POINT                               | HERE                                                                                                                      | 2                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Around there" + ICONIC (tracepath)               | AROUND                                                                                                                    | 1                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I want to go over there." + POINT                | THERE                                                                                                                     | 6                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "Lots of big ones to open" + ICONIC (for big)     | BIG                                                                                                                       | 3                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I want to flip it" + ICONIC (for flip)           | FLIP                                                                                                                      | 4                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I don't like it" + SHAKE                         | NOT                                                                                                                       | 3 (see CHAT)                                                                                                           |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I have apples and oranges" + POINT               | \*APPLES ORANGES                                                                                                          | \*3,5                                                                                                                  |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "I want the **yellow** one" + BEAT                | YELLOW                                                                                                                    | 4                                                                                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

Nonadjacent Correlates
----------------------

When a gesture has more than one word as a semantic correlate and those words are nonadjacent, then both words and both words numbers should be coded and are be preceded by `*`.  

When more than one word in an utterance could be the semantic correlate of a gesture, the coder should use their judgment to determine if one word is more likely to be the correlate than the other. If both are equally possible, then the gesture should be coded as having more than one correlate.


Example
^^^^^^^

+---------------------------------+--------------------------+----------------------------------+
| **Utterance + GESTURE**         | **Semantic Correlate**   | **Semantic Correlate Number:**   |
+---------------------------------+--------------------------+----------------------------------+
| "No, I don't like it" + SHAKE   | NO                       | 1                                |
+---------------------------------+--------------------------+----------------------------------+

Demonstratives: *this* and *that*
---------------------------------

When "this" and "that" are used as demonstrative pronouns, then they are the semantic correlates. When "this" and "that" are used as determiners (e.g. "this truck"), then the noun is the semantic correlate. When "this" and "that" are used with another pronoun (i.e. "this one"), the semantic correlate is both (e.g. this one). The same is true when "this" or "that" is combined with "way" (e.g. this way).

Examples
^^^^^^^^

+-------------------------------+--------------------------+----------------------------------+
| **Utterance + GESTURE**       | **Semantic Correlate**   | **Semantic Correlate Number:**   |
+-------------------------------+--------------------------+----------------------------------+
| "I want this" + POINT         | THIS                     | 1                                |
+-------------------------------+--------------------------+----------------------------------+
| "I want this toy" + POINT     | TOY                      | 4                                |
+-------------------------------+--------------------------+----------------------------------+
| "I want this one" + POINT     | THIS ONE                 | 3,4                              |
+-------------------------------+--------------------------+----------------------------------+
| "Let's go this way" + POINT   | THIS WAY                 | 3,4                              |
+-------------------------------+--------------------------+----------------------------------+

Quantifiers
-----------

When a series of points or a continuous point is used with a quantifier + noun (e.g. "four dogs" or "several monkeys"), both the quantifier and the noun should be included in the semantic correlate if the gesture takes in the quantity specified. However, if a point is used with a quantifier but no noun, it is an ADD and has no correlate. Each number in a counting sequence is reinforced and the semantic correlate is the number. 

Examples
^^^^^^^^

+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| **Utterance + GESTURE**                                               | **Semantic Correlate**   | **Semantic Correlate Number:**   |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| "The three bears were very hungry" + POINT (to 3 bears in sequence)   | THREE BEARS              | 2,3                              |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| "The three bears were very hungry" + CONT POINT                       | THREE BEARS              | 2,3                              |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| "The three bears were very hungry" + POINT (single point)             | BEARS                    | 3                                |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| "I see lots of circles" + DRAG                                        | LOTS OF CIRCLES          | 3,4,5                            |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| "One, two, three, four" + POINT - POINT - POINT - POINT               | ONE; TWO; THREE; FOUR    | 1;2;3;4                          |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+
| "There are four" + POINT                                              | X                        | X                                |
+-----------------------------------------------------------------------+--------------------------+----------------------------------+

Nouns with Adjectives and Possessives
-------------------------------------

When a noun is described with a possessive or an adjective (e.g. "my socks" or "the big puppy"), the semantic correlate is only coded as the noun itself. When an adjective is used with "one," the semantic correlate is comprised of both. When a possible adjective is used on its own and is of a kind of adjective able to exist as an observable noun in its own right (e.g. colors and shapes), it is the semantic correlate. However, in cases where the possessor is emphasized in speech or in gesture, the possessor should be coded as the correlate rather than the object.

Examples
^^^^^^^^

+-------------------------------------------+--------------------------+----------------------------------+
| **Utterance + GESTURE**                   | **Semantic Correlate**   | **Semantic Correlate Number:**   |
+-------------------------------------------+--------------------------+----------------------------------+
| "These are my socks" + POINT              | SOCKS                    | 4                                |
+-------------------------------------------+--------------------------+----------------------------------+
| "I love that big puppy" + POINT           | PUPPY                    | 5                                |
+-------------------------------------------+--------------------------+----------------------------------+
| "I have a red one" + POINT                | RED ONE                  | 4,5                              |
+-------------------------------------------+--------------------------+----------------------------------+
| "That pink is pretty" + POINT             | PINK                     | 2                                |
+-------------------------------------------+--------------------------+----------------------------------+
| "Bring me the big one" + POINT            | BIG ONE                  | 4,5                              |
+-------------------------------------------+--------------------------+----------------------------------+
| "My name is Franklin" + POINT (to self)   | MY                       | 1                                |
+-------------------------------------------+--------------------------+----------------------------------+
| "These are mine" + PALM (to self)         | MINE                     | 3                                |
+-------------------------------------------+--------------------------+----------------------------------+
| "The video is his" + POINT (to other)     | HIS                      | 4                                |
+-------------------------------------------+--------------------------+----------------------------------+
| "Circle" + POINT                          | CIRCLE                   | 1                                |
+-------------------------------------------+--------------------------+----------------------------------+


Attributes and Adjectives (RF.a)
--------------------------------

When a spoken attribute (e.g. "pink" or "big") accompanies a gesture toward an object possessing that attribute, the gesture-speech relationship is given as reinforcing attribute (RF.a) and the semantic correlate is given as the attribute. If the object label is spoken as well, then the gesture-speech relationship is reinforcing (RF) and the semantic correlate is the object label.

Examples
^^^^^^^^

+--------------------------------------------+------------------------+--------------------------+
| **Utterance + GESTURE**                    | **G-S Relationship**   | **Semantic Correlate**   |
+--------------------------------------------+------------------------+--------------------------+
| "Pink" + POINT (to pink car)               | RF.a                   | PINK                     |
+--------------------------------------------+------------------------+--------------------------+
| "That is pink" + POINT (to pink car)       | RF.a                   | PINK                     |
+--------------------------------------------+------------------------+--------------------------+
| "This one is pink" + POINT (to pink car)   | RF.a                   | PINK                     |
+--------------------------------------------+------------------------+--------------------------+
| "This car is pink" + POINT (to pink car)   | RF                     | CAR                      |
+--------------------------------------------+------------------------+--------------------------+

CHAT deletions
--------------

If the word or words that the gesture occurs during has/have been deleted during the removal of disfluent speech for CHAT processing, code the semantic correlate and word number as NA.

Semantic Role
=============

Goal: To determine what types of semantic roles are supported by gesture or conveyed solely in gesture. 

Explanation
-----------

Semantic role refers to the active role that a word or entity plays in relation to the actions or concepts that appear in a particular sentence. It takes into account such things as the performer of an action, the recipient of an action, whether objects are described versus moved, and whether events are framed in space or time. 

When to code
------------

Semantic role should be coded for all gestures. When gestures reinforce (RF) or disambiguate (DA) speech, the semantic role of the semantic correlate is coded. When gestures add information to speech (ADD), then the semantic role that the gesture adds to the utterance is coded if it can be determined. A particular effort should be made to code semantic role for ADDs, since we do not know what types of roles may be added by gesture.


 * When counting gestures are used, they are not given a semantic role.
 * The semantic role of a word emphasized by a beat is coded.  


+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Code**   | **Thematic Role**    | **Definition**                                                                                                                                                                                                                                              | **Examples**                                                                                                                                                                       |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TA         | Transitive Agent     | The actor purposefully performs an action to or on another entity.                                                                                                                                                                                          | * **Susan**  wrote the book                                                                                                                                                        |
|            |                      |                                                                                                                                                                                                                                                             | * **William** put the frog in a bowl                                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * Vroom (+point to car)                                                                                                                                                            |
|            |                      |                                                                                                                                                                                                                                                             | * guh (+point to letter G)                                                                                                                                                         |
|            |                      |                                                                                                                                                                                                                                                             | * What sound does **this** make (+point to letter G)                                                                                                                               |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IA         | Intransitive Agent   | The actor purposefully performs an action that does not have a patient or theme.                                                                                                                                                                            | * The **cat** slept                                                                                                                                                                |
|            |                      |                                                                                                                                                                                                                                                             | * **Jonah** jumped into the lake                                                                                                                                                   |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PO         | Possessor            | An entity characterized in a sentence by having, owning, or holding an object.                                                                                                                                                                              | * **Brian** has two turtles                                                                                                                                                        |
|            |                      |                                                                                                                                                                                                                                                             | * This is **Greg**'s purple hat                                                                                                                                                    |
|            |                      |                                                                                                                                                                                                                                                             | * It's **my** hat                                                                                                                                                                  |
|            |                      |                                                                                                                                                                                                                                                             | * These are **mine**                                                                                                                                                               |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EX         | Experiencer          | The person or entity that experiences a state or event but does not initiate or affect it. Usually the experiencer receives sensory input or is described as being affected by an emotional state.                                                          | * **I** want a cookie                                                                                                                                                              |
|            |                      |                                                                                                                                                                                                                                                             | * **Sam** knows Lois                                                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * **Richard** saw the bear                                                                                                                                                         |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PA         | Patient              | The recipient of a transformative action performed by the AGENT. The action leaves the patient changed in form or kind.                                                                                                                                     | * I read the **book**                                                                                                                                                              |
|            |                      |                                                                                                                                                                                                                                                             | * Thomas ate all the **cheese**                                                                                                                                                    |
|            |                      |                                                                                                                                                                                                                                                             | * Cut **it**!                                                                                                                                                                      |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TH         | Theme                | The entity moving in a locative action (often performed by the AGENT). The action leaves the theme changed in space or time.                                                                                                                                | * Put the **jar** on the shelf!                                                                                                                                                    |
|            |                      |                                                                                                                                                                                                                                                             | * The **ball** rolled under the couch                                                                                                                                              |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EL         | Locative Entity      | An (non patient or theme) object or entity that is described as being in a particular place.                                                                                                                                                                | * The **cup** is on the table                                                                                                                                                      |
|            |                      |                                                                                                                                                                                                                                                             | * **Dad** is in his office                                                                                                                                                         |
|            |                      |                                                                                                                                                                                                                                                             | * **It** is there                                                                                                                                                                  |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EO         | Owned Entity         | An (non patient or theme) object or entity that is described as belonging to or being in the possession of a person, animal or character. Entities described as belonging to a non-animate object (e.g. the house's chimney) are described entities (ED).   | * **This** is mine                                                                                                                                                                 |
|            |                      |                                                                                                                                                                                                                                                             | * Brian has four **trucks**                                                                                                                                                        |
|            |                      |                                                                                                                                                                                                                                                             | * Is that your **car**?                                                                                                                                                            |
|            |                      |                                                                                                                                                                                                                                                             | * Is **that** yours?                                                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * This is my **nose**                                                                                                                                                              |
|            |                      |                                                                                                                                                                                                                                                             | * Your **leg**                                                                                                                                                                     |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EP         | Perceived Entity     | An (non patient or theme) object or entity that is described as being perceived through a sense or emotion (usually paired with an experiencer)                                                                                                             | * I want **cookies**                                                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * Look at **that**!                                                                                                                                                                |
|            |                      |                                                                                                                                                                                                                                                             | * She touched the **cat**                                                                                                                                                          |
|            |                      |                                                                                                                                                                                                                                                             | * See? (**+point**)                                                                                                                                                                |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ED         | Described Entity     | An (non patient or theme) object or entity that is described as having a particular characteristic or use.                                                                                                                                                  | * **Frogs** can jump                                                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * A yellow **pen**                                                                                                                                                                 |
|            |                      |                                                                                                                                                                                                                                                             | * **It**'s for me                                                                                                                                                                  |
|            |                      |                                                                                                                                                                                                                                                             | * There are four (+point)                                                                                                                                                          |
|            |                      |                                                                                                                                                                                                                                                             | * **It** needs batteries (+point)                                                                                                                                                  |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EN         | Named Entity         | An (non patient or theme) object or entity that is labeled without further description.                                                                                                                                                                     | * This **box**                                                                                                                                                                     |
|            |                      |                                                                                                                                                                                                                                                             | * **Frogs**                                                                                                                                                                        |
|            |                      |                                                                                                                                                                                                                                                             | * He is a boy (+ point to girl) GS = ADD.err                                                                                                                                       |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AE         | Animate Endpoint     | The person/animal at which a translocational action ends.                                                                                                                                                                                                   | * I threw the ball to the **dog**                                                                                                                                                  |
|            |                      |                                                                                                                                                                                                                                                             | * Give it to **me**                                                                                                                                                                |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IE         | Inanimate Endpoint   | The place at which a translocational action ends.                                                                                                                                                                                                           | * Put it on the **table**                                                                                                                                                          |
|            |                      |                                                                                                                                                                                                                                                             | * It ran down into the **hole**                                                                                                                                                    |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AS         | Animate Source       | The person/animal from whence a translocational action originates or the origin of an entity.                                                                                                                                                               | * The cat ran away from **me**                                                                                                                                                     |
|            |                      |                                                                                                                                                                                                                                                             | * The cookies are from my **mom**                                                                                                                                                  |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IS         | Inanimate Source     | The place from whence a translocational action originates or the origin of an entity.                                                                                                                                                                       | * It ran out from under the **sofa**                                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * The dog is from the **shelter**                                                                                                                                                  |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PT         | Path                 | The relative location where an action takes place or through which an object moves.                                                                                                                                                                         | * Make it go **up and around**                                                                                                                                                     |
|            |                      |                                                                                                                                                                                                                                                             | * The car drove **through** it                                                                                                                                                     |
|            |                      |                                                                                                                                                                                                                                                             | * That one's **far away**                                                                                                                                                          |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SC         | Static Comparative   | The second argument in comparisons of static traits between entities.                                                                                                                                                                                       | * I'm taller than **you**                                                                                                                                                          |
|            |                      |                                                                                                                                                                                                                                                             | * That one is bigger than **this one**                                                                                                                                             |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AC         | Active Comparative   | The second argument in comparisons of active traits between entities.                                                                                                                                                                                       | * I can jump higher than **you**                                                                                                                                                   |
|            |                      |                                                                                                                                                                                                                                                             | * The Flash could run faster than **Superman**                                                                                                                                     |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IN         | Instrument           | A tool used to perform an action. It can take the place of an agent, but is still referred to as an instrument if it is incapable of performing the action without an agent.                                                                                | * She opened the box with a **key**                                                                                                                                                |
|            |                      |                                                                                                                                                                                                                                                             | * He was killed with a **knife**                                                                                                                                                   |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AA         | Accompanying Actor   | A person or entity that performs the action along with the agent.                                                                                                                                                                                           | * I saw the movie with my **dad**                                                                                                                                                  |
|            |                      |                                                                                                                                                                                                                                                             | * Sarah has dinner with **us**                                                                                                                                                     |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BE         | Beneficiary          | A person or animate character who benefits as the result of the action. Purposes (e.g. this is for dinner) are not coded.                                                                                                                                   | * I washed dishes for my **mom**                                                                                                                                                   |
|            |                      |                                                                                                                                                                                                                                                             | * Dad made **us** a snack                                                                                                                                                          |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TI         | Time                 | The time at which an action/event occurs.                                                                                                                                                                                                                   | * **Yesterday**, all our troubles seemed so far away                                                                                                                               |
|            |                      |                                                                                                                                                                                                                                                             | * Jasmine got one **last week**                                                                                                                                                    |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LO         | Location             | The location where an action/event occurs.                                                                                                                                                                                                                  | * I threw a penny into the well at the **park**                                                                                                                                    |
|            |                      |                                                                                                                                                                                                                                                             | * It is on the **table**                                                                                                                                                           |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UC         | Unclear              | The role of the gesture is unclear.                                                                                                                                                                                                                         |                                                                                                                                                                                    |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| X          | Doesn't exist        | The gesture refers to a part of speech that cannot take a semantic role such as a verb.                                                                                                                                                                     |                                                                                                                                                                                    |
+------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ADDs and gestures without speech
--------------------------------

Semantic role should be coded for all gestures regardless of whether they have a semantic correlate or are produced with any speech at all. When gestures are adding information to speech, the coder should try to determine what type of semantic role the object or entity produced in gesture would play in the utterance. If the semantic role for an ADD is unclear, code as UC. 

Deictics
^^^^^^^^

Deictic points produced without speech or produced along with filler utterances (ADD.f) are coded as named entities (EN), since there is no other information provided other than the possible referent.  

Deictic shows points produced without speech or produced along with filler utterances (ADD.f) are coded as perceived entities (EP) since the main effect is to have the other person look at the object and are often accompanied by "look" or "see" when speech is present.

* DP = EN
* DS = EP
* DSDP = EN


Iconics
^^^^^^^

Iconics produced without speech or produced along with filler utterances (ADD.f) may often be described entities (ED), since the form of the iconic provides additional information about the size, shape, location, manner or path of the referent.

When entities have more than one Semantic Role
----------------------------------------------

Many entities are described in more than one way and could be scored as more than one semantic role. Take the sentence "I can see my mother's old friendly turtle is in his basket." The turtle in question is, an EP, EO, ED, and EL all in the same utterance. This occurs in a less drastic way quite often, as in "my purple crayon," "the little one in the corner," or "look at the really big one!" In these cases, all of the possible roles are to be coded. The codes should be recorded in the order in which they appeared in speech and separated by commas without spaces in the form E(X),E(Y). EN is used only when no other semantic role can be used and is not used in combination with other codes. 

Examples:

+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| **Utterance + GESTURE**                                         | **Semantic Correlate**   | **Semantic Role**                         |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "My dog is huggable" + POINT (to dog)                           | DOG                      | EO,ED                                     |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "Kristin's red scissors" + POINT (to scissors)                  | SCISSORS                 | EO,ED                                     |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "The little one in the bowl" + POINT (to object)                | ONE                      | ED,EL                                     |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "He saw my bouncy ball roll under the sofa" + POINT (to ball)   | BALL                     | TH (not an entity because it is active)   |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "We need one more flat-edged one" + POINT (to puzzle piece)     | ONE                      | EP,ED                                     |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "He went to the store" + BEAT (store)                           | STORE                    | IE                                        |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "The dog" + point                                               | DOG                      | EN                                        |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+
| "The dog loves me" + point                                      | DOG                      | EX (not EN)                               |
+-----------------------------------------------------------------+--------------------------+-------------------------------------------+

* When something could be described as something other than an entity as well as an entity (e.g. is a patient but is also described as being owned as in the sentence "I ate Fred's cupcake") it should only be given the non-entity role. Entities are the fall back category when a person or object does not play a more active role in the utterance.

Attributes and Adjectives (RF.a)
--------------------------------

Sometimes a gesture will be used along with an utterance that includes a description of an object but not the object label. These types of utterances are given the G-S relationship "RF.a" for reinforcing attribute. In these situations, the semantic correlate should be listed as the adjective, but the theme as entity described (ED), since the reinforced attribute describes an entity. 

Examples:

+------------------------------+--------------+--------------------+--------------------------+---------------------+
| **Utterance**                | **G-Type**   | **G-S Relation**   | **Semantic Correlate**   | **Semantic Role**   |
+------------------------------+--------------+--------------------+--------------------------+---------------------+
| "This one is pink" + POINT   | DP           | RF.a               | PINK                     | ED                  |
+------------------------------+--------------+--------------------+--------------------------+---------------------+
| "This is pink" + POINT       | DP           | RF.a               | PINK                     | ED                  |
+------------------------------+--------------+--------------------+--------------------------+---------------------+
| "Pink" + POINT               | DP           | RF.a               | PINK                     | ED                  |
+------------------------------+--------------+--------------------+--------------------------+---------------------+
| "This bag is pink" + POINT   | DP           | RF                 | BAG                      | ED                  |
+------------------------------+--------------+--------------------+--------------------------+---------------------+

Ambiguous Verbs
---------------

Verbs such as "to have" can play different roles based on their context. For these verbs, the coder should take into account the surrounding context to try to determine whether the recipient of the verb is a patient, a theme, or an entity.

Examples:

+--------------------------------------+--------------+--------------------+--------------------------+---------------------+
| **Utterance**                        | **G-Type**   | **G-S Relation**   | **Semantic Correlate**   | **Semantic Role**   |
+--------------------------------------+--------------+--------------------+--------------------------+---------------------+
| "I had some cake at lunch" + POINT   | DP           | RF                 | CAKE                     | PA                  |
+--------------------------------------+--------------+--------------------+--------------------------+---------------------+
| "I have two frogs" + POINT           | DP           | RF                 | FROGS                    | EO                  |
+--------------------------------------+--------------+--------------------+--------------------------+---------------------+
| "The house has a chimney" + POINT    | DP           | RF                 | CHIMNEY                  | ED                  |
+--------------------------------------+--------------+--------------------+--------------------------+---------------------+

Choosing Semantic Correlate and Semantic Role for Multi-clause Utterances
-------------------------------------------------------------------------

When utterances have multiple clauses and you need to choose the semantic correlate from either the main or the subordinate clause, rely on the timing of the gesture. If it occurs during the main clause, choose the main clause. If it occurs during the subordinate clause, choose the subordinate clause. 

When utterances have multiple clauses and you need to choose the semantic role from either the main or the subordinate clause *and the semantic correlate is shared by both clauses*, choose the clause with the most action or agency. 

+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+
| Utterance                                              | G-Type          | G-S Relation   | Time       | Semantic Correlate      | Semantic Role                              |
+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+
| I'm trying to get Hanna in here so she'll calm down.   | DP (to Hanna)   | RF             | 4,5,6      | Hanna                   | TH                                         |
+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+
| I'm trying to get Hanna in here so she'll calm down.   | DP (to Hanna)   | RF             | 10,11,12   | She                     | EX                                         |
+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+
| You've got to eat what you've got.                     | DP (to child)   | DA             | 1,2,3,4    | You (in first clause)   | TA                                         |
+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+
| Do you see the chair move?                             | DP (to chair)   | RF             | 1,2,3      | Chair                   | TH (chair is part of subordinate clause)   |
+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+
| Can you bring the cat that's sleeping over there?      | DP (to cat)     | RF             | 4,5        | Cat                     | TH                                         |
+--------------------------------------------------------+-----------------+----------------+------------+-------------------------+--------------------------------------------+

Presence of Referent
====================

Goal: To record whether an object or action is physically present when it is referenced in gesture. 

Explanation
-----------

A gesture should be coded as having a referent present when the object is freely accessible in the space. In other words, could a reference to the object or action using "this" or "it" be disambiguated by a point? The object does not need to be fully accessible to both parties (since we are not making claims about visual perspective taking) only to the gesturer. If an object is out of the room, behind or under another object, or a real world object/action that is not present in the gesturer's space, then the referent is not present. If the referent is an abstract concept incapable of having a visually-accessible referent (e.g. "honor" or "cynicism"), then the present of referent should be coded as "X," since it is not applicable for that referent.

When to code
------------

Presence of referent is coded for: 
  * Deictics
  * Iconics
  * ASL signs
  * Counting

Notes:
 * Not coded for other conventionals (C) or functional acts (FA): mark cell with X
 * Deictics typically have the referent present, but some deictics may be "non-literal" and use a location or object to refer to a different one (i.e. "where is he?" +[point to dad's empty chair])
 * Iconics typically have the referent absent but when iconics refer to direction, the referent is always coded as present. 



+------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| **Code**   | **Referent Presence**                                     | **Definition**                                                                                                                                  | **Example**                                                |
+------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| Y          | Referent is present in gesture's frame of reference       | Gesturer can see the object or action (or its location) that is referred to in gesture.                                                         | "Rabbits are nice" +[point to picture of rabbit in book]   |
+------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| N          | Referent is not present in gesture's frame of reference   | Gesturer can't see the object or action (or its location) that is referred to in gesture.                                                       | "Rabbits are nice" +[iconic for rabbit hopping]            |
+------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| UC         | Coder is unsure whether referent is present               | Gesture refers to an object/action that is not visible to the camera but which might be present (e.g. something on a computer screen or book)   | "Mouse" +[point to computer screen out of camera's view]   |
+------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| X          | Not applicable                                            | Gesture refers to something that can't have a physical referent (e.g. nods, shakes, etc.)                                                       | "Let's do something else" +[dismiss]                       |
+------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+

Examples
--------

+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| **Utterance + GESTURE**                                                        | **Semantic Correlate**   | **Presence of Referent**   |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "Bunny" + POINT (to picture of rabbit)                                         | BUNNY                    | Y                          |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "I think we need one more flat-edged one" + POINT (to pile of puzzle pieces)   | X                        | UC                         |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "Sleeping" + POINT (to dog sleeping)                                           | SLEEPING                 | Y                          |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "Sleeping" + ICONIC (for sleep - sleeping dog is visible)                      | SLEEPING                 | Y                          |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "I got to scoop the ice cream" + ICONIC (for scoop - no scooping visible)      | SCOOP                    | N                          |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "I want to scoop now" + ICONIC (for scoop - mom is visibly scooping)           | SCOOP                    | Y                          |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+
| "I got to scoop the ice cream" + POINT (to fridge - no visible ice cream)      | ADD                      | N                          |
+--------------------------------------------------------------------------------+--------------------------+----------------------------+