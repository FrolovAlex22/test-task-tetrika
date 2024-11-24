def appearance(intervals: dict[str, list[int]]) -> int:
    counter_pupil = 0
    counter_tutor = 0
    counter_lesson = 0
    for key, value in intervals.items():
        if key == "lesson":
            for val in range(0, len(value), 2):
                result = (value[val+1] - value[val])
                counter_lesson += result
        if key == "pupil":
            for val in range(0, len(value), 2):
                result = (value[val+1] - value[val])
                counter_pupil += result
        elif key == "tutor":
            for val in range(0, len(value), 2):
                counter_tutor += (value[val+1] - value[val])
    return counter_pupil + counter_tutor
