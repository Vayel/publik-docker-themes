import os
import argparse
import json


def update_json(slug, label):
    with open("themes.json") as f:
        config = json.load(f)
    config.append({
        "id": slug,
        "label": label,
        "variables": {
            "css_variant": slug,
            "theme_color": "#FF0000"
        },
    })
    with open("themes.json", "w") as f:
        json.dump(config, f, indent=2)


def create_theme(slug, label):
    theme_path = os.path.join("themes", slug)
    if os.path.isdir(theme_path):
        raise ValueError("Theme '{theme}' already exists.".format(theme=slug))
    os.makedirs(theme_path)
    os.makedirs(os.path.join(theme_path, "static"))
    os.makedirs(os.path.join(theme_path, "templates"))
    update_json(slug, label)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("label", nargs="?", default=None)
    args = parser.parse_args()
    create_theme(args.slug, args.label or args.slug)
