.. _introduction:

1. Introduction
===============

The Language Development Project (LDP) is, broadly, a longitudinal study of the 
interaction between the developing language and gesture faculties of young
children and how this influences and is influenced by the parent-child
relationship.  In order to study these phenomena, the LDP films communicative 
interactions between parents, children, and the visiting experimenters and 
subsequently employs a system of transcripts that record various data about the 
nature and content of the speech and gesture captured on video.

As the project itself has developed, the usefulness and accuracy of the data 
captured in the original transcript format has been repeatedly reevaluated and
modified to meet new needs, leading to a series of standards adoptions and the 
formulation of additional annotation schemas for more fine-grained analysis of 
specific aspects of the data.  The result is a wealth of information that can be
intimidating to the uninitiated.  This specification is an attempt to draw a
unified and coherent picture of the various levels of annotation for both
researchers who have been with the LDP for many years and those interested in
leveraging the data collected for new and previously unimagined projects.


.. _notation:

.. index::
   single: format; notation

1.1. Notation
-------------

Transcripts are organized into columns, each column having its own set of
possible values and symbols.  In order to describe the permitted combinations,
we specify a column format.  The descriptions of column entry format use a 
modified :term:`BNF grammar notation` that uses the following style of
definition:

Below we will define a column we'll call "Jump":

.. productionlist::
   entry: (`null` | `code`) [`op` (`null` | `code`)]*
   null: ""
   code: "hop" | "skip" | "leap" | "vault"
   op: "+" | "-"

According to the rules, which we will explain in a moment, one possible entry 
in "Jump" is ``hop + skip - + leap``.  Why is that? Knowing how to read a column
format helps answer that question.

A definition is made up of one or more rules.  Each rule has a *name*, a 
``::=``, and a *description*.  The first rule of the definition describes the
make-up of an ``entry`` in the column, and each additional rule describes a 
sub-part of the first one.  As you read across the first rule's *description*, 
just replace each *name* with its corresponding *description*, i.e. replace 
``null`` with ``""``, ``op`` with ``"+" | "-"``, etc.  If the *description* of
a *name* has other *name*\ s in it, you can replace those with their
*definitions* and so on until all you have is a *description* of ``entry`` with
no *names* in it at all.

Each symbol in the *description*\ s has its own meaning in this notation.  
Quotation marks set aside literal strings and white spaces serve to do nothing
other than separate the tokens.

A vertical bar (``|``) is used to separate alternatives and parentheses are used
for grouping, so ``(null | code)``, which expands to
``("" | "hop" | "skip" | "leap" | "vault")``, means you can have an
empty string or any one of the words ``hop``, ``skip``, ``leap``, or ``vault``
as the first thing in an ``entry``.  In our example, ``hop`` is the first
element of our ``entry``, which satisfies this rule.

Square brackets (``[]``) set aside optional arguments, so the next part, 
``[op (null | code)]``, means you can optionally follow the first ``null`` or 
``code`` in the ``entry`` with an ``op`` followed by another ``null`` or 
``code``.  After ``hop``, we see ``+ skip``.  ``+`` is an ``op`` and ``skip`` is
one of the permitted ``code``\ s.  So far so good.

A star (``*``) indicates one or more repetitions of the unit immediately 
preceding it.  In this case, the arguments in the square brackets precede it, 
meaning that we can continue to add as many ``op`` and ``null`` or ``code`` 
pairs as we like.  The remainder of our example, ``- + leap``, is an ``op``, a
``null``, another ``op``, and one of our available ``code``\ s.  The example,
therefore, satisfies the grammar as laid out in the definition above.

Angle brackets (``<>``) surround an informal description or comment.  While
there are none of these in the definition provided, they will generally be used
when, for example, the list of possible codes is not exhaustive and but we still
want to convey a sense of what is allowed.

For the sake of completeness, here is an invalid entry in "Jump":
``hop + skip vault - flip``.  This fails on two counts.  For one, there is no
``op`` between ``skip`` and ``vault``.  Second, ``flip`` is not one of the
values listed in the *definition* of ``code``.
