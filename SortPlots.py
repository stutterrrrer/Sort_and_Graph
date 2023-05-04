from SortRunTimes import SortRunTimes
from numpy import log, arange
from scipy.optimize import curve_fit
from matplotlib import pyplot


class SortPlots:
    BUBBLE_SORT = "bubble sort"

    def __init__(self, runtimes: SortRunTimes):
        # get {method_name: {input: runtime} } dictionary from SortRunTimes class
        self.sort_run_times = runtimes.get_runtimes()
        # dictionary: {method_name: [a, b]} - where a & b are the fitted parameters
        self.fitted_parameters = dict()
        self.fit_curve()

    @staticmethod
    def square_objective(x, a, b):
        return a * x * x + b

    @staticmethod
    def linearithmic_objective(x, a, b):
        return a * log(x) + b

    def fit_curve(self):
        for sort_name in self.sort_run_times.keys():
            runtimes = self.sort_run_times[sort_name]
            # x_data and y_data for fitting
            input_size, runtime = list(runtimes.keys()), list(runtimes.values())
            # get fitted parameter after regression:
            if sort_name == self.BUBBLE_SORT:
                objective = SortPlots.square_objective
            else:
                objective = SortPlots.linearithmic_objective
            fitted_parameters, covariance = curve_fit(objective, input_size, runtime)
            self.fitted_parameters[sort_name] = fitted_parameters

    def draw_plots(self):
        for sort_name in self.sort_run_times.keys():
            runtime_dict = self.sort_run_times[sort_name]
            # x_data and y_data for scatter plots
            input_sizes, runtime_dict = list(runtime_dict.keys()), list(runtime_dict.values())
            pyplot.scatter(input_sizes, runtime_dict)
            # draw fitted curve
            parameters = self.fitted_parameters[sort_name]
            # draw regression line
            x_line = arange(min(input_sizes), max(input_sizes), 1)
            if sort_name == self.BUBBLE_SORT:
                objective = SortPlots.square_objective
                # print fitted objective function with 1 decimal precision ( running time in nano seconds)
                print(sort_name, ': running_time = %.1f * n^2 + %.1f' % (parameters[0], parameters[1]))
            else:
                objective = SortPlots.linearithmic_objective
                print(sort_name, ': running_time = log(%.1f * n) + %.1f' % (parameters[0], parameters[1]))
            y_line = objective(x_line, *parameters)
            pyplot.xlabel(sort_name + " input size")
            pyplot.ylabel("running times")
            pyplot.plot(x_line, y_line, '--', color='red')
            pyplot.show()


def draw_plot_test():
    sort_run_times = SortRunTimes()
    search_plots = SortPlots(sort_run_times)
    search_plots.draw_plots()


draw_plot_test()
