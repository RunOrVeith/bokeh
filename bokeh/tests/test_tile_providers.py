#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports
from bokeh.models.tiles import WMTSTileSource
from bokeh._testing.util.api import verify_all

# Module under test
import bokeh.tile_providers as bt

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

ALL = (
    'CARTODBPOSITRON',
    'CARTODBPOSITRON_RETINA',
    'STAMEN_TERRAIN',
    'STAMEN_TERRAIN_RETINA',
    'STAMEN_TONER',
    'STAMEN_TONER_BACKGROUND',
    'STAMEN_TONER_LABELS',
    'get_provider',
    'Provider'
)

_CARTO_URLS = {
    'CARTODBPOSITRON':        'https://tiles.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
    'CARTODBPOSITRON_RETINA': 'https://tiles.basemaps.cartocdn.com/light_all/{z}/{x}/{y}@2x.png',
}

_STAMEN_URLS = {
    'STAMEN_TERRAIN':          'http://tile.stamen.com/terrain/{Z}/{X}/{Y}.png',
    'STAMEN_TERRAIN_RETINA':   'http://tile.stamen.com/terrain/{Z}/{X}/{Y}@2x.png',
    'STAMEN_TONER':            'http://tile.stamen.com/toner/{Z}/{X}/{Y}.png',
    'STAMEN_TONER_BACKGROUND': 'http://tile.stamen.com/toner-background/{Z}/{X}/{Y}.png',
    'STAMEN_TONER_LABELS':     'http://tile.stamen.com/toner-labels/{Z}/{X}/{Y}.png',
}

_STAMEN_LIC = {
    'STAMEN_TERRAIN':          '<a href="https://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>',
    'STAMEN_TERRAIN_RETINA':   '<a href="https://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>',
    'STAMEN_TONER':            '<a href="https://www.openstreetmap.org/copyright">ODbL</a>',
    'STAMEN_TONER_BACKGROUND': '<a href="https://www.openstreetmap.org/copyright">ODbL</a>',
    'STAMEN_TONER_LABELS':     '<a href="https://www.openstreetmap.org/copyright">ODbL</a>',
}

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

Test___all__ = verify_all(bt, ALL)

@pytest.mark.parametrize('name', [ 'STAMEN_TERRAIN',  'STAMEN_TERRAIN_RETINA', 'STAMEN_TONER', 'STAMEN_TONER_BACKGROUND', 'STAMEN_TONER_LABELS',])
@pytest.mark.unit
class Test_StamenProviders(object):
    def test_type(self, name):
        with pytest.deprecated_call():
            p = getattr(bt, name)
        assert isinstance(p, WMTSTileSource)

    def test_url(self, name):
        with pytest.deprecated_call():
            p = getattr(bt, name)
        assert p.url == _STAMEN_URLS[name]

    def test_attribution(self, name):
        with pytest.deprecated_call():
            p = getattr(bt, name)
        assert p.attribution == (
            'Map tiles by <a href="https://stamen.com">Stamen Design</a>, '
            'under <a href="https://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. '
            'Data by <a href="https://openstreetmap.org">OpenStreetMap</a>, '
            'under %s.'
        ) % _STAMEN_LIC[name]

    def test_copies(self, name):
        with pytest.deprecated_call():
            p1 = getattr(bt, name)
            p2 = getattr(bt, name)
        assert p1 is not p2

@pytest.mark.parametrize('name', ['CARTODBPOSITRON', 'CARTODBPOSITRON_RETINA'])
@pytest.mark.unit
class Test_CartoProviders(object):
    def test_type(self, name):
        with pytest.deprecated_call():
            p = getattr(bt, name)
        assert isinstance(p, WMTSTileSource)

    def test_url(self, name):
        with pytest.deprecated_call():
            p = getattr(bt, name)
        assert p.url == _CARTO_URLS[name]

    def test_attribution(self, name):
        with pytest.deprecated_call():
            p = getattr(bt, name)
        assert p.attribution == (
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors,'
            '&copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
        )

    def test_copies(self, name):
        with pytest.deprecated_call():
            p1 = getattr(bt, name)
            p2 = getattr(bt, name)
        assert p1 is not p2

@pytest.mark.parametrize('name', ['CARTODBPOSITRON', 'CARTODBPOSITRON_RETINA', 'STAMEN_TERRAIN',
                                  'STAMEN_TERRAIN_RETINA', 'STAMEN_TONER', 'STAMEN_TONER_BACKGROUND',
                                  'STAMEN_TONER_LABELS',])
@pytest.mark.unit
class Test_GetProvider(object):

    def test_get_provider(self, name):
        assert name in bt.Provider.__members__
        enum_member = bt.Provider.__members__[name]
        p1 = bt.get_provider(enum_member)
        p2 = bt.get_provider(name)
        assert isinstance(p1, WMTSTileSource)
        assert isinstance(p2, WMTSTileSource)
        assert p1 is not p2

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
