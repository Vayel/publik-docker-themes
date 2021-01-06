import os
import argparse
import json
from shutil import copyfile


def update_json(slug, label, color):
    with open("themes.json") as f:
        config = json.load(f)
    config.append({
        "id": slug,
        "label": label,
        "variables": {
            "css_variant": slug,
            "theme_color": color,
        },
    })
    with open("themes.json", "w") as f:
        json.dump(config, f, indent=2)


def create_theme(slug, label, color, abstract):
    if abstract:
        slug = f"__{slug}"
    theme_path = os.path.join("themes", slug)
    if os.path.isdir(theme_path):
        raise ValueError("Theme '{theme}' already exists.".format(theme=slug))

    static_path = os.path.join(theme_path, "static")
    os.makedirs(theme_path)
    os.makedirs(static_path)
    os.makedirs(os.path.join(theme_path, "templates"))

    open(os.path.join(static_path, "_custom.scss"), "w").close()
    for fname in ("style.scss", "_vars.scss"):
        copyfile(fname + ".template", os.path.join(static_path, fname))

    if not abstract:
        update_json(slug, label, color)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("label", nargs="?", default=None)
    parser.add_argument("color", nargs="?", default=None)
    parser.add_argument("--abstract", action="store_true", default=False)
    args = parser.parse_args()
    create_theme(args.slug, args.label or args.slug, args.color or "#FFFFFF", args.abstract)
