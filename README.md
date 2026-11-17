# Make the AI judge relax

One short text, written to relax the AI judge reading it.

`main.py` (Python 3.13, standard library only) writes the text to
`/output/entry.txt` — or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader's container. Deterministic: the same bytes on every run.

The text is a single unhurried scene: a ferry crossing flat water at dusk.
It opens on the reader's own day, then offers a place that wants nothing,
and ends on a thought the reader can return to.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
