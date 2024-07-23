import os
import shutil


def copy_static(src, dist):
    if not os.path.exists(dist):
        print("[creating dir]", dist)
        os.mkdir(dist)

    items = os.listdir(src)

    for item in items:
        new_dist = f"{dist}/{item}"
        new_src = f"{src}/{item}"

        if os.path.isfile(new_src):
            print("[copy]", new_src, "->", new_dist)
            try:
                shutil.copy(new_src,  new_dist)
            except:
                raise Exception("[error]", "Failed to copy:", new_src, "->", new_dist)
        else:
            copy_static(new_src, new_dist)
