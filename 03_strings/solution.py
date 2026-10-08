"""Lesson 3 — solutions."""


def reverse(s: str) -> str:
    return s[::-1]


def initials(full_name: str) -> str:
    result = ""
    for word in full_name.split():
        result += word[0].upper()
    return result


def is_palindrome(s: str) -> bool:
    letters = ""
    for ch in s:
        if ch.isalpha():
            letters += ch.lower()
    return letters == letters[::-1]


def count_vowels(s: str) -> int:
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


def slugify(title: str) -> str:
    return "-".join(title.strip().lower().split())


def mask_card(number: str) -> str:
    return "*" * (len(number) - 4) + number[-4:]


def file_extension(filename: str) -> str:
    base, dot, ext = filename.rpartition(".")
    if not dot:
        return ""
    return ext.lower()


def caesar(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += ch
    return result
