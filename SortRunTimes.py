import time
from Sort import Sort


class SortRunTimes:
    TIME_UNIT_SCALE = pow(10, 6)  # record time in micro-seconds

    def __init__(self, list_count=20, min_list_size=50, list_size_increments=5, repeat=10):
        # create list_count number of lists in descending order
        self.lists_to_sort = []
        cur_list_size = min_list_size
        for i in range(list_count):
            self.lists_to_sort.append([*range(cur_list_size, 0, -1)])
            cur_list_size += list_size_increments

        # methods is a dictionary of sort methods {sort_name: method}
        # runtimes is a dictionary of dictionaries - {method_name: {input : runtime} }
        self.sort_methods = {
            "bubble sort": Sort.bubble_sort,
            "quick sort": Sort.quick_sort_simple,
            "merge sort": Sort.mergesort
        }
        self.runtimes = dict()
        for sort_name in self.sort_methods.keys():
            self.runtimes[sort_name] = dict()

        self.repeat = repeat

        # start recording sort run times
        self.record_runtimes()

    def record_runtimes(self):
        for sort_name in self.sort_methods.keys():
            # for each sort method, run it on each descending list for repeat times
            # record total time, average and save to self.runtimes
            sort = self.sort_methods[sort_name]
            for list_to_sort in self.lists_to_sort:
                time_bgn = time.time()
                for i in range(self.repeat):
                    sort(list_to_sort)
                avg_time = (time.time() - time_bgn) / self.repeat
                self.runtimes[sort_name][len(list_to_sort)] = avg_time * self.TIME_UNIT_SCALE

    def get_runtimes(self):
        return self.runtimes


def test_sort_run_times():
    sort_runt_times = SortRunTimes()
    for sort_runtime in sort_runt_times.get_runtimes().items():
        print(sort_runtime)


# test_sort_run_times()
