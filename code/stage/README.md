# LDP Transcript Staging

We use the staging area (`stage`) to convert incoming LDP transcripts (as native excel files) into TSV files and ultimately a batch SQL insert/update file.  The resulting SQL file is then applied to the canonical LDP dataset (`$LDP_DB`).

The files resulting from this batch conversion process are stored in dated directories indicating when each batch was converted and integrated into the dataset.  These dated archives are then placed in the appropriate subdir (either `home` for home visits or `school` for school visits, etc.).  The `fix` directory to track and store various fixes we apply to the LDP dataset.

    .
    ├── fix           # fixes applied to LDP dataset
    ├── home          # home visits
    │   ├── base      #   P2 (normally-developing subjects)
    │   └── base_bi   #   P3 (brain-injured subjects)
    ├── school        # school visits
    └── stage         # staging area


## Transcript Conversion Process

We use this staging directory to convert a set of incoming transcripts (excel files) to a set of SQL insert (or update) files to be applied to the LDP dataset (a sqlite database, which should be referenced by the `$LDP_DB` environment variable): one for inserting/updating the `utterances` table and another for the `transcripts` table.

We extract the `info` worksheet from each transcript in order to update the `transcripts` table, (which contains meta-info about each transcript, such as the spontaneous speech time that was recorded, etc.).

We extract the `transcript` workseet from each transcript in order to update the `utterances` table (which contains rows for each transcribed utterance).

(Note: This is all rather hackish. Much could be streamlined if we had strong guarantees regarding transcript formatting.  As it is, the transcribers often unintentionally introduce formatting errors which foil any possibility of a monolithic updating/conversion process.  This possibility should be revisited, though, if stronger transcript formatting validation can be incorporated into the transript submission process.)


## Converting `transcript` worksheets

* Run the initialization script (`init.sh`) to set up a dated directory 
  structure and temporary database (`MM-DD-YY/data.db`).

* Copy new/incoming transcripts to the resulting `MM-DD-YY/excel` directory.

* Use `dump_sheets.sh` to dump the `info` and `transcript` worksheets of
  each transcript file in the `excel` directory.
   
* Use `trans2tsv` (in `$LDP/code/trunk/bin`) to generate a batch TSV file called `utterances.tsv` with data from each transcript worksheet.

```
$ SOURCE_DIR=$(date "+%Y-%m-%d")  
$ trans2tsv $SOURCE_DIR/sheets/transcript/* > $SOURCE_DIR/utterances.tsv
```

* Use `import.py` to import canonical transcript data into sqlite db
  (`import.py $SOURCE_DIR`).

* Use `copy.py` to copy **p_utts** and **c_utts** column values to 
  **p_utts_orig** and **c_utts_orig** (`copy.py $SOURCE_DIR`).

* Use `fix.py` to fix case on first word of each utterance (`fix.py $SOURCE_DIR`).

* Use `export.py` to export utterances table as TSV file (`export.py
  $SOURCE_DIR/utterances.revised.tsv`).

* Use `tsv2sql` to convert revised/exported utterances to SQL insert statements
  (`tsv2sql --mode insert --table utterances $SOURCE_DIR/utterances.revised.tsv > $SOURCE_DIR/insert.sql`)

* Apply insert statements to the working copy of the LDP database (`sqlite3 $LDP_DB < $SOURCE_DIR/insert.sql`).

> `$LDP_DB` should reference the path to your working copy of the LDP 
> sqlite database (e.g., `~/Documents/Work/LDP/data/ldp.db`).

... or ...

Alternatively, use the following command to create a sql insert file:

    sqlite3 $SOURCE_DIR/temp.db 'select * from utterances' | 
      sed 1d | 
      tsv2sql --mode insert --table utterances - > $SOURCE_DIR/insert.sql

This file can then be used to update the LDP Dataset:

    sqlite3 $LDP_DB < $SOURCE_DIR/insert.sql 

... or ...

Copy the contents over in a single pipeline without intermediary file:

    sql $SOURCE_DIR/temp.db 'select * from utterances' | 
      sed 1d | 
      tsv2sql --mode insert --table utterances - | 
      sqlite3 $LDP_DB


## Converting `info` worksheets

* use the dumped **info** worksheets to extract out the spontaneous speech times.  It's easy enough to grep for `^Spontaneous`:

```bash
for i in *tsv; do echo "$i\t" >> minutes.tsv; grep "^Spon" $i >> minutes.tsv;
done;
```

* update `transcripts` table


## Updating the LDP Master/Reference Database

The latest version of the LDP database is always hosted on [`joyrexus.spc.uchicago.edu`](http://joyrexus.spc.uchicago.edu/ldp/data/db/latest/), so any batch inserts are typically applied to the local working copy of the LDP database on that host
(viz., `/Users/jvoigt/Documents/Work/LDP/data/trunk/ldp.db`).  Use the
[`Makefile`](https://github.com/joyrexus/ldp/blob/master/data/Makefile#L38-L41) within the same directory to update the hosted reference version
(`http://joyrexus.spc.uchicago.edu/ldp/data/db/latest/`):

    ssh joyrexus.spc.uchicago.edu
    cd /Users/jvoigt/Documents/Work/LDP/data/trunk/
    make dump
    
Users with pre-existing working copies of the LDP database can then use the
Makefile's `make new` directive to get the latest instance.

Alternatively, [this build script](https://github.com/joyrexus/ldp/blob/master/data/build.sh) can be used to build a new copy.
