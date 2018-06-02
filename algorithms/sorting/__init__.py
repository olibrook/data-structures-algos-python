def main():
    import algorithms.sorting.insertion_sort as i_sort
    import algorithms.sorting.selection_sort as s_sort
    import algorithms.sorting.bubble_sort as b_sort
    import algorithms.sorting.heap_sort as h_sort
    import algorithms.sorting.merge_sort as m_sort

    for m in [i_sort, s_sort, b_sort, h_sort, m_sort]:
        actual = m.sort(list(reversed(range(10))))
        expected = list(range(10))
        print(actual)
        assert actual == expected
        assert m.sort([]) == []

    print('ok')


if __name__ == '__main__':
    main()
