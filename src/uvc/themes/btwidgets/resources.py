# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH

from fanstatic import Library, Resource
from js.bootstrap import bootstrap_css

library = Library('uvc.themes.btwidgets', 'static')
btw_css = Resource(library, 'btwidgets.css', depends=[bootstrap_css])
