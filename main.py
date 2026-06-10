def count_words(text: str) -> int:
    """Повертає кількість слів у рядку."""
    return len(text.split())


def count_characters(text: str) -> int:
    """Повертає кількість символів без пробілів."""
    return len(text.replace(" ", ""))


def main():
    sample_text = "Git допомагає контролювати зміни у проекті"
    print("Лабораторна робота Git/GitHub")
    print(f"Текст: {sample_text}")
    print(f"Кількість слів: {count_words(sample_text)}")
    print(f"Кількість символів без пробілів: {count_characters(sample_text)}")


if __name__ == "__main__":
    main()
