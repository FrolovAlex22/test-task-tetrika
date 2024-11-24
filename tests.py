import asyncio
import unittest

from test_1 import sum_two
from test_2 import main
from test_3 import appearance


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [
                       1594663340, 1594663389, 1594663390, 1594663395,
                       1594663396, 1594666472
                    ],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 6300
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [
                       1594702789, 1594704500, 1594702807, 1594704542,
                       1594704512, 1594704513, 1594704564, 1594705150,
                       1594704581, 1594704582, 1594704734, 1594705009,
                       1594705095, 1594705096, 1594705106, 1594706480,
                       1594705158, 1594705773, 1594705849, 1594706480,
                       1594706500, 1594706875, 1594706502, 1594706503,
                       1594706524, 1594706524, 1594706579, 1594706641
                       ],
                    'tutor': [
                        1594700035, 1594700364, 1594702749, 1594705148,
                        1594705149, 1594706463
                        ]
                    },
    'answer': 11410
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 8636
    },
]

class Tests(unittest.TestCase):
    def test_task_1(self):
        "Сравнение двух чисел."
        result = sum_two(1, 2)
        self.assertEqual(result, 3)

        with self.assertRaises(TypeError, msg="Ожидалась ошибка 'TypeError'."):
            result = sum_two(1, 2.4)

    def test_task_2(self):
        """Проверка наличия ключа 'Я' в csv-файле."""
        with open("result.csv", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("Я", content, "Файл не содержит букву 'Я'")

    def test_task_3(self):
        """Подсчет времени на уроке."""
        for i, test in enumerate(tests):
            answer = appearance(test["intervals"])
            self.assertEqual(
                answer,
                test["answer"],
                msg=f"Error on test {i}, got {answer}, expected "
                    f"{test['answer']}"
            )


if __name__ == "__main__":
    asyncio.run(main())
    unittest.main()