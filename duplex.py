def parse_skip_pages(skip_str: str, n: int) -> tuple[set[int], list[str]]:
    """
    Parse a string like '2, 4-5, 9' into a set of ints within [1, n].
    Returns (skips, warnings).
    - Warns about malformed tokens.
    - Warns when pages/ranges are outside [1, n]; trims ranges that partially overlap.
    """
    skips = set()
    warnings: list[str] = []
    if not skip_str:
        return skips, warnings

    tokens = [t.strip() for t in skip_str.split(",") if t.strip()]
    for token in tokens:
        if "-" in token:
            try:
                a_str, b_str = token.split("-", 1)
                a, b = int(a_str), int(b_str)
                lo, hi = (a, b) if a <= b else (b, a)
                in_range = [i for i in range(lo, hi + 1) if 1 <= i <= n]

                if not in_range:
                    warnings.append(f"Range '{token}' is outside 1..{n} and was ignored.")
                    continue

                if lo < 1 or hi > n:
                    warnings.append(
                        f"Range '{token}' partially outside 1..{n}; using {in_range[0]}-{in_range[-1]}."
                    )
                skips.update(in_range)
            except ValueError:
                warnings.append(f"Malformed token '{token}' was ignored.")
        else:
            try:
                i = int(token)
                if 1 <= i <= n:
                    skips.add(i)
                else:
                    warnings.append(f"Page '{i}' is outside 1..{n} and was ignored.")
            except ValueError:
                warnings.append(f"Malformed token '{token}' was ignored.")
    return skips, warnings


def format_pages(pages: list[int]) -> str:
    return ",".join(map(str, pages))


def main():
    # Get user inputs
    try:
        n = int(input("Enter total number of pages (n): ").strip())
        if n <= 0:
            print("n must be a positive integer.")
            return
    except ValueError:
        print("Please enter a valid integer for n.")
        return

    skip_str = input(
        "Pages to skip (e.g., '2, 4-5'; leave blank for none): "
    ).strip()

    # Build the filtered page list
    skips, warnings = parse_skip_pages(skip_str, n)
    all_pages = list(range(1, n + 1))
    remaining = [p for p in all_pages if p not in skips]

    # Show warnings (if any)
    for w in warnings:
        print(f"Warning: {w}")

    if not remaining:
        print("Nothing to print: all pages were skipped.")
        return

    # Alternate remaining pages between side-one and side-two
    side_one = remaining[0::2]
    side_two = remaining[1::2]

    # Output
    print("side-one:", format_pages(side_one))
    print("side-two:", format_pages(side_two))


if __name__ == "__main__":
    main()

