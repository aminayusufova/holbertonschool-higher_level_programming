#!/usr/bin/env bash
-- script that removes all records with score <= 5 in the
-- second_table
DELETE FROM second_table
WHERE score <= 5;
