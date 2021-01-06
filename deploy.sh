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

BASE_DIR=`pwd`
DEST_DIR=$BASE_DIR/deployed

mkdir -p "$DEST_DIR/templates/variants"

cd themes
for theme in *
do
  if [ "$theme" = __* ]; then
    echo "Skipping deployment for abstract theme $theme"
    continue
  fi

  echo "Deploying $theme..."
  copy_dir "$BASE_DIR/themes/$theme/static" "$DEST_DIR/static/$theme"
  copy_dir "$BASE_DIR/themes/$theme/templates" "$DEST_DIR/templates/variants/$theme"
done

cp "$BASE_DIR/themes.json" "$DEST_DIR/themes.json"
