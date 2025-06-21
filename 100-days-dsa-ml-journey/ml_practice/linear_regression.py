
# %% 
"""
Linear Regression
Convention: https://www.deeplearningbook.org/contents/ml.html (Goodfellow et. al.)

Given, x, y, w, b of dim (n), 1, (n,1), (1)  -------- y = w^T * x + b  ----------------- 

For m test examples, 

y(test) = X(test)@w + b, metrics: mse(test) = 1/m * (sum_i [ (y_pred(test) - y_true(test) ) ]_i  )

mse(test)  = 1/m * || y_pred(test) - y_true(test) || ** 2




Grads: Minimize mse over train to find optimal w, 

Grad_w (mse_train) = 0 
=> Grad_w (1/m . || y_pred(train) - y_true(train) || ** 2) = 0
=> Grad_w (1/m . || X(train) * w - y_true(train) || ** 2 ) = 0
=> Grad_w (1/m . ( X(train) * w - y_true(train) ) ^T  ( X(train) * w - y_true(train) ) ) = 0

=> Grad_w (1/m . ( w^T * X(train)^T - y_true(train)^T ) ( X(train) * w - y_true(train) ) ) = 0

=> Grad_w (1/m . ( w^T * X(train)^T * X(train) * w - w^T * X(train)^T * y_true(train) - 
            y_true(train)^T * X(train) * w + y_true(train)^T * y_true(train) ) ) = 0


=> Grad_w (1/m . ( w^T * X(train)^T * X(train) * w - (X(train) w)^T * y_true(train) - 
            y_true(train)^T * (X(train) * w)  +  y_true(train)^T * y_true(train) ) ) = 0


=> 1/m . ( w^T * X(train)^T * X(train) * w - 2 w^T X(train)^T * y_true(train) + y_true(train)^T * y_true(train) ) = 0

=> 1/m . ( 2 * X(train)^T * X(train) * w - 2 * X(train)^T * y_true(train) ) = 0

=> X(train)^T * X(train) * w = X(train)^T * y_true(train)

=> w = (X(train)^T * X(train))^(-1) * X(train)^T * y_true(train)



"""

class LinearRegression:
    def __init__(self, lr=0.01, n_iters=1000, batch_size=10, tolerance=1e-4):
        self.lr = lr
        self.n_iters = n_iters
        self.w = None
        self.b = None
        self.batch_size = batch_size
        self.tolerance = tolerance
        self.mse_train = []

    def predict(self, X):
        return X@self.w + self.b
# %%
