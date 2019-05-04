#!/usr/bin/env bash
for file in content/*.md content/*/*.md
do
    sed -i "/^tags:/s/ '/ /g" $file
    sed -i "/^tags:/s/'$//g" $file
done
pelican content
yarn run para-cli create "output/**/*.html" --endpoint https://paraio.com --type "blogpost" --sanitize --accessKey $PARA_ACCESS_KEY --secretKey $PARA_SECRET_KEY
