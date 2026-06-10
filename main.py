def count_words(text: str) -> int:
    """Повертає кількість слів у рядку."""
    return len(text.split())


def main():
    sample_text = "Git допомагає контролювати зміни у проекті"
    print("Лабораторна робота Git/GitHub")
    print(f"Текст: {sample_text}")
    print(f"Кількість слів: {count_words(sample_text)}")


if __name__ == "__main__":
    main()
