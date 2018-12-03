train:
	python -m rasa_nlu.train -c nlu_config.yml --data data/intents.md -o models --fixed_model_name nlu --project current --verbose
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue

run:
	python -m rasa_core.run -d models/dialogue/ -u models/current/nlu/ --debug --enable_api 

