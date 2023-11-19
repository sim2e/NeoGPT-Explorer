# NEO-GPT for 소종

## Raw Data
`/joseon-data` 폴더 안에 인물별로 정리되어 있음 by 상헌

## Data Preprocess and Relation Extraction
### `/notebooks/Preprocess.ipynb`
    1.  Data 폴더안을 순회하면서 데이터들의 텍스트들을 list에 추가
    2.  diffbot API를 통해 Relation Extraction 결과를 `/data` 폴더안에 `joseon_nlp_output.json` 파일로 저장

## Graph Database Import
###  `/notebooks/Import.ipynb`
    1. `joseon_nlp_output.json` 파일을 읽어서 localhost에 실행한 Neo4j Server(Noe4j Desktop)에 데이터를 양식에 맞게 넣음

