# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

pytest_plugins = "pytester",


def test_mozversion(testdir, httpserver, monkeypatch):
    httpserver.serve_content(content='{"spam":"ham"}')
    monkeypatch.setenv('PYTEST_BASE_URL', httpserver.url)
    testdir.makepyfile("""
        def test_pass(metadata):
            assert metadata['version'] == {'spam': 'ham'}
    """)
    result = testdir.runpytest()
    assert result.ret == 0
