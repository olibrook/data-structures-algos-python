import pyalgos.puzzles.symmetric as s


def test_symmetric():
    _ = s.TreeNode

    # Single
    assert s.is_symmetric(_('a'))

    # Single chain
    assert s.is_symmetric(
        _('a', [
            _('b', [
                _('c')
            ])
        ])
    )

    assert not s.is_symmetric(
        _('a', [
            _('b'),
            _('c'),
        ])
    )

    assert s.is_symmetric(
        _('a', [
            _('b'),
            _('b'),
        ])
    )

    assert s.is_symmetric(
        _('a', [
            _('b'),
            _('c'),
            _('b'),
        ])
    )

    assert not s.is_symmetric(
        _('a', [
            _('b'),
            _('c'),
            _('c'),
        ])
    )

    assert s.is_symmetric(
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

    assert s.is_symmetric(
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
    assert s.is_symmetric(
        _('a', [
            _('b'),
            _('c', [
                _('d'),
                _('d'),
            ]),
            _('b'),
        ])
    )

    assert not s.is_symmetric(
        _('a', [
            _('b'),
            _('c', [
                _('d'),
                _('e'),
            ]),
            _('b'),
        ])
    )
