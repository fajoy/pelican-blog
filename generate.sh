#!/bin/bash
cd `dirname $0`
pelican  content/ -s pelicanconf.py
