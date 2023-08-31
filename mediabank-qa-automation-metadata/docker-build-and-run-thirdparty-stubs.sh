#!/bin/bash
docker stop ms-thirdparty-stubs
docker rm ms-thirdparty-stubs
echo "[STARTING] Building the docker image for ms-stubs:"
docker build -t ms-thirdparty-stubs:0.0.1 .
echo "[FINISHED] Building the docker image for ms-stubs"
echo
echo
echo "[STARTING] Running the docker container for ms-stubs:"
docker run --hostname ms-thirdparty-stubs --name ms-thirdparty-stubs -p 8020:8020 -p 8030:8030 -p 8040:8040 -d ms-thirdparty-stubs:0.0.1
echo "[FINISHED] Running the docker container for ms-stubs"
echo
echo "**************************************************************************"
echo "KSS STUBS Running:"
echo " - SPORTRADAR STUB:      http://sportradar-service-stub:8020"
echo " - ESPN STUB:            http://espn-service-stub:8030"
echo " - TAG INTEGRATION STUB: http://tag-integration-service-stub:8040"
echo "**************************************************************************"


