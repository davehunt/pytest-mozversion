# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    base_url = config.getoption('base_url')
    if base_url:
        version = requests.get('{0}/__version__'.format(base_url)).json()
        config._metadata['version'] = version
