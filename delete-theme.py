import os
import argparse
import json
import shutil


def update_json(slug):
    themes = []
    with open("themes.json") as f:
        for theme in json.load(f):
            if theme["id"] != slug:
                themes.append(theme)
    with open("themes.json", "w") as f:
        json.dump(themes, f, indent=2)


def delete_theme(slug):
    theme_path = os.path.join("themes", slug)
    shutil.rmtree(theme_path)
    update_json(slug)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()

    confirm = input("Confirm deletion of {theme}? [y/n] ".format(theme=args.slug))
    if confirm.lower() == "y":
        delete_theme(args.slug)
    else:
        print("Operation aborted.")
