# GitHub Actions로 노트북 실행하기

## 파일 위치(필수)
- `notebooks/Untitled12.ipynb` : 실행할 노트북
- `requirements.txt` : 실행에 필요한 파이썬 패키지
- `scripts/run_notebook.py` : Papermill로 노트북 실행하는 런처
- `.github/workflows/run-notebook.yml` : GitHub Actions 워크플로우

## Secrets 설정(노트북에서 Mistral 등 API Key를 쓰는 경우)
Repo → **Settings → Secrets and variables → Actions → New repository secret**
- Name: `MISTRAL_API_KEY`
- Value: `sk-...`

## 실행 방법
1) GitHub에서 Actions 탭 → **Run Colab Notebook in GitHub Actions** 선택  
2) **Run workflow** 클릭  
3) 완료 후, 실행 결과는 **Artifacts**에 `notebook-outputs`로 업로드됩니다.

## 파라미터 주입(선택)
워크플로우 입력값 `parameters_json`에 JSON을 넣으면 노트북의 파라미터 셀로 전달됩니다.
예) `{"QUESTION":"R&D사업 관련 정책 요약"}`

> 노트북이 Papermill 파라미터를 받으려면, 노트북 상단에 `parameters` 태그가 붙은 셀에서 변수를 선언하는 방식이 가장 안정적입니다.
