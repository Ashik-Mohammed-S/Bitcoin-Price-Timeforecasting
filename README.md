# Bitcoin-Price-Timeforecasting
BitPredict--Bitcoin-Price-forecasting-model
The above Colab notebook consists of different time series forecasting models for the bitcoin prices based on the historical prices from october 2013. All preprocessing details and related resources are mentioned in the notebook itself. The architectures used in the notebook are:

1. A basic Naive model as the threshold.
2. Dense model, horizon =1, window =7,
3. Dense model, horizon = 1, window =30,
4. Dense model, horizon = 7, window = 30,
5. Conv1D
6. LSTM
7. Dense model, but with multivariate data
8. N-BEATS algorithm (the reference paper is mentioned in the notebook),
9. Ensemble (multiple models optimized on different loss functions)
10. Future prediction model ( model to predict the future)
11. Dense model (but with turkey data introduced, turkey data is nothing but an anomaly that we deliberately put in the training data to show that time series forecasting is actually BS. )
