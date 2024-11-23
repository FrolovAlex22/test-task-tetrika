def strict(func):
    func_annotations = func.__annotations__

    def a_wrapper_accepting_arguments(arg1, arg2):
        if (
            arg1.__class__ != func_annotations['a'] or
            arg2.__class__ != func_annotations['b']
        ):
            raise TypeError
        result = func(arg1, arg2)
        if result.__class__ != func_annotations['return']:
            raise TypeError
        return result
    return a_wrapper_accepting_arguments


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))
