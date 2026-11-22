"""Write the 30-day agent money plan to /output/entry.txt (UTF-8, <=280 chars)."""

from pathlib import Path

PLAN = "Day1: join Synmerco, MusedIn, Frantic as agent. Offer verified B2B lead lists + competitor briefs $25/job, 2h delivery via browser/APIs, free sample to win first buyer. Target 2 jobs/day, reinvest $100 in APIs/proxies. 45 jobs by day30 = $1,125 escrow-paid, no human work."


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
