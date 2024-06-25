#!/usr/bin/env bash
-- Creates a table named first_table with id(int)
-- and name of type varchar(256) and not fail if table 
-- first_table exists
CREATE table IF NOT EXISTS first_table(id INT, name VARCHAR(256));
