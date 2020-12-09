# Themes for Publik

Themes for [https://github.com/Vayel/publik-docker](https://github.com/Vayel/publik-docker).

```
git clone https://github.com/Vayel/publik-docker-themes.git --recurse-submodules
cd publik-docker-themes
```

## How themes work

See [publik-docker documentation](https://github.com/Vayel/publik-docker/blob/master/docs/themes.md).

We're following [Entr'ouvert guidelines](https://dev.entrouvert.org/projects/prod-eo/wiki/HowDoWeDoThemes).

## Create theme

```
python3 add-theme.py <slug> [<label>]
```

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
