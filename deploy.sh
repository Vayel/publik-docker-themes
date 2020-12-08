#!/bin/bash

./compile-css.sh

function copy_dir() {
  SRC=$1
  DEST=$2

  rm -rf $DEST
  mkdir -p $DEST
  cp -R "$SRC/*" $DEST
}

DEST_DIR=/usr/share/publik/themes/publik-base

cd themes
for theme in *
do
  echo "Deploying $theme..."
  copy_dir "$theme/static" "$DEST_DIR/static/$theme"
  copy_dir "$theme/templates" "$DEST_DIR/templates/variants/$theme"
done

cd ..
cp themes.json "$DEST_DIR/themes.json"
