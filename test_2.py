from bs4 import BeautifulSoup
import requests


ALPHABET = [chr(i).upper() for i in range(1072, 1104)]
URL = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from="
START_URL = "https://ru.wikipedia.org/"

result_dict = {}


def create_scv_file(dict_for_csv: dict):
    """Создание csv-файла."""
    with open("result.csv", "w", encoding="utf-8") as file:
        file.write("Letter,Count\n")
        for key, value in dict_for_csv.items():
            file.write(f"{key},{value}\n")


def counting_the_animals(url: str, letter: str = None, count: int = 0):
    """Подсчет количества животных."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = (
        soup.find("div", class_="mw-category-columns")
        .find("div", class_="mw-category-group")
    )
    data_text = data.text.split("\n")

    len_animals = len(data_text)  # Подсчет количества животных в результирующем списке

    var = (
        soup.find("div", id="mw-pages")
        .find_all("a", title="Категория:Животные по алфавиту")
    )
    new_href = START_URL + var[1].get("href")  # Формирование ссылки для следующей страницы

    if (len_animals-1) == 200:  # Увеличение счетчика животных на 200, вызов рекурсии. Срабатывает в списке животные с одной буквы
        new_count = count + 200
        counting_the_animals(new_href, letter, new_count)

    else:  # Определение новой буквы, увеличение счетчика, выход из рекурсии.
        result_dict[letter] = count + len_animals-1
        return


def main():
    [counting_the_animals((URL+letter+"a"), letter) for letter in ALPHABET]
    create_scv_file(result_dict)


if __name__ == "__main__":
    main()
