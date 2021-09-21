profanity-plugins
=================

* [Website documentation](https://profanity-im.github.io/plugins.html)

Building Profanity with plugin support
--------------------------------------

Dependencies required:

```
autoconf-archive
libtool
```

For Python plugins the following is also required:

```
python-dev
```

Installing plugins
------------------

Use the `/plugins install` command, e.g.

```
/plugins install ~/projects-git/profanity-plugins/stable/say.py
```

See the `/help plugins` command for further plugin management options.

Branches
--------

* `0.5.0`: Maintenance branch compatible Profanity 0.5.0
* `0.5.1`: Maintenance branch compatible Profanity 0.5.1
* `master`: Development for Profanity 0.6.0 - 0.11.x

Developing plugins
------------------

API Documentation:
* [Python API](https://profanity-im.github.io/plugins/0.5.1/python/html/prof.html)
* [Python hooks](https://profanity-im.github.io/plugins/0.5.1/python/html/plugin.html)
* [C API](https://profanity-im.github.io/plugins/0.5.1/c/html/profapi_8h.html)
* [C hooks](https://profanity-im.github.io/plugins/0.5.1/c/html/profhooks_8h.html)

