from core import main
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

if __name__ == "__main__":
    main.main()