# Themes for Publik

Themes for [https://github.com/Vayel/publik-docker](https://github.com/Vayel/publik-docker).

```
cd publik-docker/data
git clone https://github.com/Vayel/publik-docker-themes.git themes --recurse-submodules
```

## How themes work

See [publik-docker documentation](https://github.com/Vayel/publik-docker/blob/master/docs/themes.md).

We're following [Entr'ouvert guidelines](https://dev.entrouvert.org/projects/prod-eo/wiki/HowDoWeDoThemes).

## Create theme

```
python3 add-theme.py <slug> [<label>] [<color>] [--abstract]
```

Abstract themes are bases for other themes. They may contain uncomplete SCSS that
will be completed by their children (e.g. the main colors). They are not added
to the `themes.json` and their slug is prepended by `__`.

## Delete theme

```
python3 delete-theme.py <slug>
```

## Update base theme

```
cd publik-base-theme
git fetch
git checkout master
cd ..
git add publik-base-theme
git commit -m "Update base theme"
```

## Compile theme

```
./deploy.sh
```

Assets are compiled and moved to `deployed`. Notice that it's just for testing
purpose. To apply themes to publik instances, refer to https://github.com/Vayel/publik-docker/blob/master/docs/themes.md
