from os.path import join

CASCADES = {
    "Face front": {
        "path": join("haarcascades", "faces", "haarcascade_frontalface_default.xml"),
        "color": (255, 0, 0),
        "draw": True
    },
    "Face profile": {
        "path": join("haarcascades", "faces", "haarcascade_profileface.xml"),
        "color": (255, 0, 0),
        "draw": True
    },
    "Smile": {
        "path": join("haarcascades", "faces", "haarcascade_smile.xml"),
        "color": (0, 255, 0),
        "draw": False
    },
    "Eyes": {
        "path": join("haarcascades", "faces", "haarcascade_eye.xml"),
        "color": (0, 255, 0),
        "draw": True
    },
    "Full body": {
        "path": join("haarcascades", "faces", "haarcascade_fullbody.xml"),
        "color": (0, 255, 0),
        "draw": False
    },
    "Cat face": {
        "path": join("haarcascades", "faces", "haarcascade_frontalcatface_extended.xml"),
        "color": (0, 255, 0),
        "draw": False
    }
}
