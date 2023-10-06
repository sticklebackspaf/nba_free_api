#!/usr/bin/env sh

sqlite3 -batch "$PWD/free_nba_cache.sqlite" <"$PWD/db/initdb.sql"