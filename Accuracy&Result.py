from DifferentialPrivacy import diffAverage, diff_end_time, diff_start_time
from noPrivacyProtection import noPrivacyAverage, noPrivacy_end_time, noPrivacy_start_time
from Paillier import paillierAverage, paillier_end_time, paillier_start_time
from Shamir import shamirAverage, shamir_end_time, shamir_start_time

def GetAccuracy(noPrivacyAverage, comparison):

    if (comparison < 0):
        return

    if (noPrivacyAverage > comparison):
        percentage = (1-((noPrivacyAverage-comparison)/noPrivacyAverage)) * 100
    if (noPrivacyAverage < comparison):
        percentage = (1-((comparison-noPrivacyAverage)/noPrivacyAverage)) * 100
    else:
        percentage=100

    return percentage

paillier = GetAccuracy(noPrivacyAverage, paillierAverage)
shamir = GetAccuracy(noPrivacyAverage, shamirAverage)
differential = GetAccuracy(noPrivacyAverage, diffAverage)


print(f"The average of No Privacy Protection: {noPrivacyAverage}")
print(f"The average of Paillier: {paillierAverage}")
print(f"The average of Shamir: {shamirAverage}")
print(f"The average Differential Privacy: {diffAverage}")

print(f"Runtime for No Privacy Protection: {noPrivacy_end_time - noPrivacy_start_time:.4f} seconds")
print(f"Runtime for Pailler: {paillier_end_time - paillier_start_time:.4f} seconds")
print(f"Runtime for Shamir: {shamir_end_time - shamir_start_time:.4f} seconds")
print(f"Runtime for Differential Privacy: {diff_end_time - diff_start_time:.4f} seconds")

print(f"The accuracy Paillier: {paillier}")
print(f"The accuracy Shamir: {shamir}")
print(f"The accuracy Differential Privacy: {differential}")
