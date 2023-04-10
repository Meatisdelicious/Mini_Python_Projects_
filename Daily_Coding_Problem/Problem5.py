# Problem #22

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

from heapq import heappush, heappop


class Time_table_management:

    def Min_meeting_rooms(self, intervals):
        # in the case we don't have any interval (single instead of pair)
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda it: (it.start, it.end))

        room_count = 0
        heap = []
        # [(30, 75), (0, 50), (60, 150)]
        # -->
        # print([(i.start, i.end) for i in sorted_intervals])
        for inter in sorted_intervals:
            # iterates though the list
            # and decomposes the start.value and end.value
            start, end = inter.start, inter.end
            # while heap
            while heap and heap[0] <= start:
                heappop(heap)
            heappush(heap, end)

            # counts the pairs (time intervals)
            room_count = max(len(heap), room_count)
            # print(start, end, heap)
        return room_count


if __name__ == "__main__":
    time_table_management = Time_table_management()

    time_intervals = [(30, 75), (0, 50), (60, 150)]
    print(type(time_intervals))
    print(time_table_management.Min_meeting_rooms(time_intervals))


# problem the tuple --> à résoudre
