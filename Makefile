run:
	docker build --progress=plain -t cognee_neo4j .
	docker run --gpus all -it --rm --name cognee_neo4j --env-file=.env cognee_neo4j

build:
	docker build --no-cache --progress=plain -t cognee_neo4j .