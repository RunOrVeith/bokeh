#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Various kinds of button widgets.

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports
from ...core.enums import ButtonType
from ...core.has_props import abstract, HasProps
from ...core.properties import Bool, Enum, Instance, Int, List, Override, String, Tuple

from ..callbacks import Callback

from .icons import AbstractIcon
from .widget import Widget

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'AbstractButton',
    'Button',
    'ButtonLike',
    'Dropdown',
    'Toggle',
)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

@abstract
class ButtonLike(HasProps):
    ''' Shared properties for button-like widgets.

    '''

    button_type = Enum(ButtonType, help="""
    A style for the button, signifying it's role.
    """)

@abstract
class AbstractButton(Widget, ButtonLike):
    ''' A base class that defines common properties for all button types.

    '''

    label = String("Button", help="""
    The text label for the button to display.
    """)

    icon = Instance(AbstractIcon, help="""
    An optional image appearing to the left of button's text.
    """)

    callback = Instance(Callback, help="""
    A callback to run in the browser whenever the button is activated.
    """)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class Button(AbstractButton):
    ''' A click button.

    '''

    clicks = Int(0, help="""
    A private property used to trigger ``on_click`` event handler.
    """)

    def on_click(self, handler):
        ''' Set up a handler for button clicks.

        Args:
            handler (func) : handler function to call when button is clicked.

        Returns:
            None

        '''
        self.on_change('clicks', lambda attr, old, new: handler())

    def js_on_click(self, handler):
        ''' Set up a JavaScript handler for button clicks. '''
        self.js_on_change('clicks', handler)


class Toggle(AbstractButton):
    ''' A two-state toggle button.

    '''

    label = Override(default="Toggle")

    active = Bool(False, help="""
    The initial state of a button. Also used to trigger ``on_click`` event
    handler.
    """)

    def on_click(self, handler):
        """ Set up a handler for button state changes (clicks).

        Args:
            handler (func) : handler function to call when button is toggled.

        Returns:
            None

        """
        self.on_change('active', lambda attr, old, new: handler(new))

    def js_on_click(self, handler):
        """ Set up a JavaScript handler for button state changes (clicks). """
        self.js_on_change('active', handler)

class Dropdown(AbstractButton):
    ''' A dropdown button.

    '''

    label = Override(default="Dropdown")

    value = String(help="""
    A private property used to trigger ``on_click`` event handler.
    """)

    default_value = String(help="""
    A default value to set when a split Dropdown's top button is clicked.

    Setting this property will cause the Dropdown to be rendered as
    split.
    """)

    menu = List(Tuple(String, String), help="""
    Button's dropdown menu consisting of entries containing item's text and
    value name. Use ``None`` as a menu separator.
    """)

    def on_click(self, handler):
        ''' Set up a handler for button or menu item clicks.

        Args:
            handler (func) : handler function to call when button is activated.

        Returns:
            None

        '''
        self.on_change('value', lambda attr, old, new: handler(new))

    def js_on_click(self, handler):
        ''' Set up a JavaScript handler for button or menu item clicks. '''
        self.js_on_change('value', handler)

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
