# Pelican Theme: Waste of Space

pelican-wasteofspace is a theme for the Pelican static site generator.

This theme focuses on tags rather than categories.  Opengraph
meta properties are presented for each page of content.

## Incomplete Release
This theme doesn't support pagination or multiple languages yet.
I'm sure other issues will need addressed if anybody else starts
using the theme.

## pelicanconf Configuration File
A sample [pelicanconf-example.py] config file is included with this theme.

### Selet the theme
Choose the theme and set the required configuration variables

``` python3
# add to pelicanconf.py

SITENAME ='Waste Of Space'

# Use theme wasteofspace
THEME = 'themes/pelican-wasteofspace'

SITESUBTITLE = 'Custom-made, luxury planet building.'
HEADER_IMAGE = '/theme/images/header-image.png'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True


```

### Social Media Icons
The theme can display a series of social media buttons, or other links.
Any url may be specified.  The label for each url must be selected from
a [http://fontawesome.io/icons](Font Awesome icon identifier).

``` python3
# add to pelicanconf.py

SOCIAL = (('phone','tel:5558675309'),
          ('email','mailto:mitch@mitchjacksontech.com'),
          ('facebook','https://facebook.com/mitchjacksontech'),
          ('github','https://github.com/mitchjacksontech'),
          ('linkedin','https://linkedin.com/in/mitchjacksontech'))

```

### Footer links and copyright slug
A series of links may be displayed on the footer.

``` python3
# Add to pelicanconf.py
LINKS_TITLE = 'powered by:'
LINKS = (('Pelican','https://github.com/getpelican/pelican'),
         ('pelican-wasteofspace theme','#'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Boostrap', 'https://getbootstrap.com'),
         ('Linode', 'https://linode.com'))

COPYRIGHT_SLUG = '2017 Jackson Runs Some Servers'

```


### OpenGraph
[http://ogp.me/](Open Graph) provides a standardized set of metadata
attributes enabling social media platforms to better present content
from your website.

Set these metadata properties globally for your website with these
variables.  Then override them in the metadata section of your pages.

``` python3

# Open Graph default metadata
OG_TYPE        = 'article'
OG_TITLE       = 'Website Home Page'
OG_DESCRIPTION = 'Visit the home page of my website, where I publish content'
OG_IMAGE       = '/theme/images/og_image.png'
OG_SITE_NAME   = 'Pelican Static Website'

```

### HTML Metadata Tags
Optional additional meta tags may be included by defining a METADATA list.

``` python3

# Include HTML Metadata
METADATA = (('author', 'webmaster@mywebsite.com'),
            ('description', 'Website Home Page'))

```


### Jinja filter allowing sort_by_article_count
The following block must be included within pelicanconf.py.
[https://github.com/getpelican/pelican/issues/1667](Attributed)

``` python3
# must be included within pelicaonconf.py

# JINJA Filter sort_by_article_count
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order


```
