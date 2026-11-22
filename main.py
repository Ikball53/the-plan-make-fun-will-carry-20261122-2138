from pathlib import Path

ENTRY = (
    "Day1: post $25 Shopify/Stripe webhook fixes on Fiverr+Upwork; "
    "ship 2/day with browser+code, bank $40. Spend $20 on Fiverr Pro. "
    "Days2-30: 4 jobs/day at $30 avg, upsell $50/mo uptime checks to 8 shops. "
    "Day30: ~$1,860 net, repeatable, no luck needed. Edge: same-day fix + proof."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
