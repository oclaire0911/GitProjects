# Study Log

A small module for tracking study sessions and quiz scores by topic.

## Setup

No external dependencies — pure Python standard library.

```
pip install pytest
```

## Running the tests

```
pytest test_study_log.py -v
```

You should see some failures. The code has bugs — that's expected starting state.

## Task

1. Run the test suite and read the failures.
2. Fix the bugs in `study_log.py` one at a time. After each individual fix,
   re-run the tests to confirm that specific failure is resolved before
   moving to the next one.
3. Once all tests pass, implement the new requirement described in
   `NEW_REQUIREMENT.md`. No test is pre-written for it — write your own
   example or test case before or alongside your implementation.

## Files

- `study_log.py` — the module (contains the bugs to find and fix)
- `test_study_log.py` — the test suite
- `NEW_REQUIREMENT.md` — a feature to add after the bugs are fixed
- `SOLUTIONS.md` — reference answers (only look after attempting it yourself)
