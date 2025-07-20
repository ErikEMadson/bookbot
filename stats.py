def count_words(text: str) -> int:
    return len(text.split())

def character_count_dictionary(text: str) -> dict[str, int]:
    counts = {}
    for character in text.lower():
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1
    return counts

def rank_character_count(character_count: dict[str, int]) -> list[dict[str, int]]:
    ranking = [{"char": character, "num": count} for character, count in character_count.items()]
    ranking.sort(reverse=True, key=lambda x: x["num"])
    return ranking
