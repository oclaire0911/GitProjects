# study_log.py — starting code for the collaborative coding exercise practice.
# Contains 4 bugs. Narrate hypothesis -> fix -> re-run test, one at a time.

import copy


def clone_log(sessions):
    """Return an independent copy of the session log, safe to modify
    without affecting the original."""
    return copy.deepcopy(sessions)


def remove_sessions_for_topic(sessions, topic):
    """Remove all logged sessions matching a given topic."""
    sessions[:] = [session for session in sessions if session["topic"] != topic]
    return sessions


def total_minutes(sessions, topic):
    """Sum total minutes studied for a topic across all sessions."""
    total = 0
    for session in sessions:
        if session["topic"] == topic:
            try:
                total += session["minutes"]
            except:
                pass
    return total


def get_last_score(scores, topic):
    """Look up the most recent quiz score for a topic.
    Should return None if the topic hasn't been scored yet."""
    if topic not in scores:
        return None
    else:
        return scores[topic][-1]
