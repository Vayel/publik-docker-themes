# Theme for Publik by https://www.laetis.fr/

```
git clone https://github.com/Vayel/publik-themes.git --recurse-submodules
cd publik-themes
```

## How themes work

We're following [Entr'ouvert guidelines](https://dev.entrouvert.org/projects/prod-eo/wiki/HowDoWeDoThemes).

Themes are made of two folders:

* `static` that contains theme-specific static files (css, images...)
* `templates` that contains theme-specific Django templates with the same structure as `publik-base-theme/templates`

Custom themes are built on top of Publik base theme. It means that you only have
the templates and the statics you want to add/override compared to the base theme.

## Create theme

```
python3 create-theme.py <slug>
```

## Deploy themes

When you are on the machine where your Publik instance is running:

```
./deploy.sh
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
