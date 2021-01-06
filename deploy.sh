#!/bin/bash

./compile-css.sh

function copy_dir() {
  SRC=$1
  DEST=$2

  rm -rf $DEST
  mkdir -p $DEST
  if [ -d "$SRC" ] && [ ! -z "$(ls -A $SRC)" ]; then
    cp -R $SRC/* $DEST
  fi
}

DEST_DIR=deployed
BASE_DIR=`pwd`

mkdir -p "$DEST_DIR/templates/variants"

cd themes
for theme in *
do
  echo "Deploying $theme..."
  copy_dir "$BASE_DIR/themes/$theme/static" "$DEST_DIR/static/$theme"
  copy_dir "$BASE_DIR/themes/$theme/templates" "$DEST_DIR/templates/variants/$theme"
done

cp "$BASE_DIR/themes.json" "$DEST_DIR/themes.json"
