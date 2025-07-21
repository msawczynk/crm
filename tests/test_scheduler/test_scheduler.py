import time
from typing import List
from _pytest.monkeypatch import MonkeyPatch

from scheduler import SimpleScheduler


def test_scheduler_runs(monkeypatch: MonkeyPatch) -> None:
    calls: List[int] = []

    def task() -> None:
        calls.append(1)

    sched = SimpleScheduler(0.01, task)
    sched.start()
    time.sleep(0.03)
    sched.stop()
    assert len(calls) >= 2
