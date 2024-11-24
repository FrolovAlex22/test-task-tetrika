import aiohttp
import asyncio
from bs4 import BeautifulSoup


ALPHABET = [chr(i).upper() for i in range(1072, 1104)]
URL = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&from="
START_URL = "https://ru.wikipedia.org/"

result_dict = {}


def create_scv_file(dict_for_csv: dict):
    """Создание csv-файла."""
    with open("result.csv", "w", encoding="utf-8") as file:
        file.write("Animal counter alphabetically:\n")
        sorted_dict = sorted(dict_for_csv.items())
        for key, value in sorted_dict:
            file.write(f"{key},{value}\n")


async def counting_the_animals(
        url: str,
        letter: str = None,
        count: int = 0,
        session: aiohttp.ClientSession = None
        ):
    """Подсчет количества животных."""
    async with aiohttp.ClientSession() as session:

        response = await session.get(url)
        text = await response.text()

    soup = BeautifulSoup(text, "html.parser")

    data = (
        soup.find("div", class_="mw-category-columns")
        .find("div", class_="mw-category-group")
    )
    data_text = data.text.split("\n")

    len_animals = len(data_text)  # Подсчет количества животных в результирующем списке

    href_var = (
        soup.find("div", id="mw-pages")
        .find_all("a", title="Категория:Животные по алфавиту")
    )
    new_href = START_URL + href_var[1].get("href")  # Формирование ссылки для следующей страницы

    if (len_animals-1) == 200:  # Увеличение счетчика животных на 200, вызов рекурсии. Срабатывает в списке животные с одной буквы.
        new_count = count + 200
        await counting_the_animals(new_href, letter, new_count, session)

    else:  # Увеличение счетчика, выход из рекурсии.
        result_dict[letter] = count + len_animals-1
        return


async def main():
    """Основная функция."""
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(
                counting_the_animals((URL+letter+"a"), letter, 0, session)
            ) for letter in ALPHABET
        ]
        await asyncio.gather(*tasks)
        create_scv_file(result_dict)


if __name__ == "__main__":
    asyncio.run(main())
