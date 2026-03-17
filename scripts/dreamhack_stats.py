
import requests
import re

USERNAME = "GUnT_0x9"

def get_stats():
    try:
        url = f"https://dreamhack.io/users/{USERNAME}"
        r = requests.get(url, timeout=10)
        html = r.text

        solved = "Unknown"
        rank = "Unknown"

        solved_match = re.search(r"Solved.*?(\d+)", html)
        rank_match = re.search(r"Rank.*?(\d+)", html)

        if solved_match:
            solved = solved_match.group(1)

        if rank_match:
            rank = rank_match.group(1)

        return solved, rank

    except:
        return "Unknown", "Unknown"

def update_stats():
    solved, rank = get_stats()

    section = f"""
## Dreamhack Activity

![Dreamhack](https://img.shields.io/badge/Dreamhack-CTF-red?style=for-the-badge)

User: {USERNAME}  
Solved Challenges: {solved}  
Rank: {rank}
"""

    with open("DREAMHACK_STATS.md", "w") as f:
        f.write(section)

if __name__ == "__main__":
    update_stats()
