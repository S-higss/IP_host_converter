.DEFAULT_GOAL := install
.PHONY: push-all
push-all:	## カレントディレクトリ以下の全ての変更を反映
	@git add .
	@git commit -m "commit all changes"
	@git push origin HEAD

.PHONY: install
install:	## 必要なライブラリのインストール
	@pip install -r requirements.txt

.PHONY: run
run:	## main.pyを実行
	@python main.py

.PHONY: help
help:	## show commands
	@grep -E '^[[:alnum:]_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
