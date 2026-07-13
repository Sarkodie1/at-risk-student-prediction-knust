# KNUST Student Experience Survey 2026 - Data Schema

This file describes the schema and coding mappings for the KNUST Student Experience Survey dataset (both the restricted raw dataset and the public synthetic dataset).

## Target Variable
*   **Withdrawal Intention (Q5):** Binary classification target indicating at-risk status.
    *   `1` = At-risk (Student answered 'Seriously considered withdrawing' or 'Briefly considered withdrawing')
    *   `0` = Not at-risk (Student answered 'No')

## Predictor Variables (14 Features)

The 14 training features are mapped to Tinto's (2025) Student Integration constructs and coded ordinally:

### 1. Academic Integration (Q1–Q4)
*   **Q1_Academic_Performance:** Self-rated academic performance.
    *   `0` = Struggling significantly
    *   `1` = Below average
    *   `2` = Average
    *   `3` = Good
    *   `4` = Excellent
*   **Q2_Attendance:** Frequency of class attendance.
    *   `0` = Less than 40%
    *   `1` = 40–60%
    *   `2` = 60–80%
    *   `3` = More than 80%
*   **Q3_Assignments:** Timely assignment submissions (out of last 5).
    *   `1` = None
    *   `2` = 1 or 2
    *   `3` = 3 or 4
    *   `4` = All 5
*   **Q4_Repeating:** Course repetition status.
    *   `0` = No
    *   `1` = Yes

### 2. Social and Institutional Integration (Q13, Q14, Q16)
*   **Q13_Faculty:** Faculty or College of enrolment.
    *   `1` = College of Engineering
    *   `2` = College of Science
    *   `3` = College of Arts and Social Sciences
    *   `4` = School of Business
    *   `5` = College of Health Sciences
    *   `6` = Other Faculty / School
*   **Q14_Year:** Year of study.
    *   `1` = Year 1
    *   `2` = Year 2
    *   `3` = Year 3
    *   `4` = Year 4
    *   `5` = Year 5 or above (undergraduate)
*   **Q16_Belonging:** Perceived sense of institutional belonging.
    *   `0` = Strongly disagree
    *   `1` = Disagree
    *   `2` = Neutral
    *   `3` = Agree
    *   `4` = Strongly agree

### 3. Contextual Barriers & Mental Health (Q6–Q12)
*   **Q6_PHQ2_Interest:** Frequency of anhedonia (loss of interest) over the last 2 weeks (PHQ-2).
    *   `0` = Not at all
    *   `1` = Several days
    *   `2` = More than half the days
    *   `3` = Nearly every day
*   **Q7_PHQ2_Depressed:** Frequency of depressed mood over the last 2 weeks (PHQ-2).
    *   `0` = Not at all
    *   `1` = Several days
    *   `2` = More than half the days
    *   `3` = Nearly every day
*   **Q8_GAD2_Nervous:** Frequency of feeling nervous or anxious over the last 2 weeks (GAD-2).
    *   `0` = Not at all
    *   `1` = Several days
    *   `2` = More than half the days
    *   `3` = Nearly every day
*   **Q9_GAD2_Worry:** Frequency of uncontrolled worry over the last 2 weeks (GAD-2).
    *   `0` = Not at all
    *   `1` = Several days
    *   `2` = More than half the days
    *   `3` = Nearly every day
*   **Q10_Financial_Difficulty:** Degree to which financial difficulty affected study participation.
    *   `0` = Not at all
    *   `1` = Slightly (rarely affected participation)
    *   `2` = Moderately (sometimes limited participation)
    *   `3` = Severely (significantly limited participation)
*   **Q11_Internet_Access:** Reliability of internet access.
    *   `0` = Very limited (serious barrier)
    *   `1` = Frequently unreliable (regular difficulties)
    *   `2` = Mostly reliable (occasional difficulties)
    *   `3` = Reliable access (rarely a problem)
*   **Q12_Outside_Responsibilities:** Responsibilities outside of studies.
    *   `0` = No (does not affect study time)
    *   `1` = Sometimes (occasionally affects study time)
    *   `2` = Yes (regularly takes significant time)

### 4. Demographic Variables (Fairness Analysis)
*   **Q15_Gender:** Student gender.
    *   `0` = Female
    *   `1` = Male
