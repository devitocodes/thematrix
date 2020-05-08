#!/bin/bash

if [[ `git status --porcelain` ]]; then
  echo "Changes"
else
  echo "No changes"
fi
