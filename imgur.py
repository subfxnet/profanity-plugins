"""
Requires imgur API
    pip install imgurpython
Requires scrot installed for screenshot
    sudo apt-get install scrot

"""

import prof
import subprocess
from os import path

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

client_id = '19c4ba3fc2c26ef'
client_secret = 'dd5b0918a2f5d36391d574bd2061c50b47bade63'
client = ImgurClient(client_id, client_secret)


def _cmd_imgur(arg1):
    if arg1 == "screenshot":
        file_path = "/tmp/_prof_scrot.png"
        command = "scrot " + file_path
        subprocess.call(command, shell=True)
    else:
        try:
            file_path = path.expanduser(arg1)
        except IOError as ioe:
            prof.cons_show('Could not find file at ' + file_path)
            return
    try:
        data = client.upload_from_path(file_path, config=None, anon=True)
        prof.send_line(data['link'])
    except ImgurClientError as e:
        prof.log_error('Could not upload to Imgur - ' + e.error_message)
        prof.log_error('Imgur status code - ' + e.status_code)


def prof_init(version, status, account_name, fulljid):
    synopsis = [
        "/imgur <file_path>",
        "/imgur screenshot"
    ]
    description = "Upload an image or screenshot to imgur and send the link"
    args = [
        [ "<file_path>",  "full path to image file" ],
        [ "screenshot", "upload a full screen capture" ]
    ]
    examples = [
        "/imgur ~/images/cats.jpg",
        "/imgur screenshot"
    ]

    prof.register_command("/imgur", 1, 1, synopsis, description, args, examples, _cmd_imgur)
    prof.completer_add("/imgur", [ "screenshot" ])