## Template Pelican blog

This is a template of my blog https://blog.formallyapplied.com

The repository contains:
- A slightly modified [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) theme
- Formally, a customized [bootswatch](https://bootswatch.com/) theme based on Sandstone.
- Two plugins: sitemap generation using **extended_sitemap** plugin and multi-language support using **i18n_subsites**.
- Required config files.

## Usage

Basically, you only need to install  [Pelican](http://docs.getpelican.co) and then move to the home directory of this repository. From there, start the local webserver which listens on port 8000 by default.

```bash
$ make devserver
```
Now checkout the blog on https://localhost:8000. Enjoy!

## License

My contributions are in the public domain. Please check the respective licenses of the components used.
