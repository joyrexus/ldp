# README

NORC is requesting counts of word types and tokens for each student (for each story) as well as counts of the `|` delimiter used within subject utterances.

---

NOTE: To some extent, it seems the `|` code was used more as a clause *marker* than as a [delimiter](http://en.wikipedia.org/wiki/Delimiter-separated_values) separating clause values.

The report file named `compare.tsv` compares the counts of the `|` code found
in each story with the clause count judgments made by human reviewers.

---

NORC provided an excel file (`excel/data.xlsx` originally "`WPB new order.xlsx`") containing all utterances to be analyzed.

The provided data file contains 11 columns of interest, 5 for each of the two stories (A and B):

    INDEX  COL    HEADER          
        0    A    SU_ID           # STUDENT ID

                                  # STORY A
        1    B    WPBNA_PG1-2     # 1
        2    C    WPBNA_PG3-4     # 2
        3    D    WPBNA_PG5-6     # 3
        4    E    WPBNA_PG7-8     # 4 
        5    F    WPBNA_PG9-10    # 5
        
                                  # STORY B
       11    L    WPBNB_PG1-2     # 1
       12    M    WPBNB_PG3-4     # 2
       13    N    WPBNB_PG5-6     # 3
       14    O    WPBNB_PG7-8     # 4 
       15    P    WPBNB_PG9-10    # 5


I converted this (see `data.tsv`) into a more convenient format with the following columns:

    ID     - student id
    STORY  - A or B
    PAGE   - 1 (1-2), 2 (3-4), etc.
    |      - count of "|" delimiters within original text
    TOKENS - word tokens parsed from TEXT with commas to separate clauses
    TEXT   - original text


The final report (`report.xls`) contains the following columns:

    ID      - student ID
    STORY   - A or B
    DELIMS  - delimiter count
    TOKENS  - word token count
    TYPES   - word type count
