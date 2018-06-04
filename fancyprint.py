#!/usr/bin/env/python3
#===============================================================================
# fancyprint.py
#===============================================================================

"""Print text with fancy colors and formatting"""




# Functions --------------------------------------------------------------------

def fprint(*objects, color='', style='', **kwargs):
    """Print text with fancy colors and formatting
    
    Parameters
    ----------
    *objects
        objects to print
    color : str
        one- or two-character string specifying color:
        r (red)
        dr (dark red)
        hr (highlight red)
        g (green)
        dg (dark green)
        hg (highlight green)
        y (yellow)
        dy (dark yellow)
        hy (highlight yellow)
        b (blue)
        db (dark blue)
        hb (highlight blue)
        m (magenta)
        dm (dark magenta)
        hm (highlight magenta)
        c (cyan)
        dc (dark cyan)
        hc (highlight cyan)
    style : str
        one- or two-character string specifying style
        b (bold)
        u (underline)
    **kwargs
        other arguments passed to print()
    """

    print(
        *(
            '{}{}{}\033[0m'.format(
                COLOR_DICT[color] if color else '',
                ''.join(STYLE_DICT[char] for char in style),
                object
            )
            for
            object
            in
            objects
        ),
        **kwargs
    )




# Constants --------------------------------------------------------------------

COLOR_DICT = {
    'r': '\033[91m',
    'dr': '\033[31m',
    'hr': '\033[41m',
    'g': '\033[92m',
    'dg': '\033[32m',
    'hg': '\033[42m',
    'y': '\033[93m',
    'dy': '\033[33m',
    'hy': '\033[43m',
    'b': '\033[94m',
    'db': '\033[34m',
    'hb': '\033[44m',
    'm': '\033[95m',
    'dm': '\033[35m',
    'hm': '\033[45m',
    'c': '\033[96m',
    'dc': '\033[36m',
    'hc': '\033[46m'
}

STYLE_DICT = {'b': '\033[1m', 'u': '\033[4m'}
