# Will-learning-Python-Give-me-a-raise

## Summary
A Logistic Regression model predicting salary raise probability from Python study hours. The model shows that after studying Python for 70 hours, the probability of getting a raise is at least 80%. The model achieves 85% accuracy, which beats the 69% baseline accuracy. The relationship is visualized with an S-curve showing increasing probability with more study hours.

## How to run
1. Install requirements: pip install pandas scikit-learn matplotlib
2. Run: python main.py

## Data
data.csv contains hours studied and whether raise was received (0/1).

## Results
- Baseline accuracy: 69%
- Model accuracy: 85%
- At 70 hours, probability > 80%
