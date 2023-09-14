# Matrix algebra framework

Code to compute basic matrix operations

## Framework installation

To install the framework you need anaconda and git on a linux machine. In a terminal type:
1. Clone the repository:
  ```
  git clone git@github.com:andrex-naranjas/matrix-algebra.git
  ```
2. Access the code:
  ```
  cd matrix-algebra
  ```
3. Install the conda enviroment:
  ```
  conda env create -f config.yml
  conda activate matrix-algebra
  conda develop .
  ```
3.1 Update the conda enviroment:
   ```
   conda env update --file config.yml --prune
   ```

4. Minimal run:
  ```
  python3 ./scripts/test_matrix_multiplication.py
  ```
