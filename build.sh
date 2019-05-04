#!/usr/bin/env bash
for file in content/*.md content/*/*.md
do
    sed -i "/^tags:/s/ '/ /g" $file
    sed -i "/^tags:/s/'$//g" $file
done
pelican content
