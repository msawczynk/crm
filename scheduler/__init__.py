from __future__ import annotations

import threading
from typing import Callable


class SimpleScheduler:
    """Very small scheduler that runs a task every ``interval`` seconds."""

    def __init__(self, interval: float, func: Callable[[], None]) -> None:
        self.interval = float(interval)
        self.func = func
        self._timer: threading.Timer | None = None

    def _run(self) -> None:
        self.func()
        self.start()

    def start(self) -> None:
        self._timer = threading.Timer(self.interval, self._run)
        self._timer.daemon = True
        self._timer.start()

    def stop(self) -> None:
        if self._timer:
            self._timer.cancel()
            self._timer = None
