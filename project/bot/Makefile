train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/intents.md \
	-o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md \
		-o models/dialogue -c config.yml

train: train-nlu train-core

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

run:
	python -m rasa_core.run -d models/dialogue/ -u models/current/nlu/ \
		--endpoints endpoints.yml --debug --enable_api

run-telegram:
	python -m rasa_core.run -d models/dialogue -u models/current/nlu \
		--endpoints endpoints.yml --port 5002 \
		--credentials credentials.yml
