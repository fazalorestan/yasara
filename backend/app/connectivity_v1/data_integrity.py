from pydantic import BaseModel

class GapCheckResultV1(BaseModel):
    expected_interval: int
    gaps: list[tuple[int, int]]

class DataIntegrityCheckerV1:
    def find_time_gaps(self, timestamps: list[int], expected_interval: int) -> GapCheckResultV1:
        ordered = sorted(timestamps)
        gaps = []
        for prev, current in zip(ordered, ordered[1:]):
            if current - prev > expected_interval:
                gaps.append((prev, current))
        return GapCheckResultV1(expected_interval=expected_interval, gaps=gaps)
