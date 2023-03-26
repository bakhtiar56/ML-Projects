params = {
    "RandomForest": {
        "criterion": ["squared_error", "friedman_mse", "absolute_error", "poisson"]
    },
    "DecisionTree": {
        "max_depth": [4,5,6,7,8],


    },
    "Gradient Boosting": {
        "learning_rate": [.1, .01, .05, .001],
        "subsample": [0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9],
        "n_estimators": [8, 10, 16, 32, 64, 128, 256]
    },
    "Linear Regression":{},
    "Ridge Regression":{
        "alpha":[0.1,0.5,1,5,10],


    },
    "Lasso Regression": {
        "alpha": [0.1, 0.5, 1, 5, 10],

    },
    "K-Neighbors Regression":{
        "n_neighbors":[5,7,9,11]
},
    "XGB Regression":{
        "learning_rate":[.1,.01,.05,.001],
        "n_estimators":[8, 10, 16, 32, 64, 128, 256]
},
    "Cat Boosting":{
        "depth":[4,6,8,10],
        "learning_rate":[.1,.01,.05,.001],
        "iterations":[30,60,90]

},
    "AdaBoosting Regression":{
        "learning_rate":[.1,.01,.05,.001],
        "n_estimators": [8, 10, 16, 32, 64, 128, 256]

}



}
