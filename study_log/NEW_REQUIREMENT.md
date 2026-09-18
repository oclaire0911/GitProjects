# New requirement (implement after all 4 bugs are fixed)

Add a function `get_topics_needing_review(sessions, min_minutes=30)` to `study_log.py`.

**Spec:** Given the session log (a list of `{"topic": ..., "minutes": ...}` dicts),
return a list of topic names whose *total* studied minutes across all sessions
is strictly less than `min_minutes`. Each topic name should appear once in the
result, even if it has multiple sessions.

No test is pre-written for this one — same as the real interview format.
Before writing the implementation:
1. Restate the spec in your own words out loud.
2. Sketch the function signature and think through the return shape.
3. Write a quick example or a test case first (or alongside), same habit as before.
