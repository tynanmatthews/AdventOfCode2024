class NuclearPlantVerifier():

    def __init__(self, reports):
        self.reports = reports
        
    def printReports(self):
        print(self.reports)

    def generateExceptionReports(self, report):
        """Creates copies of the input report with one value less in each

        Iterates through the report, copies the list and removes one value.
        The result is a 2D List of length of the input report, with each list
        within having length of 1 - length of input report.
        """
        exception_reports = [] # 2D Array
        for i in range(0, len(report)):
            # For each value in the report, copy the list without that value
            temp_report = report.copy()
            temp_report.pop(i) # needs to be pop as value removes 'first' occurance
            exception_reports.append(temp_report)
        print(f"Original Report {report}")
        print(f"Exception reports: {exception_reports}")
        return exception_reports
            
    def allDecreasing(self, report):
        for i in range(1, len(report)):
            if report[i] > report[i - 1]:
                return False
        return True

    def allIncreasing(self, report):
        for i in range(1, len(report)):
            if report[i] < report[i - 1]:
                return False
        return True
                
    def differenceQuota(self, report):
        min_distance = 1
        max_distance = 3
        for i in range(1, len(report)):
            distance = report[i] - report[i - 1]
            abs_distance = abs(distance)
            if (abs_distance < min_distance) or (abs_distance > max_distance):
                return False
        # all passed
        return True

    def reportVerifier(self, report):
        if self.allDecreasing(report) or self.allIncreasing(report):
            if self.differenceQuota(report):
                return True
        return False

    def findSafeReportsTest(self):
        first_report = self.reports[0]
        is_safe = self.reportVerifier(first_report)
        print(f"It is {is_safe} that the first report is safe")

    def findSafeReportsVerbose(self):
        safe_reports = []
        for report in self.reports:
            if self.reportVerifier(report):
                safe_reports.append(report)
        safe_report_count = len(safe_reports)
        print(f"There were {safe_report_count} safe reports found")
        print(f"Here they are below: ")
        print(safe_reports)

    def findSafeReportsProblemDampener(self):
        safe_reports = []
        for report in self.reports:
            exception_reports = self.generateExceptionReports(report)
            isSafe = False
            for exception_report in exception_reports:
                if self.reportVerifier(exception_report):
                    isSafe = True
            if isSafe:
                safe_reports.append(report)
        safe_report_count = len(safe_reports)
        print(f"There were {safe_report_count} safe reports found")
        print(f"Here they are below: ")
        print(safe_reports)



def processFile(dirty_file):
    ret = []
    for line in dirty_file:
        temp_int = []
        split_line = line.split()
        for string in split_line:
            temp_int.append(int(string))
        ret.append(temp_int)
    return ret

f = open("nuclear_reports")
dirty_file = f.readlines()
nuclear_reports = processFile(dirty_file)

example_report = [[7, 6, 4, 2, 1],[1, 2, 7, 8, 9],[9, 7, 6, 2, 1],[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]



npv = NuclearPlantVerifier(nuclear_reports)
# npv.printReports()
# npv.findSafeReportsVerbose()

npvpd = NuclearPlantVerifier(nuclear_reports)
npvpd.findSafeReportsProblemDampener()
