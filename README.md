### RAG Movie Recommender
- Set up virtual environment
    - pyenv virtualenv 3.10.12 moviegpt_venv
    - pyenv activate moviegpt_venv
- Install required packages
    - pip install -r requirements.txt
- In the src folder, run setup.py
    - cd src
    - python setup.py install
- Load movies data
    - cd src/data
    - python load.py
    - Data is stored in the folder raw_data
- Create vector index from the movies dataset
    - cd src/data
    - python vector_index.py
- Query vector index for movie recommendations
    - cd src/application
    - fastapi dev app.py

### Sample Output

<img width="828" alt="sample_output" src="https://github.com/user-attachments/assets/e62d19df-c27c-4a0a-afbc-067e31fcd5e6">
