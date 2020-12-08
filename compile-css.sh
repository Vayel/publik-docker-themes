#!/bin/bash

BASE_DIR=`pwd`

cd themes
for theme in *
do
  cd $BASE_DIR
  echo "Building $theme..."

  static_dir=themes/$theme/static

	python3 make_data_uris.py --source $static_dir/images/ \
    --source publik-base-theme/static/includes/img/ \
    --dest $static_dir/_data_uris.scss \
    --dest publik-base-theme/static/includes/_data_uris.scss

  cd $static_dir && sassc style.scss style.css
	rm -rf $static_dir/.sass-cache/
done
