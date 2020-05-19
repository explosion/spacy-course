SHELL := /bin/bash

APP_NAME = "spacy_course"

# import settings config
settingsfile=docker/config.env
ifneq ("$(wildcard $(settingsfile))","")
	ifdef stt
	settingsfile=$(stt)
	endif
	include $(settingsfile)
	export $(shell sed 's/=.*//' $(settingsfile))
endif

build:
	docker build \
		--pull \
		--tag $(APP_NAME) \
		--file $(CURDIR)/docker/Dockerfile \
		$(CURDIR)

run:
	docker run -it --rm \
	    -v $(PWD):/host \
	    -p 8000:8000 \
	    -e PYTHONIOENCODING="utf-8" \
		$(APP_NAME) \
		$(SHELL)

gatsby-dev:
	docker run -it --rm \
	    -v $(PWD):/host \
	    -p 8000:8000 \
	    -e PYTHONIOENCODING="utf-8" \
		$(APP_NAME) \
		$(SHELL) -c "npm run dev"


pytest:
	docker run -it --rm \
	    -v $(PWD):/host \
	    -p 8000:8000 \
	    -e PYTHONIOENCODING="utf-8" \
		$(APP_NAME) \
		$(SHELL) -c "python -m pytest __tests__"