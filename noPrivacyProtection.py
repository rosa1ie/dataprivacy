from Utility import numlist
import time

noPrivacy_start_time = time.perf_counter()

noPrivacyAverage = sum(numlist) / len(numlist)

noPrivacy_end_time = time.perf_counter()
