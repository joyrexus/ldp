# Makefile for LDP dataset

VERSION := $(shell cat VERSION)
 
.PHONY: svn all clean

all: svn ldp.db update

svn:
	svn update

ldp.db: init.sh
	@echo "Making the LDP dataset ... please be patient"
	sh init.sh
	@echo "Finished making ldp.db"

updates := $(wildcard tables/*/updates/$(VERSION)/*.sql)

apply: $(updates)
	@for file in $?; \
		do echo "Applying updates from $$file"; \
            sqlite3 ldp.db < $$file; \
		done

update: svn apply
	@svn info $(LDP_DATA/tables/utterances/updates) | \
		 awk '/Rev:/ { sub(/.*: /, ""); print }' > update
				
clean:
	rm ldp.db
	rm update

new: svn build.sh
	@echo "Making the latest LDP dataset ... please be patient"
	sh build.sh
	@echo "Finished making ldp.db"

dump: 
	@echo "Dumping contents of the latest LDP dataset ... please be patient"
	sh dump.sh
	@echo "Finished dumping ldp.db"
