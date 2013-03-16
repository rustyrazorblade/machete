from mako import exceptions
from mako import lookup

_debug = True
_tmpl_lookup = None
_static_dir = None

def setup(template_directories, static_directory, debug=False):
    """
    Configures the template renderer

    :param template_directories: list of directories containing templates
    :param static_directory: the directory where static files are found (css, js, etc)
    """
    global _debug
    global _tmpl_lookup
    global _static_dir
    kwargs = {'directories':template_directories}
#    if debug:
#        kwargs['format_exceptions'] = True

    _tmpl_lookup = lookup.TemplateLookup(**kwargs)
    _static_dir = static_directory
    _debug = debug

def _url_for(dir, filename=''):
    return '/' + dir + '/' + filename

def _add_basic_context(ctx):
    """
    Adds some helper methods and values to the template context
    """
    ctx.setdefault('url_for', _url_for)

def render(template_path, context={}, debug=False):
    """
    renders the template at the given path

    :param template_path: the path to the template to be rendered
    :param context: a dictionary containing all the variables to be passed to the template
    :param debug: show debugging info on template errors
    """
    assert type(template_path) in (str, unicode)
    assert type(context) == dict

    tmpl_ctx = context.copy()
    _add_basic_context(tmpl_ctx)

    try:
        t = _tmpl_lookup.get_template(template_path)
        output = t.render(**tmpl_ctx)
        return output
    except:
        if debug:
            return exceptions.html_error_template().render()
        else:
            raise

