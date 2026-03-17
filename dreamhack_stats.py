
import requests
import re

USERNAME = "GUnT_0x9"

def get_stats():
    try:
        url = f"https://dreamhack.io/users/{USERNAME}"
        r = requests.get(url, timeout=10)
        html = r.text

        solved_match = re.search(r"Solved\s*Challenges\s*</[^>]+>\s*<[^>]+>(\d+)", html)
        rank_match = re.search(r"Rank\s*</[^>]+>\s*<[^>]+>([^<]+)", html)

        solved = solved_match.group(1) if solved_match else "Unknown"
        rank = rank_match.group(1).strip() if rank_match else "Unknown"

        return solved, rank
    except Exception:
        return "Unknown", "Unknown"

def update_readme():
    solved, rank = get_stats()

    section = f"""
## Dreamhack Activity

![Dreamhack](https://img.shields.io/badge/Dreamhack-CTF-red?style=for-the-badge)

**User:** {USERNAME}  
**Solved Challenges:** {solved}  
**Rank:** {rank}
"""

    with open("DREAMHACK_STATS.md", "w", encoding="utf-8") as f:
        f.write(section)

if __name__ == "__main__":
    update_readme()
