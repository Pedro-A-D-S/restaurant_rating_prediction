init:
	poetry env use python3.10
	poetry shell
	poetry install

download:
	bash utils/download_data.sh 