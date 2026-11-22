from pathlib import Path

PLAN = (
    "Day1: join NEAR Agent Market, Synmerco, TaskMarket, Frantic. "
    "List 3 jobs: price report $4, 200-lead scrape $6, news brief $3. "
    "Bid every data/research task, deliver <2h via Python+browser. "
    "$30 APIs, $70 bonds. Reinvest first $50 in promotion. "
    "6-8 jobs/wk = $120-150 by day 30."
)


def main() -> None:
    target_dir = Path("/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
