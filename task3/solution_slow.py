def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals["lesson"]
    pupil = intervals["pupil"]
    tutor = intervals["tutor"]
    all_time = 0
    diff_slices = []
    for tutor_left in range(0, len(tutor)-1, 2):
        for pupil_left in range(0, len(pupil)-1, 2):
            if pupil[pupil_left] > tutor[tutor_left+1]:
                break
            if pupil[pupil_left+1] < tutor[tutor_left]:
                continue
            curr_slice = [max(lesson[0], pupil[pupil_left], tutor[tutor_left]), min(lesson[1], tutor[tutor_left+1], pupil[pupil_left+1])]
            dl = max(0, curr_slice[1] - curr_slice[0])
            if dl > 0:
                diff_slices.append(curr_slice)
    sl_left = 1
    all_time += diff_slices[0][1] - diff_slices[0][0]
    while sl_left < len(diff_slices):
        if diff_slices[sl_left-1][1] > diff_slices[sl_left][0]:
            if diff_slices[sl_left-1][1] > diff_slices[sl_left][1]:
                diff_slices.pop(sl_left)
                continue
            else:
                diff_slices[sl_left][0] = diff_slices[sl_left-1][1]
        all_time += diff_slices[sl_left][1] - diff_slices[sl_left][0]
        sl_left += 1
    return all_time

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'