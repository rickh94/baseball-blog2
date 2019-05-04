#!/usr/bin/env bash
for file in content/*.md content/*/*.md
do
    sed -i "/^tags:/s/ '/ /g" $file
    sed -i "/^tags:/s/'$//g" $file
done
pelican content
yarn run para-cli create "output/20*.html" --endpoint https://paraio.com --type "article" --sanitize --accessKey $PARA_ACCESS_KEY --secretKey $PARA_SECRET_KEY
yarn run para-cli create "output/tag/*.html" --endpoint https://paraio.com --type "tag" --sanitize --accessKey $PARA_ACCESS_KEY --secretKey $PARA_SECRET_KEY
yarn run para-cli create "output/category/*.html" --endpoint https://paraio.com --type "category" --sanitize --accessKey $PARA_ACCESS_KEY --secretKey $PARA_SECRET_KEY
yarn run para-cli create "output/author/*.html" --endpoint https://paraio.com --type "author" --sanitize --accessKey $PARA_ACCESS_KEY --secretKey $PARA_SECRET_KEY
