if __name__ == "__main__":
    import kagglehub
    import os
    import shutil
    
    path = kagglehub.dataset_download("blastchar/telco-customer-churn")
    print("Path to dataset files:", path)
    # shutil.move(path, "./data/")
    shutil.move(path, ".")
    os.rename("1/", "data/")
