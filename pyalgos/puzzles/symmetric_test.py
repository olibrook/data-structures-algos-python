import pyalgos.puzzles.symmetric as s


def test_symmetric():
    _ = s.TreeNode

    # Single
    assert s.run(_('a'))

    # Single chain
    assert s.run(
        _('a', [
            _('b', [
                _('c')
            ])
        ])
    )

    assert not s.run(
        _('a', [
            _('b'),
            _('c'),
        ])
    )

    assert s.run(
        _('a', [
            _('b'),
            _('b'),
        ])
    )

    assert s.run(
        _('a', [
            _('b'),
            _('c'),
            _('b'),
        ])
    )

    assert not s.run(
        _('a', [
            _('b'),
            _('c'),
            _('c'),
        ])
    )

    assert s.run(
        _('a', [
            _('b', [
                _('c', [
                    _('d', [
                        _('e')
                    ])
                ])
            ]),
            _('c'),
            _('b', [
                _('c', [
                    _('d', [
                        _('e')
                    ])
                ])
            ]),
        ])
    )

    assert s.run(
        _('a', [
            _('b', [
                _('c', [
                    _('d', [
                        _('e'), _('f')
                    ])
                ])
            ]),
            _('c'),
            _('b', [
                _('c', [
                    _('d', [
                        _('f'), _('e')
                    ])
                ])
            ]),
        ])
    )

    # Check proper handling of center nodes
    assert s.run(
        _('a', [
            _('b'),
            _('c', [
                _('d'),
                _('d'),
            ]),
            _('b'),
        ])
    )

    assert not s.run(
        _('a', [
            _('b'),
            _('c', [
                _('d'),
                _('e'),
            ]),
            _('b'),
        ])
    )
