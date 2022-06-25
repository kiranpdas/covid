docker run -it \
    --mount source=$(pwd)/kpra_covid/,destination=/kpra_covid/,type=bind \
    covid19