import nbformat

notebook_path = "C:\\Users\\jarne\\Downloads\\Cancer_Research.ipynb"  # Update with your filename

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

widgets = nb.metadata.get("widgets", {})
widget_block = widgets.get("application/vnd.jupyter.widget-state+json", {})

# Only fix if "state" key is missing
if "state" not in widget_block:
    print("Wrapping widget data in 'state' key...")
    nb.metadata["widgets"]["application/vnd.jupyter.widget-state+json"] = {
        "state": widget_block
    }

    with open(notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print("Notebook widget metadata fixed.")
else:
    print("Notebook already valid.")

